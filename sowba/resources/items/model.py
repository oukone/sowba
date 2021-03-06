from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field
from sowba.security.acl import BaseResourceAcl


class ItemType(str, Enum):
    foo = "foo"
    bar = "bar"


class BaseItem(BaseResourceAcl):
    created_on: datetime = Field(default_factory=datetime.utcnow)
