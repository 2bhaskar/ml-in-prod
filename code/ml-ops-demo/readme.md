## Introduction

This module is showing a demo of the `MLOps` framework in local machine with an approximated scope.

## Dependency

You must have the following s/w tools:
- Docker
- Docker compose (here we have use the lates docker package which uses the command `docker compose` instead of `docker-compose`)
- Python >= 3.11
- OS that can run `.sh` scripts

## Running the scripts

### Build ml-flow docker container
'''bash

cd tools_setup
cd ml-flow
chmod +x ci.sh
./ci.sh

'''
### Up and run `ml-flow` with `minio` and `mysql`

You should be in `ml-ops-demo` folder
'''bash
chmod +x ml-flow-cd.sh
./ml-flow-cd.sh

'''

### Check your `ml-flow`

'''bash
sudo docker ps
'''
And you should see

'''bash

ml_flow_server:latest
mysql
minio/minio 

'''

From your web-browser you can check the `ml-flow` from `http://localhost:5000`

### Run python experiment and check it in `ml-flow`
You should be in `ml-ops-demo` folder
'''bash
<active your python virtual env>
<install all the requirements from requirements.txt>
export set PYTHONPATH=.
python src/train.py 
'''
You will your experiment detail in the local `ml-flow` at `http://localhost:5000`

You can edit the file `local.env` to change all the values and even rename this file, if rename happens you must change also `ml-flow-cd.sh`