# DATABASE SCHEMA - CONTPAQi Comercial

## TABLE: admAcumulados

**Descripción:** Tabla que almacena valores acumulados por período contable para diferentes entidades del sistema (clientes, productos, proveedores, etc.). Registra importes iniciales y desglosados por cada uno de los 12 períodos del ejercicio fiscal, permitiendo realizar análisis históricos, reportes de tendencias, estadísticas de ventas/compras acumuladas y seguimiento de métricas financieras a lo largo del tiempo. Es fundamental para reportes gerenciales y análisis de desempeño por período.

## Columns

- CIDACUMULADO: INTEGER | PK: YES | Nullable: NO
- CIDTIPOACUMULADO: INTEGER | PK: NO | Nullable: NO
- CIDOWNER1: INTEGER | PK: NO | Nullable: NO
- CIDOWNER2: INTEGER | PK: NO | Nullable: NO
- CIMPORTEMODELO: INTEGER | PK: NO | Nullable: NO
- CIDEJERCICIO: INTEGER | PK: NO | Nullable: NO
- CIMPORTEINICIAL: FLOAT | PK: NO | Nullable: NO
- CIDMONEDA: INTEGER | PK: NO | Nullable: NO
- CIMPORTEPERIODO1: FLOAT | PK: NO | Nullable: NO
- CIMPORTEPERIODO2: FLOAT | PK: NO | Nullable: NO
- CIMPORTEPERIODO3: FLOAT | PK: NO | Nullable: NO
- CIMPORTEPERIODO4: FLOAT | PK: NO | Nullable: NO
- CIMPORTEPERIODO5: FLOAT | PK: NO | Nullable: NO
- CIMPORTEPERIODO6: FLOAT | PK: NO | Nullable: NO
- CIMPORTEPERIODO7: FLOAT | PK: NO | Nullable: NO
- CIMPORTEPERIODO8: FLOAT | PK: NO | Nullable: NO
- CIMPORTEPERIODO9: FLOAT | PK: NO | Nullable: NO
- CIMPORTEPERIODO10: FLOAT | PK: NO | Nullable: NO
- CIMPORTEPERIODO11: FLOAT | PK: NO | Nullable: NO
- CIMPORTEPERIODO12: FLOAT | PK: NO | Nullable: NO
- CTIMESTAMP: VARCHAR(23) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO

---

## TABLE: admAcumuladosTipos

**Descripción:** Catálogo que define los diferentes tipos de acumulados que se pueden generar en el sistema. Especifica qué tipo de información se acumulará (ventas, compras, costos, etc.), qué entidades participan (owner1 y owner2 pueden ser clientes, productos, proveedores), el tipo de actualización (automática o manual), y la moneda en que se registran los acumulados. Es la tabla maestra que configura el comportamiento de los acumulados del sistema.

## Columns

- CIDTIPOACUMULADO: INTEGER | PK: YES | Nullable: NO
- CNOMBRE: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTIPOOWNER1: INTEGER | PK: NO | Nullable: NO
- CTIPOOWNER2: INTEGER | PK: NO | Nullable: NO
- CTIPOACTUALIZACION: INTEGER | PK: NO | Nullable: NO
- CTIPOMONEDA: INTEGER | PK: NO | Nullable: NO

---

## TABLE: admAgentes

**Descripción:** Catálogo de agentes de ventas y cobranza que operan en la empresa. Almacena información completa de vendedores, cobradores y representantes comerciales, incluyendo sus comisiones por venta y cobro, clasificaciones, segmentos contables, y relación con clientes/proveedores específicos. Es esencial para el control de fuerza de ventas, cálculo de comisiones, asignación de territorios y seguimiento de desempeño comercial.

## Columns

- CIDAGENTE: INTEGER | PK: YES | Nullable: NO
- CCODIGOAGENTE: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNOMBREAGENTE: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CFECHAALTAAGENTE: DATETIME | PK: NO | Nullable: NO
- CTIPOAGENTE: INTEGER | PK: NO | Nullable: NO
- CCOMISIONVENTAAGENTE: FLOAT | PK: NO | Nullable: NO
- CCOMISIONCOBROAGENTE: FLOAT | PK: NO | Nullable: NO
- CIDCLIENTE: INTEGER | PK: NO | Nullable: NO
- CIDPROVEEDOR: INTEGER | PK: NO | Nullable: NO
- CIDVALORCLASIFICACION1: INTEGER | PK: NO | Nullable: NO
- CIDVALORCLASIFICACION2: INTEGER | PK: NO | Nullable: NO
- CIDVALORCLASIFICACION3: INTEGER | PK: NO | Nullable: NO
- CIDVALORCLASIFICACION4: INTEGER | PK: NO | Nullable: NO
- CIDVALORCLASIFICACION5: INTEGER | PK: NO | Nullable: NO
- CIDVALORCLASIFICACION6: INTEGER | PK: NO | Nullable: NO
- CSEGCONTAGENTE: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTEXTOEXTRA1: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTEXTOEXTRA2: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTEXTOEXTRA3: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CFECHAEXTRA: DATETIME | PK: NO | Nullable: NO
- CIMPORTEEXTRA1: FLOAT | PK: NO | Nullable: NO
- CIMPORTEEXTRA2: FLOAT | PK: NO | Nullable: NO
- CIMPORTEEXTRA3: FLOAT | PK: NO | Nullable: NO
- CIMPORTEEXTRA4: FLOAT | PK: NO | Nullable: NO
- CTIMESTAMP: VARCHAR(23) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSCAGENTE2: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSCAGENTE3: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO

---

## TABLE: admAlmacenes

**Descripción:** Catálogo de almacenes, bodegas o centros de distribución donde se resguarda el inventario de la empresa. Contiene datos de identificación, ubicación, clasificaciones y segmentos contables de cada almacén. Es fundamental para el control de inventarios multi-almacén, trazabilidad de productos, costeo por ubicación, y generación de reportes de existencias por bodega. Permite manejar operaciones con múltiples puntos de almacenamiento.

## Columns

- CIDALMACEN: INTEGER | PK: YES | Nullable: NO
- CCODIGOALMACEN: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNOMBREALMACEN: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CFECHAALTAALMACEN: DATETIME | PK: NO | Nullable: NO
- CIDVALORCLASIFICACION1: INTEGER | PK: NO | Nullable: NO
- CIDVALORCLASIFICACION2: INTEGER | PK: NO | Nullable: NO
- CIDVALORCLASIFICACION3: INTEGER | PK: NO | Nullable: NO
- CIDVALORCLASIFICACION4: INTEGER | PK: NO | Nullable: NO
- CIDVALORCLASIFICACION5: INTEGER | PK: NO | Nullable: NO
- CIDVALORCLASIFICACION6: INTEGER | PK: NO | Nullable: NO
- CSEGCONTALMACEN: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTEXTOEXTRA1: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTEXTOEXTRA2: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTEXTOEXTRA3: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CFECHAEXTRA: DATETIME | PK: NO | Nullable: NO
- CIMPORTEEXTRA1: FLOAT | PK: NO | Nullable: NO
- CIMPORTEEXTRA2: FLOAT | PK: NO | Nullable: NO
- CIMPORTEEXTRA3: FLOAT | PK: NO | Nullable: NO
- CIMPORTEEXTRA4: FLOAT | PK: NO | Nullable: NO
- CBANDOMICILIO: INTEGER | PK: NO | Nullable: NO
- CTIMESTAMP: VARCHAR(23) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSCALMAC2: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSCALMAC3: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSISTORIG: INTEGER | PK: NO | Nullable: NO

---

## TABLE: admAperturas

**Descripción:** Registro de aperturas y cortes de caja para puntos de venta (POS). Almacena información sobre sesiones de trabajo en cajas registradoras, incluyendo usuario operador, terminal, fechas y horas de apertura y corte, estado de la sesión y factura asociada al cierre. Es crucial para control de efectivo en puntos de venta, conciliación de ingresos diarios, auditoría de operaciones de caja y seguimiento de responsabilidades por turno.

## Columns

- CIDAPERTURA: INTEGER | PK: YES | Nullable: NO
- CIDCAJA: INTEGER | PK: NO | Nullable: NO
- CIDAGENTE: INTEGER | PK: NO | Nullable: NO
- CUSUARIO: VARCHAR(15) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: YES
- CTERMINAL: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CESTADO: INTEGER | PK: NO | Nullable: NO
- CFECHAAPERTURA: DATETIME | PK: NO | Nullable: NO
- CHORAAPERTURA: VARCHAR(6) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CFECHACORTE: DATETIME | PK: NO | Nullable: NO
- CHORACORTE: VARCHAR(6) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CFECHAFACTURA: DATETIME | PK: NO | Nullable: NO
- CIDFACTURA: INTEGER | PK: NO | Nullable: NO
- CTIMESTAMP: VARCHAR(23) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO

---

## TABLE: admAsientosContables

**Descripción:** Catálogo de plantillas de asientos contables predefinidos que se generan automáticamente al afectar documentos en el sistema comercial. Define la estructura, frecuencia, tipo de póliza, origen del número, concepto y diario contable para la integración con CONTPAQi Contabilidad. Permite automatizar la generación de pólizas contables desde operaciones comerciales (ventas, compras, pagos) hacia el sistema contable.

## Columns

- CIDASIENTOCONTABLE: INTEGER | PK: YES | Nullable: NO
- CNUMEROASIENTOCONTABLE: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNOMBREASIENTOCONTABLE: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CFRECUENCIA: INTEGER | PK: NO | Nullable: NO
- CORIGENFECHA: INTEGER | PK: NO | Nullable: NO
- CTIPOPOLIZA: INTEGER | PK: NO | Nullable: NO
- CORIGENNUMERO: INTEGER | PK: NO | Nullable: NO
- CORIGENCONCEPTO: INTEGER | PK: NO | Nullable: NO
- CCONCEPTO: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CDIARIO: VARCHAR(10) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTIMESTAMP: VARCHAR(23) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO

---

## TABLE: admAsocAcumConceptos

**Descripción:** Tabla de asociación que vincula conceptos de documentos (ventas, compras, etc.) con tipos de acumulados. Define cómo cada concepto afecta los acumulados estadísticos, especificando si suma o resta al importe modelo correspondiente. Es fundamental para la actualización automática de estadísticas y acumulados cuando se generan documentos comerciales.

## Columns

- CIDCONCEPTOTIPOACUMULADO: INTEGER | PK: YES | Nullable: NO
- CIDCONCEPTODOCUMENTO: INTEGER | PK: NO | Nullable: NO
- CIDTIPOACUMULADO: INTEGER | PK: NO | Nullable: NO
- CIMPORTEMODELO: INTEGER | PK: NO | Nullable: NO
- CSUMARESTA: INTEGER | PK: NO | Nullable: NO

---

## TABLE: admAsocCargosAbonos

**Descripción:** Tabla que registra la aplicación de pagos (abonos) a facturas o cargos pendientes. Almacena la relación entre documentos de abono (pagos, notas de crédito) y documentos de cargo (facturas, notas de débito), incluyendo importes aplicados, fechas de aplicación y referencias a descuentos por pronto pago, utilidades/pérdidas cambiarias y ajustes de IVA. Es esencial para el control de cuentas por cobrar y pagar, antigüedad de saldos y conciliación de pagos.

## Columns

- CIDAUTOINCSQL: INTEGER | PK: NO | Nullable: NO
- CIDDOCUMENTOABONO: INTEGER | PK: YES | Nullable: NO
- CIDDOCUMENTOCARGO: INTEGER | PK: YES | Nullable: NO
- CIMPORTEABONO: FLOAT | PK: NO | Nullable: NO
- CIMPORTECARGO: FLOAT | PK: NO | Nullable: NO
- CFECHAABONOCARGO: DATETIME | PK: NO | Nullable: NO
- CIDDESCUENTOPRONTOPAGO: INTEGER | PK: NO | Nullable: NO
- CIDUTILIDADPERDIDACAMB: INTEGER | PK: NO | Nullable: NO
- CIDAJUSIVA: INTEGER | PK: NO | Nullable: NO

---

## TABLE: admAsocCargosAbonosImp

**Descripción:** Tabla detallada de impuestos relacionados con la aplicación de cargos y abonos. Registra el desglose de tasas impositivas (IVA, IEPS, retenciones) aplicadas en cada asociación cargo-abono, incluyendo información fiscal detallada como tipo de impuesto, tipo de factor, tasa/cuota, objeto de impuesto, método de pago y proporcionalidad. Es crucial para cumplimiento fiscal, cálculo de impuestos en pagos parciales y generación de complementos de pago en CFDI.

## Columns

- CIDAUTOINCSQL: INTEGER | PK: NO | Nullable: NO
- CIDDOCUMENTOABONO: INTEGER | PK: YES | Nullable: NO
- CIDDOCUMENTOCARGO: INTEGER | PK: YES | Nullable: NO
- CTEXTOTASA: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: YES | Nullable: NO
- CNETO: FLOAT | PK: NO | Nullable: NO
- CTASA: FLOAT | PK: NO | Nullable: NO
- CESDETALLE: INTEGER | PK: NO | Nullable: NO
- CTIPOIMP01: INTEGER | PK: NO | Nullable: NO
- CTIPOFAC01: INTEGER | PK: NO | Nullable: NO
- CTASACUOTA: FLOAT | PK: NO | Nullable: NO
- CESRETEN01: INTEGER | PK: NO | Nullable: NO
- CPROPORC01: FLOAT | PK: NO | Nullable: NO
- CMETODOPAG: VARCHAR(100) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- COBJIMPU01: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CCOMPUTA01: INTEGER | PK: NO | Nullable: NO
- CNOMIMPLOC: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO

---

## TABLE: admAsocLigasPagos

**Descripción:** Tabla de asociación entre ligas de pago electrónico y documentos comerciales. Vincula pagos generados mediante plataformas de pago en línea (PayPal, Stripe, etc.) con los documentos que están siendo pagados, registrando el importe del pago. Facilita la conciliación de pagos electrónicos con facturas y la integración con servicios de pago en la nube.

## Columns

- CIDLIGA: INTEGER | PK: YES | Nullable: NO
- CIDDOCTO: INTEGER | PK: YES | Nullable: NO
- CIMPORTEPAGO: FLOAT | PK: NO | Nullable: NO

---

## TABLE: admBanderas

**Descripción:** Catálogo de banderas (imágenes) de países utilizadas en el sistema para identificación visual de monedas y configuraciones regionales. Almacena el nombre, imagen (en formato binario) y clave ISO del país. Se utiliza principalmente en la configuración de monedas extranjeras y en la interfaz de usuario para representación gráfica de divisas.

## Columns

- CIDBANDERA: INTEGER | PK: YES | Nullable: NO
- CNOMBREBANDERA: VARCHAR(40) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CBANDERA: TEXT(16) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: YES
- CCLAVEISO: VARCHAR(3) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO

---

## TABLE: admBitacoras

**Descripción:** Registro de auditoría que almacena todas las operaciones significativas realizadas en el sistema. Contiene información detallada sobre cada evento: fecha, hora, usuario que ejecuta la acción, usuario afectado (si aplica), proceso realizado, datos involucrados, sistema de origen y equipo desde donde se realizó. Es esencial para auditoría de operaciones, rastreo de cambios, seguridad, resolución de problemas y cumplimiento de normativas que requieren trazabilidad de transacciones.

## Columns

- IDBITACORA: INTEGER | PK: YES | Nullable: NO
- FECHA: DATETIME | PK: NO | Nullable: NO
- HORA: VARCHAR(4) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- USUARIO: VARCHAR(15) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- NOMBRE: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- USUARIO2: VARCHAR(15) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- NOMBRE2: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- PROCESO: VARCHAR(100) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- DATOS: VARCHAR(100) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- IDSISTEMA: INTEGER | PK: NO | Nullable: NO
- CTEXTOEX01: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTEXTOEX02: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTEXTOEX03: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CFECHAEX01: DATETIME | PK: NO | Nullable: NO
- CIMPORTE01: FLOAT | PK: NO | Nullable: NO
- CIMPORTE02: FLOAT | PK: NO | Nullable: NO
- CIMPORTE03: FLOAT | PK: NO | Nullable: NO
- EQUIPO: VARCHAR(256) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO

---

## TABLE: admCajas

**Descripción:** Catálogo de cajas registradoras o puntos de venta (POS) configurados en el sistema. Contiene información de cada caja incluyendo código, nombre, estatus (activa/inactiva), fechas de alta/baja, folios de notas y devoluciones, almacén asociado, usuario asignado, cliente por defecto para ventas mostrador, y configuración de reportes. Es fundamental para operación de tiendas retail, control de ventas por punto de venta y gestión de múltiples cajas.

## Columns

- CIDCAJA: INTEGER | PK: YES | Nullable: NO
- CCODIGOCAJA: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNOMBRECAJA: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CESTATUS: INTEGER | PK: NO | Nullable: NO
- CFECHAALTA: DATETIME | PK: NO | Nullable: NO
- CFECHABAJA: DATETIME | PK: NO | Nullable: NO
- CIDVALORCLASIFICACION1: INTEGER | PK: NO | Nullable: NO
- CFOLIONOTA: FLOAT | PK: NO | Nullable: NO
- CSERIENOTA: VARCHAR(11) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CFOLIODEVN: FLOAT | PK: NO | Nullable: NO
- CSERIEDEVN: VARCHAR(11) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDALMACEN: INTEGER | PK: NO | Nullable: NO
- CIDUSUARIO: INTEGER | PK: NO | Nullable: NO
- CIDCLIENTE: INTEGER | PK: NO | Nullable: NO
- CTEXTOEXTRA1: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTEXTOEXTRA2: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTEXTOEXTRA3: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CFECHAEXTRA: DATETIME | PK: NO | Nullable: NO
- CIMPORTEEXTRA1: FLOAT | PK: NO | Nullable: NO
- CIMPORTEEXTRA2: FLOAT | PK: NO | Nullable: NO
- CIMPORTEEXTRA3: FLOAT | PK: NO | Nullable: NO
- CIMPORTEEXTRA4: FLOAT | PK: NO | Nullable: NO
- CTIMESTAMP: VARCHAR(23) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- cReporteApertura: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- cReporteCorte: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- cReporteNota: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO

