from multiprocessing import cpu_count

 # Socket Path
bind = 'unix:/home/fastapi-user/ai_papi/run/gunicorn.sock'

 # Worker Options
workers = cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'

 # Logging Options
loglevel = 'debug'
accesslog = '/home/fastapi-user/ai_papi/logs/access.log'
errorlog =  '/home/fastapi-user/ai_papi/p_api/logs/error.log'
