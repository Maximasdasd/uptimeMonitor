from fastapi import FastAPI
from uptimemonitor.routers.auth import authrouter

app = FastAPI(
    title="UptimeMonitor",
    version="0.1.0",
    description="API для сервиса мониторинг сайтов",
)

app.include_router(authrouter, prefix="/api/v1/auth", tags=["Auth"])


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}