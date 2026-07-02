import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from cognee_client import (
    remember_ticket_message,
    recall_for_customer,
    resolve_and_improve,
    forget_dataset,
)

app = FastAPI(title="OnceTold Memory Service")

# Comma-separated list of allowed origins, e.g.
#   ALLOWED_ORIGINS=https://oncetold-production.up.railway.app,http://localhost:3000
# Defaults to localhost so local dev keeps working without setting anything.
_origins_env = os.environ.get("ALLOWED_ORIGINS", "http://localhost:3000")
ALLOWED_ORIGINS = [origin.strip() for origin in _origins_env.split(",") if origin.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class RememberRequest(BaseModel):
    customer_id: str
    ticket_id: str
    content: str


class ImproveRequest(BaseModel):
    customer_id: str
    ticket_id: str
    resolution: str


@app.post("/remember")
async def remember_endpoint(req: RememberRequest):
    status = await remember_ticket_message(req.content, customer_id=req.customer_id)
    return {"status": status}


@app.get("/recall")
async def recall_endpoint(customer_id: str, query: str = ""):
    status, results = await recall_for_customer(query or "recent history", customer_id=customer_id)
    return {"customer_id": customer_id, "status": status, "memories": results}


@app.post("/improve")
async def improve_endpoint(req: ImproveRequest):
    status = await resolve_and_improve(req.resolution, customer_id=req.customer_id)
    return {"status": status}


@app.post("/forget")
async def forget_endpoint(customer_id: str):
    status = await forget_dataset(customer_id)
    return {"status": status}


@app.get("/")
async def root():
    return {"service": "OnceTold Memory Service", "status": "running"}


@app.get("/health")
async def health():
    return {"status": "ok"}