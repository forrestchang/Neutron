from app import app
from flask_script import Manager, Server


manager = Manager(app)
manager.add_command(
    "runserver",
    Server(host='0.0.0.0', port=5000, use_debugger=True, threaded=True)
)

if __name__ == '__main__':
    manager.run()
