# Gunakan image python resmi sebagai base
FROM python:3.11-slim

# Set direktori kerja di dalam container
WORKDIR /app

# Salin file requirements dan install dependency
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh file backend ke container
COPY . .

# Set variabel env
ENV PYTHONUNBUFFERED=1

# Jalankan gunicorn pada port dari Railway
CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "app:app"]
