web: env APPD_NODE_NAME=$(hostname) APPD_TIER_NAME=$WEB_APPD_TIER_NAME pyagent run -- gunicorn -w 1 -b 0.0.0.0:$PORT run:app
worker: env APPD_NODE_NAME=$(hostname) APPD_TIER_NAME=$WORKER_APPD_TIER_NAME pyagent run --  python -c 'from worker.main import main; main()'
