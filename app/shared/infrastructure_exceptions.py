from app.shared.errors import BaseAppException


class InfrastructureException(BaseAppException):
    def __init__(self, message, **kwargs):
        kwargs.setdefault("error_code", "INFRASTRUCTURE_EXCEPTION")
        super().__init__(message, **kwargs)


class DatabaseException(InfrastructureException):
    def __init__(self, message: str, query: str = None, **kwargs):
        details = kwargs.get("details", {})
        if query:
            details["query"] = query
        kwargs["details"] = details
        kwargs.setdefault("error_code", "DATABASE_ERROR")
        super().__init__(message, **kwargs)


class VectorStoreException(InfrastructureException):
    def __init__(self, message: str, collection: str = None, **kwargs):
        details = kwargs.get("details", {})
        if collection:
            details["collection"] = collection
        kwargs["details"] = details
        kwargs.setdefault("error_code", "VECTOR_STORE_ERROR")
        super().__init__(message, **kwargs)


class LLMException(InfrastructureException):
    def __init__(self, message, model: str = None, **kwargs):
        details = kwargs.get("details", {})
        if model:
            details["model"] = model

        kwargs["details"] = details
        kwargs.setdefault("error_code", "LLM_ERROR")
        super().__init__(message, **kwargs)
