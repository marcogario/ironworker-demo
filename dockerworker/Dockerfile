FROM iron/python:2-dev

# This image will be executed as:
# docker run --rm -e "PAYLOAD_FILE=hello.payload.json" \
#    -v "$PWD":/worker \
#    -w /worker <ARGS> \
#     <IMAGE> \
#     <CMD>


RUN pip install iron-mq>=0.5
RUN pip install iron-worker>=1.3.1

ADD make_hash.py .

CMD python make_hash.py