---

## TABLE: admCapasProducto

**Descripción:** Tabla de control de inventarios por método de capas (PEPS/UEPS). Registra cada capa o lote de producto en almacén, incluyendo información de trazabilidad como número de lote, fechas de caducidad y fabricación, datos de pedimentos aduanales (para importaciones), existencias y costo por capa. Es esencial para empresas que requieren trazabilidad de lotes, control de caducidades, cumplimiento de normas de importación y métodos de costeo por capas (primeras entradas primeras salidas).

## Columns

- CIDCAPA: INTEGER | PK: YES | Nullable: NO
- CIDALMACEN: INTEGER | PK: NO | Nullable: NO
- CIDPRODUCTO: INTEGER | PK: NO | Nullable: NO
- CFECHA: DATETIME | PK: NO | Nullable: NO
- CTIPOCAPA: INTEGER | PK: NO | Nullable: NO
- CNUMEROLOTE: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CFECHACADUCIDAD: DATETIME | PK: NO | Nullable: NO
- CFECHAFABRICACION: DATETIME | PK: NO | Nullable: NO
- CPEDIMENTO: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CADUANA: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CFECHAPEDIMENTO: DATETIME | PK: NO | Nullable: NO
- CTIPOCAMBIO: FLOAT | PK: NO | Nullable: NO
- CEXISTENCIA: FLOAT | PK: NO | Nullable: NO
- CCOSTO: FLOAT | PK: NO | Nullable: NO
- CIDCAPAORIGEN: INTEGER | PK: NO | Nullable: NO
- CTIMESTAMP: VARCHAR(23) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNUMADUANA: INTEGER | PK: NO | Nullable: NO
- CCLAVESAT: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO

---

## TABLE: admCaracteristicas

**Descripción:** Catálogo maestro de características de productos (tallas, colores, modelos, etc.). Define los tipos de características que se pueden asignar a productos para crear variantes o combinaciones. Permite la gestión de productos con múltiples variaciones (ejemplo: una camisa en diferentes tallas y colores), facilitando el control de inventario de productos con características variables y la presentación de opciones en ventas.

## Columns

- CIDPADRECARACTERISTICA: INTEGER | PK: YES | Nullable: NO
- CNOMBRECARACTERISTICA: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO

---

## TABLE: admCaracteristicasValores

**Descripción:** Catálogo de valores específicos para cada característica de producto. Almacena los valores posibles de cada característica (ejemplo: para la característica "Talla" los valores serían CH, M, G, XG; para "Color" serían Rojo, Azul, Verde, etc.). Incluye un nemónico de 3 caracteres para identificación rápida. Se utiliza en conjunto con admCaracteristicas para gestionar productos con variantes.

## Columns

- CIDVALORCARACTERISTICA: INTEGER | PK: YES | Nullable: NO
- CIDPADRECARACTERISTICA: INTEGER | PK: NO | Nullable: NO
- CVALORCARACTERISTICA: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNEMOCARACTERISTICA: VARCHAR(3) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO

---

## TABLE: admClasificaciones

**Descripción:** Catálogo maestro de clasificaciones personalizables que se pueden aplicar a diferentes entidades del sistema (clientes, productos, proveedores, almacenes, agentes). Define los nombres de hasta 6 clasificaciones configurables que permiten segmentar y categorizar información según las necesidades específicas del negocio (ejemplo: Clasificación 1 = Zona Geográfica, Clasificación 2 = Tipo de Cliente, etc.).

## Columns

- CIDCLASIFICACION: INTEGER | PK: YES | Nullable: NO
- CNOMBRECLASIFICACION: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO

---

## TABLE: admClasificacionesValores

**Descripción:** Catálogo de valores específicos para cada clasificación personalizable. Almacena los valores concretos que puede tomar cada clasificación definida en admClasificaciones (ejemplo: para "Zona Geográfica" podría tener valores como "Norte", "Sur", "Centro"). Incluye código abreviado y hasta 3 segmentos contables para integración con contabilidad. Es fundamental para segmentación de información, reportes analíticos y contabilización por segmentos de negocio.

## Columns

- CIDVALORCLASIFICACION: INTEGER | PK: YES | Nullable: NO
- CVALORCLASIFICACION: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDCLASIFICACION: INTEGER | PK: NO | Nullable: NO
- CCODIGOVALORCLASIFICACION: VARCHAR(3) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGCONT1: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGCONT2: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGCONT3: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO

---

## TABLE: admClientes

**Descripción:** Catálogo maestro de clientes y proveedores (catálogo dual). Almacena información completa de clientes y proveedores incluyendo datos fiscales (RFC, CURP, razón social), condiciones comerciales (listas de precios, descuentos, crédito, días de pago), agentes asignados, impuestos y retenciones aplicables, clasificaciones, segmentos contables, datos de contacto y configuración para facturación electrónica (CFDI). Es la tabla central para gestión de relaciones comerciales, control de crédito, cuentas por cobrar/pagar y facturación.

## Columns

- CIDCLIENTEPROVEEDOR: INTEGER | PK: YES | Nullable: NO
- CCODIGOCLIENTE: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CRAZONSOCIAL: VARCHAR(60)

COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO

- CFECHAALTA: DATETIME | PK: NO | Nullable: NO
- CRFC: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CCURP: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CDENCOMERCIAL: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CREPLEGAL: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDMONEDA: INTEGER | PK: NO | Nullable: NO
- CLISTAPRECIOCLIENTE: INTEGER | PK: NO | Nullable: NO
- CDESCUENTODOCTO: FLOAT | PK: NO | Nullable: NO
- CDESCUENTOMOVTO: FLOAT | PK: NO | Nullable: NO
- CBANVENTACREDITO: INTEGER | PK: NO | Nullable: NO
- CIDVALORCLASIFCLIENTE1: INTEGER | PK: NO | Nullable: NO
- CIDVALORCLASIFCLIENTE2: INTEGER | PK: NO | Nullable: NO
- CIDVALORCLASIFCLIENTE3: INTEGER | PK: NO | Nullable: NO
- CIDVALORCLASIFCLIENTE4: INTEGER | PK: NO | Nullable: NO
- CIDVALORCLASIFCLIENTE5: INTEGER | PK: NO | Nullable: NO
- CIDVALORCLASIFCLIENTE6: INTEGER | PK: NO | Nullable: NO
- CTIPOCLIENTE: INTEGER | PK: NO | Nullable: NO
- CESTATUS: INTEGER | PK: NO | Nullable: NO
- CFECHABAJA: DATETIME | PK: NO | Nullable: NO
- CFECHAULTIMAREVISION: DATETIME | PK: NO | Nullable: NO
- CLIMITECREDITOCLIENTE: FLOAT | PK: NO | Nullable: NO
- CDIASCREDITOCLIENTE: INTEGER | PK: NO | Nullable: NO
- CBANEXCEDERCREDITO: INTEGER | PK: NO | Nullable: NO
- CDESCUENTOPRONTOPAGO: FLOAT | PK: NO | Nullable: NO
- CDIASPRONTOPAGO: INTEGER | PK: NO | Nullable: NO
- CINTERESMORATORIO: FLOAT | PK: NO | Nullable: NO
- CDIAPAGO: INTEGER | PK: NO | Nullable: NO
- CDIASREVISION: INTEGER | PK: NO | Nullable: NO
- CMENSAJERIA: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CCUENTAMENSAJERIA: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CDIASEMBARQUECLIENTE: INTEGER | PK: NO | Nullable: NO
- CIDALMACEN: INTEGER | PK: NO | Nullable: NO
- CIDAGENTEVENTA: INTEGER | PK: NO | Nullable: NO
- CIDAGENTECOBRO: INTEGER | PK: NO | Nullable: NO
- CRESTRICCIONAGENTE: INTEGER | PK: NO | Nullable: NO
- CIMPUESTO1: FLOAT | PK: NO | Nullable: NO
- CIMPUESTO2: FLOAT | PK: NO | Nullable: NO
- CIMPUESTO3: FLOAT | PK: NO | Nullable: NO
- CRETENCIONCLIENTE1: FLOAT | PK: NO | Nullable: NO
- CRETENCIONCLIENTE2: FLOAT | PK: NO | Nullable: NO
- CIDVALORCLASIFPROVEEDOR1: INTEGER | PK: NO | Nullable: NO
- CIDVALORCLASIFPROVEEDOR2: INTEGER | PK: NO | Nullable: NO
- CIDVALORCLASIFPROVEEDOR3: INTEGER | PK: NO | Nullable: NO
- CIDVALORCLASIFPROVEEDOR4: INTEGER | PK: NO | Nullable: NO
- CIDVALORCLASIFPROVEEDOR5: INTEGER | PK: NO | Nullable: NO
- CIDVALORCLASIFPROVEEDOR6: INTEGER | PK: NO | Nullable: NO
- CLIMITECREDITOPROVEEDOR: FLOAT | PK: NO | Nullable: NO
- CDIASCREDITOPROVEEDOR: INTEGER | PK: NO | Nullable: NO
- CTIEMPOENTREGA: INTEGER | PK: NO | Nullable: NO
- CDIASEMBARQUEPROVEEDOR: INTEGER | PK: NO | Nullable: NO
- CIMPUESTOPROVEEDOR1: FLOAT | PK: NO | Nullable: NO
- CIMPUESTOPROVEEDOR2: FLOAT | PK: NO | Nullable: NO
- CIMPUESTOPROVEEDOR3: FLOAT | PK: NO | Nullable: NO
- CRETENCIONPROVEEDOR1: FLOAT | PK: NO | Nullable: NO
- CRETENCIONPROVEEDOR2: FLOAT | PK: NO | Nullable: NO
- CBANINTERESMORATORIO: INTEGER | PK: NO | Nullable: NO
- CCOMVENTAEXCEPCLIENTE: FLOAT | PK: NO | Nullable: NO
- CCOMCOBROEXCEPCLIENTE: FLOAT | PK: NO | Nullable: NO
- CBANPRODUCTOCONSIGNACION: INTEGER | PK: NO | Nullable: NO
- CSEGCONTCLIENTE1: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGCONTCLIENTE2: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGCONTCLIENTE3: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGCONTCLIENTE4: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGCONTCLIENTE5: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGCONTCLIENTE6: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGCONTCLIENTE7: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGCONTPROVEEDOR1: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGCONTPROVEEDOR2: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGCONTPROVEEDOR3: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGCONTPROVEEDOR4: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGCONTPROVEEDOR5: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGCONTPROVEEDOR6: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGCONTPROVEEDOR7: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTEXTOEXTRA1: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTEXTOEXTRA2: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTEXTOEXTRA3: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CFECHAEXTRA: DATETIME | PK: NO | Nullable: NO
- CIMPORTEEXTRA1: FLOAT | PK: NO | Nullable: NO
- CIMPORTEEXTRA2: FLOAT | PK: NO | Nullable: NO
- CIMPORTEEXTRA3: FLOAT | PK: NO | Nullable: NO
- CIMPORTEEXTRA4: FLOAT | PK: NO | Nullable: NO
- CBANDOMICILIO: INTEGER | PK: NO | Nullable: NO
- CBANCREDITOYCOBRANZA: INTEGER | PK: NO | Nullable: NO
- CBANENVIO: INTEGER | PK: NO | Nullable: NO
- CBANAGENTE: INTEGER | PK: NO | Nullable: NO
- CBANIMPUESTO: INTEGER | PK: NO | Nullable: NO
- CBANPRECIO: INTEGER | PK: NO | Nullable: NO
- CTIMESTAMP: VARCHAR(23) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CFACTERC01: INTEGER | PK: NO | Nullable: NO
- CCOMVENTA: FLOAT | PK: NO | Nullable: NO
- CCOMCOBRO: FLOAT | PK: NO | Nullable: NO
- CIDMONEDA2: INTEGER | PK: NO | Nullable: NO
- CEMAIL1: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CEMAIL2: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CEMAIL3: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTIPOENTRE: INTEGER | PK: NO | Nullable: NO
- CCONCTEEMA: INTEGER | PK: NO | Nullable: NO
- CFTOADDEND: INTEGER | PK: NO | Nullable: NO
- CIDCERTCTE: INTEGER | PK: NO | Nullable: NO
- CENCRIPENT: INTEGER | PK: NO | Nullable: NO
- CBANCFD: INTEGER | PK: NO | Nullable: NO
- CTEXTOEXTRA4: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTEXTOEXTRA5: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIMPORTEEXTRA5: FLOAT | PK: NO | Nullable: NO
- CIDADDENDA: INTEGER | PK: NO | Nullable: NO
- CCODPROVCO: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CENVACUSE: INTEGER | PK: NO | Nullable: NO
- CCON1NOM: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CCON1TEL: VARCHAR(15) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CQUITABLAN: INTEGER | PK: NO | Nullable: NO
- CFMTOENTRE: INTEGER | PK: NO | Nullable: NO
- CIDCOMPLEM: INTEGER | PK: NO | Nullable: NO
- CDESGLOSAI2: INTEGER | PK: NO | Nullable: NO
- CLIMDOCTOS: INTEGER | PK: NO | Nullable: NO
- CSITIOFTP: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CUSRFTP: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CMETODOPAG: VARCHAR(100) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNUMCTAPAG: VARCHAR(100) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDCUENTA: INTEGER | PK: NO | Nullable: NO
- CUSOCFDI: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CREGIMFISC: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CWHATSAPP: VARCHAR(15) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO

---

## TABLE: admComponentesPaquete

**Descripción:** Tabla que define los componentes individuales que conforman un producto tipo paquete o kit. Registra qué productos específicos (con sus características y unidades) forman parte de cada paquete, permitiendo vender conjuntos de productos como una sola unidad. Es fundamental para gestión de kits de productos, paquetes promocionales, despiece automático de inventarios y control de existencias de productos compuestos.

## Columns

- CIDCOMPONENTE: INTEGER | PK: YES | Nullable: NO
- CIDPAQUETE: INTEGER | PK: NO | Nullable: NO
- CIDPRODUCTO: INTEGER | PK: NO | Nullable: NO
- CCANTIDADPRODUCTO: FLOAT | PK: NO | Nullable: NO
- CIDVALORCARACTERISTICA1: INTEGER | PK: NO | Nullable: NO
- CIDVALORCARACTERISTICA2: INTEGER | PK: NO | Nullable: NO
- CIDVALORCARACTERISTICA3: INTEGER | PK: NO | Nullable: NO
- CTIPOPRODUCTO: INTEGER | PK: NO | Nullable: NO
- CIDUNIDADVENTA: INTEGER | PK: NO | Nullable: NO

---

## TABLE: admConceptos

**Descripción:** Catálogo maestro de conceptos de documentos que define el comportamiento de cada tipo de documento comercial (facturas, pedidos, remisiones, notas de crédito, órdenes de compra, etc.). Configura aspectos fundamentales como: naturaleza del documento (cargo/abono), foliación, campos visibles/editables, fórmulas de cálculo de precios/costos/impuestos/descuentos, integración contable, manejo de inventarios, requisitos de captura, formato de impresión y configuración para facturación electrónica (CFD/CFDI). Es la tabla de configuración más importante del sistema comercial.

## Columns

