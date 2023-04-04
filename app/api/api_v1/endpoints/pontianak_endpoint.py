# module of an endpoint
from ..services.pontianak_service import PontianakService
from ....core.logging import logger


class PontianakEndpoint:
    def __init__(self):
        pass

    def get_author(self, text):
        logger.info(f'API request received.')

        pontianakService = PontianakService()
        result = pontianakService.get_author(text)
        return result