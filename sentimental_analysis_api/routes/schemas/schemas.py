from pydantic import BaseModel


class IndividualDataSchema(BaseModel):
    input_data: str
    algorithm: str
    sarcasm: bool
    emoji: bool
    lang: str


class BatchDataSchema(BaseModel):
    file_name: str
    file_type: str
    review_field: str
    algorithm: str
    sarcasm: bool
    emoji: bool
    lang: str
