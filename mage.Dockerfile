FROM mageai/mageai:latest

ARG PROJECT_NAME=magic
ARG MAGE_CODE_PATH=/home/src

ARG USER_CODE_PATH=${MAGE_CODE_PATH}/${PROJECT_NAME}

COPY ${PROJECT_NAME}/requirements.txt ${USER_CODE_PATH}/requirements.txt 

RUN pip3 install -r ${USER_CODE_PATH}/requirements.txt
