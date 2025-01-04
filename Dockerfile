FROM python:3.9-slim
COPY inject_ga4.py /inject_ga4.py
WORKDIR /
ENTRYPOINT ["python3", "/inject_ga4.py"]