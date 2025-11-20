# Schema de Base de Datos - CONTPAQi Comercial

## Catálogo: Agentes (admAgentes)

El catálogo de Agentes almacena información sobre los representantes de ventas y cobro. Cada agente tiene un identificador único CIDAGENTE y un código alfanumérico CCODIGOAGENTE de hasta 30 caracteres. El nombre del agente se guarda en CNOMBREAGENTE con capacidad de 60 caracteres.

Los agentes se clasifican por tipo mediante CTIPOAGENTE: el valor 1 representa Agentes de Ventas, el valor 2 indica Agente Venta/Cobro, y el valor 3 corresponde a Agente de Cobro. Cada agente tiene asociadas comisiones: CCOMISIONVENTAAGENTE para comisión de ventas y CCOMISIONCOBROAGENTE para comisión de cobro.

La tabla permite relaciones especiales: CIDCLIENTE permite considerar un cliente como agente, mientras que CIDPROVEEDOR permite considerar un agente como proveedor. Los agentes pueden ser clasificados mediante seis campos de clasificación: CIDVALORCLASIFICACION1 hasta CIDVALORCLASIFICACION6.

Para integración contable, los agentes tienen tres segmentos contables: CSEGCONTAGENTE para el primer segmento, CSCAGENTE2 para el segundo, y CSCAGENTE3 para el tercero, cada uno con capacidad de 50 caracteres.

Los campos extras incluyen tres campos de texto (CTEXTOEXTRA1, CTEXTOEXTRA2, CTEXTOEXTRA3), una fecha extra (CFECHAEXTRA), y cuatro importes extras (CIMPORTEEXTRA1 a CIMPORTEEXTRA4). La fecha de alta se registra en CFECHAALTAAGENTE y el control de concurrencia se maneja con CTIMESTAMP de 23 caracteres.

---

## Catálogo: Almacenes (admAlmacenes)

El catálogo de Almacenes gestiona los lugares físicos donde se almacena inventario. Cada almacén se identifica únicamente por CIDALMACEN y tiene un código en CCODIGOALMACEN de hasta 30 caracteres y un nombre en CNOMBREALMACEN de hasta 60 caracteres.

Similar a los agentes, los almacenes soportan seis niveles de clasificación mediante CIDVALORCLASIFICACION1 hasta CIDVALORCLASIFICACION6. La integración contable se realiza con tres segmentos: CSEGCONTALMACEN, CSCALMAC2, y CSCALMAC3, cada uno de 50 caracteres.

Los almacenes tienen campos extras con la misma estructura que otras tablas: tres textos extras, una fecha extra, y cuatro importes extras. El campo CBANDOMICILIO es una bandera que indica si el almacén lleva información de domicilio. El campo CSISTORIG identifica el sistema de origen del almacén.

La fecha de alta se almacena en CFECHAALTAALMACEN y la concurrencia se controla con CTIMESTAMP de 23 caracteres.

---

## Catálogo: Clientes y Proveedores (admClientes)

Esta es una tabla unificada que almacena tanto clientes como proveedores. El identificador único es CIDCLIENTEPROVEEDOR. Cada registro tiene un código en CCODIGOCLIENTE de 30 caracteres y la razón social en CRAZONSOCIAL de 60 caracteres.

**Información Fiscal:** El RFC se almacena en CRFC con 20 caracteres, y el CURP o número de identidad tributaria para extranjeros en CCURP también con 20 caracteres. El régimen fiscal del cliente se guarda en CREGIMFISC de 20 caracteres. La denominación comercial se almacena en CDENComercial de 50 caracteres.

**Tipo de Entidad:** El campo CTIPOCLIENTE determina si es: 1=Cliente, 2=Cliente/Proveedor, o 3=Proveedor. El estatus actual se indica en CESTATUS donde 0=Inactivo y 1=Activo. Si está inactivo, CFECHABAJA registra cuándo quedó inactivo.

**Información de Crédito para Clientes:** CBANVENTACREDITO indica si tiene ventas a crédito activas (0=No, 1=Sí). El límite de crédito se define en CLIMITECREDITOCLIENTE, los días de crédito en CDIASCREDITOCLIENTE, y CBANEXCEDERCREDITO indica si puede exceder su límite. El descuento por pronto pago se especifica en CDESCUENTOPRONTOPAGO con sus días en CDIASPRONTOPAGO. Los intereses moratorios se manejan con CINTERESMORATORIO y CBANINTERESMORATORIO indica si se calculan.

**Información de Crédito para Proveedores:** El límite que otorga el proveedor está en CLIMITECREDITOPROVEEDOR, los días de crédito en CDIASCREDITOPROVEEDOR, el tiempo de entrega en CTIEMPOENTREGA, y los días de embarque en CDIASEMBARQUEPROVEEDOR.

**Agentes:** Los clientes/proveedores tienen asociados un agente de ventas en CIDAGENTEVENTA y un agente de cobro en CIDAGENTECOBRO. Las comisiones específicas se manejan con CCOMVENTA y CCOMCOBRO para todos los documentos, y CCOMVENTAEXCEPCLIENTE y CCOMCOBROEXCEPCLIENTE para excepciones.

**Impuestos:** Tres campos de porcentaje de impuesto para clientes (CIMPUESTO1, CIMPUESTO2, CIMPUESTO3) y tres para proveedores (CIMPUESTOPROVEEDOR1, CIMPUESTOPROVEEDOR2, CIMPUESTOPROVEEDOR3). Las retenciones se manejan con CRETENCIONCLIENTE1, CRETENCIONCLIENTE2 para clientes y CRETENCIONPROVEEDOR1, CRETENCIONPROVEEDOR2 para proveedores.

**Clasificaciones:** Seis clasificaciones para clientes (CIDVALORCLASIFCLIENTE1 a 6) y seis para proveedores (CIDVALORCLASIFPROVEEDOR1 a 6).

**Segmentos Contables:** Siete segmentos contables para clientes (CSEGCONTCLIENTE1 a CSEGCONTCLIENTE7) y siete para proveedores (CSEGCONTPROVEEDOR1 a CSEGCONTPROVEEDOR7), cada uno de 50 caracteres.

**Facturación Electrónica (CFD/CFDI):** Tres correos electrónicos (CEMAIL1, CEMAIL2, CEMAIL3) de 60 caracteres cada uno. CTIPOENTRE define el tipo de entrega: 0=Correo electrónico, 1=Impresión, 2=Archivo en disco, 6=Correo con ZIP (XML y PDF). CBANCFD indica si maneja CFD (0=No, 1=Sí). CUSOCFDI de 30 caracteres define el uso que el cliente dará a los CFDIs por omisión. CMETODOPAG de 100 caracteres indica el método de pago y CNUMCTAPAG de 100 caracteres el número de cuenta de pago.

**Otros Campos Importantes:** CIDMONEDA y CIDMONEDA2 para manejar monedas. CLISTAPRECIOCLIENTE para la lista de precios asignada. CFACTERC01 indica si puede facturar a terceros. CBANPRODUCTOCONSIGNACION indica si permite productos en consignación. CLIMDOCTOS define el número máximo de documentos vencidos permitidos. CWHATSAPP de 15 caracteres guarda el número de contacto de WhatsApp.

Los campos extras incluyen cinco textos (CTEXTOEXTRA1 a CTEXTOEXTRA5), una fecha (CFECHAEXTRA), y cinco importes (CIMPORTEEXTRA1 a CIMPORTEEXTRA5). Múltiples banderas controlan qué secciones tienen datos: CBANDOMICILIO, CBANCREDITOYCOBRANZA, CBANENVIO, CBANAGENTE, CBANIMPUESTO, CBANPRECIO.

---

## Catálogo: Conceptos de Documento (admConceptos)

