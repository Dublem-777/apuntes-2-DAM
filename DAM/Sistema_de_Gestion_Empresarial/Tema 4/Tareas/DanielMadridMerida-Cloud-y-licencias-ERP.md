---
asignatura: SGE
tema: 4
tipo: ejercicio
estado: completo
fecha: 2026-10-28
tags:
  - DAM/ejercicio
  - DAM/sge/cloud-computing
  - DAM/sge/licencias-software
---

# Cloud Computing y licencias de software

**Nombre y apellidos:** Daniel Madrid Mérida

---

## Actividad 4.1

> [!question] Enunciado
> Elabora un pequeño informe explicando las diferencias de los conceptos de Cloud Computing siguientes: IaaS, PaaS, SaaS. Organiza la información en una tabla (Concepto, ¿Qué significa?, ¿Qué ofrece el proveedor?, Ejemplo) y responde a las tres cuestiones.

### Informe

El Cloud Computing (computación en la nube) consiste en usar recursos informáticos (servidores, almacenamiento, programas, etc.) a través de Internet, en lugar de tenerlos en la propia empresa. Se paga por lo que se usa, normalmente con una cuota mensual o según el consumo.

Hay tres modelos de servicio. La diferencia entre ellos está en qué parte gestiona el proveedor y qué parte le toca a la empresa cliente:

- **IaaS (Infraestructura como servicio):** el proveedor alquila la parte física, es decir, servidores virtuales, almacenamiento y red. La empresa se encarga de todo lo demás: instalar el sistema operativo, las bases de datos y los programas, y mantenerlos. Es el modelo que da más control, pero también el que pide más conocimientos técnicos.
- **PaaS (Plataforma como servicio):** el proveedor da, además de la infraestructura, un entorno preparado para programar: sistema operativo, base de datos, herramientas de desarrollo y servidor de aplicaciones. La empresa solo se preocupa de su código y sus datos. Está pensado sobre todo para desarrolladores.
- **SaaS (Software como servicio):** el proveedor da la aplicación terminada y la mantiene él (actualizaciones, copias de seguridad, servidores, etc.). La empresa solo entra desde el navegador con su usuario y la usa. Es el más fácil de usar, pero el que menos se puede cambiar.

Se puede ver como una escalera: cuanto más se sube de IaaS a PaaS y de PaaS a SaaS, más cosas hace el proveedor y menos tiene que hacer la empresa.

### Tabla resumen

| Concepto | ¿Qué significa? | ¿Qué ofrece el proveedor? | Ejemplo |
| --- | --- | --- | --- |
| **IaaS** | Infrastructure as a Service, infraestructura como servicio. | Servidores virtuales, almacenamiento, red y seguridad física del centro de datos. El cliente instala y gestiona el sistema operativo y las aplicaciones. | Amazon Web Services EC2, Microsoft Azure Virtual Machines, Google Compute Engine. |
| **PaaS** | Platform as a Service, plataforma como servicio. | La infraestructura más un entorno listo para desarrollar, probar y ejecutar aplicaciones (sistema operativo, base de datos, lenguajes y herramientas). El cliente solo pone su código. | Google App Engine, Microsoft Azure App Service, Heroku, SAP Business Technology Platform. |
| **SaaS** | Software as a Service, software como servicio. | Una aplicación completa, lista para usar por Internet, con el mantenimiento y las actualizaciones incluidos. El cliente solo la usa. | Gmail, Microsoft 365, Zoho CRM, Odoo Online, SAP S/4HANA Cloud. |

### Cuestiones

#### 1. ERP para una pequeña empresa sin personal informático

Lo más adecuado es SaaS. La empresa no tiene informáticos y no quiere instalar programas ni administrar servidores, y eso es justo lo que da este modelo: el ERP ya está preparado y funcionando en los servidores del proveedor, y los empleados entran por Internet desde el navegador. El proveedor se encarga de las actualizaciones, la seguridad y las copias de seguridad. Además, la forma de pago que describe el enunciado (una cuota periódica por usar el servicio) es la típica del SaaS. Con IaaS o PaaS la empresa tendría que instalar y mantener el ERP por su cuenta, y no tiene personal para hacerlo.

#### 2. Alquilar servidores virtuales para instalar su propio ERP

Lo más adecuado es IaaS. Lo que la empresa quiere alquilar son servidores virtuales, que es lo que ofrece este modelo, y así se ahorra comprar servidores físicos. Pero el ERP lo instala y lo gestiona ella misma, igual que haría en sus propias máquinas: elige el sistema operativo, monta la base de datos, configura el ERP y lo mantiene. No es SaaS porque no contrata el ERP ya hecho, y no es PaaS porque no va a programar una aplicación, sino a instalar una que ya existe.

