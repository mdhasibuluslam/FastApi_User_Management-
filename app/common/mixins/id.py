"""
Primary Key Mixin

Every database table will automatically have
an integer primary key named 'id'.
"""

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class IDMixin:
    """
    Reusable Integer Primary Key.
    """

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        
    )