Los conceptos definen el comportamiento y configuración de los diferentes tipos de documentos. Cada concepto tiene un identificador CIDCONCEPTODOCUMENTO, un código en CCODIGOCONCEPTO de 30 caracteres, y un nombre en CNOMBRECONCEPTO de 60 caracteres.

**Configuración Básica:** CIDDOCUMENTODE referencia el tipo de documento modelo de la tabla TblDocumentoDe. CNATURALEZA define la naturaleza: 0=Cargo, 1=Abono, 2=Sin naturaleza. CDOCTOACREDITO indica si es a crédito (1) o contado (0).

**Folio:** CTIPOFOLIO define el tipo: 1=Folio automático calculado al crear el documento y modificable, 2=Folio automático calculado antes de imprimir y modificable. CSERIEPOROMISION de 11 caracteres define la serie por omisión. CNOFOLIO contiene el folio asumido.

**Cálculos:** CORDENCALCULO define el orden de cálculo de impuestos, descuentos y retenciones con 6 combinaciones posibles: 1=Descuentos-Impuestos-Retenciones, 2=Descuentos-Retenciones-Impuestos, 3=Impuestos-Descuentos-Retenciones, 4=Impuestos-Retenciones-Descuentos, 5=Retenciones-Impuestos-Descuentos, 6=Retenciones-Descuentos-Impuestos.

**Visibilidad de Campos del Encabezado:** Múltiples campos CUSA* controlan la visibilidad y capturabilidad de campos en el documento: 1=No visible, 2=Visible solo lectura, 3=Visible y capturable. Estos incluyen: CUSANOMBRECTEPROV, CUSARFC, CUSAFECHAVENCIMIENTO, CUSAFECHAENTREGARECEPCION, CUSAMONEDA, CUSATIPOCAMBIO, CUSACODIGOAGENTE, CUSANOMBREAGENTE, CUSADIRECCION, CUSAREFERENCIA.

**Visibilidad de Columnas de Movimientos:** Similar al encabezado, controlan las columnas en el grid de movimientos. CUSANOMBREPRODUCTO controla la columna del nombre del producto (1=No se usa, 2=No visible, 3=Visible solo lectura, 4=Visible y capturable). Lo mismo aplica para CUSAALMACEN, CUSAPRECIO, CUSACOSTOCAPTURADO, CUSAEXISTENCIA, CUSANETO, y todas las columnas de impuestos, retenciones y descuentos.

**Impuestos y Retenciones:** Cada impuesto (1, 2, 3) tiene dos campos: uno para el porcentaje (CUSAPORCENTAJEIMPUESTO*) y otro para el importe (CUSAIMPUESTO*), cada uno con su fórmula asociada (CIDFORMULAPORCIMPUESTO*, CIDFORMULAIMPUESTO*). Lo mismo para retenciones (CUSAPORCENTAJERETENCION*, CUSARETENCION*) y cinco niveles de descuentos.

**Descuentos:** Cinco niveles de descuentos en movimientos, cada uno con porcentaje e importe. Dos descuentos a nivel documento (CUSADESCUENTODOC1, CUSADESCUENTODOC2) con sus fórmulas (CIDFORMULADESDOC1, CIDFORMULADESDOC2).

**Gastos:** Tres gastos sobre compra (CUSAGASTO1, CUSAGASTO2, CUSAGASTO3) con sus fórmulas (CIDFORMULAGASTO1, CIDFORMULAGASTO2, CIDFORMULAGASTO3). CUSAEXTRACOMOGASTO indica si se usa algún importe extra como gasto: 0=No, 1=Importe Extra 1, 2=Importe Extra 2, 3=Importe Extra 3, 4=Importe Extra 4.

**Campos Extra en Movimientos:** Tres textos extras (CUSATEXTOEXTRA1, CUSATEXTOEXTRA2, CUSATEXTOEXTRA3), una fecha extra (CUSAFECHAEXTRA), y cuatro importes extras (CUSAIMPORTEEXTRA1 a 4), cada uno con sus fórmulas correspondientes.

**Campos Extra en Documento:** Banderas para hacer visibles campos extras a nivel documento: CUSATEXTOEXTRA1DOC a 3DOC, CUSAFECHAEXTRADOC, CUSAIMPORTEEXTRA1DOC a 4DOC.

**Pantallas que se Presentan:** Múltiples banderas CPRESENTA* controlan qué pantallas se muestran después de capturar: CPRESENTAFISCAL, CPRESENTAREFERENCIA, CPRESENTACONDICIONES, CPRESENTAENVIO, CPRESENTADETALLE, CPRESENTAIMPRIMIR, CPRESENTAPAGAR, CPRESENTASALDAR, CPRESENTADOCUMENTAR, CPRESENTAGASTOSCOMPRA.

**Segmentos Contables:** CSEGCONTCONCEPTO de 50 caracteres para el segmento del concepto, CSCCPTO2 y CSCCPTO3 para segmentos adicionales. CSCMOVTO para segmento contable de movimientos.

**Facturación Electrónica (CFD/CFDI):** CESCFD indica si es Comprobante Fiscal Digital. CIDFIRMARL es el identificador de la firma electrónica. CGDAPASSW guarda la contraseña del certificado. CEMITEYENT indica si emite y entrega a la vez. CBANCFD indica si tiene configuración de CFD. CREPIMPCFD de 253 caracteres guarda la ruta del reporte de impresión. CVERFACELE indica la versión del anexo 20: 0=v1.0, 1=v2.0, 2=v4.0. CVERESQUE de 50 caracteres guarda la versión del esquema SAT. CREGIMFISC de 100 caracteres define el régimen fiscal por omisión. CMETODOPAG de 50 caracteres define el método de pago por omisión. CUSAOBJIMP indica si permite seleccionar objeto de impuesto (0=No, 1=Sí).

**Transformaciones:** CCALFECHAS controla el recálculo de fechas en transformaciones con 7 opciones (0 a 6). CTIPCAMTR1 y CTIPCAMTR2 controlan el tipo de cambio en transformaciones entre monedas. CCONSOLIDA activa si el documento destino puede consolidarse. CBANTRANS indica si se configuró transformaciones. CIDCPTODE1, CIDCPTODE2, CIDCPTODE3 son identificadores de conceptos destino de transformación.

**Seguridad:** Múltiples campos CIDPRSEG* identifican procesos de seguridad: CIDPRSEG02 para modificación, CIDPRSEG03 para eliminación, CIDPRSEG04 para cancelación, CIDPRSEG05 para cambiar estado de impreso, CIDPRSEG06 para creación, CIDPRSEG07 para impresión.

**Otros:** CMAXIMOMOVTOS define el número máximo de movimientos. CCREACLIENTE indica si se puede crear cliente en la captura. CIDASTOCON es el identificador del asiento contable. CIDCONAUTO para concepto que se genera automáticamente. CIDALMASUM para almacén asumido. CUSACOMVTA indica si usa comisión de venta. CAPFORMULA indica si recalcula fórmulas en transformaciones. CESTATUS indica si el concepto está activo (0=No, 1=Sí). CRESERVADO indica si es concepto reservado.

---

## Tabla: Documentos (admDocumentos)

La tabla de documentos almacena todos los documentos generados: facturas, pedidos, remisiones, compras, etc. Cada documento tiene un identificador único CIDDOCUMENTO.

**Identificación:** CIDDOCUMENTODE referencia el tipo de documento modelo. CIDCONCEPTODOCUMENTO identifica el concepto usado. CSERIEDOCUMENTO y CFOLIO forman la serie-folio del documento. CFECHA es la fecha del documento.

**Cliente/Proveedor:** CIDCLIENTEPROVEEDOR identifica al cliente o proveedor (puede estar vacío en documentos de almacén). CRAZONSOCIAL guarda la razón social del cliente y CRFC su RFC. CUSACLIENTE y CUSAPROVEEDOR indican si usa cliente o proveedor.

