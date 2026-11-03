"""Console-script wrappers for BunkrDownloader.

The upstream entry points (``downloader.main`` and ``main.main``) are
``async def``, so they cannot be used as console scripts directly -- a
``[project.scripts]`` target must be a plain callable. These thin wrappers
run the coroutines and mirror the ``KeyboardInterrupt`` handling that the
upstream ``if __name__ == "__main__"`` blocks perform.
"""

from __future__ import annotations

import asyncio
import sys

from downloader import main as _download_main
from main import main as _batch_main


def download() -> None:
    """Download a single album or media URL (upstream ``downloader.py``)."""
    try:
        asyncio.run(_download_main())
    except KeyboardInterrupt:
        sys.exit(1)


def batch() -> None:
    """Process every URL in ``URLs.txt`` (upstream ``main.py``)."""
    try:
        asyncio.run(_batch_main())
    except KeyboardInterrupt:
        sys.exit(1)
