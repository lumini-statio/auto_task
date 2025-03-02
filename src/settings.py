from enum import Enum
from pathlib import Path
import os


class Paths(Enum):
    BASE = Path(__file__).resolve().parent.parent
    DATA = os.path.join(BASE, 'data')