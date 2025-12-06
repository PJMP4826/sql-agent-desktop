from typing import Optional, Dict, Any
from app.shared.errors import BaseAppException


class DomainException(BaseAppException):
    def __init__(
        self,
        message: str,
        *,
        error_code: str = "DOMAIN_EXCEPTION",
        details: Optional[Dict[str, Any]] = None,
        **kwargs: Any
    ) -> None:
        super().__init__(
            message,
            error_code=error_code,
            details=details or {},
            **kwargs
        )


class AgentException(DomainException):
    def __init__(
        self,
        message: str,
        *,
        agent_name: Optional[str] = None,
        error_code: str = "AGENT_ERROR",
        details: Optional[Dict[str, Any]] = None,
        **kwargs: Any
    ) -> None:
        final_details: Dict[str, Any] = details.copy() if details else {}
        if agent_name:
            final_details["agent_name"] = agent_name

        super().__init__(
            message,
            error_code=error_code,
            details=final_details,
            **kwargs
        )


class WorkflowException(DomainException):
    def __init__(
        self,
        message: str,
        *,
        workflow_id: Optional[str] = None,
        error_code: str = "WORKFLOW_ERROR",
        details: Optional[Dict[str, Any]] = None,
        **kwargs: Any
    ) -> None:
        final_details: Dict[str, Any] = details.copy() if details else {}
        if workflow_id:
            final_details["workflow_id"] = workflow_id

        super().__init__(
            message,
            error_code=error_code,
            details=final_details,
            **kwargs
        )
