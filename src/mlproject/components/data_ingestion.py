from dataclasses import dataclass
from pathlib import Path
from mlproject import logger
from mlproject.utils.common import read_sql_data
from sklearn.model_selection import train_test_split
import pandas as pd


home_dir = Path(__file__).parent.parent.parent.parent

@dataclass(frozen=True)
class DataIngestionConfig:
    train_data_path: Path = Path('artifacts') / 'train.csv'
    test_data_path: Path = Path('artifacts') / 'test.csv'
    raw_data_path: Path = Path('artifacts') / 'raw.csv'


class DataIngestion:
    def __init__(self) -> None:
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            df = pd.read_csv(home_dir / 'artifacts/raw.csv')
            logger.info("Reading completed mysql database")

            Path(self.ingestion_config.train_data_path.parent).mkdir(parents=True, exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logger.info("Data ingestion is completed")
            
            return (self.ingestion_config.train_data_path,
                    self.ingestion_config.test_data_path)

        except Exception as e:
            raise e