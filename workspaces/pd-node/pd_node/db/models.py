from sqlmodel import Field, SQLModel 
from datetime import datetime, timezone

def utc_now():
    return datetime.now(timezone.utc)

class ObjectDetection(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    model: str
    detection_start: datetime = Field(default_factory=utc_now)
    detection_end: datetime = Field(default_factory=utc_now)

