from pydantic.main import BaseModel


class ResponsePrediction(BaseModel):
    pred_str: str
    error_code: str | None
