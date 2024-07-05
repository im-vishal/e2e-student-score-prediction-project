from dataclasses import dataclass
from pathlib import Path
from mlproject import logger
import pandas as pd
import sys


@dataclass(frozen=True)
class DataIngestionConfig:
    train_data_path: str = os.path