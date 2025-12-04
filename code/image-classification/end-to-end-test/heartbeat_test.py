import requests

def do_heartbeat_test():
    url = 'http://0.0.0.0:9000/heartbeat'
    response = requests.get(url)

    print(response.json())


if __name__ == '__main__':
    do_heartbeat_test()