#### 3. Empresa de software que quiere desarrollar una aplicación de gestión

Debería contratar PaaS. Este modelo está pensado para desarrolladores: el proveedor da la plataforma con todo lo necesario para programar, probar y ejecutar la aplicación (lenguajes, base de datos, servidor de aplicaciones, etc.) y se encarga de los servidores. La empresa se puede centrar solo en crear su aplicación. Con IaaS tendría que preparar y administrar los servidores ella misma, que es lo que no quiere, y SaaS no le sirve porque da una aplicación ya terminada, no un sitio donde crear la suya.

<div style="page-break-after: always;"></div>

## Actividad 4.2. Licencias de software

### Parte 1. Investigación sobre licencias

> [!question] Enunciado
> Explica con tus propias palabras los conceptos de copyright, copyleft y Creative Commons, y responde a las preguntas.

#### Copyright

Es el derecho que tiene el autor sobre su obra (un libro, una canción, una foto, un programa, etc.) solo por haberla creado, sin tener que registrarla. En España se llama derechos de autor y lo regula la Ley de Propiedad Intelectual.

Le da al autor dos tipos de derechos:

- **Derechos morales:** que se le reconozca como autor y que nadie cambie la obra sin su permiso. No se pueden vender ni perder.
- **Derechos de explotación:** decidir quién puede copiar, distribuir, modificar o mostrar en público la obra, y cobrar por ello. Estos sí se pueden ceder o vender. Duran toda la vida del autor y 70 años más.

Si no se dice nada, por defecto todos los derechos están reservados: nadie puede usar la obra sin permiso del autor.

#### Copyleft

Es una forma de usar el propio copyright al revés. El autor sigue siendo el dueño de la obra, pero la publica con una licencia que deja a cualquiera usarla, copiarla, modificarla y distribuirla, con una condición: si alguien la modifica y la reparte, tiene que hacerlo con la misma licencia.

Lo que pretende es que la obra y todas las versiones que salgan de ella sigan siendo libres siempre, y que nadie pueda coger el trabajo y cerrarlo para venderlo como algo propio. El ejemplo más conocido es la licencia GPL de la Free Software Foundation, que es la que usa Linux.

#### Creative Commons

Son unas licencias ya preparadas que el autor puede poner a su obra para decir qué se puede hacer con ella sin tener que pedirle permiso cada vez. Pasan de "todos los derechos reservados" a "algunos derechos reservados".

Se montan combinando cuatro condiciones:

- **BY (reconocimiento):** hay que citar al autor. La llevan todas.
- **NC (no comercial):** no se puede usar para ganar dinero.
- **ND (sin obras derivadas):** no se puede modificar.
- **SA (compartir igual):** las obras derivadas tienen que llevar la misma licencia. Es el copyleft dentro de Creative Commons.

Se usan sobre todo para contenidos culturales y educativos: textos, fotos, música, vídeos, presentaciones, apuntes, etc. Por ejemplo, Wikipedia usa la licencia CC BY-SA.

#### ¿Qué diferencias existen entre copyright y copyleft?

| Aspecto                  | Copyright                                                         | Copyleft                                                         |
| ------------------------ | ----------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Idea**                 | Proteger la obra y que el autor controle su uso.                  | Que la obra se pueda usar y compartir libremente.                |
| **Permisos por defecto** | Todos los derechos reservados. Hace falta permiso para casi todo. | Se permite usar, copiar, modificar y distribuir.                 |
| **Obras derivadas**      | Solo con permiso del autor.                                       | Se pueden hacer, pero tienen que llevar la misma licencia libre. |
| **Ejemplo**              | Microsoft Windows, una película comercial.                        | Linux (GPL), Wikipedia (CC BY-SA).                               |

El copyleft no va en contra del copyright, sino que se apoya en él: como el autor tiene el copyright, puede elegir una licencia que obligue a mantener la obra libre.

#### ¿Las licencias Creative Commons son adecuadas para distribuir programas informáticos?

No. La propia organización Creative Commons recomienda no usarlas para software. Las razones son:

- No dicen nada del código fuente, que es lo que importa en un programa. Una licencia de software libre obliga a dar el código o deja claro cómo se puede usar.
- No tratan temas propios del software, como las patentes o qué pasa al mezclar el programa con otras librerías.
- No son compatibles con licencias de software como la GPL, así que crean problemas al juntar código.

Para programas es mejor usar licencias hechas para eso, como GPL, LGPL, MIT o Apache. Las Creative Commons sí sirven para lo que acompaña al programa, como el manual, las imágenes o la página web.

