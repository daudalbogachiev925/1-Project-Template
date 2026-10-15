# Git Flow

## Ветки
- main — production, только через PR из release
- develop — интеграционная ветка
- feature/<ticket>-<slug> — новая функциональность
- bugfix/<ticket>-<slug> — исправления
- release/<version> — подготовка релиза
- hotfix/<version> — срочные правки в production

## Коммиты
Формат: <type>(<scope>): <subject>

Типы:
- feat: новая функциональность
- fix: исправление
- refactor: рефакторинг
- perf: оптимизация
- docs: документация
- test: тесты
- chore: обновления инфраструктуры

Пример:
feat(catalog): добавлен справочник Товары с иерархией
fix(report): исправлен расчёт НДС в отчёте Продажи
