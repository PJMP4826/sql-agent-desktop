ERROR_PATTERS = {
    # Autenticación / Credenciales
    "18456": "Error de inicio de sesión. Credenciales inválidas, cuenta deshabilitada o modo de autenticación incorrecto. Verifica usuario/contraseña y configuración de autenticación MIXTA o Windows.",
    "28000": "SQLSTATE 28000 indica fallo de autenticación. Usuario/contraseña inválidos o no autorizado.",
    # Base de datos concreta
    "4060": "No se puede abrir la base de datos solicitada. Puede que no exista, esté offline o el usuario no tenga acceso.",
    # Conectividad / red
    "Error related to network or instance specific": "Error genérico de conectividad SQL Server. Suele indicar que no se encontró la instancia, no está escuchando o no acepta conexiones remotas.",
    "provider: Named Pipes Provider, error: 40": "No se pudo abrir una conexión a SQL Server. Nombre de instancia incorrecto o no se permiten conexiones remotas.",
    "Microsoft SQL Server, Error: 53": "La ruta de red no se encontró o el servidor no accesible. Puerto/TCP no abierto o servicio SQL Server apagado.",
    "Microsoft SQL Server, Error: 11001": "TCP Provider: Host no existe o no puede resolverse (DNS/hostname incorrecto).",
    "Microsoft SQL Server, Error: 26": "Error al localizar servidor/instancia especificados.",
    "Microsoft SQL Server, Error: 10060": "Tiempo de espera de conexión agotado. No responde el servidor en tiempo límite.",
    # Rechazo / firewall
    "Connection refused": "No se estableció conexión porque la máquina destino la rechazó activamente. Firewall o no hay listener TCP.",
    "TCP Provider: No connection could be made because the target machine actively refused it": "Rechazo de conexión a nivel TCP. SQL Server no está escuchando en esa IP/puerto.",
    # Timeout de conexión
    "Login timeout expired": "Tiempo de espera para inicio de sesión agotado porque el servidor no respondió o está inaccesible.",
    # ODBC / Driver
    "ODBC Driver 17": "Error de driver ODBC SQL Server. Instala/actualiza ODBC Driver 17+.",
    "SQLSTATE[08001]": "El cliente no puede establecer conexión con la fuente de datos. Indica falla de red o configuración (servidor inaccesible, protocolo/despliegue incorrecto, firewall, DNS, servicios no habilitados).",
    "08001": "El cliente no puede establecer conexión con la fuente de datos. Indica falla de red o configuración (servidor inaccesible, protocolo/despliegue incorrecto, firewall, DNS, servicios no habilitados).",
    "SQLSTATE[01000]": "Advertencia general de ODBC; puede acompañar errores de conexión como 53 o 10060.",
    "01000": "Advertencia general de ODBC; puede acompañar errores de conexión como 53 o 10060.",
    # OLE DB / proveedores
    "An OLE DB record is available": "Error OLE DB genérico en la conexión. Suele preceder a detalles de red/instancia o credenciales.",
    "Proveedor TCP: Se cerró a la fuerza una conexión existente": "TCP Provider indica que el host remoto cortó la conexión. Problema de red o idle timeout.",
    # Otros errores potenciales de SQL Server
    "Provider SSL error": "Error de seguridad/SSL al conectar (ej., certificado no confiable o configuración TLS).",
    "233": "Se estableció la conexión, pero no hay proceso en el otro extremo de la canalización (protocolos no habilitados/local).",
}

def format_db_error(error_code: str) -> str:
    for i, friendy_message in ERROR_PATTERS.items():
        if i in error_code:
            return friendy_message
    
    return "Error de conexión inesperado. Contacte a soporte técnico."