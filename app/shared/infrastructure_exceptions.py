from typing import Optional, Dict, Any
from app.shared.errors import BaseAppException


class InfrastructureException(BaseAppException):
    def __init__(
        self,
        message: str,
        *,
        error_code: str = "INFRASTRUCTURE_EXCEPTION",
        details: Optional[Dict[str, Any]] = None,
        **kwargs: Any
    ) -> None:
        final_details = {**(details or {})}

        super().__init__(
            message,
            error_code=error_code,
            details=final_details,
            **kwargs
        )


class VectorStoreException(InfrastructureException):
    def __init__(
        self,
        message: str,
        *,
        collection: Optional[str] = None,
        error_code: str = "VECTOR_STORE_ERROR",
        details: Optional[Dict[str, Any]] = None,
        **kwargs: Any
    ) -> None:
        final_details = {**(details or {})}
        if collection:
            final_details["collection"] = collection

        super().__init__(
            message,
            error_code=error_code,
            details=final_details,
            **kwargs
        )


class LLMException(InfrastructureException):
    def __init__(
        self,
        message: str,
        *,
        model: Optional[str] = None,
        error_code: str = "LLM_ERROR",
        details: Optional[Dict[str, Any]] = None,
        **kwargs: Any
    ) -> None:
        final_details = {**(details or {})}
        if model:
            final_details["model"] = model

        super().__init__(
            message,
            error_code=error_code,
            details=final_details,
            **kwargs
        )