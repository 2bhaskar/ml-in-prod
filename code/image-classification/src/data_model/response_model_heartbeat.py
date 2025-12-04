from pydantic.main import BaseModel

class ResponseHeartBeat(BaseModel):
    is_alive: bool
