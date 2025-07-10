FROM python:3.12.3

WORKDIR /app

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Копируем requirements.txt первым для лучшего кэширования
COPY requirements.txt .

# Устанавливаем Python зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы
COPY . .

RUN pip install gunicorn

# Создаем непривилегированного пользователя
RUN adduser --disabled-password --gecos '' appuser

RUN chown -R appuser:appuser /app

USER appuser

CMD ["uwsgi", "app.ini"]