**Agente:** CIDAGENTE identifica al agente (puede estar vacío en documentos de proveedor y almacén).

**Fechas:** CFECHAVENCIMIENTO para vencimiento del documento, CFECHAPRONTOPAGO para pronto pago, CFECHAENTREGARECEPCION para entrega en ventas o recepción en compras, CFECHAULTIMOINTERES para último cálculo de intereses moratorios.

**Moneda:** CIDMONEDA identifica la moneda. CTIPOCAMBIO contiene el tipo de cambio (1 si es moneda base, el tipo de cambio específico si es extranjera).

**Referencia y Observaciones:** CREFERENCIA de 20 caracteres para la referencia. COBSERVACIONES tipo Text para observaciones del documento.

**Naturaleza:** CNATURALEZA indica: C=Cargo, A=Abono, N=Sin naturaleza.

**Estados del Documento:** CPLANTILLA indica si es plantilla (0=No, 1=Sí). CAFECTADO indica si está afectado (0=No, 1=Sí). CIMPRESO indica si está impreso (0=No, 1=Sí). CCANCELADO indica si está cancelado (0=No, 1=Sí). CDEVUELTO indica si fue devuelto (0=No, 1=Sí).

**Contabilidad:** CIDPREPOLIZA contiene el ID de la prepóliza cuando está precontabilizado. CIDPREPOLIZACANCELACION contiene el ID de la prepóliza de cancelación. CESTADOCONTABLE indica el estado: 1=No Contabilizado, 2=Prepóliza documento, 3=Prepóliza Diaria, 4=Prepóliza por Periodo, 5=Póliza documento, 6=Póliza Diaria, 7=Póliza por Periodo, 8=Póliza modificada.

**Importes Totales:** CNETO para total del neto. Tres impuestos (CIMPUESTO1, CIMPUESTO2, CIMPUESTO3) y dos retenciones (CRETENCION1, CRETENCION2). CDESCUENTOMOV para descuentos de movimientos. Dos descuentos de documento (CDESCUENTODOC1, CDESCUENTODOC2). Tres gastos sobre compra (CGASTO1, CGASTO2, CGASTO3). CTOTAL para el total general. CPENDIENTE para saldo pendiente. CTOTALUNIDADES para unidades totales.

**Porcentajes:** CDESCUENTOPRONTOPAGO, CPORCENTAJEIMPUESTO1, CPORCENTAJEIMPUESTO2, CPORCENTAJEIMPUESTO3, CPORCENTAJERETENCION1, CPORCENTAJERETENCION2, CPORCENTAJEINTERES para los respectivos porcentajes.

**Campos Extra:** Tres textos (CTEXTOEXTRA1, CTEXTOEXTRA2, CTEXTOEXTRA3) de 50 caracteres, una fecha (CFECHAEXTRA), y cuatro importes (CIMPORTEEXTRA1 a CIMPORTEEXTRA4).

**Envío:** CDESTINATARIO de 60 caracteres para nombre del destinatario. CNUMEROGUIA de 60 caracteres para número de guía. CMENSAJERIA de 20 caracteres para nombre de mensajería. CCUENTAMENSAJERIA de 60 caracteres para cuenta. CNUMEROCAJAS y CPESO para número y peso de cajas.

**Banderas de Captura:** CBAN OBSERVACIONES indica si se capturaron observaciones. CBANDATOSENVIO si se capturaron datos de envío. CBANCONDICIONESCREDITO si se capturaron condiciones de crédito. CBANGASTOS si se capturaron gastos.

**Otros:** CUNIDADESPENDIENTES para unidades por surtir. CIDDOCUMENTOORIGEN identifica el documento origen (usado en descuentos por pronto pago, intereses moratorios, etc.). CSISTORIG identifica el sistema origen: 5=AdminPAQ, 205=CONTPAQi Comercial, 101=Punto de venta, 202=Factura electrónica, 301=CONTPAQi Cobra.

**CFD/CFDI:** CESCFD indica si es Comprobante Fiscal Digital. CLUGAREXPE de 80 caracteres para lugar de expedición. CMETODOPAG de 100 caracteres para método de pago. CNUMPARCIA para número de parcialidades. CCANTPARCI para cantidad de parcialidades. CCONDIPAGO de 253 caracteres para condiciones de pago. CNUMCTAPAG de 100 caracteres para número de cuenta de pago. CGUIDDOCUMENTO de 40 caracteres como identificador único en SQL. CIDCUENTA para identificador de cuenta bancaria. CVERESQUE de 6 caracteres para versión del esquema SAT. CDATOSADICIONALES tipo Varchar MAX para datos adicionales como archivo INI del CCP.

**Relaciones:** CIDCOPIADE identifica el documento del cual se copió el actual.

---

## Tabla: Documentos Modelo (admDocumentosModelo)

Define los tipos de documentos soportados por el sistema. CIDDOCUMENTODE es el identificador del tipo de documento.

**Tipos de Documentos (CIDDOCUMENTODE):**
- 1=Cotización, 2=Pedido, 3=Remisión, 4=Factura, 5=Devolución sobre Venta, 6=Devolución de Remisión, 7=Nota de Crédito, 8=Cambio del cliente, 9=Pago del cliente, 10=Cheque recibido
- 11=Honorarios del cliente, 12=Abono del Cliente, 13=Nota de Cargo al Cliente, 14=Descuento por pronto pago, 15=Pagaré, 16=Interés Moratorio
- 17=Orden de Compra, 18=Consignación del Proveedor, 19=Compra, 20=Devolución sobre Compra, 21=Devolución de Consignación, 22=Nota de Crédito del Proveedor, 23=Pago al proveedor, 24=Cheque emitido, 25=Honorarios del Proveedor, 26=Abono al Proveedor, 27=Cargo del Proveedor
- 28=Utilidad Cambiaria Cliente, 29=Pérdida Cambiaria Cliente, 30=Utilidad Cambiaria Proveedor, 31=Pérdida Cambiaria Proveedor
- 32=Entrada al Almacén, 33=Salida del Almacén, 34=Traspasos, 35=Nota de Venta, 36=Devolución sobre Nota de Venta, 37=Ajuste al Costo

**Atributos:** CDESCRIPCION de 50 caracteres describe el documento. CNATURALEZA indica naturaleza (0=Cargo, 1=Abono, 2=Sin naturaleza). CAFECTAEXISTENCIA define cómo afecta existencias: 1=Entradas, 2=Salidas, 3=Ninguno.

**Módulo:** CMODULO indica de dónde se capturan: 1=Ventas, 2=Compras, 3=Clientes, 4=Proveedores, 5=Inventarios.

**Otros:** CNOFOLIO para el folio. CIDCONCEPTODOCTOASUMIDO para el concepto que se muestra por omisión en modo inserción. CUSACLIENTE y CUSAPROVEEDOR indican si usa cliente o proveedor. CIDASIENTOCONTABLE para el identificador del asiento contable.

---

## Tabla: Folios Digitales (admFoliosDigitales)

Almacena información sobre folios fiscales digitales (CFD/CFDI). CIDFOLDIG es el identificador único del folio digital.

**Relaciones:** CIDDOCTODE identifica el documento modelo. CIDCPTODOC identifica el concepto. CIDDOCTO identifica el documento asociado. CIDDOCALDI relaciona documentos de almacén con folios digitales.

**Certificado:** CIDFIRMARL es el identificador del certificado del sello digital. CNOORDEN es el número de orden de generación del sello.

**Serie y Folio:** CSERIE de 10 caracteres para la serie digital. CFOLIO para el folio digital. CNOAPROB para número de aprobación. CFECAPROB para fecha de aprobación.

