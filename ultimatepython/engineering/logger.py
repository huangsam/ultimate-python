"""
Production software requires observability into application state, diagnostic
events, and unexpected errors.

While `print` is convenient for quick scripts, production systems rely on the
standard `logging` module. It provides configurable severity levels, modular
formatting (timestamps, module names, line numbers), and decoupled handlers that
route records to console streams, files, or network sinks without changing business logic.
"""

import io
import logging


def configure_memory_logger(name: str, level: int = logging.INFO) -> tuple[logging.Logger, io.StringIO]:
    """Create an isolated logger directing output to an in-memory string buffer."""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.handlers.clear()

    buffer = io.StringIO()
    handler = logging.StreamHandler(buffer)
    formatter = logging.Formatter("[%(levelname)s] %(name)s: %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Prevent propagating records to root logger to avoid polluting stdout
    logger.propagate = False
    return logger, buffer


def main() -> None:
    # 1. Initialize an isolated logger at DEBUG level
    logger, buffer = configure_memory_logger("app", logging.DEBUG)

    # 2. Emit messages across different severity levels
    logger.debug("Database connection pool initialized")
    logger.info("Server listening on port %d", 8080)
    logger.warning("Cache miss rate exceeded %d%%", 15)

    # 3. Dynamic level filtering: suppress messages below threshold
    logger.setLevel(logging.ERROR)
    logger.info("This informational message is ignored")
    logger.error("Failed to commit transaction to replica")

    # 4. Capture exceptions with full tracebacks using logger.exception
    try:
        _ = 1 / 0
    except ZeroDivisionError:
        logger.exception("Mathematical error encountered")

    # 5. Inspect and verify the buffered log records
    output = buffer.getvalue()

    assert "[DEBUG] app: Database connection pool initialized" in output
    assert "[INFO] app: Server listening on port 8080" in output
    assert "[WARNING] app: Cache miss rate exceeded 15%" in output

    # Verify level filtering dropped the INFO message emitted after level change
    assert "This informational message is ignored" not in output
    assert "[ERROR] app: Failed to commit transaction to replica" in output

    # Verify exception logging captured both message and traceback
    assert "Mathematical error encountered" in output
    assert "ZeroDivisionError: division by zero" in output


if __name__ == "__main__":
    main()
