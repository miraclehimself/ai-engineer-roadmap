from pydantic import BaseModel
from typing import Any

class StrandardResponse(BaseModel):
    valid: bool
    message: str
    data: Any | None = None