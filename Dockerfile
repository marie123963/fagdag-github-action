FROM python:3.12.5-alpine3.20

RUN pip install --no-cache pyyaml PyGithub
RUN pip install pyfiglet

WORKDIR /usr/src

COPY src .

ENTRYPOINT [ "python", "/usr/src/main.py" ]
