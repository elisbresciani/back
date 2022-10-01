FROM python:3.10
COPY ./requirements.txt /api/requirements.txt
WORKDIR /api
RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt
COPY . /api
ENTRYPOINT [ "python" ]

CMD ["app.py" ]