- CIDCONCEPTODOCUMENTO: INTEGER | PK: YES | Nullable: NO
- CCODIGOCONCEPTO: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNOMBRECONCEPTO: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDDOCUMENTODE: INTEGER | PK: NO | Nullable: NO
- CNATURALEZA: INTEGER | PK: NO | Nullable: NO
- CDOCTOACREDITO: INTEGER | PK: NO | Nullable: NO
- CTIPOFOLIO: INTEGER | PK: NO | Nullable: NO
- CMAXIMOMOVTOS: INTEGER | PK: NO | Nullable: NO
- CCREACLIENTE: INTEGER | PK: NO | Nullable: NO
- CSUMARPROMOCIONES: INTEGER | PK: NO | Nullable: NO
- CFORMAPREIMPRESA: VARCHAR(253) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CORDENCALCULO: INTEGER | PK: NO | Nullable: NO
- CUSANOMBRECTEPROV: INTEGER | PK: NO | Nullable: NO
- CUSARFC: INTEGER | PK: NO | Nullable: NO
- CUSAFECHAVENCIMIENTO: INTEGER | PK: NO | Nullable: NO
- CUSAFECHAENTREGARECEPCION: INTEGER | PK: NO | Nullable: NO
- CUSAMONEDA: INTEGER | PK: NO | Nullable: NO
- CUSATIPOCAMBIO: INTEGER | PK: NO | Nullable: NO
- CUSACODIGOAGENTE: INTEGER | PK: NO | Nullable: NO
- CUSANOMBREAGENTE: INTEGER | PK: NO | Nullable: NO
- CUSADIRECCION: INTEGER | PK: NO | Nullable: NO
- CUSAREFERENCIA: INTEGER | PK: NO | Nullable: NO
- CSERIEPOROMISION: VARCHAR(11) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CANCHOCODIGOPRODUCTO: INTEGER | PK: NO | Nullable: NO
- CUSANOMBREPRODUCTO: INTEGER | PK: NO | Nullable: NO
- CANCHONOMBREPRODUCTO: INTEGER | PK: NO | Nullable: NO
- CUSAALMACEN: INTEGER | PK: NO | Nullable: NO
- CANCHOCODIGOALMACEN: INTEGER | PK: NO | Nullable: NO
- CANCHOIMPORTES: INTEGER | PK: NO | Nullable: NO
- CANCHOPORCENTAJES: INTEGER | PK: NO | Nullable: NO
- CANCHOUNIDADPESOMEDIDA: INTEGER | PK: NO | Nullable: NO
- CUSAPRECIO: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAPRECIO: INTEGER | PK: NO | Nullable: NO
- CUSACOSTOCAPTURADO: INTEGER | PK: NO | Nullable: NO
- CIDFORMULACOSTOCAPTURADO: INTEGER | PK: NO | Nullable: NO
- CUSAEXISTENCIA: INTEGER | PK: NO | Nullable: NO
- CUSANETO: INTEGER | PK: NO | Nullable: NO
- CIDFORMULANETO: INTEGER | PK: NO | Nullable: NO
- CUSAPORCENTAJEIMPUESTO1: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAPORCIMPUESTO1: INTEGER | PK: NO | Nullable: NO
- CUSAIMPUESTO1: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAIMPUESTO1: INTEGER | PK: NO | Nullable: NO
- CUSAPORCENTAJEIMPUESTO2: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAPORCIMPUESTO2: INTEGER | PK: NO | Nullable: NO
- CUSAIMPUESTO2: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAIMPUESTO2: INTEGER | PK: NO | Nullable: NO
- CUSAPORCENTAJEIMPUESTO3: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAPORCIMPUESTO3: INTEGER | PK: NO | Nullable: NO
- CUSAIMPUESTO3: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAIMPUESTO3: INTEGER | PK: NO | Nullable: NO
- CUSAPORCENTAJERETENCION1: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAPORCRETENCION1: INTEGER | PK: NO | Nullable: NO
- CUSARETENCION1: INTEGER | PK: NO | Nullable: NO
- CIDFORMULARETENCION1: INTEGER | PK: NO | Nullable: NO
- CUSAPORCENTAJERETENCION2: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAPORCRETENCION2: INTEGER | PK: NO | Nullable: NO
- CUSARETENCION2: INTEGER | PK: NO | Nullable: NO
- CIDFORMULARETENCION2: INTEGER | PK: NO | Nullable: NO
- CUSAPORCENTAJEDESCUENTO1: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAPORCDESCUENTO1: INTEGER | PK: NO | Nullable: NO
- CUSADESCUENTO1: INTEGER | PK: NO | Nullable: NO
- CIDFORMULADESCUENTO1: INTEGER | PK: NO | Nullable: NO
- CUSAPORCENTAJEDESCUENTO2: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAPORCDESCUENTO2: INTEGER | PK: NO | Nullable: NO
- CUSADESCUENTO2: INTEGER | PK: NO | Nullable: NO
- CIDFORMULADESCUENTO2: INTEGER | PK: NO | Nullable: NO
- CUSAPORCENTAJEDESCUENTO3: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAPORCDESCUENTO3: INTEGER | PK: NO | Nullable: NO
- CUSADESCUENTO3: INTEGER | PK: NO | Nullable: NO
- CIDFORMULADESCUENTO3: INTEGER | PK: NO | Nullable: NO
- CUSAPORCENTAJEDESCUENTO4: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAPORCDESCUENTO4: INTEGER | PK: NO | Nullable: NO
- CUSADESCUENTO4: INTEGER | PK: NO | Nullable: NO
- CIDFORMULADESCUENTO4: INTEGER | PK: NO | Nullable: NO
- CUSAPORCENTAJEDESCUENTO5: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAPORCDESCUENTO5: INTEGER | PK: NO | Nullable: NO
- CUSADESCUENTO5: INTEGER | PK: NO | Nullable: NO
- CIDFORMULADESCUENTO5: INTEGER | PK: NO | Nullable: NO
- CUSATOTAL: INTEGER | PK: NO | Nullable: NO
- CANCHOREFERENCIA: INTEGER | PK: NO | Nullable: NO
- CUSACLASIFICACIONMOVTO: INTEGER | PK: NO | Nullable: NO
- CANCHOVALORCLASIFICACION: INTEGER | PK: NO | Nullable: NO
- CIDFORMULATOTAL: INTEGER | PK: NO | Nullable: NO
- CUSADESCUENTODOC1: INTEGER | PK: NO | Nullable: NO
- CIDFORMULADESDOC1: INTEGER | PK: NO | Nullable: NO
- CUSADESCUENTODOC2: INTEGER | PK: NO | Nullable: NO
- CIDFORMULADESDOC2: INTEGER | PK: NO | Nullable: NO
- CUSAGASTO1: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAGASTO1: INTEGER | PK: NO | Nullable: NO
- CUSAGASTO2: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAGASTO2: INTEGER | PK: NO | Nullable: NO
- CUSAGASTO3: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAGASTO3: INTEGER | PK: NO | Nullable: NO
- CUSATEXTOEXTRA1: INTEGER | PK: NO | Nullable: NO
- CUSATEXTOEXTRA2: INTEGER | PK: NO | Nullable: NO
- CUSATEXTOEXTRA3: INTEGER | PK: NO | Nullable: NO
- CANCHOTEXTOEXTRA: INTEGER | PK: NO | Nullable: NO
- CUSAFECHAEXTRA: INTEGER | PK: NO | Nullable: NO
- CANCHOFECHAEXTRA: INTEGER | PK: NO | Nullable: NO
- CUSAIMPORTEEXTRA1: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAEXTRA1: INTEGER | PK: NO | Nullable: NO
- CUSAIMPORTEEXTRA2: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAEXTRA2: INTEGER | PK: NO | Nullable: NO
- CUSAIMPORTEEXTRA3: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAEXTRA3: INTEGER | PK: NO | Nullable: NO
- CUSAIMPORTEEXTRA4: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAEXTRA4: INTEGER | PK: NO | Nullable: NO
- CUSATEXTOEXTRA1DOC: INTEGER | PK: NO | Nullable: NO
- CUSATEXTOEXTRA2DOC: INTEGER | PK: NO | Nullable: NO
- CUSATEXTOEXTRA3DOC: INTEGER | PK: NO | Nullable: NO
- CUSAFECHAEXTRADOC: INTEGER | PK: NO | Nullable: NO
- CUSAIMPORTEEXTRA1DOC: INTEGER | PK: NO | Nullable: NO
- CUSAIMPORTEEXTRA2DOC: INTEGER | PK: NO | Nullable: NO
- CUSAIMPORTEEXTRA3DOC: INTEGER | PK: NO | Nullable: NO
- CUSAIMPORTEEXTRA4DOC: INTEGER | PK: NO | Nullable: NO
- CUSAEXTRACOMOGASTO: INTEGER | PK: NO | Nullable: NO
- CUSAOBSERVACIONES: INTEGER | PK: NO | Nullable: NO
- CPRESENTAFISCAL: INTEGER | PK: NO | Nullable: NO
- CPRESENTAREFERENCIA: INTEGER | PK: NO | Nullable: NO
- CPRESENTACONDICIONES: INTEGER | PK: NO | Nullable: NO
- CPRESENTAENVIO: INTEGER | PK: NO | Nullable: NO
- CPRESENTADETALLE: INTEGER | PK: NO | Nullable: NO
- CPRESENTAIMPRIMIR: INTEGER | PK: NO | Nullable: NO
- CPRESENTAPAGAR: INTEGER | PK: NO | Nullable: NO
- CPRESENTASALDAR: INTEGER | PK: NO | Nullable: NO
- CPRESENTADOCUMENTAR: INTEGER | PK: NO | Nullable: NO
- CPRESENTAGASTOSCOMPRA: INTEGER | PK: NO | Nullable: NO
- CSEGCONTCONCEPTO: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CBANENCABEZADO: INTEGER | PK: NO | Nullable: NO
- CBANMOVIMIENTO: INTEGER | PK: NO | Nullable: NO
- CBANDESCUENTO: INTEGER | PK: NO | Nullable: NO
- CBANIMPUESTO: INTEGER | PK: NO | Nullable: NO
- CBANACCIONAUTOMATICA: INTEGER | PK: NO | Nullable: NO
- CTIMESTAMP: VARCHAR(23) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNOFOLIO: FLOAT | PK: NO | Nullable: NO
- CIDPROCESOSEGURIDAD: INTEGER | PK: NO | Nullable: NO
- CUSAGTOMOV: INTEGER | PK: NO | Nullable: NO
- CUSASCMOV: INTEGER | PK: NO | Nullable: NO
- CIDASTOCON: INTEGER | PK: NO | Nullable: NO
- CSCCPTO2: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSCCPTO3: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSCMOVTO: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDCONAUTO: INTEGER | PK: NO | Nullable: NO
- CIDALMASUM: INTEGER | PK: NO | Nullable: NO
- CUSACOMVTA: INTEGER | PK: NO | Nullable: NO
- CIDPRSEG02: INTEGER | PK: NO | Nullable: NO
- CIDPRSEG03: INTEGER | PK: NO | Nullable: NO
- CIDPRSEG04: INTEGER | PK: NO | Nullable: NO
- CIDPRSEG05: INTEGER | PK: NO | Nullable: NO
- CFORMAAJ01: INTEGER | PK: NO | Nullable: NO
- CIDPRSEG06: INTEGER | PK: NO | Nullable: NO
- CAPFORMULA: INTEGER | PK: NO | Nullable: NO
- CESCFD: INTEGER | PK: NO | Nullable: NO
- CIDFIRMARL: INTEGER | PK: NO | Nullable: NO
- CGDAPASSW: INTEGER | PK: NO | Nullable: NO
- CEMITEYENT: INTEGER | PK: NO | Nullable: NO
- CBANCFD: INTEGER | PK: NO | Nullable: NO
- CREPIMPCFD: VARCHAR(253) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDDIRSUCU: INTEGER | PK: NO | Nullable: NO
- CBANDIRSUC: INTEGER | PK: NO | Nullable: NO
- CVERFACELE: INTEGER | PK: NO | Nullable: NO
- CCALFECHAS: INTEGER | PK: NO | Nullable: NO
- CTIPCAMTR1: INTEGER | PK: NO | Nullable: NO
- CTIPCAMTR2: INTEGER | PK: NO | Nullable: NO
- CCONSOLIDA: INTEGER | PK: NO | Nullable: NO
- CENVIODIG: INTEGER | PK: NO | Nullable: NO
- CBANTRANS: INTEGER | PK: NO | Nullable: NO
- CCONFNOAPR: INTEGER | PK: NO | Nullable: NO
- CNOAPROB: INTEGER | PK: NO | Nullable: NO
- CAUTOIMPR: INTEGER | PK: NO | Nullable: NO
- CRECIBECFD: INTEGER | PK: NO | Nullable: NO
- CSISTORIG: INTEGER | PK: NO | Nullable: NO
- CIDCPTODE1: INTEGER | PK: NO | Nullable: NO
- CIDCPTODE2: INTEGER | PK: NO | Nullable: NO
- CIDCPTODE3: INTEGER | PK: NO | Nullable: NO
- CPLAMIGCFD: VARCHAR(253) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDPRSEG07: INTEGER | PK: NO | Nullable: NO
- CRESERVADO: INTEGER | PK: NO | Nullable: NO
- CVERREFER: INTEGER | PK: NO | Nullable: NO
- CVERDOCORI: INTEGER | PK: NO | Nullable: NO
- CCBB: INTEGER | PK: NO | Nullable: NO
- CCARTAPOR: INTEGER | PK: NO | Nullable: NO
- CCOMPDONAT: INTEGER | PK: NO | Nullable: NO
- COBSXML: INTEGER | PK: NO | Nullable: NO
- CRUTAENTREGA: VARCHAR(253) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CPREFIJOCONCEPTO: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CREGIMFISC: VARCHAR(100) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CCOMPEDUCA: INTEGER | PK: NO | Nullable: NO
- CMETODOPAG: VARCHAR(100) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CVERESQUE: VARCHAR(6) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDFIRMADSL: VARCHAR(40) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CORDENCAPTURA: VARCHAR(52) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CESTATUS: INTEGER | PK: NO | Nullable: NO
- CIDMONEDA: INTEGER | PK: NO | Nullable: NO
- CIDCUENTA: INTEGER | PK: NO | Nullable: NO
- CCLAVESAT: VARCHAR(8) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDPRSEG08: INTEGER | PK: NO | Nullable: NO
- CUSAOBJIMP: INTEGER | PK: NO | Nullable: NO

---

## TABLE: admConceptosBack

**Descripción:** Tabla de respaldo (backup) del catálogo de conceptos. Almacena una copia de seguridad de la configuración de conceptos de documentos, utilizada para restauración en caso de errores o para mantener historial de cambios en la configuración. Tiene la misma estructura que admConceptos y sirve como mecanismo de recuperación ante modificaciones incorrectas.

## Columns

