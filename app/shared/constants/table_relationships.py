TABLE_RELATIONSHIPS: dict[str, dict[str, str]] = {
    "admDocumentos": {
        # Relaciones principales
        "admClientes": "admDocumentos.CIDCLIENTEPROVEEDOR = admClientes.CIDCLIENTEPROVEEDOR",
        "admConceptos": "admDocumentos.CIDCONCEPTODOCUMENTO = admConceptos.CIDCONCEPTODOCUMENTO",
        "admDocumentosModelo": "admDocumentos.CIDDOCUMENTODE = admDocumentosModelo.CIDDOCUMENTODE",
        "admAgentes": "admDocumentos.CIDAGENTE = admAgentes.CIDAGENTE",
        "admMonedas": "admDocumentos.CIDMONEDA = admMonedas.CIDMONEDA",
        # Relaciones de detalle
        "admMovimientos": "admDocumentos.CIDDOCUMENTO = admMovimientos.CIDDOCUMENTO",
        # Auto-relaciones (transformaciones y origen)
        "admDocumentos_origen": "admDocumentos.CIDDOCUMENTOORIGEN = admDocumentos.CIDDOCUMENTO",
        "admDocumentos_copia": "admDocumentos.CIDCOPIADE = admDocumentos.CIDDOCUMENTO",
        # Relaciones contables
        "admAsocCargosAbonos_abono": "admDocumentos.CIDDOCUMENTO = admAsocCargosAbonos.CIDDOCUMENTOABONO",
        "admAsocCargosAbonos_cargo": "admDocumentos.CIDDOCUMENTO = admAsocCargosAbonos.CIDDOCUMENTOCARGO",
        # Relaciones con folios digitales (CFDI)
        "admFoliosDigitales": "admDocumentos.CIDDOCUMENTO = admFoliosDigitales.CIDDOCTO",
    },
    "admMovimientos": {
        # Relacion con documento padre
        "admDocumentos": "admMovimientos.CIDDOCUMENTO = admDocumentos.CIDDOCUMENTO",
        # Relaciones con catalogos
        "admProductos": "admMovimientos.CIDPRODUCTO = admProductos.CIDPRODUCTO",
        "admAlmacenes": "admMovimientos.CIDALMACEN = admAlmacenes.CIDALMACEN",
        # Auto-relaciones (transformaciones y traspasos)
        "admMovimientos_origen": "admMovimientos.CIDMOVTOORIGEN = admMovimientos.CIDMOVIMIENTO",
        "admMovimientos_owner": "admMovimientos.CIDMOVTOOWNER = admMovimientos.CIDMOVIMIENTO",
        "admMovimientos_destino": "admMovimientos.CIDMOVTODESTINO = admMovimientos.CIDMOVIMIENTO",
    },
    "admConceptos": {
        # Relacion con modelo de documento
        "admDocumentosModelo": "admConceptos.CIDDOCUMENTODE = admDocumentosModelo.CIDDOCUMENTODE",
        # Relaciones de transformacion automatica
        "admConceptos_autotrafo": "admConceptos.CIDCONAUTO = admConceptos.CIDCONCEPTODOCUMENTO",
        "admConceptos_destino1": "admConceptos.CIDCPTODE1 = admConceptos.CIDCONCEPTODOCUMENTO",
        "admConceptos_destino2": "admConceptos.CIDCPTODE2 = admConceptos.CIDCONCEPTODOCUMENTO",
        "admConceptos_destino3": "admConceptos.CIDCPTODE3 = admConceptos.CIDCONCEPTODOCUMENTO",
        # Almacen asumido
        "admAlmacenes": "admConceptos.CIDALMASUM = admAlmacenes.CIDALMACEN",
    },
    "admDocumentosModelo": {
        # Relacion con conceptos hijos
        "admConceptos": "admDocumentosModelo.CIDDOCUMENTODE = admConceptos.CIDDOCUMENTODE",
        # Concepto asumido por defecto
        "admConceptos_asumido": "admDocumentosModelo.CIDCONCEPTODOCTOASUMIDO = admConceptos.CIDCONCEPTODOCUMENTO",
    },
    "admClientes": {
        # Relaciones con agentes
        "admAgentes_venta": "admClientes.CIDAGENTEVENTA = admAgentes.CIDAGENTE",
        "admAgentes_cobro": "admClientes.CIDAGENTECOBRO = admAgentes.CIDAGENTE",
        # Relaciones con catalogos
        "admMonedas": "admClientes.CIDMONEDA = admMonedas.CIDMONEDA",
        "admMonedas_secundaria": "admClientes.CIDMONEDA2 = admMonedas.CIDMONEDA",
        # Cliente puede ser almacen
        "admAlmacenes": "admClientes.CIDALMACEN = admAlmacenes.CIDALMACEN",
    },
    "admProductos": {
        # Relaciones con catalogos
        "admMonedas": "admProductos.CIDMONEDA = admMonedas.CIDMONEDA",
        # Relaciones con existencias
        "admExistenciaCosto": "admProductos.CIDPRODUCTO = admExistenciaCosto.CIDPRODUCTO",
    },
    "admAlmacenes": {
        # Relaciones inversas (productos en este almacen)
        "admExistenciaCosto": "admAlmacenes.CIDALMACEN = admExistenciaCosto.CIDALMACEN",
        "admMovimientos": "admAlmacenes.CIDALMACEN = admMovimientos.CIDALMACEN",
    },
    "admAgentes": {
        # Cliente puede ser agente
        "admClientes_agente": "admAgentes.CIDCLIENTE = admClientes.CIDCLIENTEPROVEEDOR",
        # Agente puede ser proveedor
        "admClientes_proveedor": "admAgentes.CIDPROVEEDOR = admClientes.CIDCLIENTEPROVEEDOR",
    },
    "admAsocCargosAbonos": {
        # Relaciones con documentos
        "admDocumentos_abono": "admAsocCargosAbonos.CIDDOCUMENTOABONO = admDocumentos.CIDDOCUMENTO",
        "admDocumentos_cargo": "admAsocCargosAbonos.CIDDOCUMENTOCARGO = admDocumentos.CIDDOCUMENTO",
        # Documentos generados por la asociacion
        "admDocumentos_dpp": "admAsocCargosAbonos.CIDDESCUENTOPRONTOPAGO = admDocumentos.CIDDOCUMENTO",
        "admDocumentos_utilperd": "admAsocCargosAbonos.CIDUTILIDADPERDIDACAMB = admDocumentos.CIDDOCUMENTO",
        "admDocumentos_ajusteiva": "admAsocCargosAbonos.CIDAJUSIVA = admDocumentos.CIDDOCUMENTO",
    },
    "admExistenciaCosto": {
        # Relaciones con catalogos
        "admAlmacenes": "admExistenciaCosto.CIDALMACEN = admAlmacenes.CIDALMACEN",
        "admProductos": "admExistenciaCosto.CIDPRODUCTO = admProductos.CIDPRODUCTO",
        "admEjercicios": "admExistenciaCosto.CIDEJERCICIO = admEjercicios.CIDEJERCICIO",
    },
    "admFoliosDigitales": {
        # Relaciones con documentos
        "admDocumentos": "admFoliosDigitales.CIDDOCTO = admDocumentos.CIDDOCUMENTO",
        "admDocumentosModelo": "admFoliosDigitales.CIDDOCTODE = admDocumentosModelo.CIDDOCUMENTODE",
        "admConceptos": "admFoliosDigitales.CIDCPTODOC = admConceptos.CIDCONCEPTODOCUMENTO",
        "admConceptos_original": "admFoliosDigitales.CIDCPTOORI = admConceptos.CIDCONCEPTODOCUMENTO",
    },
    "admDomicilios": {
        "admClientes": "admDomicilios.CIDCATALOGO = admClientes.CIDCLIENTEPROVEEDOR AND admDomicilios.CTIPOCATALOGO = 1",
        "admDocumentos_envio": "admDomicilios.CIDCATALOGO = admDocumentos.CIDDOCUMENTO AND admDomicilios.CTIPOCATALOGO = 3",
        "admEmpresas": "admDomicilios.CIDCATALOGO = admParametros.CIDEMPRESA AND admDomicilios.CTIPOCATALOGO = 4",
    },
}