**Estado del Folio (CESTADO):**
- 0=Disponible, 1=Ocupado no emitido, 2=Ocupado y emitido, 3=Cancelado
- 4=Por Confirmar timbrado (Requiere clave), 5=Por Autorizar cancelación (esperando confirmación receptor), 6=Por confirmar cancelación (Confirmar o rechazar)
- 10=Disponible no asociado, 11=Recibido no asociado, 12=Recibido cancelado, 13=Recibido asociado Adw, 14=Recibido asociado Ctw

**Emisión:** CFECHAEMI para fecha de emisión. CHORAEMI para hora de emisión. CENTREGADO indica si fue entregado (0=No, 1=Sí).

**Entrega:** CEMAIL de 60 caracteres guarda el correo electrónico de entrega. CARCHDIDIS de 253 caracteres guarda la ruta del archivo en disco.

**Cancelación:** CFECHACANC para fecha de cancelación. CHORACANC de 8 caracteres para hora. CREFEREN01 de 20 caracteres para motivo de cancelación. CACUSECAN de 30 caracteres para nombre del archivo de acuse de cancelación del SAT.

**UUID y Relacionados:** CUUID de 60 caracteres guarda el UUID del documento timbrado. CCADPEDI tipo Medium Text contiene la lista de UUIDs de CFDIs relacionados. CUSUBAN02 de 20 caracteres indica el tipo de relación con otros CFDIs.

**Documento Recibido:** Para CFDs recibidos, CTIPO de 1 caracter indica tipo (I=Ingreso, E=Egreso). CSERIEREC de 25 caracteres para serie recibida. CFOLIOREC para folio recibido. CRFC de 20 caracteres y CRAZON de 253 caracteres para RFC y razón social del emisor. CTOTAL para importe total. CCFDPRUEBA indica si se generó con certificado de prueba.

**Asociación Contable:** Para documentos recibidos asociados a pólizas: CSISORIGEN para sistema origen, CEJERPOL para ejercicio, CPERPOL para periodo, CTIPOPOL para tipo, CNUMPOL para número, CTIPOLDESC de 100 caracteres para descripción. CALIASBDCT de 50 caracteres para alias de base de datos de CONTPAQi Contabilidad.

**Facturación Global:** CPAGADOBAN para año de facturación global. CDESPAGBAN de 20 caracteres para periodicidad. CFOLIOBAN de 20 caracteres para meses.

**Complemento de Pagos:** CDESCONCBA de 100 caracteres para número de operación (NumOperación del complemento). CNUMCTABAN de 30 caracteres para cuenta bancaria. CUSUAUTBAN de 20 caracteres para tipo de pago (TipoCadPago).

**Uso CFDI y Régimen:** CCODCONCBA de 30 caracteres para uso del CFDI. CDESCAUT03 de 20 caracteres para moneda. CDESCAUT02 de 20 caracteres para tipo de cambio. CDESCAUT03 de 20 caracteres para régimen fiscal del receptor.

**Cancelación y Confirmación:** CUSUBAN01 de 20 caracteres para clave de confirmación. CAUTUSBA01 indica estado de cancelación: 0=Sin intentos, 1=Rechazado, 2=Sin Aceptación, 3=Plazo Vencido, 4=Con Aceptación, 5=En proceso.

**Configuraciones CFDI 4.0:** CAUTUSBA02 indica opciones de timbrado: 0=No desglosa IEPS, 1=Con desglose de IEPS. CAUTUSBA03 almacena tipo de exportación: 1=No aplica, 2=Definitiva A1, 3=Temporal, 4=Definitiva distinta A1.

**Otros:** CESTRAD indica estado: 0=Digital, 1=Tradicional. COBSERVA01 de 253 caracteres para observaciones del XML. CUSUBAN03 de 20 caracteres para hora de pago. CINIVIG y CFINVIG para inicio y fin de vigencia. CIDCPTOORI para identificador del concepto original. CIDDOCDEBA para identificador del documento bancario asociado. CERRORVAL maneja errores de validaciones en almacén digital. CIDDOCTODSL de 40 caracteres es el identificador en el ADD (Administrador de Documentos Digitales).

---

## Catálogo: Monedas (admMonedas)

Almacena las monedas utilizadas en el sistema. CIDMONEDA es el identificador único de la moneda.

**Identificación:** CNOMBREMONONEDA de 60 caracteres para el nombre de la moneda. CSIMBOLOMONEDA de 1 caracter para el símbolo ($, €, etc.). CPOSICIONSIMBOLO indica la posición: 0=Antes de la cifra, 1=Después de la cifra.

**Descripción:** CPLURAL de 60 caracteres para el plural de la moneda (Pesos, Dólares). CSINGULAR de 60 caracteres para el singular (Peso, Dólar). CDESCRIPCIONPROTEGIDA de 60 caracteres para la descripción de cantidad protegida.

**Otros:** CIDBANDERA es el identificador de la bandera asociada. CDECIMALESMONEDA indica el número de decimales de la moneda. CTIMESTAMP de 23 caracteres para control de concurrencia.

---

## Tabla: Movimientos (admMovimientos)

Almacena las líneas o detalles de los documentos. Cada movimiento representa un producto/servicio en un documento. CIDMOVIMIENTO es el identificador único del movimiento.

**Documento:** CIDDOCUMENTO identifica el documento al que pertenece. CFECHA es la fecha del documento (denormalizada para consultas).

**Producto:** CIDPRODUCTO identifica el producto del movimiento. CIDALMACEN identifica el almacén del movimiento.

**Unidades:** CUNIDADES contiene la cantidad en la unidad base del producto **Unidades (continuación):** CUNIDADES contiene la cantidad en la unidad base del producto. CUNIDADESCAPTURADAS contiene la cantidad en la unidad que el usuario capturó (puede ser diferente si usa unidades con equivalencia). CIDUNIDAD identifica la unidad de peso y medida capturada (puede ser base o convertible). CIDUNIDADNC identifica la unidad no convertible si la tiene.

**Precios y Costos:** CPRECIO contiene el precio unitario del producto en la unidad base. CPRECIOCAPTURADO es el precio en la unidad capturada por el usuario. CCOSTOCAPTURADO es el costo unitario capturado manualmente (usado en devoluciones sobre ventas). CCOSTOESPECIFICO es el costo calculado del movimiento (importante: en costeo promedio o último costo puede no aparecer en reportes de Kárdex ya que se toma de Costos históricos).

**Importes del Movimiento:** CNETO para el importe neto. CTOTAL para el importe total del movimiento.

**Impuestos:** Tres niveles de impuestos, cada uno con su importe y porcentaje: CIMPUESTO1 con CPORCENTAJEIMPUESTO1, CIMPUESTO2 con CPORCENTAJEIMPUESTO2, CIMPUESTO3 con CPORCENTAJEIMPUESTO3.

**Retenciones:** Dos niveles de retenciones: CRETENCION1 con CPORCENTAJERETENCION1, CRETENCION2 con CPORCENTAJERETENCION2.

**Descuentos:** Cinco niveles de descuentos, cada uno con importe y porcentaje: CDESCUENTO1 con CPORCENTAJEDESCUENTO1, hasta CDESCUENTO5 con CPORCENTAJEDESCUENTO5.

**Comisiones:** CPORCENTAJECOMISION para el porcentaje de comisión del movimiento. CCOMVENTA indica la comisión de venta por ese movimiento específico.

**Referencia y Observaciones:** CREFERENCIA de 20 caracteres para la referencia del movimiento. COBSERVAMOV tipo Text para observaciones del movimiento.

**Control de Existencias:** CAFECTAEXISTENCIA indica cómo afecta existencias: 1=Entradas, 2=Salidas, 3=Ninguno. CAFECTADOSALDOS indica si ya afectó saldos y estadísticas (0=No, 1=Sí). CAFECTADOINVENTARIO indica si ya afectó existencias y costos (0=No, 1=Sí).

