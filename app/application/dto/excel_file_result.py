from typing import Any
from dataclasses import dataclass


@dataclass
class ExcelFileResult:
    type: str
    filename: str
    content: str  # base64
    mime_type: str
    size_bytes: int
    sheets_count: int = 1
    message: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "type": "excel_file",
            "filename": self.filename,
            "content": self.content,
            "mime_type": self.mime_type,
            "size_bytes": self.size_bytes,
            "message": self.message,
            "metadata": {"sheets_count": self.sheets_count},
        }

    def to_websocket_message(self) -> dict[str, Any]:
        """convierte a formato de mensaje WebSocket (para JSON)"""
        return {
            "type": "excel_file",
            "filename": self.filename,
            "content": self.content,
            "mime_type": self.mime_type,
            "size_bytes": self.size_bytes,
            "message": self.message,
            "metadata": {"sheets_count": self.sheets_count},
        }