- CIDCONCEPTODOCUMENTO: INTEGER | PK: YES | Nullable: NO
- CCODIGOCONCEPTO: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNOMBRECONCEPTO: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDDOCUMENTODE: INTEGER | PK: NO | Nullable: NO
- CNATURALEZA: INTEGER | PK: NO | Nullable: NO
- CDOCTOACREDITO: INTEGER | PK: NO | Nullable: NO
- CTIPOFOLIO: INTEGER | PK: NO | Nullable: NO
- CMAXIMOMOVTOS: INTEGER | PK: NO | Nullable: NO
- CCREACLIENTE: INTEGER | PK: NO | Nullable: NO
- CSUMARPROMOCIONES: INTEGER | PK: NO | Nullable: NO
- CFORMAPREIMPRESA: VARCHAR(253) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CORDENCALCULO: INTEGER | PK: NO | Nullable: NO
- CUSANOMBRECTEPROV: INTEGER | PK: NO | Nullable: NO
- CUSARFC: INTEGER | PK: NO | Nullable: NO
- CUSAFECHAVENCIMIENTO: INTEGER | PK: NO | Nullable: NO
- CUSAFECHAENTREGARECEPCION: INTEGER | PK: NO | Nullable: NO
- CUSAMONEDA: INTEGER | PK: NO | Nullable: NO
- CUSATIPOCAMBIO: INTEGER | PK: NO | Nullable: NO
- CUSACODIGOAGENTE: INTEGER | PK: NO | Nullable: NO
- CUSANOMBREAGENTE: INTEGER | PK: NO | Nullable: NO
- CUSADIRECCION: INTEGER | PK: NO | Nullable: NO
- CUSAREFERENCIA: INTEGER | PK: NO | Nullable: NO
- CSERIEPOROMISION: VARCHAR(11) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CANCHOCODIGOPRODUCTO: INTEGER | PK: NO | Nullable: NO
- CUSANOMBREPRODUCTO: INTEGER | PK: NO | Nullable: NO
- CANCHONOMBREPRODUCTO: INTEGER | PK: NO | Nullable: NO
- CUSAALMACEN: INTEGER | PK: NO | Nullable: NO
- CANCHOCODIGOALMACEN: INTEGER | PK: NO | Nullable: NO
- CANCHOIMPORTES: INTEGER | PK: NO | Nullable: NO
- CANCHOPORCENTAJES: INTEGER | PK: NO | Nullable: NO
- CANCHOUNIDADPESOMEDIDA: INTEGER | PK: NO | Nullable: NO
- CUSAPRECIO: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAPRECIO: INTEGER | PK: NO | Nullable: NO
- CUSACOSTOCAPTURADO: INTEGER | PK: NO | Nullable: NO
- CIDFORMULACOSTOCAPTURADO: INTEGER | PK: NO | Nullable: NO
- CUSAEXISTENCIA: INTEGER | PK: NO | Nullable: NO
- CUSANETO: INTEGER | PK: NO | Nullable: NO
- CIDFORMULANETO: INTEGER | PK: NO | Nullable: NO
- CUSAPORCENTAJEIMPUESTO1: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAPORCIMPUESTO1: INTEGER | PK: NO | Nullable: NO
- CUSAIMPUESTO1: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAIMPUESTO1: INTEGER | PK: NO | Nullable: NO
- CUSAPORCENTAJEIMPUESTO2: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAPORCIMPUESTO2: INTEGER | PK: NO | Nullable: NO
- CUSAIMPUESTO2: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAIMPUESTO2: INTEGER | PK: NO | Nullable: NO
- CUSAPORCENTAJEIMPUESTO3: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAPORCIMPUESTO3: INTEGER | PK: NO | Nullable: NO
- CUSAIMPUESTO3: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAIMPUESTO3: INTEGER | PK: NO | Nullable: NO
- CUSAPORCENTAJERETENCION1: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAPORCRETENCION1: INTEGER | PK: NO | Nullable: NO
- CUSARETENCION1: INTEGER | PK: NO | Nullable: NO
- CIDFORMULARETENCION1: INTEGER | PK: NO | Nullable: NO
- CUSAPORCENTAJERETENCION2: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAPORCRETENCION2: INTEGER | PK: NO | Nullable: NO
- CUSARETENCION2: INTEGER | PK: NO | Nullable: NO
- CIDFORMULARETENCION2: INTEGER | PK: NO | Nullable: NO
- CUSAPORCENTAJEDESCUENTO1: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAPORCDESCUENTO1: INTEGER | PK: NO | Nullable: NO
- CUSADESCUENTO1: INTEGER | PK: NO | Nullable: NO
- CIDFORMULADESCUENTO1: INTEGER | PK: NO | Nullable: NO
- CUSAPORCENTAJEDESCUENTO2: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAPORCDESCUENTO2: INTEGER | PK: NO | Nullable: NO
- CUSADESCUENTO2: INTEGER | PK: NO | Nullable: NO
- CIDFORMULADESCUENTO2: INTEGER | PK: NO | Nullable: NO
- CUSAPORCENTAJEDESCUENTO3: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAPORCDESCUENTO3: INTEGER | PK: NO | Nullable: NO
- CUSADESCUENTO3: INTEGER | PK: NO | Nullable: NO
- CIDFORMULADESCUENTO3: INTEGER | PK: NO | Nullable: NO
- CUSAPORCENTAJEDESCUENTO4: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAPORCDESCUENTO4: INTEGER | PK: NO | Nullable: NO
- CUSADESCUENTO4: INTEGER | PK: NO | Nullable: NO
- CIDFORMULADESCUENTO4: INTEGER | PK: NO | Nullable: NO
- CUSAPORCENTAJEDESCUENTO5: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAPORCDESCUENTO5: INTEGER | PK: NO | Nullable: NO
- CUSADESCUENTO5: INTEGER | PK: NO | Nullable: NO
- CIDFORMULADESCUENTO5: INTEGER | PK: NO | Nullable: NO
- CUSATOTAL: INTEGER | PK: NO | Nullable: NO
- CANCHOREFERENCIA: INTEGER | PK: NO | Nullable: NO
- CUSACLASIFICACIONMOVTO: INTEGER | PK: NO | Nullable: NO
- CANCHOVALORCLASIFICACION: INTEGER | PK: NO | Nullable: NO
- CIDFORMULATOTAL: INTEGER | PK: NO | Nullable: NO
- CUSADESCUENTODOC1: INTEGER | PK: NO | Nullable: NO
- CIDFORMULADESDOC1: INTEGER | PK: NO | Nullable: NO
- CUSADESCUENTODOC2: INTEGER | PK: NO | Nullable: NO
- CIDFORMULADESDOC2: INTEGER | PK: NO | Nullable: NO
- CUSAGASTO1: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAGASTO1: INTEGER | PK: NO | Nullable: NO
- CUSAGASTO2: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAGASTO2: INTEGER | PK: NO | Nullable: NO
- CUSAGASTO3: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAGASTO3: INTEGER | PK: NO | Nullable: NO
- CUSATEXTOEXTRA1: INTEGER | PK: NO | Nullable: NO
- CUSATEXTOEXTRA2: INTEGER | PK: NO | Nullable: NO
- CUSATEXTOEXTRA3: INTEGER | PK: NO | Nullable: NO
- CANCHOTEXTOEXTRA: INTEGER | PK: NO | Nullable: NO
- CUSAFECHAEXTRA: INTEGER | PK: NO | Nullable: NO
- CANCHOFECHAEXTRA: INTEGER | PK: NO | Nullable: NO
- CUSAIMPORTEEXTRA1: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAEXTRA1: INTEGER | PK: NO | Nullable: NO
- CUSAIMPORTEEXTRA2: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAEXTRA2: INTEGER | PK: NO | Nullable: NO
- CUSAIMPORTEEXTRA3: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAEXTRA3: INTEGER | PK: NO | Nullable: NO
- CUSAIMPORTEEXTRA4: INTEGER | PK: NO | Nullable: NO
- CIDFORMULAEXTRA4: INTEGER | PK: NO | Nullable: NO
- CUSATEXTOEXTRA1DOC: INTEGER | PK: NO | Nullable: NO
- CUSATEXTOEXTRA2DOC: INTEGER | PK: NO | Nullable: NO
- CUSATEXTOEXTRA3DOC: INTEGER | PK: NO | Nullable: NO
- CUSAFECHAEXTRADOC: INTEGER | PK: NO | Nullable: NO
- CUSAIMPORTEEXTRA1DOC: INTEGER | PK: NO | Nullable: NO
- CUSAIMPORTEEXTRA2DOC: INTEGER | PK: NO | Nullable: NO
- CUSAIMPORTEEXTRA3DOC: INTEGER | PK: NO | Nullable: NO
- CUSAIMPORTEEXTRA4DOC: INTEGER | PK: NO | Nullable: NO
- CUSAEXTRACOMOGASTO: INTEGER | PK: NO | Nullable: NO
- CUSAOBSERVACIONES: INTEGER | PK: NO | Nullable: NO
- CPRESENTAFISCAL: INTEGER | PK: NO | Nullable: NO
- CPRESENTAREFERENCIA: INTEGER | PK: NO | Nullable: NO
- CPRESENTACONDICIONES: INTEGER | PK: NO | Nullable: NO
- CPRESENTAENVIO: INTEGER | PK: NO | Nullable: NO
- CPRESENTADETALLE: INTEGER | PK: NO | Nullable: NO
- CPRESENTAIMPRIMIR: INTEGER | PK: NO | Nullable: NO
- CPRESENTAPAGAR: INTEGER | PK: NO | Nullable: NO
- CPRESENTASALDAR: INTEGER | PK: NO | Nullable: NO
- CPRESENTADOCUMENTAR: INTEGER | PK: NO | Nullable: NO
- CPRESENTAGASTOSCOMPRA: INTEGER | PK: NO | Nullable: NO
- CSEGCONTCONCEPTO: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CBANENCABEZADO: INTEGER | PK: NO | Nullable: NO
- CBANMOVIMIENTO: INTEGER | PK: NO | Nullable: NO
- CBANDESCUENTO: INTEGER | PK: NO | Nullable: NO
- CBANIMPUESTO: INTEGER | PK: NO | Nullable: NO
- CBANACCIONAUTOMATICA: INTEGER | PK: NO | Nullable: NO
- CTIMESTAMP: VARCHAR(23) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNOFOLIO: FLOAT | PK: NO | Nullable: NO
- CIDPROCESOSEGURIDAD: INTEGER | PK: NO | Nullable: NO
- CUSAGTOMOV: INTEGER | PK: NO | Nullable: NO
- CUSASCMOV: INTEGER | PK: NO | Nullable: NO
- CIDASTOCON: INTEGER | PK: NO | Nullable: NO
- CSCCPTO2: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSCCPTO3: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSCMOVTO: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDCONAUTO: INTEGER | PK: NO | Nullable: NO
- CIDALMASUM: INTEGER | PK: NO | Nullable: NO
- CUSACOMVTA: INTEGER | PK: NO | Nullable: NO
- CIDPRSEG02: INTEGER | PK: NO | Nullable: NO
- CIDPRSEG03: INTEGER | PK: NO | Nullable: NO
- CIDPRSEG04: INTEGER | PK: NO | Nullable: NO
- CIDPRSEG05: INTEGER | PK: NO | Nullable: NO
- CFORMAAJ01: INTEGER | PK: NO | Nullable: NO
- CIDPRSEG06: INTEGER | PK: NO | Nullable: NO
- CAPFORMULA: INTEGER | PK: NO | Nullable: NO
- CESCFD: INTEGER | PK: NO | Nullable: NO
- CIDFIRMARL: INTEGER | PK: NO | Nullable: NO
- CGDAPASSW: INTEGER | PK: NO | Nullable: NO
- CEMITEYENT: INTEGER | PK: NO | Nullable: NO
- CBANCFD: INTEGER | PK: NO | Nullable: NO
- CREPIMPCFD: VARCHAR(253) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDDIRSUCU: INTEGER | PK: NO | Nullable: NO
- CBANDIRSUC: INTEGER | PK: NO | Nullable: NO
- CVERFACELE: INTEGER | PK: NO | Nullable: NO
- CCALFECHAS: INTEGER | PK: NO | Nullable: NO
- CTIPCAMTR1: INTEGER | PK: NO | Nullable: NO
- CTIPCAMTR2: INTEGER | PK: NO | Nullable: NO
- CCONSOLIDA: INTEGER | PK: NO | Nullable: NO
- CENVIODIG: INTEGER | PK: NO | Nullable: NO
- CBANTRANS: INTEGER | PK: NO | Nullable: NO
- CCONFNOAPR: INTEGER | PK: NO | Nullable: NO
- CNOAPROB: INTEGER | PK: NO | Nullable: NO
- CAUTOIMPR: INTEGER | PK: NO | Nullable: NO
- CRECIBECFD: INTEGER | PK: NO | Nullable: NO
- CSISTORIG: INTEGER | PK: NO | Nullable: NO
- CIDCPTODE1: INTEGER | PK: NO | Nullable: NO
- CIDCPTODE2: INTEGER | PK: NO | Nullable: NO
- CIDCPTODE3: INTEGER | PK: NO | Nullable: NO
- CPLAMIGCFD: VARCHAR(253) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDPRSEG07: INTEGER | PK: NO | Nullable: NO
- CRESERVADO: INTEGER | PK: NO | Nullable: NO
- CVERREFER: INTEGER | PK: NO | Nullable: NO
- CVERDOCORI: INTEGER | PK: NO | Nullable: NO
- CCBB: INTEGER | PK: NO | Nullable: NO
- CCARTAPOR: INTEGER | PK: NO | Nullable: NO
- CCOMPDONAT: INTEGER | PK: NO | Nullable: NO
- COBSXML: INTEGER | PK: NO | Nullable: NO
- CRUTAENTREGA: VARCHAR(253) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CPREFIJOCONCEPTO: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CREGIMFISC: VARCHAR(100) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CCOMPEDUCA: INTEGER | PK: NO | Nullable: NO
- CMETODOPAG: VARCHAR(100) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CVERESQUE: VARCHAR(6) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDFIRMADSL: VARCHAR(40) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CORDENCAPTURA: VARCHAR(52) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CCLAVESAT: VARCHAR(8) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CUSAOBJIMP: INTEGER | PK: NO | Nullable: NO

---

## TABLE: admConfigProveedoresNube

**Descripción:** Tabla de configuración para servicios en la nube de proveedores externos (timbrado de CFDI, servicios web, etc.). Define la activación, vigencia y días de validez de servicios contratados con proveedores externos. Permite gestionar la integración con servicios de terceros para facturación electrónica, pagos en línea y otras funcionalidades cloud.

## Columns

- CIDPROVEEDORSERVICIO: INTEGER | PK: YES | Nullable: NO
- CACTIVO: INTEGER | PK: NO | Nullable: NO
- CTIENEVIGENCIA: INTEGER | PK: NO | Nullable: NO
- CDIASVIGENCIA: INTEGER | PK: NO | Nullable: NO

---

## TABLE: admConversionesUnidad

**Descripción:** Tabla de factores de conversión entre diferentes unidades de medida. Almacena las relaciones matemáticas que permiten convertir cantidades entre unidades distintas (ejemplo: de kilogramos a gramos, de cajas a piezas, de litros a mililitros). Es fundamental para el manejo de productos con múltiples unidades de medida, permitiendo comprar en una unidad y vender en otra, manteniendo la integridad del inventario.

## Columns

- CIDAUTOINCSQL: INTEGER | PK: NO | Nullable: NO
- CIDUNIDAD1: INTEGER | PK: YES | Nullable: NO
- CIDUNIDAD2: INTEGER | PK: YES | Nullable: NO
- CFACTORCONVERSION: FLOAT | PK: NO | Nullable: NO
- CEXPRESIONFACTOR: VARCHAR(11) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO

---

## TABLE: admCostosHistoricos

**Descripción:** Tabla que registra el historial de cambios en los costos de productos por almacén. Almacena cada modificación de costo con su fecha, costo nuevo, costo anterior y movimiento que originó el cambio. Es esencial para análisis de variaciones de costos, auditoría de valuación de inventarios, cálculo de utilidades históricas y seguimiento de tendencias en precios de compra o costos de producción.

## Columns

- CIDCOSTOH: INTEGER | PK: YES | Nullable: NO
- CIDPRODUCTO: INTEGER | PK: NO | Nullable: NO
- CIDALMACEN: INTEGER | PK: NO | Nullable: NO
- CFECHACOSTOH: DATETIME | PK: NO | Nullable: NO
- CCOSTOH: FLOAT | PK: NO | Nullable: NO
- CULTIMOCOSTOH: FLOAT | PK: NO | Nullable: NO
- CIDMOVIMIENTO: INTEGER | PK: NO | Nullable: NO
- CTIMESTAMP: VARCHAR(23) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO

---

## TABLE: admCuentasBancarias

**Descripción:** Catálogo de cuentas bancarias de la empresa. Almacena información completa de cuentas bancarias incluyendo número de cuenta, CLABE interbancaria, banco, moneda, estatus (activa/inactiva), clave SAT, RFC del banco, segmentos contables y asociación con clientes o proveedores. Es fundamental para control de tesorería, conciliación bancaria, emisión de recibos de pago electrónicos (complementos de pago CFDI) y gestión de flujo de efectivo.

## Columns

- CIDCUENTA: INTEGER | PK: YES | Nullable: NO
- CACCOUNTID: VARCHAR(26) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNUMEROCUENTA: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNOMBRECUENTA: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CFECHAALTA: DATETIME | PK: NO | Nullable: NO
- CFECHABAJA: DATETIME | PK: NO | Nullable: NO
- CESTATUS: INTEGER | PK: NO | Nullable: NO
- CCLABE: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CCLAVE: VARCHAR(3) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGCONT01: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGCONT02: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGCONT03: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTEXTOEXTRA1: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTEXTOEXTRA2: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTEXTOEXTRA3: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CFECHAEXTRA: DATETIME | PK: NO | Nullable: NO
- CIMPORTEEXTRA1: FLOAT | PK: NO | Nullable: NO
- CIMPORTEEXTRA2: FLOAT | PK: NO | Nullable: NO
- CIMPORTEEXTRA3: FLOAT | PK: NO | Nullable: NO
- CIMPORTEEXTRA4: FLOAT | PK: NO | Nullable: NO
- CTIMESTAMP: VARCHAR(23) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDMONEDA: INTEGER | PK: NO | Nullable: NO
- CIDCATALOGO: INTEGER | PK: NO | Nullable: NO
- CTIPOCATALOGO: INTEGER | PK: NO | Nullable: NO
- CNOMBANEXT: VARCHAR(254) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CRFCBANCO: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO

---

## TABLE: admDatosAddenda

**Descripción:** Tabla que almacena datos adicionales personalizados (addendas) requeridos por clientes específicos en sus facturas electrónicas. Las addendas son información extra que algunos clientes corporativos solicitan incluir en el CFDI según sus sistemas internos (números de orden de compra, códigos de autorización, referencias de contrato, etc.). Es crucial para cumplir con requisitos específicos de grandes clientes y cadenas comerciales.

## Columns

- CIDAUTOINCSQL: INTEGER | PK: NO | Nullable: NO
- IDADDENDA: INTEGER | PK: YES | Nullable: NO
- TIPOCAT: INTEGER | PK: YES | Nullable: NO
- IDCAT: INTEGER | PK: YES | Nullable: NO
- NUMCAMPO: INTEGER | PK: YES | Nullable: NO
- VALOR: VARCHAR(254) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO

---

## TABLE: admDocumentos

**Descripción:** Tabla transaccional principal que almacena todos los documentos comerciales del sistema (facturas, pedidos, remisiones, notas de crédito, órdenes de compra, cotizaciones, etc.). Contiene el encabezado completo de cada documento incluyendo: identificación (folio, serie, fecha), datos del cliente/proveedor, agente, moneda y tipo de cambio, importes totales (neto, impuestos, retenciones, descuentos, gastos), saldos pendientes, datos de envío, referencias, estado del documento (afectado, cancelado, impreso), información contable, datos fiscales (UUID, lugar de expedición, método de pago) y relación con otros documentos. Es el corazón del sistema comercial.

## Columns

