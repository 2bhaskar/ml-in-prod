
class ImageClassificationHandler:

    def __init__(self):

        self.model = None

    def load_model(self, model_path):
        self.model = 