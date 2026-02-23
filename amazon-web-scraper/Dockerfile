FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml /tmp/pyproject.toml

RUN python - <<'PY'
import subprocess
import tomllib

with open("/tmp/pyproject.toml", "rb") as f:
    dependencies = tomllib.load(f)["project"]["dependencies"]

subprocess.check_call(["pip", "install", "--no-cache-dir", *dependencies])
PY

COPY . /app

CMD ["streamlit", "run", "main.py", "--server.address=0.0.0.0", "--server.port=8501"]
