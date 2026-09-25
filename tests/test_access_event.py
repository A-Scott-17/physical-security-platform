from datetime import datetime

import pytest
from pydantic import ValidationError

from backend.models import AccessEvent, AccessResult, EventType

def test_valid_access_granted_event():
    event = AccessEvent(
        event_id = "EVT-0001",
        timestamp = datetime.now(),
        event_type = EventType.ACCESS_GRANTED,
        badge_id = "BADGE-0001",
        person_id = "Alex-0001",
        door_id = "DOOR-0001",
        door_name = "Front Entrance",
        facility_id = "FAC-0001",
        access_result = AccessResult.GRANTED,
        reason = "AUTHORIZED",
    )

    assert event.event_type == EventType.ACCESS_GRANTED
    assert event.access_result == AccessResult.GRANTED
    assert event.badge_id == "BADGE-0001" 

def test_forced_door_does_not_need_badge():
    event = AccessEvent(
        event_id = "EVT-0002",
        timestamp = datetime.now(),
        event_type = EventType.DOOR_FORCED_OPEN,
        door_id = "DOOR-0101",
        door_name = "Server Room",
        facility_id = "FAC-0001",
        reason = "NO_VALID_BADGE_EVENT",
    )

    assert event.badge_id is None
    assert event.person_id is None

def test_invalid_event_type_is_rejected():
    with pytest.raises(ValidationError):
        AccessEvent(
            event_id = "EVT-0003",
            timestamp = datetime.now(),
            event_type = "SOMETHING_RANDOM",
            badge_id = "BADGE-9999",
            person_id = "PERSON-9999",
            door_id = "DOOR-0001",
            door_name = "Front Entrance",
            facility_id = "FAC-0001",
            access_result = AccessResult.DENIED,
        )


