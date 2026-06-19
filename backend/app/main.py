from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.auth.dependencies import CurrentUser, get_current_user
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


@app.get("/me")
async def me(user: CurrentUser = Depends(get_current_user)) -> dict[str, str]:
    return {"id": str(user.id), "email": user.email}


if __name__ == "__main__":
    # import uvicorn here to avoid import-time issues in environments
    # where uvicorn isn't available to static analyzers
    import uvicorn

    uvicorn.run("app.main:app", host="127.0.0.1", port=8000)
