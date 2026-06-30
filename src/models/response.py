from pydantic import BaseModel
from typing import Any

class StandardResponse(BaseModel):
    valid: bool
    message: str
    data: Any | None = None
    