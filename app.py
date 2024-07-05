from mlproject import logger
from mlproject.components.data_ingestion import DataIngestion
import sys





if __name__ == "__main__":
    logger.info("The execution has started")


    try:
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logger.exception(e)
        raise e