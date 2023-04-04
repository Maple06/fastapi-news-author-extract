# for load machine learning models
import os
from ..core.logging import logger

CWD = os.getcwd()

class Models:
    def __init__(self):
        pass

    def load_dataset(self, text):
        try:
            pass
        except Exception as e:
            logger.error('Error when finding author:', e, 'Text:', text)
            quit()
           
models = Models()