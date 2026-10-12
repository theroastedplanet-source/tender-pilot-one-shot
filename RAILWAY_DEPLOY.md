# Railway synthetic preview

Deploy this repository as a Dockerfile service. Set `PUBLIC_DEMO_ONLY=1`, `HOST=0.0.0.0`, `DATA_DIR=/data`. Mount a Railway volume at `/data` for SQLite and uploads. Set `PUBLIC_ORIGIN` to the exact generated HTTPS origin, e.g. `https://your-app.up.railway.app` (no trailing slash), then redeploy. Never set `OPENAI_API_KEY` for the public preview. The public preview only supports synthetic demo accounts; do not upload real customer documents. Local credentials are not production authentication. No real customer access is approved.
