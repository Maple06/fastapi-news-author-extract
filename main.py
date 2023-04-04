import uvicorn
from fastapi import FastAPI
from app.api.router import router

API_VERSION = 1.0
app = FastAPI()
app.include_router(router)

# Default root path
@app.get('/')
async def root():

    message = {
        'message': f'This is News Author Extraction API v{API_VERSION}'
    }

    return message

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3578)