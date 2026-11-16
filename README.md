# UptimeMonitor


## Структура папок

```text
uptimeMonitor/api/  # апи часть
uptimeMonitor/monitor/  # мониторинг часть
uptimeMonitor/alerts/  # оповещения часть
```

## Запуск приложения


запуск из корня проекта!
/uptimemonitor/

api:
poetry run uvicorn uptimemonitor.main:app --app-dir api --reload

адрес проверки http://127.0.0.1:8000/health;
адрес документации http://127.0.0.1:8000/docs.