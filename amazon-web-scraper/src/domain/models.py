from collections.abc import Callable
from typing import Any

ProductData = dict[str, Any]
ProgressCallback = Callable[[int, int, int, str], None]
