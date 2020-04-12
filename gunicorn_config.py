pidfile = 'gunicorn.pid'
bind = [':80']

workers = 8
worker_class = 'gevent'
worker_connections = 4096
threads = 8

preload_app = True
keepalive = 0

accesslog = '-'
errorlog = '-'
syslog = False
disable_redirect_access_to_syslog = True
