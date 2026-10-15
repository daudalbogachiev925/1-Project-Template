# 1-Project-Templatе

Корпоративный шаблон 1С-проекта для команд от 3 разработчиков.

## Что внутри
- Структура репозитория (configuration, extensions, common)
- Скрипты сборки, выгрузки, инициализации
- CI/CD (GitHub Actions + SonarQube)
- Pre-commit хуки (BSL LS)
- Стандарты кода, именования, git-flow
- Makefile для типовых задач

## Быстрый старт
```bash
make init
make dump
make build
make test
```

## Требования
- 1С:Предприятие 8.3.24+
- EDT или Конфигуратор
- Python 3.10+
- SonarQube (опционально)
