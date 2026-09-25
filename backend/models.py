from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel

# Event types for access control and door events
class EventType(str, Enum):
    ACCESS_GRANTED = "ACCESS_GRANTED"
    ACCESS_DENIED = "ACCESS_DENIED"
    DOOR_FORCED_OPEN = "DOOR_FORCED_OPEN"
    DOOR_HELD_OPEN = "DOOR_HELD_OPEN"
    DOOR_SECURED = "DOOR_SECURED"

# Result of access control attempt
class AccessResult(str, Enum):
    GRANTED = "GRANTED"
    DENIED = "DENIED"
    
# Access event model
class AccessEvent(BaseModel):
    event_id: str
    timestamp: datetime
    event_type: EventType

    badge_id: Optional[str] = None
    person_id: Optional[str] = None

    door_id: str
    door_name: str
    facility_id: str

    access_result: Optional[AccessResult] = None
    reason: Optional[str] = None