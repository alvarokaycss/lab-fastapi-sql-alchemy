from fastapi import FastAPI

from app.core.settings import settings
from app.api.v1.api import api_router

app = FastAPI(title="Curso API", version="1.0.0", description="API para gerenciamento de cursos")
app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.HOST, port=settings.PORT, reload=settings.RELOAD, log_level=settings.LOG_LEVEL)
    