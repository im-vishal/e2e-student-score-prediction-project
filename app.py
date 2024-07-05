from mlproject import logger
from mlproject.components.data_ingestion import DataIngestion
from mlproject.components.data_transformation import DataTransformation





if __name__ == "__main__":
    logger.info("The execution has started")


    try:
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

        data_transformation_config = DataTransformation()
        data_transformation_config.initiate_data_transformation(train_data_path, test_data_path)
    except Exception as e:
        logger.exception(e)
        raise e