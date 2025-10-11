from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional, Dict, Any

@dataclass
class Document:
    title: str = ""
    id: Optional[str] = None
    file_path: Optional[str] = None
    file_type: Optional[str] = None
    size_bytes: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    tags: List[str] = field(default_factory=list)
