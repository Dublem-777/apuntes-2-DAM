---
asignatura: SGE
tema: 1
tipo: ejercicio
estado: en curso
fecha: 2026-10-06
tags:
  - DAM/sge/crm
  - DAM/sge/practica
---
**Alumno:** Daniel Madrid Mérida · **Módulo:** Sistema de Gestión Empresarial · 2.º DAM  
**Consulta de planes y ayuda:**  08 de octubre de 2026

![Portal de aplicaciones de Zoho con acceso a CRM](<Evidencias/captura-portal.png>)

*Portal de productos de Zoho; se identifica CRM como aplicación del ecosistema.*

Zoho CRM es una aplicación de gestión de relaciones con clientes (CRM) ofrecida en la nube. Centraliza clientes potenciales, cuentas, contactos, oportunidades, actividades y comunicaciones; sus informes y paneles ayudan a consultar la actividad comercial. Un flujo habitual consiste en configurar la organización y sus permisos, importar o crear cuentas y contactos, registrar oportunidades y seguimientos, conectar el correo y revisar informes.

### Recorrido funcional y conceptos básicos

La información se organiza en módulos. Un **cliente potencial (lead)** es un posible cliente todavía no cualificado; tras validar su interés puede convertirse en **contacto** (persona) y **cuenta** (empresa), y asociarse a una **oportunidad** o trato comercial. Esta separación evita tratar el nombre de una empresa como si fuera el de una persona. En la importación de esta práctica, el libro mezcla los datos de empresa y del contacto en una fila, por lo que es importante decidir primero qué registro se desea crear y dónde guardar los datos complementarios.

Las **actividades** —tareas, llamadas y reuniones— permiten registrar la siguiente acción, el responsable, la fecha límite y su estado. Es útil redactar asuntos concretos, vincular cada actividad con el contacto/cuenta correcto y cerrar o reprogramar las tareas al completarlas. Los **informes** resumen los registros con filtros y agrupaciones; los **paneles** presentan esos informes o gráficos en una vista rápida. Revisar la ayuda del módulo antes de importar evita confundir entidades y permite comprobar qué campos son obligatorios.

Un orden recomendado es: (1) revisar perfiles, idioma, zona horaria y moneda; (2) limpiar la hoja y mapear columnas; (3) importar una muestra pequeña y verificarla; (4) completar el resto controlando duplicados; (5) registrar actividades y comunicaciones; y (6) crear informes para evaluar resultados. La documentación consultada está enlazada al final.

<!-- pdf-page-break -->

## 1. Organización y configuración básica

La captura de configuración permite reconocer la instancia abierta y algunos datos regionales. En ella aparecen el nombre de organización «ejemplo (1)», la zona horaria Europe/Madrid y el acceso a la URL de CRM. Se han ocultado en la imagen que se incorpora al informe el correo, teléfono e identificadores de cuenta que no son necesarios para explicar la configuración.

![Detalles de la organización en Zoho CRM](<Evidencias/captura-configuracion-redactada.png>)

*Detalles de organización y zona horaria.*

Para completar la configuración que pide la actividad, se propone usar una empresa ficticia coherente y completar todos sus datos en **Configuración → Detalles de empresa**:

| Campo | Valor de ejemplo (ficticio) |
|---|---|
| Empresa | Nexo Comercial, S.L. |
| Actividad | Distribución y soporte de soluciones informáticas |
| País / zona horaria | España / Europe-Madrid |
| Moneda | EUR |
| Dirección | Calle de la Innovación, 12, Madrid |

La captura no acredita que estos datos ficticios se hayan aplicado: muestra otra denominación y no evidencia una dirección corporativa completa. Hay que sustituir los datos de ejemplo en la instancia solo si la actividad exige específicamente la empresa ficticia.

<!-- pdf-page-break -->

## 2. Importación de los datos

El libro adjunto contiene **124 filas** con código de cliente, empresa, persona de contacto, identificador fiscal, teléfono y dirección. Se preparó `ListadoClientes_Zoho_Cuentas.csv`, con encabezados adaptados y columnas de cuenta y facturación. Los campos «Contact Person», «Tax ID» y «Region» requieren campos personalizados si se importan como cuentas. El país se completa como España salvo el registro de Andorra.

![Asistente de carga de fichero en el módulo Contactos](<Evidencias/captura-importacion.png>)

*Zoho muestra el asistente «Importar Contactos» y el fichero cargado.*

La captura indica que el fichero se cargó en el módulo **Contactos**. El CSV se había preparado con estructura de **Cuentas**; por tanto, hay que revisar la asignación de campos y algunos registros importados para confirmar que nombre, apellidos y cuenta asociada quedaron correctos. Si el objetivo es tener empresas en el módulo Cuentas, realizar una importación separada allí con el CSV preparado y revisar posibles duplicados antes de confirmar. El archivo original no contiene correos electrónicos de los contactos.

<!-- pdf-page-break -->

## 3. Resultado visible de la importación

![Resumen de importación de contactos en Zoho CRM](<Evidencias/captura-resultado-importacion.png>)

*Figura 4. El resumen de Zoho informa de 124 contactos agregados, 0 actualizados y 0 omitidos.*

Esta pantalla sí acredita que Zoho aceptó **124 registros de Contactos** en esa operación. No demuestra por sí sola que cada columna se asignase al campo deseado ni que las cuentas asociadas sean correctas. Se recomienda abrir varios registros representativos, comprobar nombre, teléfono, empresa asociada y ausencia de duplicados, y corregir la correspondencia si fuera necesario. El dato del resumen debe describirse como contactos importados, no como 124 cuentas.

