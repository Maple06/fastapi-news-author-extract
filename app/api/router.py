# api core module for all endpoints
from fastapi import APIRouter
from .api_v1.endpoints.pontianak_endpoint import PontianakEndpoint
# from .api_v1.schemas.pontianak_schema import PontianakSchema
from fastapi import Form

router = APIRouter(
    prefix='/api/v1',
    responses = {
        404: {'description': 'Not Found'}
    }
)

@router.post('/pontianak')
async def pontianak(text: str = Form(...)):
    pontianakEndpoint = PontianakEndpoint()

    result = pontianakEndpoint.get_author(text)
    return result