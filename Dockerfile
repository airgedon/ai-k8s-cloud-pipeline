FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

# --no-cache-dir 옵션을 빼거나 캐시 마운트를 활용합니다
RUN pip install -r requirements.txt

COPY ./app ./app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
