""" UUID mixin"""

import uuid
from sqlalchemy.orm import Mapped, mapped_column



class UUIDMixin:
    uuid:Mapped[uuid.UUID] = mapped_column(default=uuid.uuid4,unique=True,nullable=False)



