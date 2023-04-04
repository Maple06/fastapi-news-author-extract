FROM python:3.8

COPY ./ /
RUN pip install --no-cache-dir -r ./requirements/base.txt
# WORKDIR /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3578", "--workers", "5"]