- CIDDOCUMENTO: INTEGER | PK: YES | Nullable: NO
- CIDDOCUMENTODE: INTEGER | PK: NO | Nullable: NO
- CIDCONCEPTODOCUMENTO: INTEGER | PK: NO | Nullable: NO
- CSERIEDOCUMENTO: VARCHAR(11) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CFOLIO: FLOAT | PK: NO | Nullable: NO
- CFECHA: DATETIME | PK: NO | Nullable: NO
- CIDCLIENTEPROVEEDOR: INTEGER | PK: NO | Nullable: NO
- CRAZONSOCIAL: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CRFC: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDAGENTE: INTEGER | PK: NO | Nullable: NO
- CFECHAVENCIMIENTO: DATETIME | PK: NO | Nullable: NO
- CFECHAPRONTOPAGO: DATETIME | PK: NO | Nullable: NO
- CFECHAENTREGARECEPCION: DATETIME | PK: NO | Nullable: NO
- CFECHAULTIMOINTERES: DATETIME | PK: NO | Nullable: NO
- CIDMONEDA: INTEGER | PK: NO | Nullable: NO
- CTIPOCAMBIO: FLOAT | PK: NO | Nullable: NO
- CREFERENCIA: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- COBSERVACIONES: TEXT(16) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: YES
- CNATURALEZA: INTEGER | PK: NO | Nullable: NO
- CIDDOCUMENTOORIGEN: INTEGER | PK: NO | Nullable: NO
- CPLANTILLA: INTEGER | PK: NO | Nullable: NO
- CUSACLIENTE: INTEGER | PK: NO | Nullable: NO
- CUSAPROVEEDOR: INTEGER | PK: NO | Nullable: NO
- CAFECTADO: INTEGER | PK: NO | Nullable: NO
- CIMPRESO: INTEGER | PK: NO | Nullable: NO
- CCANCELADO: INTEGER | PK: NO | Nullable: NO
- CDEVUELTO: INTEGER | PK: NO | Nullable: NO
- CIDPREPOLIZA: INTEGER | PK: NO | Nullable: NO
- CIDPREPOLIZACANCELACION: INTEGER | PK: NO | Nullable: NO
- CESTADOCONTABLE: INTEGER | PK: NO | Nullable: NO
- CNETO: FLOAT | PK: NO | Nullable: NO
- CIMPUESTO1: FLOAT | PK: NO | Nullable: NO
- CIMPUESTO2: FLOAT | PK: NO | Nullable: NO
- CIMPUESTO3: FLOAT | PK: NO | Nullable: NO
- CRETENCION1: FLOAT | PK: NO | Nullable: NO
- CRETENCION2: FLOAT | PK: NO | Nullable: NO
- CDESCUENTOMOV: FLOAT | PK: NO | Nullable: NO
- CDESCUENTODOC1: FLOAT | PK: NO | Nullable: NO
- CDESCUENTODOC2: FLOAT | PK: NO | Nullable: NO
- CGASTO1: FLOAT | PK: NO | Nullable: NO
- CGASTO2: FLOAT | PK: NO | Nullable: NO
- CGASTO3: FLOAT | PK: NO | Nullable: NO
- CTOTAL: FLOAT | PK: NO | Nullable: NO
- CPENDIENTE: FLOAT | PK: NO | Nullable: NO
- CTOTALUNIDADES: FLOAT | PK: NO | Nullable: NO
- CDESCUENTOPRONTOPAGO: FLOAT | PK: NO | Nullable: NO
- CPORCENTAJEIMPUESTO1: FLOAT | PK: NO | Nullable: NO
- CPORCENTAJEIMPUESTO2: FLOAT | PK: NO | Nullable: NO
- CPORCENTAJEIMPUESTO3: FLOAT | PK: NO | Nullable: NO
- CPORCENTAJERETENCION1: FLOAT | PK: NO | Nullable: NO
- CPORCENTAJERETENCION2: FLOAT | PK: NO | Nullable: NO
- CPORCENTAJEINTERES: FLOAT | PK: NO | Nullable: NO
- CTEXTOEXTRA1: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTEXTOEXTRA2: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTEXTOEXTRA3: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CFECHAEXTRA: DATETIME | PK: NO | Nullable: NO
- CIMPORTEEXTRA1: FLOAT | PK: NO | Nullable: NO
- CIMPORTEEXTRA2: FLOAT | PK: NO | Nullable: NO
- CIMPORTEEXTRA3: FLOAT | PK: NO | Nullable: NO
- CIMPORTEEXTRA4: FLOAT | PK: NO | Nullable: NO
- CDESTINATARIO: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNUMEROGUIA: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CMENSAJERIA: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CCUENTAMENSAJERIA: VARCHAR(120) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNUMEROCAJAS: FLOAT | PK: NO | Nullable: NO
- CPESO: FLOAT | PK: NO | Nullable: NO
- CBANOBSERVACIONES: INTEGER | PK: NO | Nullable: NO
- CBANDATOSENVIO: INTEGER | PK: NO | Nullable: NO
- CBANCONDICIONESCREDITO: INTEGER | PK: NO | Nullable: NO
- CBANGASTOS: INTEGER | PK: NO | Nullable: NO
- CUNIDADESPENDIENTES: FLOAT | PK: NO | Nullable: NO
- CTIMESTAMP: VARCHAR(23) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIMPCHEQPAQ: FLOAT | PK: NO | Nullable: NO
- CSISTORIG: INTEGER | PK: NO | Nullable: NO
- CIDMONEDCA: INTEGER | PK: NO | Nullable: NO
- CTIPOCAMCA: FLOAT | PK: NO | Nullable: NO
- CESCFD: INTEGER | PK: NO | Nullable: NO
- CTIENECFD: INTEGER | PK: NO | Nullable: NO
- CLUGAREXPE: VARCHAR(380) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CMETODOPAG: VARCHAR(100) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNUMPARCIA: INTEGER | PK: NO | Nullable: NO
- CCANTPARCI: INTEGER | PK: NO | Nullable: NO
- CCONDIPAGO: VARCHAR(253) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNUMCTAPAG: VARCHAR(100) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CGUIDDOCUMENTO: VARCHAR(40) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CUSUARIO: VARCHAR(15) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDPROYECTO: INTEGER | PK: NO | Nullable: NO
- CIDCUENTA: INTEGER | PK: NO | Nullable: NO
- CTRANSACTIONID: VARCHAR(26) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDCOPIADE: INTEGER | PK: NO | Nullable: NO
- CVERESQUE: VARCHAR(6) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CDATOSADICIONALES: VARCHAR COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: YES
- CIDAPERTURA: INTEGER | PK: NO | Nullable: NO

---

## TABLE: admDocumentosModelo

**Descripción:** Catálogo maestro de modelos de documentos que define los tipos base de documentos comerciales en el sistema (ventas, compras, movimientos de inventario). Establece la naturaleza fundamental de cada modelo (cargo/abono), si afecta existencias, el módulo al que pertenece, foliación, conceptos predeterminados y asientos contables asociados. Es la estructura de clasificación superior a los conceptos de documentos y define el comportamiento general de grandes grupos documentales.

## Columns

- CIDDOCUMENTODE: INTEGER | PK: YES | Nullable: NO
- CDESCRIPCION: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNATURALEZA: INTEGER | PK: NO | Nullable: NO
- CAFECTAEXISTENCIA: INTEGER | PK: NO | Nullable: NO
- CMODULO: INTEGER | PK: NO | Nullable: NO
- CNOFOLIO: FLOAT | PK: NO | Nullable: NO
- CIDCONCEPTODOCTOASUMIDO: INTEGER | PK: NO | Nullable: NO
- CUSACLIENTE: INTEGER | PK: NO | Nullable: NO
- CUSAPROVEEDOR: INTEGER | PK: NO | Nullable: NO
- CIDASIENTOCONTABLE: INTEGER | PK: NO | Nullable: NO

---

## TABLE: admDocumentosModeloBack

**Descripción:** Tabla de respaldo (backup) del catálogo de modelos de documentos. Funciona como copia de seguridad para recuperación en caso de errores o pérdida de configuración. Nota: Esta tabla presenta error en su estructura según el schema proporcionado.

---

## TABLE: admDomicilios

**Descripción:** Catálogo de direcciones físicas asociadas a diferentes entidades del sistema (clientes, proveedores, almacenes, sucursales, empresa). Almacena información completa de domicilios incluyendo: calle, números exterior e interior, colonia, código postal, ciudad, estado, municipio, país, múltiples teléfonos, email, sitio web y tipo de dirección (fiscal, entrega, cobro, etc.). Es fundamental para facturación electrónica (domicilio fiscal), logística de entregas, envío de correspondencia y cumplimiento de requisitos del SAT.

## Columns

- CIDDIRECCION: INTEGER | PK: YES | Nullable: NO
- CIDCATALOGO: INTEGER | PK: NO | Nullable: NO
- CTIPOCATALOGO: INTEGER | PK: NO | Nullable: NO
- CTIPODIRECCION: INTEGER | PK: NO | Nullable: NO
- CNOMBRECALLE: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNUMEROEXTERIOR: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNUMEROINTERIOR: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CCOLONIA: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CCODIGOPOSTAL: VARCHAR(6) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTELEFONO1: VARCHAR(15) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTELEFONO2: VARCHAR(15) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTELEFONO3: VARCHAR(15) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTELEFONO4: VARCHAR(15) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CEMAIL: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CDIRECCIONWEB: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CPAIS: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CESTADO: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CCIUDAD: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTEXTOEXTRA: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTIMESTAMP: VARCHAR(23) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CMUNICIPIO: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSUCURSAL: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO

---

## TABLE: admEjercicios

**Descripción:** Catálogo de ejercicios fiscales y contables configurados en el sistema. Define la estructura temporal de períodos contables, estableciendo las fechas de inicio de cada uno de los 12 períodos del ejercicio y la fecha final. Es fundamental para el control contable, cálculo de acumulados por período, cierre de ejercicios, generación de reportes financieros periódicos y cumplimiento de obligaciones fiscales.

## Columns

- CIDEJERCICIO: INTEGER | PK: YES | Nullable: NO
- CNUMEROEJERCICIO: INTEGER | PK: NO | Nullable: NO
- CFECINIPERIODO1: DATETIME | PK: NO | Nullable: NO
- CFECINIPERIODO2: DATETIME | PK: NO | Nullable: NO
- CFECINIPERIODO3: DATETIME | PK: NO | Nullable: NO
- CFECINIPERIODO4: DATETIME | PK: NO | Nullable: NO
- CFECINIPERIODO5: DATETIME | PK: NO | Nullable: NO
- CFECINIPERIODO6: DATETIME | PK: NO | Nullable: NO
- CFECINIPERIODO7: DATETIME | PK: NO | Nullable: NO
- CFECINIPERIODO8: DATETIME | PK: NO | Nullable: NO
- CFECINIPERIODO9: DATETIME | PK: NO | Nullable: NO
- CFECINIPERIODO10: DATETIME | PK: NO | Nullable: NO
- CFECINIPERIODO11: DATETIME | PK: NO | Nullable: NO
- CFECINIPERIODO12: DATETIME | PK: NO | Nullable: NO
- CFECHAFINAL: DATETIME | PK: NO | Nullable: NO
- CEJERCICIO: INTEGER | PK: NO | Nullable: NO

---

## TABLE: admExistenciaCosto

**Descripción:** Tabla que almacena el resumen de movimientos de existencias y costos por producto, almacén y ejercicio. Registra entradas y salidas tanto en unidades como en valores monetarios (costos) para cada uno de los 12 períodos del ejercicio, más los valores iniciales. Incluye bandera de congelamiento para proteger datos históricos. Es esencial para reportes de inventarios por período, análisis de rotación, cálculo de costo de ventas, valuación de inventarios y auditorías de movimientos de almacén.

## Columns

- CIDEXISTENCIA: INTEGER | PK: YES | Nullable: NO
- CIDALMACEN: INTEGER | PK: NO | Nullable: NO
- CIDPRODUCTO: INTEGER | PK: NO | Nullable: NO
- CIDEJERCICIO: INTEGER | PK: NO | Nullable: NO
- CTIPOEXISTENCIA: INTEGER | PK: NO | Nullable: NO
- CENTRADASINICIALES: FLOAT | PK: NO | Nullable: NO
- CSALIDASINICIALES: FLOAT | PK: NO | Nullable: NO
- CCOSTOINICIALENTRADAS: FLOAT | PK: NO | Nullable: NO
- CCOSTOINICIALSALIDAS: FLOAT | PK: NO | Nullable: NO
- CENTRADASPERIODO1: FLOAT | PK: NO | Nullable: NO
- CENTRADASPERIODO2: FLOAT | PK: NO | Nullable: NO
- CENTRADASPERIODO3: FLOAT | PK: NO | Nullable: NO
- CENTRADASPERIODO4: FLOAT | PK: NO | Nullable: NO
- CENTRADASPERIODO5: FLOAT | PK: NO | Nullable: NO
- CENTRADASPERIODO6: FLOAT | PK: NO | Nullable: NO
- CENTRADASPERIODO7: FLOAT | PK: NO | Nullable: NO
- CENTRADASPERIODO8: FLOAT | PK: NO | Nullable: NO
- CENTRADASPERIODO9: FLOAT | PK: NO | Nullable: NO
- CENTRADASPERIODO10: FLOAT | PK: NO | Nullable: NO
- CENTRADASPERIODO11: FLOAT | PK: NO | Nullable: NO
- CENTRADASPERIODO12: FLOAT | PK: NO | Nullable: NO
- CSALIDASPERIODO1: FLOAT | PK: NO | Nullable: NO
- CSALIDASPERIODO2: FLOAT | PK: NO | Nullable: NO
- CSALIDASPERIODO3: FLOAT | PK: NO | Nullable: NO
- CSALIDASPERIODO4: FLOAT | PK: NO | Nullable: NO
- CSALIDASPERIODO5: FLOAT | PK: NO | Nullable: NO
- CSALIDASPERIODO6: FLOAT | PK: NO | Nullable: NO
- CSALIDASPERIODO7: FLOAT | PK: NO | Nullable: NO
- CSALIDASPERIODO8: FLOAT | PK: NO | Nullable: NO
- CSALIDASPERIODO9: FLOAT | PK: NO | Nullable: NO
- CSALIDASPERIODO10: FLOAT | PK: NO | Nullable: NO
- CSALIDASPERIODO11: FLOAT | PK: NO | Nullable: NO
- CSALIDASPERIODO12: FLOAT | PK: NO | Nullable: NO
- CCOSTOENTRADASPERIODO1: FLOAT | PK: NO | Nullable: NO
- CCOSTOENTRADASPERIODO2: FLOAT | PK: NO | Nullable: NO
- CCOSTOENTRADASPERIODO3: FLOAT | PK: NO | Nullable: NO
- CCOSTOENTRADASPERIODO4: FLOAT | PK: NO | Nullable: NO
- CCOSTOENTRADASPERIODO5: FLOAT | PK: NO | Nullable: NO
- CCOSTOENTRADASPERIODO6: FLOAT | PK: NO | Nullable: NO
- CCOSTOENTRADASPERIODO7: FLOAT | PK: NO | Nullable: NO
- CCOSTOENTRADASPERIODO8: FLOAT | PK: NO | Nullable: NO
- CCOSTOENTRADASPERIODO9: FLOAT | PK: NO | Nullable: NO
- CCOSTOENTRADASPERIODO10: FLOAT | PK: NO | Nullable: NO
- CCOSTOENTRADASPERIODO11: FLOAT | PK: NO | Nullable: NO
- CCOSTOENTRADASPERIODO12: FLOAT | PK: NO | Nullable: NO
- CCOSTOSALIDASPERIODO1: FLOAT | PK: NO | Nullable: NO
- CCOSTOSALIDASPERIODO2: FLOAT | PK: NO | Nullable: NO
- CCOSTOSALIDASPERIODO3: FLOAT | PK: NO | Nullable: NO
- CCOSTOSALIDASPERIODO4: FLOAT | PK: NO | Nullable: NO
- CCOSTOSALIDASPERIODO5: FLOAT | PK: NO | Nullable: NO
- CCOSTOSALIDASPERIODO6: FLOAT | PK: NO | Nullable: NO
- CCOSTOSALIDASPERIODO7: FLOAT | PK: NO | Nullable: NO
- CCOSTOSALIDASPERIODO8: FLOAT | PK: NO | Nullable: NO
- CCOSTOSALIDASPERIODO9: FLOAT | PK: NO | Nullable: NO
- CCOSTOSALIDASPERIODO10: FLOAT | PK: NO | Nullable: NO
- CCOSTOSALIDASPERIODO11: FLOAT | PK: NO | Nullable: NO
- CCOSTOSALIDASPERIODO12: FLOAT | PK: NO | Nullable: NO
- CBANCONGELADO: INTEGER | PK: NO | Nullable: NO
- CTIMESTAMP: VARCHAR(23) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO

---

## TABLE: admFoliosDigitales

**Descripción:** Tabla que registra toda la información relacionada con la facturación electrónica (CFDI). Almacena datos del comprobante fiscal digital: UUID, serie y folio fiscal, certificado de sello digital, estado del CFDI (vigente, cancelado), fechas de emisión y cancelación, información de timbrado, datos del PAC (Proveedor Autorizado de Certificación), acuse de cancelación, relación con pólizas contables, información de pagos y validación. Es crucial para cumplimiento fiscal, auditorías del SAT, control de CFDI emitidos y recibidos, y gestión de cancelaciones.

## Columns

- CIDFOLDIG: INTEGER | PK: YES | Nullable: NO
- CIDDOCTODE: INTEGER | PK: NO | Nullable: NO
- CIDCPTODOC: INTEGER | PK: NO | Nullable: NO
- CIDDOCTO: INTEGER | PK: NO | Nullable: NO
- CIDDOCALDI: INTEGER | PK: NO | Nullable: NO
- CIDFIRMARL: INTEGER | PK: NO | Nullable: NO
- CNOORDEN: INTEGER | PK: NO | Nullable: NO
- CSERIE: VARCHAR(10) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CFOLIO: FLOAT | PK: NO | Nullable: NO
- CNOAPROB: INTEGER | PK: NO | Nullable: NO
- CFECAPROB: DATETIME | PK: NO | Nullable: NO
- CESTADO: INTEGER | PK: NO | Nullable: NO
- CENTREGADO: INTEGER | PK: NO | Nullable: NO
- CFECHAEMI: DATETIME | PK: NO | Nullable: NO
- CHORAEMI: VARCHAR(8) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CEMAIL: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CARCHDIDIS: VARCHAR(253) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDCPTOORI: INTEGER | PK: NO | Nullable: NO
- CFECHACANC: DATETIME | PK: NO | Nullable: NO
- CHORACANC: VARCHAR(8) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CESTRAD: INTEGER | PK: NO | Nullable: NO
- CCADPEDI: TEXT(16) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: YES
- CARCHCBB: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CINIVIG: DATETIME | PK: NO | Nullable: NO
- CFINVIG: DATETIME | PK: NO | Nullable: NO
- CTIPO: VARCHAR(1) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSERIEREC: VARCHAR(25) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CFOLIOREC: FLOAT | PK: NO | Nullable: YES
- CRFC: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CRAZON: VARCHAR(253) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSISORIGEN: INTEGER | PK: NO | Nullable: NO
- CEJERPOL: INTEGER | PK: NO | Nullable: NO
- CPERPOL: INTEGER | PK: NO | Nullable: NO
- CTIPOPOL: INTEGER | PK: NO | Nullable: NO
- CNUMPOL: INTEGER | PK: NO | Nullable: NO
- CTIPOLDESC: VARCHAR(100) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTOTAL: FLOAT | PK: NO | Nullable: NO
- CALIASBDCT: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CCFDPRUEBA: INTEGER | PK: NO | Nullable: NO
- CDESESTADO: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CPAGADOBAN: INTEGER | PK: NO | Nullable: NO
- CDESPAGBAN: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CREFEREN01: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- COBSERVA01: VARCHAR(253) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CCODCONCBA: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CDESCONCBA: VARCHAR(100) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNUMCTABAN: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CFOLIOBAN: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDDOCDEBA: INTEGER | PK: NO | Nullable: NO
- CUSUAUTBAN: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CUUID: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CUSUBAN01: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CAUTUSBA01: INTEGER | PK: NO | Nullable: NO
- CUSUBAN02: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CAUTUSBA02: INTEGER | PK: NO | Nullable: NO
- CUSUBAN03: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CAUTUSBA03: INTEGER | PK: NO | Nullable: NO
- CDESCAUT01: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CDESCAUT02: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CDESCAUT03: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CERRORVAL: INTEGER | PK: NO | Nullable: NO
- CACUSECAN: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDDOCTODSL: VARCHAR(40) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO

---

## TABLE: admFormasPago

**Descripción:** Catálogo de formas de pago configuradas en el sistema (efectivo, transferencia, cheque, tarjeta de crédito/débito, etc.). Almacena código, nombre, estatus, clave SAT oficial para facturación electrónica, moneda asociada y campos extras personalizables. Es fundamental para registro de cobros y pagos, emisión de recibos electrónicos (complementos de pago CFDI), control de caja, conciliación bancaria y cumplimiento de requisitos fiscales del SAT.

## Columns

- CIDFORMAPAGO: INTEGER | PK: YES | Nullable: NO
- CCODIGOFORMAPAGO: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNOMBREFORMAPAGO: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CESTATUS: INTEGER | PK: NO | Nullable: NO
- CFECHAALTA: DATETIME | PK: NO | Nullable: NO
- CFECHABAJA: DATETIME | PK: NO | Nullable: NO
- CCLAVESAT: VARCHAR(3) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDMONEDA: INTEGER | PK: NO | Nullable: NO
- CTEXTOEXTRA1: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTEXTOEXTRA2: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTEXTOEXTRA3: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CFECHAEXTRA: DATETIME | PK: NO | Nullable: NO
- CIMPORTEEXTRA1: FLOAT | PK: NO | Nullable: NO
- CIMPORTEEXTRA2: FLOAT | PK: NO | Nullable: NO
- CIMPORTEEXTRA3: FLOAT | PK: NO | Nullable: NO
- CIMPORTEEXTRA4: FLOAT | PK: NO | Nullable: NO
- CTIMESTAMP: VARCHAR(23) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO

---

## TABLE: admLigasPago

**Descripción:** Tabla que gestiona ligas de pago electrónico generadas para cobro mediante plataformas digitales (PayPal, Stripe, OXXO Pay, etc.). Almacena información del cliente, moneda, proveedor de servicio de pago, vigencia de la liga, estado del pago, URL de pago, GUID de referencia externa y documentos asociados. Es esencial para integración con pasarelas de pago en línea, cobros por internet, seguimiento de pagos pendientes y conciliación automática de ingresos digitales.

## Columns

- CIDLIGA: INTEGER | PK: YES | Nullable: NO
- CIDCLIENTEPROVEEDOR: INTEGER | PK: NO | Nullable: NO
- CIDMONEDA: INTEGER | PK: NO | Nullable: NO
- CIDPROVEEDORSERVICIO: INTEGER | PK: NO | Nullable: NO
- CFECHAINIVIG: DATETIME | PK: NO | Nullable: NO
- CFECHAFINVIG: DATETIME | PK: NO | Nullable: NO
- CFECHAPAGO: DATETIME | PK: NO | Nullable: NO
- CESTADO: INTEGER | PK: NO | Nullable: NO
- CTIPOPAGO: INTEGER | PK: NO | Nullable: NO
- CLIGA: VARCHAR COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: YES
- CGUIDEXTERNALREF: VARCHAR(40) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CGUIDLIGA: VARCHAR(255) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDDOCTOABONO: INTEGER | PK: NO | Nullable: NO
- CTOTAL: FLOAT | PK: NO | Nullable: NO

---

## TABLE: admMaximosMinimos

**Descripción:** Tabla que define los niveles de inventario mínimos y máximos por producto y almacén. Establece puntos de reorden, existencias de seguridad y máximos de stock tanto en unidad base como en unidades no convertibles. Incluye información de ubicación física (zona, pasillo, anaquel, repisa) para facilitar la localización en bodega. Es fundamental para planeación de compras, alertas de inventario bajo, optimización de niveles de stock, prevención de roturas y ubicación eficiente de productos.

## Columns

- CIDAUTOINCSQL: INTEGER | PK: NO | Nullable: NO
- CIDALMACEN: INTEGER | PK: YES | Nullable: NO
- CIDPRODUCTO: INTEGER | PK: YES | Nullable: NO
- CIDPRODUCTOPADRE: INTEGER | PK: NO | Nullable: NO
- CEXISTENCIAMINBASE: FLOAT | PK: NO | Nullable: NO
- CEXISTENCIAMAXBASE: FLOAT | PK: NO | Nullable: NO
- CEXISTMINNOCONVERTIBLE: FLOAT | PK: NO | Nullable: NO
- CEXISTMAXNOCONVERTIBLE: FLOAT | PK: NO | Nullable: NO
- CZONA: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CPASILLO: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CANAQUEL: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CREPISA: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO

---

## TABLE: admMonedas

**Descripción:** Catálogo de monedas configuradas en el sistema. Almacena información completa de cada divisa: nombre, símbolo, posición del símbolo, formas en plural y singular, descripción protegida, bandera asociada (para representación visual), número de decimales y clave SAT oficial. Es fundamental para operaciones multidivisa, manejo de tipos de cambio, facturación en moneda extranjera, conversiones automáticas y cumplimiento de requisitos fiscales en transacciones internacionales.

## Columns

- CIDMONEDA: INTEGER | PK: YES | Nullable: NO
- CNOMBREMONEDA: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSIMBOLOMONEDA: VARCHAR(1) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CPOSICIONSIMBOLO: INTEGER | PK: NO | Nullable: NO
- CPLURAL: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSINGULAR: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CDESCRIPCIONPROTEGIDA: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDBANDERA: INTEGER | PK: NO | Nullable: NO
- CDECIMALESMONEDA: INTEGER | PK: NO | Nullable: NO
- CTIMESTAMP: VARCHAR(23) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CCLAVESAT: VARCHAR(3) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO

---

## TABLE: admMovimientos

**Descripción:** Tabla transaccional que almacena el detalle (partidas/renglones) de todos los documentos comerciales. Cada registro representa una línea de documento con información del producto, almacén, cantidades en diferentes unidades, precios, costos, impuestos (IVA, IEPS), retenciones, descuentos (hasta 5 niveles), total, comisiones, referencias, observaciones, afectación a inventario y saldos, clasificaciones, relaciones con otros movimientos y campos personalizables. Es la tabla de detalle más importante, complemento esencial de admDocumentos para el registro completo de transacciones comerciales.

## Columns

- CIDMOVIMIENTO: INTEGER | PK: YES | Nullable: NO
- CIDDOCUMENTO: INTEGER | PK: NO | Nullable: NO
- CNUMEROMOVIMIENTO: FLOAT | PK: NO | Nullable: NO
- CIDDOCUMENTODE: INTEGER | PK: NO | Nullable: NO
- CIDPRODUCTO: INTEGER | PK: NO | Nullable: NO
- CIDALMACEN: INTEGER | PK: NO | Nullable: NO
- CUNIDADES: FLOAT | PK: NO | Nullable: NO
- CUNIDADESNC: FLOAT | PK: NO | Nullable: NO
- CUNIDADESCAPTURADAS: FLOAT | PK: NO | Nullable: NO
- CIDUNIDAD: INTEGER | PK: NO | Nullable: NO
- CIDUNIDADNC: INTEGER | PK: NO | Nullable: NO
- CPRECIO: FLOAT | PK: NO | Nullable: NO
- CPRECIOCAPTURADO: FLOAT | PK: NO | Nullable: NO
- CCOSTOCAPTURADO: FLOAT | PK: NO | Nullable: NO
- CCOSTOESPECIFICO: FLOAT | PK: NO | Nullable: NO
- CNETO: FLOAT | PK: NO | Nullable: NO
- CIMPUESTO1: FLOAT | PK: NO | Nullable: NO
- CPORCENTAJEIMPUESTO1: FLOAT | PK: NO | Nullable: NO
- CIMPUESTO2: FLOAT | PK: NO | Nullable: NO
- CPORCENTAJEIMPUESTO2: FLOAT | PK: NO | Nullable: NO
- CIMPUESTO3: FLOAT | PK: NO | Nullable: NO
- CPORCENTAJEIMPUESTO3: FLOAT | PK: NO | Nullable: NO
- CRETENCION1: FLOAT | PK: NO | Nullable: NO
- CPORCENTAJERETENCION1: FLOAT | PK: NO | Nullable: NO
- CRETENCION2: FLOAT |PK: NO | Nullable: NO
- CPORCENTAJERETENCION2: FLOAT | PK: NO | Nullable: NO
- CDESCUENTO1: FLOAT | PK: NO | Nullable: NO
- CPORCENTAJEDESCUENTO1: FLOAT | PK: NO | Nullable: NO
- CDESCUENTO2: FLOAT | PK: NO | Nullable: NO
- CPORCENTAJEDESCUENTO2: FLOAT | PK: NO | Nullable: NO
- CDESCUENTO3: FLOAT | PK: NO | Nullable: NO
- CPORCENTAJEDESCUENTO3: FLOAT | PK: NO | Nullable: NO
- CDESCUENTO4: FLOAT | PK: NO | Nullable: NO
- CPORCENTAJEDESCUENTO4: FLOAT | PK: NO | Nullable: NO
- CDESCUENTO5: FLOAT | PK: NO | Nullable: NO
- CPORCENTAJEDESCUENTO5: FLOAT | PK: NO | Nullable: NO
- CTOTAL: FLOAT | PK: NO | Nullable: NO
- CPORCENTAJECOMISION: FLOAT | PK: NO | Nullable: NO
- CREFERENCIA: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- COBSERVAMOV: TEXT(16) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: YES
- CAFECTAEXISTENCIA: INTEGER | PK: NO | Nullable: NO
- CAFECTADOSALDOS: INTEGER | PK: NO | Nullable: NO
- CAFECTADOINVENTARIO: INTEGER | PK: NO | Nullable: NO
- CFECHA: DATETIME | PK: NO | Nullable: NO
- CMOVTOOCULTO: INTEGER | PK: NO | Nullable: NO
- CIDMOVTOOWNER: INTEGER | PK: NO | Nullable: NO
- CIDMOVTOORIGEN: INTEGER | PK: NO | Nullable: NO
- CUNIDADESPENDIENTES: FLOAT | PK: NO | Nullable: NO
- CUNIDADESNCPENDIENTES: FLOAT | PK: NO | Nullable: NO
- CUNIDADESORIGEN: FLOAT | PK: NO | Nullable: NO
- CUNIDADESNCORIGEN: FLOAT | PK: NO | Nullable: NO
- CTIPOTRASPASO: INTEGER | PK: NO | Nullable: NO
- CIDVALORCLASIFICACION: INTEGER | PK: NO | Nullable: NO
- CTEXTOEXTRA1: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTEXTOEXTRA2: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTEXTOEXTRA3: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CFECHAEXTRA: DATETIME | PK: NO | Nullable: NO
- CIMPORTEEXTRA1: FLOAT | PK: NO | Nullable: NO
- CIMPORTEEXTRA2: FLOAT | PK: NO | Nullable: NO
- CIMPORTEEXTRA3: FLOAT | PK: NO | Nullable: NO
- CIMPORTEEXTRA4: FLOAT | PK: NO | Nullable: NO
- CTIMESTAMP: VARCHAR(23) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CGTOMOVTO: FLOAT | PK: NO | Nullable: NO
- CSCMOVTO: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CCOMVENTA: FLOAT | PK: NO | Nullable: NO
- CIDMOVTODESTINO: INTEGER | PK: NO | Nullable: NO
- CNUMEROCONSOLIDACIONES: INTEGER | PK: NO | Nullable: NO
- COBJIMPU01: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO

---

## TABLE: admMovimientosCapas

**Descripción:** Tabla de relación entre movimientos de inventario y capas de costo. Registra cómo cada movimiento afecta las diferentes capas de inventario cuando se utiliza el método de costeo por capas (PEPS/UEPS). Almacena la capa específica afectada, fecha, unidades consumidas o agregadas, tipo de capa y unidad de medida. Es fundamental para trazabilidad de costos por lote, seguimiento de caducidades, cumplimiento de métodos de valuación PEPS/UEPS y auditoría detallada de movimientos por capa.

## Columns

- CIDAUTOINCSQL: INTEGER | PK: NO | Nullable: NO
- CIDMOVIMIENTO: INTEGER | PK: YES | Nullable: NO
- CIDCAPA: INTEGER | PK: YES | Nullable: NO
- CFECHA: DATETIME | PK: NO | Nullable: NO
- CUNIDADES: FLOAT | PK: NO | Nullable: NO
- CTIPOCAPA: INTEGER | PK: NO | Nullable: NO
- CIDUNIDAD: INTEGER | PK: NO | Nullable: NO

---

## TABLE: admMovimientosContables

**Descripción:** Tabla que define las reglas para generar movimientos contables (cargos y abonos) en pólizas a partir de documentos comerciales. Especifica la cuenta contable, tipo de movimiento (cargo/abono), importe base, porcentaje a aplicar, origen de la referencia, diario, concepto, segmentos de negocio, tratamiento de monedas y si es complemento. Es la plantilla que traduce operaciones comerciales en registros contables para integración automática con CONTPAQi Contabilidad.

## Columns

- CIDMOVIMIENTOCONTABLE: INTEGER | PK: YES | Nullable: NO
- CIDASIENTOCONTABLE: INTEGER | PK: NO | Nullable: NO
- CCUENTA: VARCHAR(250) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTIPOMOVIMIENTO: INTEGER | PK: NO | Nullable: NO
- CIMPORTEBASE: FLOAT | PK: NO | Nullable: NO
- CPORCENTAJE: FLOAT | PK: NO | Nullable: NO
- CORIGENREFERENCIA: INTEGER | PK: NO | Nullable: NO
- CREFERENCIA: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CORIGENDIARIO: INTEGER | PK: NO | Nullable: NO
- CDIARIO: VARCHAR(10) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CORIGENCONCEPTO: INTEGER | PK: NO | Nullable: NO
- CCONCEPTO: VARCHAR(100) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTIMESTAMP: VARCHAR(23) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSUMARIZ: INTEGER | PK: NO | Nullable: NO
- CSUPMOVS0: INTEGER | PK: NO | Nullable: NO
- CORISEGNEG: INTEGER | PK: NO | Nullable: NO
- CSEGNEG: VARCHAR(4) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIMPMONEXT: INTEGER | PK: NO | Nullable: NO
- CIMPMONDOC: INTEGER | PK: NO | Nullable: NO
- CCOMPLEMEN: INTEGER | PK: NO | Nullable: NO

---

## TABLE: admMovimientosPrepoliza

**Descripción:** Tabla de detalle que almacena los movimientos contables individuales (cargos y abonos) de cada pré-póliza generada desde documentos comerciales antes de ser enviada a contabilidad. Contiene ejercicio, período, tipo de póliza, número, cuenta contable, tipo de movimiento, referencia, importe, diario, moneda, concepto, fecha y segmento de negocio. Permite revisar y validar los asientos contables antes de su transferencia definitiva al sistema contable.

## Columns

- CIDMOVIMIENTOPREPOLIZA: INTEGER | PK: YES | Nullable: NO
- CIDPREPOLIZA: INTEGER | PK: NO | Nullable: NO
- EJE: INTEGER | PK: NO | Nullable: NO
- PERIODO: INTEGER | PK: NO | Nullable: NO
- TIPOPOL: INTEGER | PK: NO | Nullable: NO
- NUMPOL: INTEGER | PK: NO | Nullable: NO
- MOVTO: INTEGER | PK: NO | Nullable: NO
- CUENTA: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- TIPOMOV: INTEGER | PK: NO | Nullable: NO
- REFERENCIA: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- IMPORTE: FLOAT | PK: NO | Nullable: NO
- DIARIO: VARCHAR(10) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- MONEDA: FLOAT | PK: NO | Nullable: NO
- CONCEPTO: VARCHAR(100) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- FECHA: DATETIME | PK: NO | Nullable: NO
- SEGNEG: VARCHAR(10) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO

---

## TABLE: admMovimientosSerie

**Descripción:** Tabla de relación entre movimientos de inventario y números de serie de productos. Registra qué números de serie específicos fueron vendidos, comprados o movidos en cada transacción de productos serializados. Incluye fecha del movimiento para trazabilidad temporal. Es esencial para control de productos con número de serie (electrónicos, vehículos, maquinaria), garantías, rastreo individual de artículos, prevención de duplicados y auditoría de movimientos por serie.

## Columns

- CIDAUTOINCSQL: INTEGER | PK: NO | Nullable: NO
- CIDMOVIMIENTO: INTEGER | PK: YES | Nullable: NO
- CIDSERIE: INTEGER | PK: YES | Nullable: NO
- CFECHA: DATETIME | PK: NO | Nullable: NO

---

## TABLE: admMovtosBancarios

