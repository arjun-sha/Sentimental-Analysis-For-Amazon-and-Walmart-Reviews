from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse

from sentimental_analysis_api.routes.routes import router
from fastapi.staticfiles import StaticFiles


def main():
    # app = FastAPI(docs_url=None, redoc_url=None)
    app = FastAPI()

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request, exc):
        return PlainTextResponse(str(exc), status_code=400)

    app.include_router(router)
    app.mount("/static", StaticFiles(directory="static"), name="static")

    return app