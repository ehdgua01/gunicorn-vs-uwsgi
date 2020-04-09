pidfile = 'gunicorn.pid'
bind = '127.0.0.1:80'

workers = 4
worker_class = 'gevent'
threads = 4

accesslog = '-'
errorlog = '-'
syslog = False
disable_redirect_access_to_syslog = True