**Movimientos Ocultos:** CMOVTOOCULTO indica si fue capturado por usuario o generado por sistema: 0=Movimiento real, 1=Movimiento oculto, 2=Movimiento oculto. Los movimientos ocultos se generan para almacén destino de traspasos, detalles de características, y componentes de paquetes. CIDMOVTOOWNER contiene el identificador del movimiento que originó el movimiento oculto (vacío si es movimiento real).

**Conversiones:** CIDMOVTOORIGEN contiene el ID del movimiento origen cuando proviene de una conversión (ejemplo: movimiento de factura que surtió un pedido). CUNIDADESPENDIENTES son las unidades que faltan por convertir. CUNIDADESNCPENDIENTES son las unidades no convertibles pendientes. CUNIDADESORIGEN son las unidades que el movimiento destino toma del origen en la conversión. CUNIDADESNCORIGEN son las unidades no convertibles que toma del origen.

**Traspasos:** CTIPOTRASPASO indica el tipo: 1=Sin traspaso, 2=Origen traspaso, 3=Destino traspaso, 4=Detalle características traspaso, 5=Facturación consignación cliente, 6=Compra consignación proveedor, 7=Movimiento componente.

**Clasificación:** CIDVALORCLASIFICACION identifica el valor de clasificación del movimiento (debe ser de la clasificación 31).

**Campos Extra:** Tres textos (CTEXTOEXTRA1, CTEXTOEXTRA2, CTEXTOEXTRA3) de 50 caracteres, una fecha (CFECHAEXTRA), y cuatro importes (CIMPORTEEXTRA1, CIMPORTEEXTRA2, CIMPORTEEXTRA3, CIMPORTEEXTRA4).

**Contabilidad:** CGTOMOVTO contiene el gasto sobre compra del movimiento. CSCMOVTO de 50 caracteres para el segmento contable del movimiento.

**Consolidación:** CIDMOVTODESTINO identifica el movimiento destino para consolidación. CNUMEROCONSOLIDACIONES indica el número de consolidaciones realizadas.

**Objeto de Impuesto (CFDI 4.0):** COBJIMPU01 de 20 caracteres indica: 01=No objeto de impuesto, 02=Sí objeto de impuesto, 03=Sí objeto no obligado al desglose, 04=Sí objeto no causa impuesto.

**Concurrencia:** CTIMESTAMP de 23 caracteres para control de concurrencia.

---

## Catálogo: Productos (admProductos)

Almacena productos, servicios y paquetes. CIDPRODUCTO es el identificador único.

**Identificación:** CCODIGOPRODUCTO de 30 caracteres para el código. CNOMBREPRODUCTO de 60 caracteres para el nombre. CTIPOPRODUCTO indica el tipo: 1=Producto, 2=Paquete, 3=Servicio. CSUBTIPO proporciona subclasificación: 1=Pago de servicio, 2=Paquete inventariable, 9=Servicio de facturación CONTPAQi Punto de Venta.

**Códigos Alternos:** CCODALTERN de 30 caracteres para código alterno. CNOMALTERN de 60 caracteres para nombre alterno. CDESCCORTA de 30 caracteres para descripción corta.

**Fechas:** CFECHAALTAPRODUCTO para fecha de alta. CFECHABAJA para fecha en que quedó inactivo.

**Estado:** CSTATUSPRODUCTO indica estatus: 0=Baja lógica, 1=Alta.

**Control de Existencias:** CCONTROLEXISTENCIA usa valores binarios para indicar el tipo de control: 00000001=Unidades, 00000010=Características, 00000100=Series, 00001000=Pedimentos, 00010000=Lotes. Puede combinarse múltiples controles.

**Descripción:** CIDFOTOPRODUCTO para foto del producto. CDESCRIPCIONPRODUCTO tipo Text para descripción detallada.

**Costeo:** CMETODOCOSTEO indica el método: 1=Costo Promedio base Entradas, 2=Costo Promedio base Entradas Almacén, 3=Último Costo, 4=UEPS, 5=PEPS, 6=Costo Específico, 7=Costo Estándar. CCOSTOESTANDAR contiene el valor del costo estándar. CERRORCOSTO indica errores: 0=Sin error, 1=Captura en desorden entradas, 2=Captura en desorden salidas, 3=Existencias negativas, 4=Series huérfanas, 5=Series sin costo. CFECHAERRORCOSTO indica la fecha del error. CEXISTENCIANEGATIVA indica si ha tenido existencia negativa (0=No, 1=Sí).

**Costos Extras (Producción):** Cinco costos extras con sus campos: CCOSTOEXT1 a CCOSTOEXT5 para los importes, CFECCOSEX1 a CFECCOSEX5 para fechas, CMONCOSEX1 a CMONCOSEX5 para las monedas. CBancosEX indica si fueron capturados costos extra.

**Unidades:** CIDUNIDADBASE identifica la unidad base del producto. CIDUNIDADNOCONVERTIBLE identifica la unidad no convertible. CIDUNICOMPRA indica la unidad asumida en documentos de compra. CIDUNIVENTA indica la unidad asumida en documentos de venta. CIDUNIXML identifica la unidad dentro del XML.

**Peso:** CPESOPRODUCTO contiene el peso del producto.

**Comisiones:** CCOMVENTAEXCEPPRODUCTO para comisión de venta por excepción. CCOMCOBROEXCEPPRODUCTO para comisión de cobro por excepción.

**Utilidad:** CMARGENUTILIDAD para el margen de utilidad del producto.

**Impuestos:** Tres impuestos con CIMPUESTO1, CIMPUESTO2, CIMPUESTO3 para los porcentajes. Dos retenciones con CRETENCION1, CRETENCION2. CESEXENTO indica si es exento de IVA (0=No exento, 1=Exento). CESCUOTAI2 indica si impuesto 2 es porcentaje o cuota fija (0=Porcentaje, 1=Cuota fija). CESCUOTAI3 lo mismo para impuesto 3. CDESGLOSAI2 indica si desglosa IEPS en CFD (0=No, 1=Sí).

**Características:** Tres padres de características: CIDPADRECARACTERISTICA1, CIDPADRECARACTERISTICA2, CIDPADRECARACTERISTICA3.

**Clasificaciones:** Seis clasificaciones del producto: CIDVALORCLASIFICACION1 hasta CIDVALORCLASIFICACION6.

**Segmentos Contables:** Siete segmentos contables: CSEGCONTPRODUCTO1 de 50 caracteres, CSEGCONTPRODUCTO2 de 50 caracteres, CSEGCONTPRODUCTO3 de 50 caracteres, CSEGCONTPRODUCTO4 de 20 caracteres, CSEGCONTPRODUCTO5 de 20 caracteres, CSEGCONTPRODUCTO6 de 20 caracteres, CSEGCONTPRODUCTO7 de 20 caracteres.

**Campos Extra:** Tres textos (CTEXTOEXTRA1, CTEXTOEXTRA2, CTEXTOEXTRA3) de 50 caracteres, una fecha (CFECHAEXTRA), y cuatro importes (CIMPORTEEXTRA1, CIMPORTEEXTRA2, CIMPORTEEXTRA3, CIMPORTEEXTRA4).

**Precios:** Diez niveles de precio: CPRECIO1 hasta CPRECIO10. CPRECIOCALCULADO y CESTADOPRECIO se usan solo en Actualización de listas de precios.

**Banderas de Configuración:** Múltiples banderas indican qué fue configurado: CBANUNIDADES (unidades), CBANCARACTERISTICAS (características), CBANMETODOCOSTEO (método costeo), CBANMAXMIN (máximos y mínimos), CBANPRECIO (precio), CBANIMPUESTO (impuestos), CBANCODIGOBARRA (código de barras), CBANCOMPONENTE (componentes), CBANUBICACION (ubicaciones).

**Moneda:** CIDMONEDA identifica la moneda asociada al producto.