**Descripción:** Tabla que registra movimientos bancarios importados desde bancos o servicios de banca electrónica. Almacena transacciones bancarias con su ID único, cuenta asociada, documento vinculado (si aplica), fecha, descripción, referencia, importe, estado de conciliación y campos extras. Es fundamental para conciliación bancaria automática, integración con servicios de banca en línea, seguimiento de ingresos y egresos bancarios, y vinculación de transacciones bancarias con documentos del sistema.

## Columns

- CTRANSACTIONID: VARCHAR(26) COLLATE "Modern_Spanish_CI_AS" | PK: YES | Nullable: NO
- CACCOUNTID: VARCHAR(26) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDCUENTA: INTEGER | PK: NO | Nullable: NO
- CIDDOCUMENTO: INTEGER | PK: NO | Nullable: NO
- CFECHA: DATETIME | PK: NO | Nullable: NO
- CDESCRIPCION: VARCHAR(256) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CREFERENCIA: VARCHAR(128) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIMPORTE: FLOAT | PK: NO | Nullable: NO
- CESTADO: INTEGER | PK: NO | Nullable: NO
- CTEXTOEXTRA1: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTEXTOEXTRA2: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTEXTOEXTRA3: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CFECHAEXTRA: DATETIME | PK: NO | Nullable: NO
- CIMPORTEEXTRA1: FLOAT | PK: NO | Nullable: NO
- CIMPORTEEXTRA2: FLOAT | PK: NO | Nullable: NO
- CIMPORTEEXTRA3: FLOAT | PK: NO | Nullable: NO
- CIMPORTEEXTRA4: FLOAT | PK: NO | Nullable: NO
- CTIMESTAMP: VARCHAR(23) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO

---

## TABLE: admMovtosCEPs

**Descripción:** Tabla que registra movimientos de Comprobantes Electrónicos de Pago (CEP) - cheques electrónicos. Almacena información del comprobante digital: clave, sello, certificado, cadena original, estado, concepto, IVA, importe, datos bancarios del receptor y emisor (banco, nombre, RFC, cuenta, tipo de cuenta), archivo XML y campos extras. Era utilizado para el esquema anterior de cheques electrónicos, previo a la implementación de complementos de pago en CFDI 3.3.

## Columns

- CIDMOVTOCEP: INTEGER | PK: YES | Nullable: NO
- CIDDOCUMENTO: INTEGER | PK: NO | Nullable: NO
- CFECHA: DATETIME | PK: NO | Nullable: NO
- CHORA: VARCHAR(8) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CCLAVE: VARCHAR(12) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSELLO: VARCHAR(256) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CCERTIFICADO: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CCADENA: TEXT(16) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: YES
- CESTADO: INTEGER | PK: NO | Nullable: NO
- CCONCEPTO: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIVA: FLOAT | PK: NO | Nullable: NO
- CIMPORTE: FLOAT | PK: NO | Nullable: NO
- CRBANCO: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CRNOMBRE: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CRRFC: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CRCUENTA: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CRTIPOCTA: VARCHAR(2) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CEBANCO: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CENOMBRE: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CERFC: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CECUENTA: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CETIPOCTA: VARCHAR(2) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTEXTOEXTRA1: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTEXTOEXTRA2: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTEXTOEXTRA3: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CFECHAEXTRA: DATETIME | PK: NO | Nullable: NO
- CIMPORTEEXTRA1: FLOAT | PK: NO | Nullable: NO
- CIMPORTEEXTRA2: FLOAT | PK: NO | Nullable: NO
- CIMPORTEEXTRA3: FLOAT | PK: NO | Nullable: NO
- CIMPORTEEXTRA4: FLOAT | PK: NO | Nullable: NO
- CARCHIVO: VARCHAR(256) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTIMESTAMP: VARCHAR(23) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO

---

## TABLE: admMovtosInvFisico

**Descripción:** Tabla temporal que almacena los movimientos capturados durante el proceso de inventario físico antes de generar el ajuste definitivo. Registra producto, almacén, unidades contadas en diferentes medidas y relaciones entre movimientos (owner). Es utilizada durante el levantamiento de inventarios físicos para capturar las existencias reales, comparar con el sistema y generar los ajustes correspondientes al finalizar el conteo.

## Columns

- CIDMOVIMIENTO: INTEGER | PK: YES | Nullable: NO
- CIDPRODUCTO: INTEGER | PK: NO | Nullable: NO
- CIDALMACEN: INTEGER | PK: NO | Nullable: NO
- CIDUNIDAD: INTEGER | PK: NO | Nullable: NO
- CUNIDADES: FLOAT | PK: NO | Nullable: NO
- CUNIDADESNC: FLOAT | PK: NO | Nullable: NO
- CUNIDADESCAPTURADAS: FLOAT | PK: NO | Nullable: NO
- CMOVTOOCULTO: INTEGER | PK: NO | Nullable: NO
- CIDMOVTOOWNER: INTEGER | PK: NO | Nullable: NO

---

## TABLE: admMovtosInvFisicoSerieCa

**Descripción:** Tabla temporal que registra series y capas (lotes) capturados durante el inventario físico de productos serializados o con control por lotes. Almacena números de serie, lotes, fechas de caducidad/fabricación, datos de pedimentos aduanales, cantidades contadas y referencia a capas. Se utiliza junto con admMovtosInvFisico para inventarios físicos de productos que requieren trazabilidad detallada por serie o lote, permitiendo ajustes precisos considerando información de trazabilidad.

## Columns

- CIDSERIECAPA: INTEGER | PK: YES | Nullable: NO
- CIDMOVTOINVENTARIOFISICO: INTEGER | PK: NO | Nullable: NO
- CIDPRODUCTO: INTEGER | PK: NO | Nullable: NO
- CNUMEROSERIE: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDALMACEN: INTEGER | PK: NO | Nullable: NO
- CTIPO: INTEGER | PK: NO | Nullable: NO
- CNUMEROLOTE: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CFECHACADUCIDAD: DATETIME | PK: NO | Nullable: NO
- CFECHAFABRICACION: DATETIME | PK: NO | Nullable: NO
- CPEDIMENTO: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CADUANA: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CFECHAPEDIMENTO: DATETIME | PK: NO | Nullable: NO
- CTIPOCAMBIO: FLOAT | PK: NO | Nullable: NO
- CCANTIDAD: FLOAT | PK: NO | Nullable: NO
- CIDCAPA: INTEGER | PK: NO | Nullable: NO

---

## TABLE: admPagoNotas

**Descripción:** Tabla que registra los pagos aplicados a documentos de punto de venta (notas). Almacena información de cada pago recibido: documento asociado, forma de pago utilizada, tipo de pago, importe, moneda, tipo de cambio y referencia. Es fundamental para control de caja en puntos de venta, registro de pagos mixtos (múltiples formas de pago en una venta), cortes de caja, conciliación de efectivo y emisión de tickets de venta.

## Columns

- CIDPAGO: INTEGER | PK: YES | Nullable: NO
- CIDDOCUMENTO: INTEGER | PK: NO | Nullable: NO
- CIDFORMAPAGO: INTEGER | PK: NO | Nullable: NO
- CTIPO: INTEGER | PK: NO | Nullable: NO
- CIMPORTE: FLOAT | PK: NO | Nullable: NO
- CIDMONEDA: INTEGER | PK: NO | Nullable: NO
- CTIPOCAMBIO: FLOAT | PK: NO | Nullable: NO
- CREFERENCIA: VARCHAR(100) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTIMESTAMP: VARCHAR(23) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO

---

## TABLE: admParametros

**Descripción:** Tabla maestra de configuración general del sistema que almacena todos los parámetros globales y preferencias de la empresa. Contiene configuración esencial como: datos fiscales de la empresa (RFC, razón social, régimen fiscal), ejercicio y período actual, configuración de decimales, impuestos y retenciones predeterminados, método de costeo, manejo de existencias negativas, moneda base, cliente mostrador, almacén asumido, máscaras de captura, nombres personalizados de listas de precios/impuestos/descuentos/gastos, segmentos contables generales, rutas de archivos, configuración de facturación electrónica, integración con CONTPAQi Contabilidad, límites y opciones de punto de venta, configuración de correo electrónico y múltiples banderas de comportamiento del sistema. Es la tabla de configuración central que controla el comportamiento global del sistema.

## Columns

- CIDEMPRESA: INTEGER | PK: YES | Nullable: NO
- CNOMBREEMPRESA: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CEXISTENCIANEGATIVA: INTEGER | PK: NO | Nullable: NO
- CIDEJERCICIOACTUAL: INTEGER | PK: NO | Nullable: NO
- CPERIODOACTUAL: INTEGER | PK: NO | Nullable: NO
- CRFCEMPRESA: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CCURPEMPRESA: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CREGISTROCAMARA: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CCUENTAESTATAL: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CREPRESENTANTELEGAL: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNOMBRECORTO: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDALMACENASUMIDO: INTEGER | PK: NO | Nullable: NO
- CFECHACIERRE: DATETIME | PK: NO | Nullable: NO
- CDECIMALESUNIDADES: INTEGER | PK: NO | Nullable: NO
- CDECIMALESPRECIOVENTA: INTEGER | PK: NO | Nullable: NO
- CDECIMALESCOSTOS: INTEGER | PK: NO | Nullable: NO
- CDECIMALESTIPOSCAMBIO: INTEGER | PK: NO | Nullable: NO
- CBANMARGENUTILIDAD: INTEGER | PK: NO | Nullable: NO
- CIMPUESTO1: FLOAT | PK: NO | Nullable: NO
- CIMPUESTO2: FLOAT | PK: NO | Nullable: NO
- CIMPUESTO3: FLOAT | PK: NO | Nullable: NO
- CUSOCUOTAIESPS: INTEGER | PK: NO | Nullable: NO
- CRETENCIONCLIENTE1: FLOAT | PK: NO | Nullable: NO
- CRETENCIONCLIENTE2: FLOAT | PK: NO | Nullable: NO
- CRETENCIONPROVEEDOR1: FLOAT | PK: NO | Nullable: NO
- CRETENCIONPROVEEDOR2: FLOAT | PK: NO | Nullable: NO
- CDESCUENTODOCTO: FLOAT | PK: NO | Nullable: NO
- CDESCUENTOMOVTO: FLOAT | PK: NO | Nullable: NO
- CCOMISIONVENTA: FLOAT | PK: NO | Nullable: NO
- CCOMISIONCOBRO: FLOAT | PK: NO | Nullable: NO
- CLISTAPRECIOGENERAL: INTEGER | PK: NO | Nullable: NO
- CIDALMACENCONSIGNACION: INTEGER | PK: NO | Nullable: NO
- CMANEJOFECHA: INTEGER | PK: NO | Nullable: NO
- CIDMONEDABASE: INTEGER | PK: NO | Nullable: NO
- CIDCLIENTEMOSTRADOR: INTEGER | PK: NO | Nullable: NO
- CRUTACONTPAQ: VARCHAR(253) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CUSACARACTERISTICAS: INTEGER | PK: NO | Nullable: NO
- CUSAUNIDADNC: INTEGER | PK: NO | Nullable: NO
- CMASCARILLACLIENTES: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CMASCARILLAPRODUCTO: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CMASCARILLAALMACEN: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CMASCARILLAAGENTE: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CMASCARILLARFC: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CMASCARILLACURP: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CBANDIRECCION: INTEGER | PK: NO | Nullable: NO
- CNOMBRELISTA1: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDMONEDALISTA1: INTEGER | PK: NO | Nullable: NO
- CNOMBRELISTA2: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDMONEDALISTA2: INTEGER | PK: NO | Nullable: NO
- CNOMBRELISTA3: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDMONEDALISTA3: INTEGER | PK: NO | Nullable: NO
- CNOMBRELISTA4: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDMONEDALISTA4: INTEGER | PK: NO | Nullable: NO
- CNOMBRELISTA5: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDMONEDALISTA5: INTEGER | PK: NO | Nullable: NO
- CNOMBRELISTA6: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDMONEDALISTA6: INTEGER | PK: NO | Nullable: NO
- CNOMBRELISTA7: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDMONEDALISTA7: INTEGER | PK: NO | Nullable: NO
- CNOMBRELISTA8: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDMONEDALISTA8: INTEGER | PK: NO | Nullable: NO
- CNOMBRELISTA9: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDMONEDALISTA9: INTEGER | PK: NO | Nullable: NO
- CNOMBRELISTA10: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDMONEDALISTA10: INTEGER | PK: NO | Nullable: NO
- CNOMBREIMPUESTO1: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNOMBREIMPUESTO2: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNOMBREIMPUESTO3: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNOMBRERETENCION1: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNOMBRERETENCION2: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNOMBREGASTO1: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNOMBREGASTO2: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNOMBREGASTO3: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNOMBREDESCUENTOMOV1: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNOMBREDESCUENTOMOV2: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNOMBREDESCUENTOMOV3: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNOMBREDESCUENTOMOV4: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNOMBREDESCUENTOMOV5: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNOMBREDESCUENTODOC1: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNOMBREDESCUENTODOC2: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGCONTGENERAL1: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGCONTGENERAL2: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGCONTGENERAL3: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS"| PK: NO | Nullable: NO
- CSEGCONTGENERAL4: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGCONTGENERAL5: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGCONTGENERAL6: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGCONTGENERAL7: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGCONTGENERAL8: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGCONTGENERAL9: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGCONTGENERAL10: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGCONTGENERAL11: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CCONSECUTIVODIARIO: FLOAT | PK: NO | Nullable: NO
- CCONSECUTIVOINGRESOS: FLOAT | PK: NO | Nullable: NO
- CCONSECUTIVOEGRESOS: FLOAT | PK: NO | Nullable: NO
- CCONSECUTIVOORDEN: FLOAT | PK: NO | Nullable: NO
- CTIMESTAMP: VARCHAR(23) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CFECHACONGELAMIENTO: DATETIME | PK: NO | Nullable: NO
- CBANCONGELAMIENTO: INTEGER | PK: NO | Nullable: NO
- CRUTAEMPRESAPRED: VARCHAR(253) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CBANVISTASVENTAS: INTEGER | PK: NO | Nullable: NO
- CBANVISTASCOMPRAS: INTEGER | PK: NO | Nullable: NO
- CBANVISTASCTEPROVINVEN: INTEGER | PK: NO | Nullable: NO
- CBANVISTASCATALOGOS: INTEGER | PK: NO | Nullable: NO
- CAFECTARINVAUTOMATICO: INTEGER | PK: NO | Nullable: NO
- CMETODOCOSTEO: INTEGER | PK: NO | Nullable: NO
- CBANOBLIGATORIOEXISTENCIA: INTEGER | PK: NO | Nullable: NO
- CNUMIMPUESTOIVA: INTEGER | PK: NO | Nullable: NO
- CVERSIONACTUAL: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CPRECIOSCONIVA: INTEGER | PK: NO | Nullable: NO
- CIDPRODU01: INTEGER | PK: NO | Nullable: NO
- CIDPRODU02: INTEGER | PK: NO | Nullable: NO
- CIDPRODU03: INTEGER | PK: NO | Nullable: NO
- CIDPRODU04: INTEGER | PK: NO | Nullable: NO
- CIDPRODU05: INTEGER | PK: NO | Nullable: NO
- CIDCONCE01: INTEGER | PK: NO | Nullable: NO
- CIDCONCE02: INTEGER | PK: NO | Nullable: NO
- CIDCLIEN02: INTEGER | PK: NO | Nullable: NO
- CIDCONCE03: INTEGER | PK: NO | Nullable: NO
- CIDCONCE04: INTEGER | PK: NO | Nullable: NO
- CPERANTFUT: INTEGER | PK: NO | Nullable: NO
- CVMOSTPEND: INTEGER | PK: NO | Nullable: NO
- CMOVTEXEX1: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CMOVTEXEX2: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CMOVTEXEX3: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CMOVIMPEX1: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CMOVIMPEX2: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CMOVIMPEX3: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CMOVIMPEX4: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CMOVFECEX1: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CVISTAAJ01: INTEGER | PK: NO | Nullable: NO
- CESCFD: INTEGER | PK: NO | Nullable: NO
- CTIEMPOCFD: INTEGER | PK: NO | Nullable: NO
- CINTENTOS: INTEGER | PK: NO | Nullable: NO
- CINTERFAZ: INTEGER | PK: NO | Nullable: NO
- CCONTSIMUL: INTEGER | PK: NO | Nullable: NO
- CBANACTPLP: INTEGER | PK: NO | Nullable: NO
- CPOSFOLIO: INTEGER | PK: NO | Nullable: NO
- CPOSMODOIM: INTEGER | PK: NO | Nullable: NO
- CCALCOSTO1: INTEGER | PK: NO | Nullable: NO
- CGENBITACS: INTEGER | PK: NO | Nullable: NO
- CSUGERIRRE: INTEGER | PK: NO | Nullable: NO
- CIDKEYEMP: INTEGER | PK: NO | Nullable: NO
- CALMACENAC: INTEGER | PK: NO | Nullable: NO
- CVERPOSI: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDSUCURSA: INTEGER | PK: NO | Nullable: NO
- CPERFIL: INTEGER | PK: NO | Nullable: NO
- CAUTORIZAR: INTEGER | PK: NO | Nullable: NO
- CMOSTRARDOCTOS: INTEGER | PK: NO | Nullable: NO
- CBITACORA0: INTEGER | PK: NO | Nullable: NO
- CBITACORA1: INTEGER | PK: NO | Nullable: NO
- CBITACORA2: INTEGER | PK: NO | Nullable: NO
- CBITACORA3: INTEGER | PK: NO | Nullable: NO
- CBITACORA4: INTEGER | PK: NO | Nullable: NO
- CBITACORA5: INTEGER | PK: NO | Nullable: NO
- CBITACORA6: INTEGER | PK: NO | Nullable: NO
- CBITACORA7: INTEGER | PK: NO | Nullable: NO
- CCOSTOMEN: INTEGER | PK: NO | Nullable: NO
- CSEGCIVA15: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGCIVA10: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGCIVAOT: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGCIVA16: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGCIVA11: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGPIVA15: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGPIVA10: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGPIVAOT: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGPIVA16: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGPIVA11: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CGENAJ2010: INTEGER | PK: NO | Nullable: NO
- CFECAJ2010: DATETIME | PK: NO | Nullable: NO
- CAJ2010ORI: INTEGER | PK: NO | Nullable: NO
- CHOST: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTIPESTCAL: INTEGER | PK: NO | Nullable: NO
- CCFDIMPU01: INTEGER | PK: NO | Nullable: NO
- CCFDIMPU02: INTEGER | PK: NO | Nullable: NO
- CCFDIMPU03: INTEGER | PK: NO | Nullable: NO
- CCFDIMPU04: INTEGER | PK: NO | Nullable: NO
- CCFDIMPU05: INTEGER | PK: NO | Nullable: NO
- CRUTAPLA01: VARCHAR(253) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CRUTAPLA02: VARCHAR(253) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CFECDONAT: DATETIME | PK: NO | Nullable: NO
- CNUMDONAT: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CHOSTPROXY: VARCHAR(253) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CPTOPROXY: INTEGER | PK: NO | Nullable: NO
- CUSRPROXY: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CHOSTSMTP: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CPTOPOP: INTEGER | PK: NO | Nullable: NO
- CPTOSMTP: INTEGER | PK: NO | Nullable: NO
- CCNXSEGPOP: INTEGER | PK: NO | Nullable: NO
- CRUTAENTREGA: VARCHAR(253) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CPREFIJORFC: INTEGER | PK: NO | Nullable: NO
- CVALIDACFD: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CREGIMFISC: VARCHAR(253) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CAUTRVOE: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CLEYENDON1: VARCHAR(253) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CLEYENDON2: VARCHAR(253) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CASUNTO: VARCHAR(253) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CCUERPO: TEXT(16) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: YES
- CFIRMA: VARCHAR(253) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CADJUNTO1: VARCHAR(253) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CADJUNTO2: VARCHAR(253) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CCORREOPRU: VARCHAR(253) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CGUIDDSL: VARCHAR(40) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CGUIDEMPRESA: VARCHAR(40) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CMARGENUTILIDAD: FLOAT | PK: NO | Nullable: NO
- CPROTEGERCOSTOS: INTEGER | PK: NO | Nullable: NO
- CIDCUENTA: INTEGER | PK: NO | Nullable: NO
- CSEGCIVA8: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGPIVA8: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTOKENCN: TEXT(16) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: YES
- CREFRESHTOKENCN: TEXT(16) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: YES
- CURLWSTORE: VARCHAR(250) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: YES
- CLEYENDON: VARCHAR COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CUSACORREOOAUTH: INTEGER | PK: NO | Nullable: NO
- CPROVEEDOROAUTH: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO

