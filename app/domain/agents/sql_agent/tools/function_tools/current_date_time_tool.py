from datetime import datetime
from zoneinfo import ZoneInfo
from llama_index.core.tools import FunctionTool


def get_current_date_time() -> str:
    ahora = datetime.now(ZoneInfo("America/Mexico_City"))
    fecha_formateada = ahora.strftime("%d-%m-%Y %H:%M")

    return fecha_formateada


def create_current_date_time() -> FunctionTool:
    tool = FunctionTool.from_defaults(
        fn=get_current_date_time,
        name="get_current_date_time",
        description=(
            "Utilidad para obtener la fecha y hora actual exacta en formato DD-MM-YYYY HH:MM"
            "Usala cuando el usuario haga preguntas sobre el tiempo presente, fechas de hoy, "
            "o cuando necesites una referencia temporal para realizar calculos de fechas o consultas SQL"
        ),
    )

    return tool
