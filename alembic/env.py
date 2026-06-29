import sys
from pathlib import Path
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

# ==============================================================================
# Add project root to Python path
# ==============================================================================

ROOT_DIR = Path(__file__).resolve().parents[1]

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

# ==============================================================================
# Import Application
# ==============================================================================

from app.core.config import settings
from app.database.base import Base

# Import all models so that Alembic can detect them
from app.database import models  # noqa: F401

# ==============================================================================
# Alembic Config
# ==============================================================================

config = context.config

# ==============================================================================
# Logging
# ==============================================================================

if config.config_file_name is not None:
    try:
        fileConfig(config.config_file_name)
    except KeyError:
        # Ignore logging configuration errors
        pass

# ==============================================================================
# Database URL
# ==============================================================================

config.set_main_option(
    "sqlalchemy.url",
    settings.DATABASE_URL,
)

# ==============================================================================
# Metadata
# ==============================================================================

target_metadata = Base.metadata


# ==============================================================================
# Offline Migration
# ==============================================================================

def run_migrations_offline() -> None:
    """
    Run migrations without creating a database connection.
    """

    url = config.get_main_option("sqlalchemy.url")

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={
            "paramstyle": "named",
        },
        compare_type=True,
        compare_server_default=True,
        include_schemas=True,
    )

    with context.begin_transaction():
        context.run_migrations()


# ==============================================================================
# Online Migration
# ==============================================================================

def run_migrations_online() -> None:
    """
    Run migrations using a live database connection.
    """

    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
        future=True,
    )

    with connectable.connect() as connection:

        context.configure(
            connection=connection,
            target_metadata=target_metadata,

            # Detect column type changes
            compare_type=True,

            # Detect server default changes
            compare_server_default=True,

            # Support PostgreSQL schemas
            include_schemas=True,

            # Batch mode for SQLite compatibility
            render_as_batch=False,
        )

        with context.begin_transaction():
            context.run_migrations()


# ==============================================================================
# Entry Point
# ==============================================================================

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()