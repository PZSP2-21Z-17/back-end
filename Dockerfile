FROM python:3.9-alpine
WORKDIR /app
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . ./
EXPOSE 8000
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "main:app"]
