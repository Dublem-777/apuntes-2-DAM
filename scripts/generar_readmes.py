#!/usr/bin/env python3
"""
Genera los README.md del repositorio de apuntes (GitHub) a partir de la bóveda de Obsidian.

Tres niveles:
  1. Core/README.md                       → portada con la tabla de asignaturas
  2. DAM/<Asignatura>/README.md           → índice de la asignatura (su Indice.md traducido a GitHub)
  3. DAM/<Asignatura>/<Tema N>/README.md  → notas del tema agrupadas por tipo

También reescribe la lista blanca de imágenes de resources/ en el .gitignore
y comprueba que todos los enlaces de los README generados existen.

Uso (desde cualquier carpeta):  python3 scripts/generar_readmes.py
"""
import os
import re
import sys
from pathlib import Path
from urllib.parse import quote, unquote

ROOT = Path(__file__).resolve().parent.parent          # Core/
DAM = ROOT / "DAM"
RESOURCES = ROOT / "resources"
GITIGNORE = ROOT / ".gitignore"

MARK = "<!-- generado por scripts/generar_readmes.py: no editar a mano -->"
PROJECT_URL = "https://github.com/dmadmer501/WarrantyKeep"

# Carpetas y archivos que no se suben (deben coincidir con el .gitignore)
EXCLUDED_DIRS = {".idea", "out", "logs", ".git", ".obsidian", ".trash"}
EXCLUDED_SUBJECTS = {"Proyecto"}
EXCLUDED_FILES = {
    "DAM/Sistema_de_Gestion_Empresarial/Sistemas-de-Gestion-Empresarial-LIBRO.pdf",
    "DAM/Sistema_de_Gestion_Empresarial/Tema 2/UD2. ERP (Enterprise Resource Planning).pdf",
    "DAM/Inglés/Libro Ingles.pdf",
    "DAM/Inglés/Computing-and-Information-Technology.pdf",
    # Datos personales
    "DAM/Inglés/Unit_2/2026-10-05 - Unit 2 - Email.md",
    "DAM/Sistema_de_Gestion_Empresarial/Practica/ListadoClientes_Zoho_Cuentas.csv",
    "DAM/Sistema_de_Gestion_Empresarial/Practica/1-1-b-ListadoClientes.xlsx",
}
EXCLUDED_SUFFIXES = {".class", ".iml"}

# Agrupación de notas según el campo tipo: del frontmatter
TYPE_GROUPS = [
    ("📖 Teoría y apuntes", {"tema", "clase", "guia", "norma", "indice-tema"}),
    ("💻 Ejercicios y actividades", {"ejercicio", "proyecto"}),
    ("✅ Cuestionarios y exámenes", {"cuestionario", "examen"}),
    ("🗣️ Vocabulario", {"vocabulario"}),
    ("📎 Otros", set()),                                    # cajón de sastre
]
STATUS_ICONS = {
    "completo": "✅", "completado": "✅", "terminado": "✅", "resuelto": "✅",
    "en curso": "🕒", "en_curso": "🕒", "pendiente": "⏳",
}
# Callouts de Obsidian → alertas de GitHub (solo admite estas cinco)
CALLOUT_MAP = {
    "tip": "TIP", "success": "TIP", "question": "TIP", "hint": "TIP",
    "warning": "WARNING", "caution": "CAUTION", "danger": "CAUTION", "failure": "CAUTION", "bug": "CAUTION",
    "important": "IMPORTANT",
}


def natural_key(text):
    """Orden 'natural': Tema 2 antes que Tema 10."""
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", text)]


def rel_link(target: Path, from_dir: Path) -> str:
    """Ruta relativa codificada para URL (espacios, tildes...)."""
    return quote(os.path.relpath(target, from_dir).replace("\\", "/"))


def github_slug(heading: str) -> str:
    """Aproximación al ancla que genera GitHub para un encabezado."""
    slug = re.sub(r"[^\w\- ]", "", heading.strip().lower())
    return slug.replace(" ", "-")


