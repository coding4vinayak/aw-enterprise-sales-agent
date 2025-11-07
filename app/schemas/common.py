from pydantic import BaseModel
from typing import Generic, TypeVar, Optional

T = TypeVar('T')

class APIResponse(BaseModel):
    success: bool
    message: Optional[str] = None
    data: Optional[T] = None

    class Config:
        arbitrary_types_allowed = True