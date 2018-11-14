# coding: utf-8

import signal
import socket
import argparse
from werkzeug.utils import find_modules, import_string
from app import app


def configure_blueprint(app):
    root = 'views'
    for name in find_modules(root, recursive=True):
        mod = import_string(name)
        if hasattr(mod, 'module'):
            app.register_blueprint(mod.module)


def bind_signal():
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    signal.signal(signal.SIGTERM, signal.SIG_DFL)
    signal.signal(signal.SIGHUP, signal.SIG_DFL)


def get_local_ip():
    return socket.gethostbyname(socket.gethostname())


if __name__ == '__main__':
    bind_signal()

    ip = get_local_ip()

    parser = argparse.ArgumentParser()
    parser.add_argument('--port', '-p', help='port', default=5000)
    args = parser.parse_args()

    configure_blueprint(app)
    app.run(ip, args.port, threaded=True)
