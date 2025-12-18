from typing import Optional, Dict, Any


from typing import Optional, Dict, Any
from copy import deepcopy


class BaseAppException(Exception):
    def __init__(
        self,
        message: str,
        *,
        error_code: str,
        details: Optional[Dict[str, Any]] = None,
    ) -> None:
        super().__init__(message)

        self.error_code: str = error_code

        self.details: Dict[str, Any] = deepcopy(details) if details else {}

    def __str__(self) -> str:
        return f"[{self.error_code}] {self.args[0]}"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "error": self.args[0],
            "error_code": self.error_code,
            "details": deepcopy(self.details),
            "type": self.__class__.__name__,
        }


class ValidationError(BaseAppException):
    def __init__(self, message, field: Optional[str] = None, **kwargs):
        details = kwargs.get("details", {})
        if field:
            details["field"] = field

        kwargs["details"] = details
        kwargs.setdefault("error_code", "VALIDATION_ERROR")
        super().__init__(message, **kwargs)


class NotFoundError(BaseAppException):
    def __init__(self, message, recurso_id: Optional[str] = None, **kwargs):
        message = f"{recurso_id} not found"
        if recurso_id:
            message += f":{recurso_id}"

        kwargs.setdefault("error_code", "NOT_FOUND")
        super().__init__(message, **kwargs)


class ConfigurationError(BaseAppException):
    def __init__(self, message: str, **kwargs):
        kwargs.setdefault("error_code", "CONFIGURATION_ERROR")
        super().__init__(message, **kwargs)
