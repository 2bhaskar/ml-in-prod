import logging
from pathlib import Path

import yaml
import tensorflow as tf


class ImageClassificationHandler:

    def __init__(self):

        self.model = None
        self.model_path = None
        self.model_input_shape = [224, 224]

    def load_from_config(self, config_dict_path: str):

        try:
            config_dict = yaml.safe_load(Path(config_dict_path).read_text())
        except Exception as e:
            logging.info(f"ERROR_CONFIG_FILE: {config_dict_path}, error={e}")
            raise RuntimeError("ERROR_CONFIG_FILE")

        if "model_path" not in config_dict:
            logging.info("ERROR_MODEL_PATH_NOT_IN_CONFIG")
            raise RuntimeError("ERROR_MODEL_PATH_NOT_IN_CONFIG")
        self.model_path = config_dict["model_path"]

    def load_model(self):
        try:
            self.model = tf.keras.models.load_model(self.model_path)
            logging.info(f"MODEL_LOAD_DONE: {self.model_path}")
        except Exception as e:
            logging.info(f"ERROR_MODEL_LOAD: error={e}")
            raise RuntimeError("ERROR_MODEL_LOAD")

    def get_prediction(self, image_path: str):

        if self.model is None:
            self.load_model()

        error_code = None
        pred = None
        img = None
        try:
            img = tf.keras.utils.load_img(image_path, target_size=(224, 224))
            img = tf.keras.utils.img_to_array(img) / 255.0
        except Exception as e:
            logging.info(f"ERROR_IMAGE_DECODING: error={e}")
            error_code = "ERROR_IMAGE_DECODING"

        if img is not None:
            try:
                pred = self.model.predict(tf.expand_dims(img, 0))[0][0]
            except Exception as e:
                logging.info(f"ERROR_TF_MODEL_PRED: error={e}")
                error_code = "ERROR_TF_MODEL_PRED"

        return (pred, error_code)