**Otros:** CUSABASCU indica si requiere ser pesado (0=No, 1=Sí). CCTAPRED de 150 caracteres para número de cuenta predial (usado en recibos arrendamiento). CNODESCOMP indica si desglosa componentes en XML cuando es paquete (0=Sí desglosa, 1=No desglosa). CCLAVESAT de 3 caracteres para clave SAT del producto o servicio. CCANTIDADFISCAL para proporción de base en cálculo de cuota fija IEPS.

**Concurrencia:** CTIMESTAMP de 23 caracteres para control de concurrencia.

---

## Relaciones y Flujos Principales

### Flujo de Ventas
Un documento de ventas inicia con un Cliente (admClientes con CTIPOCLIENTE=1 o 2). Se selecciona un Concepto (admConceptos) que determina el comportamiento del documento. El Concepto referencia un Documento Modelo (admDocumentosModelo) que define si es Cotización, Pedido, Remisión o Factura.

Los documentos se crean en admDocumentos con CIDDOCUMENTODE que indica el tipo de documento. Por ejemplo, el 4 corresponde a facturas, 1 a cotizaciones, 2 a pedidos,3 a remisiones apuntando al modelo correspondiente. Cada línea del documento es un registro en admMovimientos que referencia un Producto (admProductos) y un Almacén (admAlmacenes). Si el documento afecta inventario, CAFECTADOINVENTARIO se marca como 1.

Las ventas pueden tener un Agente asignado (admAgentes) tanto a nivel documento como a nivel cliente. Las comisiones se calculan usando los porcentajes definidos en el agente, cliente o producto según la configuración.

Si el documento es una Factura con facturación electrónica, se genera un registro en admFoliosDigitales con el UUID, certificado y toda la información fiscal necesaria.

### Flujo de Compras
Similar al flujo de ventas pero usando Proveedor (admClientes con CTIPOCLIENTE=2 o 3). Los documentos modelo son Orden de Compra, Compra, Devolución sobre Compra, etc. Los gastos sobre compra se pueden aplicar usando los campos CGASTO1, CGASTO2, CGASTO3 tanto a nivel documento como movimiento.

### Flujo de Inventarios
Los movimientos de almacén (Entradas, Salidas, Traspasos) se registran sin cliente ni proveedor. En los Traspasos, se crean dos movimientos: uno de origen (CTIPOTRASPASO=2) y uno oculto de destino (CTIPOTRASPASO=3, CMOVTOOCULTO=1).

### Transformación de Documentos
Un documento puede transformarse en otro (ejemplo: Pedido a Factura). El movimiento destino tiene CIDMOVTOORIGEN apuntando al movimiento origen. Las unidades pendientes se actualizan en CUNIDADESPENDIENTES. La configuración de transformación se define en el Concepto con campos como CCALFECHAS, CTIPCAMTR1, CTIPCAMTR2, CCONSOLIDA.

### Control de Existencias
Dependiendo de CCONTROLEXISTENCIA del producto, el sistema maneja unidades simples, características (variantes), series, pedimentos o lotes. Los movimientos ocultos (CMOVTOOCULTO=1) se generan automáticamente para detalles de características y componentes de paquetes.

### Costeo
El costo se calcula según CMETODOCOSTEO del producto. CCOSTOESPECIFICO en el movimiento guarda el costo calculado. Para PEPS y UEPS, se consultan tablas de costos históricos. Los errores de costeo se marcan en CERRORCOSTO con su fecha en CFECHAERRORCOSTOPRODUCTO.

### Facturación Electrónica (CFD/CFDI)
Cuando un concepto tiene CESCFD=1, se habilita la emisión de comprobantes fiscales. Al emitir, se crea un registro en admFoliosDigitales con estado CESTADO=1 (Ocupado no emitido). Al timbrar exitosamente, cambia a CESTADO=2 (Ocupado y emitido) y se guarda el UUID en CUUID.

El complemento de pagos usa campos como CDESCONCBA (NumOperación), CNUMCTABAN (cuenta bancaria), CUSUAUTBAN (TipoCadPago). Para CFDI 4.0, se usa COBJIMPU01 en movimientos para indicar objeto de impuesto, CAUTUSBA03 para tipo de exportación, y campos relacionados para régimen fiscal y uso de CFDI.

La cancelación tiene estados: primero CESTADO=5 (Por Autorizar cancelación), luego puede ser CAUTUSBA01=1 (Rechazado), =2 (Sin Aceptación), =3 (Plazo Vencido), =4 (Con Aceptación), o =5 (En proceso).

### Impuestos y Descuentos
El orden de aplicación se define en CORDENCALCULO del concepto. Los movimientos pueden tener hasta 3 impuestos, 2 retenciones y 5 descuentos. A nivel documento hay 2 descuentos adicionales y 3 gastos sobre compra. Cada uno tiene su porcentaje e importe calculado según fórmulas definidas en el concepto.

Los impuestos pueden ser porcentajes o cuotas fijas (CESCUOTAI2, CESCUOTAI3). En CFDI 4.0, COBJIMPU01 del movimiento indica si causa impuesto y si requiere desglose.

### Monedas y Tipo de Cambio
Cada documento tiene CIDMONEDA y CTIPOCAMBIO. Si la moneda es la base, CTIPOCAMBIO=1. Para monedas extranjeras, CTIPOCAMBIO contiene el tipo de cambio con que se creó. En transformaciones entre monedas, CTIPCAMTR1 y CTIPCAMTR2 del concepto controlan qué tipo de cambio usar.

### Clasificaciones
Agentes, Almacenes, Clientes, Proveedores y Productos soportan 6 niveles de clasificación mediante campos CIDVALORCLASIFICACION1 a 6. Los movimientos también tienen clasificación en CIDVALORCLASIFICACION (clasificación 31).

### Campos Extra y Extensibilidad
Todas las entidades principales tienen campos extra para personalización: textos (CTEXTOEXTRA1-3 o hasta 5), fecha (CFECHAEXTRA), e importes (CIMPORTEEXTRA1-4 o hasta 5). Los conceptos controlan si estos campos son visibles y capturables mediante banderas CUSA*.

### Seguridad
Los conceptos tienen identificadores de procesos de seguridad (CIDPRSEG01 a CIDPRSEG07) que controlan permisos para crear, modificar, eliminar, cancelar, cambiar estado impreso, e imprimir documentos.

### Contabilidad
Los documentos pueden precontabilizarse (CIDPREPOLIZA) o contabilizarse completamente (CESTADOCONTABLE). Los segmentos contables se definen a múltiples niveles: concepto, agente, almacén, cliente/proveedor, producto, y movimiento individual. Esto permite una integración contable flexible y detallada.

---

## Campos de Uso Común

**Identificadores:** Todas las tablas principales tienen un campo CID* como identificador único (Integer autoincremental). Ejemplo: CIDPRODUCTO, CIDCLIENTE PROVEEDOR, CIDDOCUMENTO, CIDMOVIMIENTO.

**Códigos:** Los catálogos tienen campos CCODIGO* (Varchar 30) para códigos alfanuméricos capturados por usuario. Ejemplo: CCODIGOPRODUCTO, CCODIGOAGENTE, CCODIGOALMACEN.

**Nombres:** Los catálogos tienen campos CNOMBRE* (Varchar 60) para nombres descriptivos. Ejemplo: CNOMBREPRODUCTO, CNOMBREAGENTE, CNOMBREALMACEN.

**Fechas de Alta:** Los catálogos tienen CFECHAALTA* (Date) para registrar cuándo se dio de alta. Ejemplo: CFECHAALTAPRODUCTO, CFECHAALTAAGENTE.

**Estatus:** Muchas tablas tienen CESTATUS (Integer) donde 0=Inactivo y 1=Activo.

**Timestamp:** Prácticamente todas las tablas tienen CTIMESTAMP (Varchar 23) para control de concurrencia en actualizaciones.

