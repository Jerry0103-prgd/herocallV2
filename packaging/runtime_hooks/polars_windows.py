"""PyInstaller runtime hook: configure Polars before any bundled import."""

import os
import sys


if sys.platform == "win32":
    # Use the compatibility native kernel included by the Windows installer.
    # This must run before PyInstaller imports hidden Polars modules.
    os.environ.setdefault("POLARS_FORCE_PKG", "compat")
    os.environ.setdefault("POLARS_SKIP_CPU_CHECK", "1")
