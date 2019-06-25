web: gunicorn -w 1 -b 0.0.0.0:$PORT run:app
worker: python -c 'from worker.main import main; main()'
