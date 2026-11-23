# OnceTold Memory — FastAPI / Cognee Bridge

A small Python service that lets the [OnceTold support application](https://github.com/OM2412/OnceTold) store and recall customer-scoped support context with Cognee.

**[Main application repository](https://github.com/OM2412/OnceTold)** · **[Published product tour](https://oncetold.pages.dev/demo.html)** (synthetic browser-only simulation)

> **Historical integration repository:** The actively packaged bridge is maintained in the main OnceTold repository under `deploy/memory/`. This repository remains useful for understanding the original standalone FastAPI integration. It is not independently advertised as a live hosted service.

## API

| Method | Path | Function |
| --- | --- | --- |
| `GET` | `/` | Basic service description |
| `GET` | `/health` | Process health |
| `POST` | `/remember` | Store a ticket message for a customer |
| `GET` | `/recall` | Retrieve relevant customer-scoped memories |
| `POST` | `/improve` | Incorporate a ticket resolution |
| `POST` | `/forget` | Delete a customer's memory dataset |

The service accepts a caller-supplied `customer_id`; **do not expose it directly to the public internet** without enforcing authentication and customer authorization in a trusted gateway. The current main application's Java API performs ownership checks.

## Local development

Use Python 3 and a valid Cognee configuration.

```bash
git clone https://github.com/OM2412/OnceTold-Memory.git
cd OnceTold-Memory
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --host 127.0.0.1 --port 8000
```

On Windows use `.venv\\Scripts\\activate`. Configure the Cognee-related values from `.env.example` in your own environment. Keep credentials out of Git.

Check [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health).

## Design and safety notes

- `main.py` defines the FastAPI endpoints and CORS configuration.
- `cognee_client.py` implements graph-memory calls.
- `spike.py` is an experimentation script, not the production entrypoint.
- `ALLOWED_ORIGINS` defaults to localhost and must be configured for legitimate browser origins when needed.
- Do not use real customer information for demos without permission, retention policies and deletion verification.

**Status:** Integration prototype / historical standalone bridge. No public service uptime claim.