#### ¿Un programa Open Source tiene que ser necesariamente gratuito?

No. Open Source quiere decir que el código fuente está disponible y que se puede ver, modificar y redistribuir, pero no dice nada de que no se pueda cobrar. La palabra inglesa "free" de "free software" significa libre, no gratis.

Se puede cobrar por vender copias del programa, por instalarlo, por adaptarlo a una empresa, por la formación o por el soporte técnico. Por ejemplo, Red Hat cobra por su Linux con soporte, y Odoo o Dolibarr tienen versiones libres pero cobran por el alojamiento en la nube, los módulos de pago o la ayuda técnica. Lo que no se puede hacer es impedir que quien tenga el programa lo comparta o lo modifique según la licencia.

### Parte 2. Investigación sobre licencias de ERP

> [!question] Enunciado
> Investiga qué tipo de licencia utilizan SAP, Odoo y Dolibarr. Indica qué producto o edición has investigado, su licencia y la fuente consultada.

| ERP                                      | ¿Propietario u Open Source? | Licencia utilizada                                                                                                                                                                                                                               |
| ---------------------------------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **SAP** (SAP S/4HANA y SAP Business One) | Propietario                 | Licencia comercial propietaria de SAP. El código es cerrado y se paga por usuario, ya sea con licencia perpetua (instalado en la empresa) o con suscripción (S/4HANA Cloud). Las condiciones están en los contratos y términos generales de SAP. |
| **Odoo** (Community Edition)             | Open Source                 | GNU LGPL v3. Es gratis, se puede descargar, modificar y redistribuir.                                                                                                                                                                            |
| **Odoo** (Enterprise Edition)            | Propietario                 | Odoo Enterprise Edition License v1.0. Se paga una suscripción por usuario y añade módulos y funciones que no están en la Community.                                                                                                              |
| **Dolibarr** (Dolibarr ERP & CRM)        | Open Source                 | GNU GPL v3 o posterior. Es gratis y libre. Los módulos de pago de su tienda (DoliStore) pueden tener otra licencia.                                                                                                                              |

| Fuente consultada                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------- |
| SAP. *Agreements*. https://www.sap.com/about/agreements.html                                                                             |
| Odoo. *Licenses*. https://www.odoo.com/documentation/master/legal/licenses.html                                                          |
| Odoo. *Licenses*. https://www.odoo.com/documentation/master/legal/licenses.html                                                          |
| Dolibarr. *Dolibarr ERP & CRM*. https://www.dolibarr.org y archivo COPYING del repositorio oficial: https://github.com/Dolibarr/dolibarr |
Odoo es el caso más curioso, porque es de los dos tipos: el núcleo es libre y la versión Enterprise es propietaria. Dolibarr es libre del todo y SAP es propietario en todos sus productos.

### Parte 3. Reflexión final

> [!question] Enunciado
> Una pequeña empresa con presupuesto limitado necesita un ERP para ventas, clientes, almacén y facturación. ¿Le recomendarías un ERP propietario o uno Open Source? Justifica tu respuesta (coste, personalización, mantenimiento y soporte técnico).

Le recomendaría un ERP Open Source, por ejemplo Odoo Community o Dolibarr. Los dos tienen los módulos que necesita esta empresa (ventas, clientes, almacén y facturación).

- **Coste:** la licencia es gratis, así que el dinero se puede gastar en instalarlo y en formar a los empleados. Un ERP propietario como SAP tiene licencias caras por usuario y está pensado para empresas más grandes.
- **Personalización:** como el código está disponible, se puede adaptar a la forma de trabajar de la empresa y añadir solo los módulos que se usen. En un ERP propietario solo se puede cambiar lo que deje el fabricante, y muchas veces pagando.
- **Mantenimiento:** aquí está la parte mala. Si la empresa no tiene informáticos, alguien tiene que instalarlo, actualizarlo y hacer copias de seguridad. Se puede solucionar contratando la versión en la nube del propio fabricante (Odoo Online, DoliCloud), que por un precio bajo se encarga de todo, o una empresa local que lo mantenga.
- **Soporte técnico:** el soporte oficial de un ERP propietario está incluido y es más fiable. En un Open Source hay una comunidad grande con foros y documentación, y si hace falta se puede pagar soporte a una empresa partner. Lo bueno es que no dependes de un único proveedor: si uno no te convence, puedes cambiar a otro.

Para una empresa pequeña con poco presupuesto, el Open Source sale mucho más barato y cubre lo que necesita. Solo elegiría uno propietario si la empresa fuera a crecer mucho y necesitara funciones muy avanzadas o un soporte oficial garantizado.