class Note:
    """Una nota .md con su frontmatter y su título."""

    def __init__(self, path: Path):
        self.path = path
        self.meta = {}
        self.title = path.stem
        text = path.read_text(encoding="utf-8", errors="replace")
        body = text
        match = re.match(r"^---\n(.*?)\n---\n?", text, re.S)
        if match:
            body = text[match.end():]
            for line in match.group(1).splitlines():
                kv = re.match(r"^(\w+):\s*(.*?)\s*(#.*)?$", line)
                if kv and kv.group(2):
                    self.meta[kv.group(1)] = kv.group(2).strip("'\"")
        h1 = re.search(r"^#\s+(.+)$", body, re.M)
        if h1:
            self.title = re.sub(r"\[¶\]\(.*?\)", "", h1.group(1)).strip()
        self.body = body

    @property
    def type(self):
        return self.meta.get("tipo", "")

    @property
    def status_icon(self):
        return STATUS_ICONS.get(self.meta.get("estado", ""), "")

    def link(self, from_dir: Path) -> str:
        icon = f" {self.status_icon}" if self.status_icon else ""
        return f"[{self.title}]({rel_link(self.path, from_dir)}){icon}"


class Vault:
    """Conoce qué archivos se publican y resuelve wikilinks como Obsidian."""

    def __init__(self):
        self.by_path, self.by_name = {}, {}
        for base in (DAM, RESOURCES):
            for f in sorted(base.rglob("*")):
                if f.is_file() and self.is_published(f):
                    rel = f.relative_to(ROOT).as_posix()
                    key = rel[:-3] if rel.endswith(".md") else rel
                    self.by_path[key] = f
                    name = f.stem if f.suffix == ".md" else f.name
                    self.by_name.setdefault(name, []).append(f)
        self.used_resources = set()

    def is_published(self, f: Path) -> bool:
        rel = f.relative_to(ROOT)
        parts = rel.parts
        if any(p in EXCLUDED_DIRS for p in parts):
            return False
        if parts[0] == "DAM" and len(parts) > 1 and parts[1] in EXCLUDED_SUBJECTS:
            return False
        if f.name == "CLAUDE.md" or f.suffix in EXCLUDED_SUFFIXES:
            return False
        if rel.as_posix() in EXCLUDED_FILES:
            return False
        if f.name == "README.md" and MARK in f.read_text(encoding="utf-8", errors="replace"):
            return False                                   # los README generados no cuentan como notas
        return True

    def resolve(self, target: str):
        target = target.strip()
        if target.startswith("DAM/") and target in self.by_path:
            return self.by_path[target]
        for key in (target, f"DAM/{target}"):
            if key in self.by_path:
                return self.by_path[key]
        # ruta parcial: "Tema 1/Tareas/Nota" → buscar una ruta que acabe así
        if "/" in target:
            for key, f in self.by_path.items():
                if key.endswith("/" + target):
                    return f
        found = self.by_name.get(target.split("/")[-1])
        return found[0] if found else None

    def convert(self, text: str, from_dir: Path) -> str:
        """Pasa el Markdown de Obsidian a Markdown que GitHub entiende."""
        def repl(m):
            embed, inner = m.group(1), m.group(2)
            parts = re.split(r"\\?\|", inner, maxsplit=1)
            target, alias = parts[0], (parts[1] if len(parts) > 1 else None)
            anchor = None
            if "#" in target:
                target, anchor = target.split("#", 1)
            label = alias or (anchor if not target else target.split("/")[-1])
            if not target:                                 # [[#ancla]] dentro de la misma nota
                return label
            f = self.resolve(target)
            if f is None:                                  # enlace roto o archivo no publicado
                return f"{label}"
            if RESOURCES in f.parents:
                self.used_resources.add(f.name)
            url = rel_link(f, from_dir) + (f"#{github_slug(anchor)}" if anchor else "")
            return f"{'!' if embed else ''}[{label}]({url})"

        text = re.sub(r"(!?)\[\[(.+?)\]\]", lambda m: repl(m), text)
        return self.convert_callouts(text)

    def convert_callouts(self, text: str) -> str:
        def repl(m):
            prefix, kind, title = m.group(1), m.group(2).lower(), m.group(3).strip()
            alert = CALLOUT_MAP.get(kind, "NOTE")
            line = f"{prefix}[!{alert}]"
            return line + (f"\n{prefix}**{title}**" if title else "")
        return re.sub(r"^([ \t]*>[ \t]*)\[!(\w+)\][-+]?[ \t]*(.*)$", repl, text, flags=re.M)


