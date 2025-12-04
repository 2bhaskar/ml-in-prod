import base64

import requests

def do_prediction_test():
    url = 'http://0.0.0.0:9000/predict'
    test_image_path = 'end-to-end-test/test_images/cat_1.jpg'
    image_byte_str = read_image(test_image_path)
    
    payload = {
        'image':image_byte_str.decode('utf-8')
    }

    response = requests.post(url, json=payload)
    print(response.json())

    test_image_path = 'end-to-end-test/test_images/dog_237.jpg'
    with open(test_image_path, 'rb') as fp:
        image_byte = fp.read()
        image_byte_str = base64.b64encode(image_byte)
    
    payload = {
        'image':image_byte_str.decode('utf-8')
    }

    response = requests.post(url, json=payload)
    print(response.json())

def read_image(test_image_path):
    with open(test_image_path, 'rb') as fp:
        image_byte = fp.read()
        image_byte_str = base64.b64encode(image_byte)
    return image_byte_str


if __name__ == '__main__':
    do_prediction_test()