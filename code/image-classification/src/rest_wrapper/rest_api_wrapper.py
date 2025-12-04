import base64
import os
import logging
import tempfile
import shutil

from fastapi import FastAPI, Request

from src.data_model.request_prediction_payload import RequestPredictionPayload
from src.data_model.response_model_heartbeat import ResponseHeartBeat
from src.data_model.response_model_prediction import ResponsePrediction
from src.handler.image_classification_handler import ImageClassificationHandler
from src.log_management import configure_logger


APP_CONFIG_PATH = os.getenv("APP_CONFIG_PATH", "config/app_config.yaml")
LOG_CONFIG_PATH = os.getenv("LOG_CONFIG_PATH", "config/log_config.ini")

configure_logger.setup_logger(log_config_file_path=LOG_CONFIG_PATH)

app = FastAPI()

image_classification_handler = ImageClassificationHandler()
image_classification_handler.load_from_config(APP_CONFIG_PATH)


@app.get("/")
async def root():
    return {"message": "Image-Classification-App"}


@app.get("/heartbeat", response_model=ResponseHeartBeat, name="heartbeat")
async def get_heartbeat() -> ResponseHeartBeat:
    logging.info("Inside heartbeat")
    heartbeat = ResponseHeartBeat(is_alive=True)
    return heartbeat


@app.post("/predict", response_model=ResponsePrediction, name="predict")
async def get_prediction(
    request: Request, request_payload: RequestPredictionPayload
) -> ResponsePrediction:

    logging.info("Inside prediction")
    response_prediction = ResponsePrediction(pred_str="unknown", error_code=None)

    # Saving image to the local folder
    image_base64 = request_payload.image

    try:

        dirpath = tempfile.mkdtemp()

        request_file_name = f"{dirpath}/request_image.jpg"

        with open(request_file_name, "wb") as fp:
            fp.write(base64.b64decode(image_base64))

        prediction_value, error_code = image_classification_handler.get_prediction(
            image_path=request_file_name
        )
        if prediction_value is not None:
            if prediction_value >= 0.5:
                response_prediction.pred_str = "dog"
            else:
                response_prediction.pred_str = "cat"
        if error_code is not None:
            response_prediction.error_code = error_code

        logging.info(
            f"DONE_GET_PREDICTION: prediction_value={prediction_value}, error_code={error_code}"
        )

        shutil.rmtree(dirpath)
    except Exception as e:
        logging.info(f"ERROR_GET_PREDICTION: error={e}")
        response_prediction.error_code = str(e)

    return response_prediction
