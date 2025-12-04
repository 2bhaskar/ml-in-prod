from pydantic import BaseModel


class RequestPredictionPayload(BaseModel):
    image: str
