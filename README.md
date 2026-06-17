# document-service

[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.135%2B-orange)](https://fastapi.tiangolo.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-6.0%2B-green)](https://www.mongodb.com/)
[![Docker](https://img.shields.io/badge/Docker-24%2B-blue)](https://www.docker.com/)
[![Ruff](https://img.shields.io/badge/ruff-check-purple)](https://docs.astral.sh/ruff/)
[![Pydantic](https://img.shields.io/badge/Pydantic-2.13%2B-yellow)](https://docs.pydantic.dev/)

## Описание проекта

**document-service** — это микросервис для обработки и хранения документов с поддержкой конструктора и хранилища. Сервис предоставляет API для работы с макетами документов (layouts) и отчетами (reports), основанными на архитектуре Clean Code с использованием dependency injection через Dishka.

### Основные функции

- 🏗️ **Конструктор документов** — создание и управление макетами документов
- 📄 **Хранилище документов** — сохранение и управление отчетами и документами
- 🗄️ **MongoDB интеграция** — асинхронная работа с MongoDB через Beanie ODM
- 🧱 **Композиционная архитектура** — модульная структура с четким разделением ответственности
- 🏗️ **Clean Code архитектура** — разделение на слои: API, Domain, Infrastructure
- 📦 **Dependency Injection** — управление зависимостями через Dishka
- 🔒 **Безопасность** — контроль доступа к документации в продакшене
- 📊 **Полнотекстовый поиск** — готовность к интеграции Elasticsearch
- ⚡ **Асинхронность** — полная асинхронная обработка запросов

### Архитектура

Проект использует слоистую архитектуру:

```
src/
├── api/              # API layer (FastAPI endpoints)
│   ├── constructor/  # Конструктор документов (v2)
│   └── storage/      # Хранилище документов (v3)
├── domain/           # Business logic layer
│   ├── layout/       # Бизнес-логика макетов
│   ├── report/       # Бизнес-логика отчетов
│   ├── models/       # Модели данных (DTO, Entities, VO)
│   └── services/     # Бизнес-сервисы
├── infra/            # Infrastructure layer
│   └── mongo/        # MongoDB инфраструктура
└── assembly/         # DI контейнеры и конфигурация
```

## Стек технологий

| Категория | Технология | Версия |
|-----------|------------|--------|
| **Язык** | Python | 3.10+ |
| **Web framework** | FastAPI | 0.135+ |
| **Ойедменеджмент** | uv | latest |
| **Контейнеризация** | Docker | 24+ |
| **База данных** | MongoDB | 6.0+ |
| **ODM** | Beanie | 2.1+ |
| **DI Container** | Dishka | 1.10+ |
| **Валидация** | Pydantic | 2.13+ |
| **Кодирование** | Ruff | latest |
| **Тесты** | pytest | 9.0+ |

## Установка и запуск

### Предварительные требования

- [Python 3.10+](https://www.python.org/downloads/)
- [uv](https://github.com/astral-sh/uv) (менеджер пакетов)
- [Docker](https://www.docker.com/get-started/) (для MongoDB)

### Быстрый старт

1. **Склонируйте репозиторий**
```bash
git clone <repository-url>
cd document-service
```

2. **Установите зависимости**
```bash
uv sync --all-extras
```

3. **Запустите MongoDB (через Docker)**
```bash
cd deployment/docker/mongo/single
docker-compose up -d
```

4. **Создайте .env файл**
```bash
cp .env.example .env
# Отредактируйте .env файл с вашими настройками
```

5. **Запустите приложение**
```bash
uv run uvicorn src.assembly.api.constructor:create_app --reload
```

Приложение будет доступно по адресу: `http://localhost:8000`

### Дополнительные команды

```bash
# Запустить тесты
uv run pytest tests/

# Запустить с покрытием
uv run pytest tests/ --cov=src --cov-report=html

# Проверка кода
uv run ruff check .
uv run ruff format --check .

# Форматирование кода
uv run ruff format .

# Проверка типов
uv run ty check .
```

## Конфигурация

Переменные окружения для API:

```env
# Основные настройки
API_ENV_PREFIX=DOC_
API_IS_DEV_MODE=true
API_ROOT_PATH=/api

# CORS
API_ALLOW_ORIGINS=["http://localhost:3000"]
API_ALLOW_HEADERS=["*"]
API_ALLOW_METHODS=["*"]

# MongoDB
MONGODB_HOST=localhost
MONGODB_PORT=27017
MONGODB_DB_NAME=document_service
MONGODB_URL=mongodb://localhost:27017

# Режимы документации
MODE=DEV  # DEV или PROD (в PROD отключается документация)
```

## API Endpoints

### Конструктор (v2)
- `POST /layouts/` — Создать/получить макет

### Хранилище (v3)
- `POST /layouts/` — Управление макетами
- `POST /reports/` — Управление отчетами

Для просмотра полной документации API запустите сервис и перейдите по адресу:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

> **Примечание**: В режиме PROD (`MODE=PROD`) документация отключается для безопасности.

## CI/CD и качество кода

Проект использует следующие инструменты для обеспечения качества:

- **Ruff** — линтер и форматтер
- **ty** — проверка CLI интерфейсов
- **pytest** — unit и integration тесты
- **Pre-commit** — хуки перед коммитами

### Definition of Done

Перед коммитом убедитесь, что все проверки прошли успешно:

```bash
uv run ruff format .
uv run ruff check . --fix
uv run pytest tests/
uv run pre-commit run --all-files
```

## Разработка

### Установка pre-commit хуков

```bash
uv run pre-commit install
```

### Добавление зависимостей

```bash
# Runtime зависимость
uv add package-name

# Dev зависимость
uv add --group dev package-name
```

### Сборка Docker образа

```bash
docker build -f deployment/docker/app/Dockerfile -t document-service .
```

## Лицензия

MIT License
