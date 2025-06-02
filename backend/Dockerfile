FROM python:3.11-slim

WORKDIR /code

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# collect static if needed (for admin or React fallback)
RUN mkdir -p /code/static && python manage.py collectstatic --noinput

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]