**Preparación local del CSV de cuentas:** `ListadoClientes_Zoho_Cuentas.csv` conserva código de cliente como Account Number, nombre de empresa como Account Name, y dirección en los campos Billing. Si se importan las empresas, crear previamente los campos de texto personalizados para persona de contacto, identificador fiscal y región. El identificador de cliente puede ayudar a controlar duplicados.

<!-- pdf-page-break -->

## 4. Paneles y componentes gráficos

La herramienta de personalización del panel ofrece varios componentes analíticos. Esta pantalla muestra el selector de componentes, entre ellos **Gráfico** y **KPI**; todavía no es evidencia de un gráfico guardado.

![Selector de componentes del panel de Zoho CRM](<Evidencias/captura-componentes-panel.png>)

*Selector de componentes disponible al personalizar la página de inicio/panel.*

Para representar la base importada, se recomienda construir un gráfico de columnas con el módulo correcto y una agrupación por región. En un panel, el gráfico debería tener un título descriptivo, por ejemplo «Contactos por región», y mostrar claramente la cantidad de registros. Si se busca la distribución de empresas, debe usarse el módulo Cuentas después de comprobar que estén importadas allí.

<!-- pdf-page-break -->

## 5. Configuración del gráfico: estado observado

![Formulario de configuración de un gráfico de columnas](<Evidencias/captura-configuracion-grafico.png>)

*Configuración preliminar: tipo de gráfico de columnas y medida «Cantidad de Contactos».*

La pantalla muestra un gráfico de columnas de Contactos con medida de cantidad, pero el campo **Agrupamiento** aún indica «Seleccionar agrupamiento»; el nombre visible tampoco es descriptivo. Por ello, la captura documenta el inicio de la configuración, no un gráfico final ni una visualización de clientes por zona. Para terminarlo, seleccionar como agrupamiento el campo Región (o Provincia), definir un nombre legible, pulsar **Fin**, guardar el panel y abrirlo para comprobar los datos. Después, sustituir o complementar esta captura con una imagen del panel ya guardado y con los ejes y leyenda visibles.

<!-- pdf-page-break -->

## 6. Análisis de la cartera y utilidad para decidir

El recuento local de las 124 filas de la hoja adjunta da esta distribución por región:

| Región | Clientes | Porcentaje aproximado |
|---|---:|---:|
| Cataluña | 37 | 29,8 % |
| Aragón | 16 | 12,9 % |
| Castilla y León | 11 | 8,9 % |
| Andalucía | 10 | 8,1 % |
| Madrid | 8 | 6,5 % |
| Extremadura | 6 | 4,8 % |
| Navarra | 6 | 4,8 % |
| Resto de regiones | 30 | 24,2 % |

Las cuatro primeras reúnen 74 clientes (59,7 %). Por provincia destacan Barcelona (24) y Zaragoza (14). Un gráfico de barras por región permite comparar tamaños de forma directa; el gráfico circular puede mostrar porcentajes, aunque resulta menos claro con numerosas categorías.

**Utilidad para la toma de decisiones.** La distribución ayuda a identificar dónde se concentra la cartera, planificar rutas, asignar representantes y localizar áreas con menor cobertura. No permite concluir qué zona es más rentable: conviene cruzar el número de clientes con ventas, oportunidades, costes de desplazamiento y potencial de mercado.

**Importante:** estos recuentos se calcularon sobre el Excel adjunto. No se han extraído de un gráfico terminado en Zoho, y no deben confundirse con la evidencia visual de las Figuras 5 y 6.

### Condiciones de la edición gratuita

La [página oficial de precios](https://www.zoho.com/crm/zohocrm-pricing.html) consultada anuncia una edición gratuita permanente para **hasta tres usuarios**, con funciones iniciales como leads, documentos y aplicación móvil. No tiene coste de licencia mientras se utilice esa edición. El número de usuarios y las funciones disponibles están limitados; no se debe presuponer que informes, paneles, integraciones, automatizaciones, almacenamiento o soporte de ediciones de pago estén incluidos. Las prestaciones pueden variar según región y cambios del proveedor, por lo que hay que verificar la comparativa vigente en la propia cuenta. También son aplicables los términos de servicio, privacidad y normativa de protección de datos. Gratuidad no significa código abierto ni alojamiento local.

<!-- pdf-page-break -->

## 7. Arquitectura y seguimiento

### SaaS y arquitectura multi-tenant

**SaaS (Software as a Service):** el proveedor opera aplicación e infraestructura en la nube y el usuario accede mediante navegador o aplicación móvil. El proveedor mantiene el servicio; la organización administra datos, usuarios, permisos y configuración. Para acceder se requiere conexión a Internet.

**Multi-tenant (multicliente):** varias organizaciones utilizan una plataforma e infraestructura compartidas y mantienen espacios lógicos de datos separados. El aislamiento y los controles de acceso deben impedir que una organización consulte los registros de otra. Compartir infraestructura no significa compartir la información comercial. El cliente también debe configurar correctamente los permisos. Esta explicación conceptual sigue la arquitectura descrita en el enunciado; no presupone detalles internos que el proveedor no publique.

## Conclusión

En conclusión, Zoho CRM puede centralizar contactos y seguimientos y ayudar a visualizar la composición geográfica de una cartera. Para que el análisis sea fiable, primero deben validarse la importación y las relaciones entre registros; después, completar el gráfico y contrastar la distribución con indicadores de venta. La evidencia disponible confirma parte del proceso, pero aún no basta para certificar todas las actividades solicitadas.

