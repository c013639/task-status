FROM python:3.11-alpine
# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED 1

COPY src /src/

WORKDIR /src

RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "custom_prom.py"]