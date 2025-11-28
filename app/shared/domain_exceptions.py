from app.shared.errors import BaseAppException


class DomainException(BaseAppException):
    def __init__(self, message, **kwargs):
        kwargs.setdefault("error_code", "DOMAIN_EXCEPTION")
        super().__init__(message, **kwargs)


class AgentException(BaseAppException):
    def __init__(self, message, agent_name: str = None, **kwargs):
        details = kwargs.get("details", {})
        if agent_name:
            details["agent_name"] = agent_name

        kwargs["details"] = details
        kwargs.setdefault("error_code", "AGENT_ERROR")
        super().__init__(message, **kwargs)


class WorkflowException(BaseAppException):
    def __init__(self, message, workflow_id: str = None, **kwargs):
        details = kwargs.get("details", {})
        if workflow_id:
            details["workflow_id"] = workflow_id

        kwargs["details"] = details
        kwargs.setdefault("error_code", "WORKFLOW_ERROR")
        super().__init__(message, **kwargs)
