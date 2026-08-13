FROM python:3.14-slim

WORKDIR /app

COPY . .

RUN pip install poetry

RUN poetry config virtualenvs.create false

RUN poetry install --no-interaction --no-ansi

EXPOSE 8000

CMD ["uvicorn", "hospital_appointment_application.main:app", "--host", "0.0.0.0", "--port", "8000", "--app-dir", "src"]