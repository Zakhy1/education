FROM python:3.12

RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

ADD https://astral.sh/uv/install.sh /uv-installer.sh

RUN sh /uv-installer.sh && rm /uv-installer.sh

ENV PATH="/root/.local/bin/:$PATH"

WORKDIR /home/app/

# Установка зависимостей
COPY uv.lock pyproject.toml ./
RUN uv sync

# Запуск приложения
COPY . .
EXPOSE 8000

# Для запуска только контейнера
#CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]