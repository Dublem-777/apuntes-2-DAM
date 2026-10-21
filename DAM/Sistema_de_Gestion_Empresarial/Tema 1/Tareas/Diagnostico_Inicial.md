---
asignatura: SGE
tema: Diagnóstico inicial
tipo: ejercicio
estado: terminado
fecha: 2026-09-17
tags:
  - DAM/ejercicio
  - DAM/SGE
fuente: Documentos/Notas/diagnostico.txt
---

# Diagnóstico Inicial — SGE

> [!info] Enunciado
> Cuestionario de diagnóstico al inicio del módulo: conceptos de ERP/CRM, integración de áreas de empresa, bases de datos/servidores/apps web, virtualización y Docker, y conocimiento de Odoo.

**Fuente:** diagnostico.txt (Notas)
**Dificultad:** nivel conceptual (diagnóstico inicial del módulo)

---

## 1. ¿Qué entiendes por ERP y CRM?

**ERP:** programa que une todas las áreas de una empresa (contabilidad, ventas, almacén, RRHH...) en un solo sistema con una única base de datos. Ejemplos: SAP, Odoo.

**CRM:** programa centrado en el cliente: guarda contactos, ventas y reclamaciones,
y ayuda a fidelizarlos. Ejemplos: Salesforce, HubSpot.

**Diferencia:** el ERP gestiona lo interno de la empresa y el CRM la relación con clientes.

## 2. ¿Qué áreas de una empresa deberían compartir información?

**Todas.** Ventas con almacén (para saber qué hay de stock), ventas y compras con
contabilidad (cada operación genera facturas), RRHH con contabilidad (nóminas)...
Si cada área usa su propio Excel, los datos se duplican y se contradicen.
Compartir la información evita repetir trabajo y da datos fiables para decidir.

## 3. ¿Qué sabes sobre bases de datos, servidores y aplicaciones web?

**Bases de datos:** guardan la información organizada en tablas (MySQL, PostgreSQL)
y se consultan con SQL.

**Servidores:** ordenador que está siempre encendido y da un servicio a los demás
(de base de datos, web, etc.).

**Aplicaciones web:** se usan desde el navegador sin instalar nada. Tienen frontend
(lo que se ve), backend (la lógica) y base de datos.

## 4. ¿Has instalado servicios o trabajado con Docker o máquinas virtuales?

Sí, manejo Linux (Fedora). He usado máquinas virtuales (VirtualBox) para probar cosas
aisladas del sistema principal, en mi NAS.

## 5. ¿Conoces Odoo u otro software de gestión? Explica para qué se utiliza

**Odoo** es un ERP libre (hay versión gratuita) hecho en Python con PostgreSQL.
Funciona por módulos: ventas, compras, inventario, contabilidad, CRM... cada uno
se instala como una app y todos comparten la misma base de datos.

**Se usa para** llevar toda la gestión de una empresa en un solo sitio: pedidos,
facturas, stock, contabilidad o tienda online.

**Otros:** SAP, Microsoft Dynamics, Sage, A3ERP (pymes españolas), Dolibarr.

---

## Reflexión

- El diagnóstico conecta con otros módulos del ciclo: BD (Acceso a Datos),
  despliegue de servicios (PSyP) y apps web (DEINT).
- SGE girará sobre implantar/integrar un ERP (Odoo): modelado de datos, módulos
  funcionales y despliegue del servidor.
