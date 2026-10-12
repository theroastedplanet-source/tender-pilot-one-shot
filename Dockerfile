FROM node:24-bookworm-slim
RUN apt-get update && apt-get install -y --no-install-recommends python3 poppler-utils && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY . .
ENV NODE_ENV=production HOST=0.0.0.0 PORT=3000 PUBLIC_DEMO_ONLY=1 DATA_DIR=/data
EXPOSE 3000
CMD ["node", "server.mjs"]
