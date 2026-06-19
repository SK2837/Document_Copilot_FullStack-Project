from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.config import settings

app = FastAPI(title="Document Copilot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


if __name__ == "__main__":
    # import uvicorn here to avoid import-time issues in environments
    # where uvicorn isn't available to static analyzers
    import uvicorn

    uvicorn.run("app.main:app", host="127.0.0.1", port=8000)
