FROM mageai/mageai:latest

ARG USER_CODE_PATH=/home/src/magic

COPY requirements.txt ${USER_CODE_PATH}/requirements.txt 

RUN pip3 install -r ${USER_CODE_PATH}/requirements.txt