**Clasificaciones:** Los catálogos principales soportan 6 clasificaciones: CIDVALORCLASIFICACION1 a CIDVALORCLASIFICACION6 (Integer).

**Campos Extra:** Patrón repetido en múltiples tablas: CTEXTOEXTRA1-3 (Varchar 50), CFECHAEXTRA (Date), CIMPORTEEXTRA1-4 (Float).

**Segmentos Contables:** Múltiples segmentos CSEGCONT* o CSC* (Varchar 50 o 20) para integración contable.

**Banderas:** Campos CBAN* (Integer) se usan como banderas booleanas (0=No/False, 1=Sí/True) para indicar configuraciones o estados. Ejemplo: CBANDOMICILIO, CBANIMPUESTO, CAFECTADO, CIMPRESO, CCANCELADO.

---

## Consideraciones

admDocumentos: Esta tabla contiene los campos con los que se crean los diferentes documentos. Existen distinto tipos de documentos como Facturas, cotizaciones, pedidos, remisiones, devoluciones de ventas, notas de crédito, compras, órdenes de Compra, etcétera. Cada uno de los diferentes tipos de documentos vienen dados o identificados por el campo ciddocumentode, dónde su tipo se encuentra en la tabla relacionada admDocumentosModelos. También se pueden tener más de un mismo tipo de documento y estos están relacionados en la tabla admConceptos. Al realizarse un Documento de cualquier tipo, los productos o servicios que incluyen, vienen detallados en la tabla admMovimientos e identificados por el identificados CidDocumento. Los productos y/o servicios están detallados en la tabla admMovimientos. Los productos se encuentran en la tabla admProductos y vienen relacionados por el campo CidProducto. Un documento puede pertenecer a un Agente, el cual se identifica con el campo CidAgente y relacionado a la tabla admAgentes.
El campo CidDocumento identifica un documento Único.
El Campo CidDocumentoDe representa el tipo de documento, como son las ventas, compras, cotizaciones, pedidos, remisiones, etc. La tabla que tiene este tipo de documentos se llama admDocumentosModelos y el campo con el que se relacionan se llama CidDocumentoDe. Esta tabla contiene los documentos modelos y un documento modelo se refiere a compra, venta, cotizaciones, pedidos, remisiones, etc.
El campo CidConceptoDocumento nos da más detalles de todos los tipos de documentos, ya que puedo tener muchos tipos de documentos e incluso muchos del mismo tipo, es decir, puedo tener muchos tipos ventas, pedidos, compras, etc. La tabla que contiene los distintos conceptos con sus detalles es admConceptos
El campo CidClienteProveedor nos indica el identificador del cliente al que pertenece el Documento. Esta tabla contiene los campos de los Clientes y Proveedores y se llama admClientes
El campo CidMoneda nos da la moneda en la que fue hecha el documento y se relaciona con la tabla admMonedas, la cual contiene los detalles de las distintas monedas
El campo CidAgente nos da el agente al que pertenece el documento y se relaciona con la tabla admAgentes, el cual contiene más información detallada de los Agentes
El campo Ccancelado indica el estatus del documento. Un documento con valor 0 indica que está vigente y con valor 1 indica que está cancelado
El campo Cneto es el importe neto del documento
El campo Cimpuesto1 normalmente es el IVA del documento
El campo Ctotal es el total del documento
El Campo CMetodoPag es la forma de pago de los documentos que son timbrados ante el SAT. El 01 es Efectivo, 02 es Cheque, 03 es Transferencia, 04 Tarjeta de Débito, 28 Tarjeta de Crédito
El Campo CcantParci nos indica el método de pago del documento donde 1 es contado o PUE y 2 crédito o PPD

admMovimientos. Tabla de Movimientos. Esta tabla contiene los movimientos realizados en los diferentes documentos y la tabla de documentos es admDocumentos. En los documentos hay dos clases de movimientos: Reales y Ocultos; ambos movimientos se guardan en la misma tabla. En esta tabla se explica en qué consisten.
Movimiento real: Son aquellos capturados por el usuario y que deben ser impresos en las formas preimpresas y aparecer en los reportes de Ventas y de Compras. Se identifican por que el campo cMovtoOculto = 0. cIdMovtoOwner = Vacío, cIdDocumento = Identificador del documento al que pertenece.
Movimiento oculto: Son aquellos generados por el sistema. Un movimiento oculto se genera para el movimiento del almacén destino en un Traspaso, los detalles de las características y los componentes de un Paquete, por ejemplo. Se identifican por que cMovtoOculto = 1, cIdDocumento = Vacío, cIdMovtoOwner = identificador del movimiento real que lo generó
Las diferencias entre los movimientos reales y ocultos sirven para que los reportes y procesos generales de ventas, compras e inventario sólo recuperen los movimientos que necesiten, sean reales u ocultos.
Todo tipo de documento tiene su detalle en esta tabla y es identificado por el CidDocumento de la tabla admDocumentos. Los productos y/p servicios vienen identificados por el campo CidProducto de la tabla admProductos.
El campo CidMovimiento es el identificador único del movimiento
El campo CidDocunento es el identificador del documento de la tabla admDocumentos. Identificador del documento dueño del movimiento. Nota: Cuando el movimiento es oculto este campo debe estar vacío.
El campo CNumeroMovimiento es el consecutivo del movimiento del documento, ya que un documento puede tener más de un registro.
El campo CidDocumentoDe es Tipo de documento del concepto de documento. Referencia de la tabla admDocumentosModelos
El campo CidProducto es el identificador del Producto o servicio y está referenciado en la tabla admProductos
El campo CidAlmacen es el identificador del almacén al que pertenece el movimiento. Nota: Algunas veces este campo está vacío porque algunos movimientos no llevan almacén o porque su documento lo lleva
El campo CidUnidad es el identificador de la unidad de medida y peso del producto o servicio y está referenciado a la tabla admUnidadesMedidaPeso. Identificador de unidad de peso y medida que representa en qué unidad se captura el movimiento. Nota: Puede ser solamente la base o una convertible.
El campo CUnidades es la cantidad del movimiento. Cantidad de unidad base del movimiento. Se diferencia del campo cUnidadesCapturadas porque cUnidades siempre está en la unidad base y cUnidadesCapturadas puede estar en una unidad con equivalencia con la base.
El campo CUnidadesCapturadas es Cantidad de unidades capturadas por el usuario. Se diferencia del campo cUnidades porque cUnidades siempre está en la unidad base y cUnidadesCapturadas puede estar en una unidad con equivalencia con la base
El campo CPrecio es el precio del producto.
El campo CPrecioCapturado es Precio capturado por el usuario. Se diferencia de cPrecio porque cPrecio es el precio de la unidad base y cPrecioCapturado es el precio de la unidad capturada por el usuario.
El campo CCostoCapturado es el Costo unitario del movimiento capturado por el usuario. Se usa para devoluciones sobre ventas
El campo CcostoEspecifico Es el costo calculado del movimiento. Nota: En caso de que tenga un costeo promedio por almacén o último costo, el valor de este campo no necesariamente aparecerá en los reportes de Kárdex, ya que tomará el valor de la tabla Costos históricos.
El campo CNeto es el Importe del neto para el movimiento.
El campo CImpuesto1 normalmente es el IVA para el movimiento
El campo CTotal es el Importe del total del movimiento
El campo CMovtoOculto Indica si un movimiento fue capturado por el usuario (movimiento real) o fue generado por el sistema (movimiento oculto). 0 = Movimiento real, 1 = Movimiento oculto, 2 = Movimiento oculto. Importante: Un movimiento oculto se genera para el movimiento del almacén destino de un traspaso, los movimientos de los detalles de características y los movimientos de los componentes de un paquete.
El campo CidMovtoOwner es el Identificador del documento dueño de un movimiento oculto. Importante: Cuando el movimiento es oculto este campo contiene el Identificador del movimiento que lo originó. Cuando el movimiento es real este campo debe estar vacío. Nota: Un movimiento oculto se genera para el movimiento del almacén destino de un traspaso, los movimientos de los detalles de características y los movimientos de los componentes de un paquete.
El campo CidMovtoOrigen es Cuando el movimiento proviene de una conversión este campo contiene el Identificador del movimiento origen. Ejemplo: Si el movimiento es de una factura que surtió a un pedido, este campo contendrá el identificador del movimiento del pedido.

