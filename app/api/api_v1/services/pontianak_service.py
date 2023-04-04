# module specific business logic (will be use for endpoints)
import re

# from ...load_models import models
from ....core.logging import logger


class PontianakService:
    def __init__(self) -> None:
        pass

    def get_author(self, text):
        try:
            authors = re.findall(r'\. ?\((.*?)\)', text)
            authors = [i.strip() for i in authors]
            if authors.count(authors[0]) == len(authors):
                authors = authors[0]

            result = {
                    'result': {
                        # 'text': text,
                        'author': authors
                    }, 
                    'status': 1
                }

            logger.info(f"API return success. Result: {result}")
            return result
        except Exception as e:
            logger.info(f'Error while request: {e}. Text: {text}')
            return {'result': {
                        # 'text': text, 
                        'author': None
                        }, 
                    'status': 0, 
                    'error-message': f'Error while request: {e}.'
                    }