class Generator:
    """Escribe los README de los tres niveles."""

    def __init__(self):
        self.vault = Vault()
        self.written = []

    # ---------- utilidades ----------
    def write(self, path: Path, content: str):
        if path.exists() and MARK not in path.read_text(encoding="utf-8", errors="replace"):
            print(f"⚠️  {path.relative_to(ROOT)} existe y no es generado: no lo toco")
            return
        path.write_text(MARK + "\n" + content.rstrip() + "\n", encoding="utf-8")
        self.written.append(path)

    def published(self, folder: Path):
        return [f for f in folder.iterdir() if f.is_file() and self.vault.is_published(f)
                and f.name not in ("README.md", "Indice.md")]

    def subdirs(self, folder: Path):
        return sorted([d for d in folder.iterdir() if d.is_dir() and d.name not in EXCLUDED_DIRS
                       and not d.name.startswith(".")], key=lambda d: natural_key(d.name))

    def notes_in(self, folder: Path, recursive=False):
        files = folder.rglob("*.md") if recursive else folder.glob("*.md")
        return [Note(f) for f in files if self.vault.is_published(f)
                and f.name not in ("README.md", "Indice.md")]

    def grouped_notes(self, notes, from_dir: Path, level="###"):
        lines = []
        remaining = sorted(notes, key=lambda n: natural_key(n.path.name))
        for title, types in TYPE_GROUPS:
            group = [n for n in remaining if n.type in types] if types else remaining
            remaining = [n for n in remaining if n not in group]
            if group:
                lines.append(f"\n{level} {title}\n")
                lines += [f"- {n.link(from_dir)}" for n in group]
        return lines

    def is_code_project(self, folder: Path):
        return (folder / "src").is_dir()

    # ---------- nivel 3: tema ----------
    def topic_readme(self, subject_name: str, subject_dir: Path, topic_dir: Path):
        notes = self.notes_in(topic_dir)
        lines = [f"# {subject_name} · {topic_dir.name}", "",
                 f"[⬅️ Volver a {subject_name}](../README.md) · [🏠 Inicio](../../../README.md)"]
        lines += self.grouped_notes(notes, topic_dir, "##")
        for sub in self.subdirs(topic_dir):
            self.subfolder_section(sub, topic_dir, lines, "##")
        attachments = [f for f in self.published(topic_dir) if f.suffix != ".md"]
        if attachments:
            lines.append("\n## 📎 Adjuntos\n")
            lines += [f"- [{f.name}]({rel_link(f, topic_dir)})" for f in sorted(attachments)]
        self.write(topic_dir / "README.md", "\n".join(lines))
        return len(self.notes_in(topic_dir, recursive=True))

    def subfolder_section(self, sub: Path, from_dir: Path, lines, level):
        rel = sub.relative_to(from_dir).as_posix()
        if self.is_code_project(sub):
            lines.append(f"\n{level} 🧩 Proyecto de código: [{sub.name}]({rel_link(sub, from_dir)})")
            return
        lines.append(f"\n{level} 📁 {rel}")
        lines += self.grouped_notes(self.notes_in(sub), from_dir, level + "#")
        others = [f for f in self.published(sub) if f.suffix != ".md"]
        lines += [f"- 📎 [{f.name}]({rel_link(f, from_dir)})" for f in sorted(others)]
        for deeper in self.subdirs(sub):
            self.subfolder_section(deeper, from_dir, lines, level)

    # ---------- nivel 2: asignatura ----------
    def subject_readme(self, subject_dir: Path):
        index = subject_dir / "Indice.md"
        index_note = Note(index) if index.exists() else None
        name = subject_dir.name.replace("_", " ")
        if index_note:
            name = re.sub(r"\s*[—-]\s*[ÍI]ndice\s*$", "", index_note.title).strip()

        topics = []
        for topic_dir in self.subdirs(subject_dir):
            count = self.topic_readme(name, subject_dir, topic_dir)
            topics.append((topic_dir, count))

        lines = [f"# {name}", "", "[🏠 Volver al inicio](../../README.md)", ""]
        if topics:
            lines += ["## 📂 Temas", "", "| Carpeta | Notas |", "| --- | --- |"]
            lines += [f"| [{d.name}]({rel_link(d / 'README.md', subject_dir)}) | {c} |" for d, c in topics]
            lines.append("")
        loose = self.notes_in(subject_dir)
        if loose and not topics:                           # p. ej. Acceso a datos: notas en la raíz
            lines.append("## 📂 Notas por tema")
            by_topic = {}
            for n in loose:
                by_topic.setdefault(n.meta.get("tema", "General"), []).append(n)
            for t in sorted(by_topic, key=natural_key):
                label = f"Tema {t}" if t[:1].isdigit() else t
                lines.append(f"\n### {label}")
                lines += self.grouped_notes(by_topic[t], subject_dir, "####")
            lines.append("")
        elif loose:
            lines.append("## 📄 Notas generales")
            lines += self.grouped_notes(loose, subject_dir)
            lines.append("")
        attachments = [f for f in self.published(subject_dir) if f.suffix != ".md"]
        if attachments:
            lines += ["## 📎 Adjuntos", ""]
            lines += [f"- [{f.name}]({rel_link(f, subject_dir)})" for f in sorted(attachments)]
            lines.append("")
        if index_note:
            body = re.sub(r"^#\s+.+\n", "", index_note.body, count=1)
            body = re.sub(r"^(#{1,5})\s", r"#\1 ", body, flags=re.M)   # baja un nivel los títulos
            lines += ["---", "", "## 🗂️ Índice de la asignatura", "",
                      "> Copia del `Indice.md` de Obsidian con los enlaces adaptados a GitHub.", "",
                      self.vault.convert(body, subject_dir).strip()]
        self.write(subject_dir / "README.md", "\n".join(lines))
        total = len(self.notes_in(subject_dir, recursive=True))
        return name, subject_dir, len(topics), total

    # ---------- nivel 1: portada ----------
    def main_readme(self, subjects):
        lines = [
            "# 📚 Apuntes de 2º DAM",
            "",
            "Apuntes, ejercicios y material de estudio del segundo curso del **Grado Superior de "
            "Desarrollo de Aplicaciones Multiplataforma** (IES El Saladillo, Algeciras), curso 2026-27.",
            "",
            "## Asignaturas",
            "",
            "| Asignatura | Temas | Notas |",
            "| --- | --- | --- |",
        ]
        for name, d, topics, total in subjects:
            lines.append(f"| [{name}]({rel_link(d / 'README.md', ROOT)}) | {topics or '—'} | {total} |")
        lines += [
            f"| Proyecto intermodular · WarrantyKeep | — | [repositorio propio]({PROJECT_URL}) |",
            "",
            "## Cómo está organizado",
            "",
            "```",
            "README.md                  ← estás aquí",
            "DAM/<Asignatura>/README.md ← índice de la asignatura",
            "DAM/<Asignatura>/Tema N/README.md ← notas, ejercicios y actividades del tema",
            "resources/                 ← imágenes que usan los apuntes",
            "```",
            "",
            "> [!NOTE]",
            "> Las notas están escritas en [Obsidian](https://obsidian.md). GitHub no entiende sus "
            "`[[wikilinks]]` ni algunos de sus *callouts*, así que dentro de las notas verás esos enlaces "
            "como texto. Los README sí usan enlaces normales. Para la mejor experiencia, clona el repo y "
            "ábrelo como bóveda de Obsidian.",
            "",
            "Los README se generan con `python3 scripts/generar_readmes.py`.",
        ]
        self.write(ROOT / "README.md", "\n".join(lines))

    # ---------- .gitignore: lista blanca de resources ----------
    def update_gitignore(self):
        start, end = "# >>> resources usados (generado)", "# <<< resources usados (generado)"
        block = [start, "resources/*"] + [f"!resources/{n}" for n in sorted(self.vault.used_resources)] + [end]
        text = GITIGNORE.read_text(encoding="utf-8") if GITIGNORE.exists() else ""
        if start in text:
            text = re.sub(re.escape(start) + r".*?" + re.escape(end), "\n".join(block), text, flags=re.S)
        else:
            text = text.rstrip() + "\n\n" + "\n".join(block) + "\n"
        GITIGNORE.write_text(text, encoding="utf-8")

    def collect_resources(self):
        """Recorre todas las notas publicadas para saber qué adjuntos de resources/ se usan."""
        for f in DAM.rglob("*.md"):
            if self.vault.is_published(f):
                self.vault.convert(f.read_text(encoding="utf-8", errors="replace"), f.parent)

    # ---------- verificación ----------
    def check_links(self):
        bad, total = [], 0
        for readme in self.written:
            text = re.sub(r"```.*?```", "", readme.read_text(encoding="utf-8"), flags=re.S)
            for url in re.findall(r"\]\(([^)]+)\)", text):
                if url.startswith("http"):
                    continue
                total += 1
                target = (readme.parent / unquote(url.split("#")[0])).resolve()
                if not target.exists() or (target.is_file() and not self.vault.is_published(target)
                                           and target.name != "README.md"):
                    bad.append((readme.relative_to(ROOT), url))
        for b in bad:
            print("ROTO", *b)
        print(f"README generados: {len(self.written)} · enlaces: {total} · rotos: {len(bad)}")
        return not bad

    def run(self):
        subjects = [self.subject_readme(d) for d in self.subdirs(DAM) if d.name not in EXCLUDED_SUBJECTS]
        self.main_readme(subjects)
        self.collect_resources()
        self.update_gitignore()
        return self.check_links()


if __name__ == "__main__":
    sys.exit(0 if Generator().run() else 1)