---

## TABLE: admParametrosBack

**Descripción:** Tabla de respaldo (backup) de la configuración general del sistema. Almacena una copia de seguridad completa de todos los parámetros de la empresa para recuperación en caso de pérdida de datos o errores en la configuración. Tiene estructura idéntica a admParametros y sirve como mecanismo de restauración de la configuración crítica del sistema.

## Columns

[Misma estructura que admParametros - columnas omitidas por brevedad]

---

## TABLE: admPreciosCompra

**Descripción:** Tabla que registra los precios de compra históricos y actuales de productos por proveedor. Almacena el precio de compra, moneda, código que el proveedor usa para identificar el producto y unidad de medida de compra. Es esencial para gestión de múltiples proveedores por producto, comparación de precios entre proveedores, seguimiento de costos históricos, generación de órdenes de compra con precios correctos y análisis de mejores opciones de abastecimiento.

## Columns

- CIDAUTOINCSQL: INTEGER | PK: NO | Nullable: NO
- CIDPRODUCTO: INTEGER | PK: YES | Nullable: NO
- CIDPROVEEDOR: INTEGER | PK: YES | Nullable: NO
- CPRECIOCOMPRA: FLOAT | PK: NO | Nullable: NO
- CIDMONEDA: INTEGER | PK: NO | Nullable: NO
- CCODIGOPRODUCTOPROVEEDOR: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDUNIDAD: INTEGER | PK: NO | Nullable: NO
- CTIMESTAMP: VARCHAR(23) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO

---

## TABLE: admPrepolizas

**Descripción:** Tabla de encabezados de pré-pólizas contables generadas desde documentos comerciales antes de ser transferidas a CONTPAQi Contabilidad. Almacena información del encabezado de la póliza: estado contable, ejercicio, período, tipo de póliza, número, clase, si está impresa, concepto, fecha, importes de cargos y abonos, diario, sistema de origen, hora, GUID de póliza y referencia de transacción. Junto con admMovimientosPrepoliza permite revisar y validar asientos antes de su envío definitivo al sistema contable.

## Columns

- CIDPREPOLIZA: INTEGER | PK: YES | Nullable: NO
- CESTADOCONTABLE: INTEGER | PK: NO | Nullable: NO
- EJE: INTEGER | PK: NO | Nullable: NO
- PERIODO: INTEGER | PK: NO | Nullable: NO
- TIPOPOL: INTEGER | PK: NO | Nullable: NO
- NUMPOL: INTEGER | PK: NO | Nullable: NO
- CLASE: INTEGER | PK: NO | Nullable: NO
- IMPRESA: INTEGER | PK: NO | Nullable: NO
- CONCEPTO: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- FECHA: DATETIME | PK: NO | Nullable: NO
- CARGOS: FLOAT | PK: NO | Nullable: NO
- ABONOS: FLOAT | PK: NO | Nullable: NO
- DIARIO: VARCHAR(10) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- SISTORIG: INTEGER | PK: NO | Nullable: NO
- CHORA: VARCHAR(8) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CGUIDPOLIZA: VARCHAR(40) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDTRANSACCION: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO

---

## TABLE: admProductos

**Descripción:** Catálogo maestro de productos y servicios. Almacena información completa de cada artículo comercializado: código, nombre, tipo (producto, paquete, servicio), fecha de alta, control de existencia, foto, descripción, método de costeo, peso, comisiones excepcionales, costo estándar, margen de utilidad, estatus, unidades de medida (base, no convertible, compra, venta), impuestos y retenciones aplicables, características, clasificaciones (hasta 6), segmentos contables, precios en 10 listas diferentes, configuración de banderas de comportamiento, códigos alternos, descripción corta, manejo con báscula, tipo de paquete, selección de precio, desglose de impuestos, cuenta contable predeterminada, clave SAT para facturación electrónica y dimensiones físicas. Es la tabla central del catálogo de productos, esencial para ventas, compras, inventarios y facturación.

## Columns

- CIDPRODUCTO: INTEGER | PK: YES | Nullable: NO
- CCODIGOPRODUCTO: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNOMBREPRODUCTO: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTIPOPRODUCTO: INTEGER | PK: NO | Nullable: NO
- CFECHAALTAPRODUCTO: DATETIME | PK: NO | Nullable: NO
- CCONTROLEXISTENCIA: INTEGER | PK: NO | Nullable: NO
- CIDFOTOPRODUCTO: INTEGER | PK: NO | Nullable: NO
- CDESCRIPCIONPRODUCTO: TEXT(16) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: YES
- CMETODOCOSTEO: INTEGER | PK: NO | Nullable: NO
- CPESOPRODUCTO: FLOAT | PK: NO | Nullable: NO
- CCOMVENTAEXCEPPRODUCTO: FLOAT | PK: NO | Nullable: NO
- CCOMCOBROEXCEPPRODUCTO: FLOAT | PK: NO | Nullable: NO
- CCOSTOESTANDAR: FLOAT | PK: NO | Nullable: NO
- CMARGENUTILIDAD: FLOAT | PK: NO | Nullable: NO
- CSTATUSPRODUCTO: INTEGER | PK: NO | Nullable: NO
- CIDUNIDADBASE: INTEGER | PK: NO | Nullable: NO
- CIDUNIDADNOCONVERTIBLE: INTEGER | PK: NO | Nullable: NO
- CFECHABAJA: DATETIME | PK: NO | Nullable: NO
- CIMPUESTO1: FLOAT | PK: NO | Nullable: NO
- CIMPUESTO2: FLOAT | PK: NO | Nullable: NO
- CIMPUESTO3: FLOAT | PK: NO | Nullable: NO
- CRETENCION1: FLOAT | PK: NO | Nullable: NO
- CRETENCION2: FLOAT | PK: NO | Nullable: NO
- CIDPADRECARACTERISTICA1: INTEGER | PK: NO | Nullable: NO
- CIDPADRECARACTERISTICA2: INTEGER | PK: NO | Nullable: NO
- CIDPADRECARACTERISTICA3: INTEGER | PK: NO | Nullable: NO
- CIDVALORCLASIFICACION1: INTEGER | PK: NO | Nullable: NO
- CIDVALORCLASIFICACION2: INTEGER | PK: NO | Nullable: NO
- CIDVALORCLASIFICACION3: INTEGER | PK: NO | Nullable: NO
- CIDVALORCLASIFICACION4: INTEGER | PK: NO | Nullable: NO
- CIDVALORCLASIFICACION5: INTEGER | PK: NO | Nullable: NO
- CIDVALORCLASIFICACION6: INTEGER | PK: NO | Nullable: NO
- CSEGCONTPRODUCTO1: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGCONTPRODUCTO2: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGCONTPRODUCTO3: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTEXTOEXTRA1: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTEXTOEXTRA2: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CTEXTOEXTRA3: VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CFECHAEXTRA: DATETIME | PK: NO | Nullable: NO
- CIMPORTEEXTRA1: FLOAT | PK: NO | Nullable: NO
- CIMPORTEEXTRA2: FLOAT | PK: NO | Nullable: NO
- CIMPORTEEXTRA3: FLOAT | PK: NO | Nullable: NO
- CIMPORTEEXTRA4: FLOAT | PK: NO | Nullable: NO
- CPRECIO1: FLOAT | PK: NO | Nullable: NO
- CPRECIO2: FLOAT | PK: NO | Nullable: NO
- CPRECIO3: FLOAT | PK: NO | Nullable: NO
- CPRECIO4: FLOAT | PK: NO | Nullable: NO
- CPRECIO5: FLOAT | PK: NO | Nullable: NO
- CPRECIO6: FLOAT | PK: NO | Nullable: NO
- CPRECIO7: FLOAT | PK: NO | Nullable: NO
- CPRECIO8: FLOAT | PK: NO | Nullable: NO
- CPRECIO9: FLOAT | PK: NO | Nullable: NO
- CPRECIO10: FLOAT | PK: NO | Nullable: NO
- CBANUNIDADES: INTEGER | PK: NO | Nullable: NO
- CBANCARACTERISTICAS: INTEGER | PK: NO | Nullable: NO
- CBANMETODOCOSTEO: INTEGER | PK: NO | Nullable: NO
- CBANMAXMIN: INTEGER | PK: NO | Nullable: NO
- CBANPRECIO: INTEGER | PK: NO | Nullable: NO
- CBANIMPUESTO: INTEGER | PK: NO | Nullable: NO
- CBANCODIGOBARRA: INTEGER | PK: NO | Nullable: NO
- CBANCOMPONENTE: INTEGER | PK: NO | Nullable: NO
- CTIMESTAMP: VARCHAR(23) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CERRORCOSTO: INTEGER | PK: NO | Nullable: NO
- CFECHAERRORCOSTO: DATETIME | PK: NO | Nullable: NO
- CPRECIOCALCULADO: FLOAT | PK: NO | Nullable: NO
- CESTADOPRECIO: INTEGER | PK: NO | Nullable: NO
- CBANUBICACION: INTEGER | PK: NO | Nullable: NO
- CESEXENTO: INTEGER | PK: NO | Nullable: NO
- CEXISTENCIANEGATIVA: INTEGER | PK: NO | Nullable: NO
- CCOSTOEXT1: FLOAT | PK: NO | Nullable: NO
- CCOSTOEXT2: FLOAT | PK: NO | Nullable: NO
- CCOSTOEXT3: FLOAT | PK: NO | Nullable: NO
- CCOSTOEXT4: FLOAT | PK: NO | Nullable: NO
- CCOSTOEXT5: FLOAT | PK: NO | Nullable: NO
- CFECCOSEX1: DATETIME | PK: NO | Nullable: NO
- CFECCOSEX2: DATETIME | PK: NO | Nullable: NO
- CFECCOSEX3: DATETIME | PK: NO | Nullable: NO
- CFECCOSEX4: DATETIME | PK: NO | Nullable: NO
- CFECCOSEX5: DATETIME | PK: NO | Nullable: NO
- CMONCOSEX1: INTEGER | PK: NO | Nullable: NO
- CMONCOSEX2: INTEGER | PK: NO | Nullable: NO
- CMONCOSEX3: INTEGER | PK: NO | Nullable: NO
- CMONCOSEX4: INTEGER | PK: NO | Nullable: NO
- CMONCOSEX5: INTEGER | PK: NO | Nullable: NO
- CBANCOSEX: INTEGER | PK: NO | Nullable: NO
- CESCUOTAI2: INTEGER | PK: NO | Nullable: NO
- CESCUOTAI3: INTEGER | PK: NO | Nullable: NO
- CIDUNIDADCOMPRA: INTEGER | PK: NO | Nullable: NO
- CIDUNIDADVENTA: INTEGER | PK: NO | Nullable: NO
- CSUBTIPO: INTEGER | PK: NO | Nullable: NO
- CCODALTERN: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNOMALTERN: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CDESCCORTA: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CIDMONEDA: INTEGER | PK: NO | Nullable: NO
- CUSABASCU: INTEGER | PK: NO | Nullable: NO
- CTIPOPAQUE: INTEGER | PK: NO | Nullable: NO
- CPRECSELEC: INTEGER | PK: NO | Nullable: NO
- CDESGLOSAI2: INTEGER | PK: NO | Nullable: NO
- CSEGCONTPRODUCTO4: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGCONTPRODUCTO5: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGCONTPRODUCTO6: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CSEGCONTPRODUCTO7: VARCHAR(20) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CCTAPRED: VARCHAR(150) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNODESCOMP: INTEGER | PK: NO | Nullable: NO
- CIDUNIXML: INTEGER | PK: NO | Nullable: NO
- CCLAVESAT: VARCHAR(8) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CCANTIDADFISCAL: FLOAT | PK: NO | Nullable: NO
- CUNIDADDIMENSION: INTEGER | PK: NO | Nullable: NO
- CALTO: FLOAT | PK: NO | Nullable: NO
- CLARGO: FLOAT | PK: NO | Nullable: NO
- CANCHO: FLOAT | PK: NO | Nullable: NO

---

## TABLE: admProductosDetalles

**Descripción:** Tabla complementaria que almacena información adicional específica para productos con características variables. Registra el tipo de producto (si es producto hijo de uno con características), el producto padre del que deriva y los valores de hasta 3 características que lo definen. Es utilizada para gestionar variantes de productos (ejemplo: una camisa azul talla M sería un registro hijo de la camisa genérica, con características: color=azul, talla=M).

## Columns

- CIDPRODUCTO: INTEGER | PK: YES | Nullable: NO
- CTIPOPRODUCTO: INTEGER | PK: NO | Nullable: NO
- CIDPRODUCTOPADRE: INTEGER | PK: NO | Nullable: NO
- CIDVALORCARACTERISTICA1: INTEGER | PK: NO | Nullable: NO
- CIDVALORCARACTERISTICA2: INTEGER | PK: NO | Nullable: NO
- CIDVALORCARACTERISTICA3: INTEGER | PK: NO | Nullable: NO
- CTIMESTAMP: VARCHAR(23) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO

---

## TABLE: admProductosFotos

**Descripción:** Catálogo de imágenes de productos. Almacena las fotografías de productos en formato binario (campo TEXT) junto con su nombre identificador. Las imágenes se relacionan con productos mediante el campo CIDFOTOPRODUCTO en la tabla admProductos. Es utilizado para mostrar imágenes en documentos impresos, catálogos electrónicos, punto de venta y e-commerce.

## Columns

- CIDFOTOPRODUCTO: INTEGER | PK: YES | Nullable: NO
- CNOMBREFOTOPRODUCTO: VARCHAR(40) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CFOTOPRODUCTO: TEXT(16) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: YES

---

## TABLE: admPromociones

**Descripción:** Catálogo de promociones y descuentos por volumen configurados en el sistema. Define reglas promocionales incluyendo: código, nombre, vigencia (fechas y horas de inicio/fin), volumen mínimo y máximo aplicable, porcentaje de descuento, clasificaciones de clientes y productos elegibles, tipo y subtipo de promoción, concepto asociado, días de aplicación y estatus. Es fundamental para gestión de descuentos automáticos por volumen, promociones temporales, descuentos por segmento de clientes, campañas comerciales y aplicación automática de ofertas en punto de venta.

## Columns

- CIDPROMOCION: INTEGER | PK: YES | Nullable: NO
- CCODIGOPROMOCION: VARCHAR(30) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CNOMBREPROMOCION: VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" | PK: NO | Nullable: NO
- CFECHAINICIO: DATETIME | PK: NO | Nullable: NO
- CFECHAFIN: DATETIME | PK: NO | Nullable: NO
- CVOLUMENMINIMO: FLOAT | PK: NO | Nullable: NO
- CVOLUMENMAXIMO: FLOAT | PK: NO | Nullable: NO
- CPORCENTAJED
