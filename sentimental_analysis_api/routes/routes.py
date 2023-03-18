from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi import File, UploadFile
import csv
import codecs
from sentimental_analysis_api.files_io import FileHandler

from sentimental_analysis_api.routes.schemas.schemas import (
    BatchDataSchema,
    IndividualDataSchema,
)
from sentimental_analysis_api.sentimental_analyser.classifier import Classifier
from sentimental_analysis_api.utils.utils import generate_file_name
from sentimental_analysis_api.utils.token_generation import TokenGenerator


router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/home")
async def get_home_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.post("/api/classifier")
async def classifier(item: IndividualDataSchema) -> JSONResponse:

    item_dict = item.dict()
    input_string = item_dict["input_data"]
    batch = item_dict["batch"]
    algorithm = item_dict["algorithm"]
    sarcasm = item_dict["sarcasm"]
    emoji = item_dict["emoji"]
    lang = item_dict["lang"]

    try:
        score = Classifier.classify(
            input_string=input_string,
            batch=batch,
            algorithm=algorithm,
            sarcasm=sarcasm,
            emoji=emoji,
            lang=lang,
        )
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"result": "Failed to analyse the input"},
        )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"result": score}
    )

@router.post("/files/upload_csv")
async def get_csv(file: UploadFile = File(...)):

    token = TokenGenerator.get_file_token()
    filename = generate_file_name(token, file.filename)

    upload_result = FileHandler.upload_file(filename, file)
    upload_result.update({"token": token})
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=upload_result,
    )

@router.post("/files/upload_json")
async def get_json(file: UploadFile = File(...)):
    return JSONResponse(
        status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
        content={"data_upload_status": "Failed"},
    )

@router.post("/api/batch_classifier")
async def batch_classifier(item: BatchDataSchema) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"result": "Positive"},
    )
