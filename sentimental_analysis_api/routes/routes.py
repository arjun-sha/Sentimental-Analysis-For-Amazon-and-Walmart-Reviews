from fastapi import APIRouter, status, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/home")
async def get_home_page(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )
