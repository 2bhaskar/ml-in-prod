import base64
from fastapi.testclient import TestClient
from src.rest_wrapper.rest_api_wrapper import app

client = TestClient(app)


def test_root_api():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Image-Classification-App"}


def test_heartbest():
    response = client.get("/heartbeat")
    assert response.status_code == 200
    assert response.json() == {"is_alive": True}


def test_prediction_cat():
    cat_image_path = "test/resources/image/cat_1.jpg"
    with open(cat_image_path, "rb") as fp:
        image_byte = fp.read()
        image_base64 = base64.b64encode(image_byte)

    request_payload = {"image": image_base64.decode("utf-8")}

    response = client.post("/predict", json=request_payload)

    assert response.status_code == 200
    assert response.json() == {"pred_str": "cat", "error_code": None}


def test_prediction_dog():
    cat_image_path = "test/resources/image/dog_237.jpg"
    with open(cat_image_path, "rb") as fp:
        image_byte = fp.read()
        image_base64 = base64.b64encode(image_byte)

    request_payload = {"image": image_base64.decode("utf-8")}

    response = client.post("/predict", json=request_payload)

    assert response.status_code == 200
    assert response.json() == {"pred_str": "dog", "error_code": None}
