FROM python:3.6-slim

RUN python3 -m pip install --upgrade pip \
  && python3 -m pip install jupyter \
  && python3 -m pip install numpy matplotlib pandas

RUN mkdir /opt/notebooks

WORKDIR /usr/src/app

CMD sleep infinity
