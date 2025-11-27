from typing import Optional, Dict, Any


class BaseAppException(Exception):
    def __init__(
        self,
        message: str,
        details: Optional[Dict[str, Any]] = None,
        error_code: Optional[str] = None,
    ):
        self.message = message
        self.details = details or {}
        self.error_code = error_code
        super().__init__(self.message)

    def __str__(self):
        if self.message:
            return f"[{self.error_code}] {self.message}"
        return self.message

    def to_dict(self) -> Dict[Any]:
        return {
            "error": self.message,
            "error_code": self.error_code,
            "details": self.details,
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
