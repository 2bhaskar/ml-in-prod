import os
import uvicorn

if __name__ == "__main__":
    num_worker = int(os.getenv('NUM_WORKER', "1"))
    uvicorn.run('src.rest_wrapper.rest_api_wrapper:app', host='0.0.0.0',
                port=9000, log_level='info', workers=num_worker)
