from pydantic import BaseModel


class IndividualDataSchema(BaseModel):
    id: int
    input_data: str
    batch: bool
    algorithm: str
    sarcasm: bool
    emoji: bool
    lang: str


class BatchDataSchema(BaseModel):
    id: int
    file_name: str
