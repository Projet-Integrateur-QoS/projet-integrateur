FROM python

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE ${SIMULATOR_PORT}
EXPOSE ${SCORER_PORT}

COPY . .
