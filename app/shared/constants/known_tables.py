KNOWN_TABLES = [
    "admAcumulados",
    "admAcumuladosTipos",
    "admAgentes",
    "admAlmacenes",
    "admAperturas",
    "admAsientosContables",
    "admAsocAcumConceptos",
    "admAsocCargosAbonos",
    "admAsocCargosAbonosImp",
    "admAsocLigasPagos",
    "admBanderas",
    "admBitacoras",
    "admCajas",
    "admCapasProducto",
    "admCaracteristicas",
    "admCaracteristicasValores",
    "admClasificaciones",
    "admClasificacionesValores",
    "admClientes",
    "admComponentesPaquete",
    "admConceptos",
    "admConceptosBack",
    "admConfigProveedoresNube",
    "admConversionesUnidad",
    "admCostosHistoricos",
    "admCuentasBancarias",
    "admDatosAddenda",
    "admDocumentos",
    "admDocumentosModelo",
    "admDocumentosModeloBack",
    "admDomicilios",
    "admEjercicios",
    "admExistenciaCosto",
    "admFoliosDigitales",
    "admFormasPago",
    "admLigasPago",
    "admMaximosMinimos",
    "admMonedas",
    "admMovimientos",
    "admMovimientosCapas",
    "admMovimientosContables",
    "admMovimientosPrepoliza",
    "admMovimientosSerie",
    "admMovtosBancarios",
    "admMovtosCEPs",
    "admMovtosInvFisico",
    "admMovtosInvFisicoSerieCa",
    "admPagoNotas",
    "admParametros",
    "admParametrosBack",
    "admPreciosCompra",
    "admPrepolizas",
    "admProductos",
    "admProductosDetalles",
    "admProductosFotos",
    "admPromociones",
    "admProyectos",
    "admSATSegmentos",
    "admTiposCambio",
    "admUnidadesMedidaPeso",
    "admVistasCampos",
    "admVistasConsultas",
    "admVistasPorModulo",
    "admVistasRecursos",
    "admVistasRelaciones",
    "admVistasTablas",
    "nubeCuentas",
    "nubeDiarios",
]

KNOWN_TABLES_SET = set(KNOWN_TABLES)


def is_valid_table(table_name: str) -> bool:
    return table_name in KNOWN_TABLES_SET


def filter_valid_tables(tables: list[str]) -> list[str]:
    valid_tables: list[str] = []

    for table_name in tables:
        if is_valid_table(table_name=table_name):
            valid_tables.append(table_name)

    return valid_tables