admClientes: Tabla de Clientes y Proveedores. Esta tabla contiene los campos de los Clientes y Proveedores.
El campo CidClienteProveedor es el Identificador único del cliente o proveedor
El campo CcodigoClienteProveedor es el Código con el que se identifica el cliente o proveedor.
El campo CRazonSocial es el nombre o Razón Social del cliente o proveedor
El campo CRFC es el Registro Federal de Contribuyentes del cliente
El campo CtipoCliente es el Tipo de cliente o proveedor: 1 = Cliente, 2 = Cliente/Proveedor, 3 = Proveedor
El campo ClimiteCreditoCliente es el Límite de crédito del cliente.
El campo CDiasCreditoCliente son los Días de crédito del cliente

admAgentes. Esta tabla contiene los campos del catálogo Agentes
El campo CidAgente contiene el identificador único del Agente
El campo CCodigoAgente contiene el código del Agente
El campo CNombreAgente contiene el nombre del Agente
El campo CTipoAgente contiene el tipo de Agente. 1 Agente de Ventas, Agente de venta y Cobro, 3 Agente de Cobro

admAlmacenes. Esta tabla contiene los campos del catálogo Almacenes.
El Campo CidAlmacen contiene el identificador único del Almacén
El campo CcodigoAlmacen contiene el código del Almacén
El campo CnombreAlmacen contiene el nombre del almacén

admConceptos. Esta tabla contiene los campos de los conceptos. Es en esta tabla donde tenemos todos los conceptos que pueden ser más de un mismo tipo y el tipo lo define el campo CidDocumentoDe que puede ser ventas, compras, cotizaciones, órdenes de compra, pedidos, remisiones, etc.
El campo CidConceptoDocumento contiene el identificador único del Concepto
El campo CcodigoConcepto contiene el código del concepto
El campo CnombreConcepto contiene el nombre del Concepto
El campo CiddocumentoDe contiene el Tipo de documento del concepto de documento. Referencia de la admDocumentosModelos.

admProductos. Esta tabla contiene los campos para los productos, servicios y paquetes.
El campo CidProducto contiene el identificador único de un producto, servicio o paquete
El campo CCodigoProducto contiene el código del producto, servicio o paquete
El campo CNombreProducto contiene el nombre del producto, servicio o paquete
El campo CTipoProducto contiene el tipo del producto, 1 producto, 2 paquete y 3 servicio
El campo CMetodoCosteo contiene el método de costeo del producto, el cual puede ser: 1 Costo Promedio Global, 2 Costo promedio por almacén, 3 Último Costo, 4 UEPS, PEPS, 6 Costo Específico y 7 Costo Estándar.
El campo CidUnidadBase contiene el identificador de la unidad base de la unidad de medida y peso. Este campo se relaciona con el identificador de la tabla admUnidadesMedidaPeso.

admUnidadesMedidaPeso: Esta tabla contiene los campos de las unidades de peso y medida de los servicios, productos y/o paquetes.
El campo CidUnidad contiene el identificador único de una unidad de medida y peso.
El campo CNombreUnidad contiene el nombre de la unidad de medida y peso

admAsocCargosAbonos. Esta tabla contiene las relaciones entre los documentos de abonos y cargos que se saldan entre ellos, ya sea parcial o completamente. Los documentos de tipo abonos disminuyen el saldo de un documento de tipo cargo de un cliente o proveedor. Los documentos de cargos aumentan el saldo del cliente o proveedor del que se trate.

**Búsquedas por Concepto de Negocio:** Los usuarios consultarán sobre "clientes", "facturas", "inventario", "impuestos", no sobre nombres técnicos de campos. El contexto debe asociar términos de negocio con estructuras técnicas.

**Relaciones Implícitas:** Muchas relaciones son por ID. Por ejemplo, un documento tiene CIDCLIENTEPROVEEDOR que apunta a admClientes, CIDCONCEPTODOCUMENTO que apunta a admConceptos, y cada movimiento tiene CIDPRODUCTO que apunta a admProductos.

**Jerarquías de Documentos:** Entender que Concepto → Documento Modelo es fundamental. Un mismo modelo (Factura) puede tener múltiples conceptos con diferentes configuraciones.

**Estados y Flujos:** Los documentos tienen estados (afectado, impreso, cancelado) que determinan qué operaciones son posibles. Los folios digitales tienen estados complejos especialmente en procesos de cancelación.

**Valores Enumerados:** Muchos campos Integer representan enumeraciones. Es crítico conocer los valores válidos y su significado (ejemplo: CTIPOAGENTE 1=Ventas, 2=Venta/Cobro, 3=Cobro).

**Campos Opcionales:** Muchos campos pueden estar vacíos (null) dependiendo del tipo de documento o configuración. Ejemplo: CIDCLIENTEPROVEEDOR puede estar vacío en documentos de almacén.

**Normalización vs Desnormalización:** Algunos campos están desnormalizados para performance (ejemplo: CFECHA en movimientos cuando ya existe en documentos).

**Versionamiento CFDI:** El sistema soporta múltiples versiones de anexo 20 del SAT. Los campos relacionados con facturación electrónica varían según la versión configurada.

**Campos Reservados:** Varios campos están marcados como "Reservado" o "Sin uso", indicando funcionalidad futura o deprecada.

## RELACIONES LOGICAS CLAVE 

### admDocumentos (Tabla Central)
- CIDCLIENTEPROVEEDOR → admClientes.CIDCLIENTEPROVEEDOR
- CIDCONCEPTODOCUMENTO → admConceptos.CIDCONCEPTODOCUMENTO
- CIDAGENTE → admAgentes.CIDAGENTE
- CIDMONEDA → admMonedas.CIDMONEDA
- CIDDOCUMENTOORIGEN → admDocumentos.CIDDOCUMENTO (auto-relación)

### admMovimientos (Detalles de Documentos)
- CIDDOCUMENTO → admDocumentos.CIDDOCUMENTO
- CIDPRODUCTO → admProductos.CIDPRODUCTO
- CIDALMACEN → admAlmacenes.CIDALMACEN
- CIDMOVTOORIGEN → admMovimientos.CIDMOVIMIENTO (auto-relación para conversiones)
- CIDMOVTOOWNER → admMovimientos.CIDMOVIMIENTO (auto-relación para movimientos ocultos)
- CIDUNIDAD → Tabla de Unidades (no documentada en tu archivo)

### admConceptos (Configuración de Documentos)
- CIDDOCUMENTODE → admDocumentosModelo.CIDDOCUMENTODE

### admClientes (Clientes y Proveedores)
- CIDMONEDA → admMonedas.CIDMONEDA
- CIDAGENTEVENTA → admAgentes.CIDAGENTE
- CIDAGENTECOBRO → admAgentes.CIDAGENTE
- CIDALMACEN → admAlmacenes.CIDALMACEN (cuando cliente es almacén)

### admFoliosDigitales (Facturación Electrónica)
- CIDDOCTO → admDocumentos.CIDDOCUMENTO
- CIDCPTODOC → admConceptos.CIDCONCEPTODOCUMENTO
- CIDDOCTODE → admDocumentosModelo.CIDDOCUMENTODE

### admProductos
- CIDUNIDADBASE → Tabla de Unidades
- CIDMONEDA → admMonedas.CIDMONEDA