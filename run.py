import os
from flask_script import Manager, Server
from app.setup import create_app  # NOQA

app = create_app()
print(app.config)
if __name__ == '__main__':
    manager = Manager(app)
    port = int(os.environ.get('PORT', 5000))
    manager.add_command("runserver", Server(host='0.0.0.0', port=port))
    manager.run()