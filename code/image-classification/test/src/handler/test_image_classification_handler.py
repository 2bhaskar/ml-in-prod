import base64
import unittest
import os

from src.handler.image_classification_handler import ImageClassificationHandler


class TestImageClassificationHandler(unittest.TestCase):

    def setUp(self):
        self.image_classification_handler = ImageClassificationHandler()
        config_path = os.getenv("APP_CONFIG_PATH", "test/config/app_config.yaml")
        self.image_classification_handler.load_from_config(config_dict_path=config_path)
        self.test_cat_image_path = "test/resources/image/cat_1.jpg"
        self.test_dog_image_path = "test/resources/image/dog_237.jpg"

    def test_load_model(self):
        self.image_classification_handler.load_model()
        assert self.image_classification_handler.model is not None

    def test_get_prediction_cat_image(self):

        prediction_value, error_code = self.image_classification_handler.get_prediction(
            image_path=self.test_cat_image_path
        )

        assert prediction_value is not None and prediction_value < 0.5
        assert error_code is None

    def test_get_prediction_dog_image(self):

        prediction_value, error_code = self.image_classification_handler.get_prediction(
            image_path=self.test_dog_image_path
        )

        assert prediction_value is not None and prediction_value >= 0.5
        assert error_code is None
