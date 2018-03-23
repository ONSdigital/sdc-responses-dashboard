import os

from app.setup import create_app  # NOQA

if not os.getenv('APP_SETTINGS'):
    os.environ['APP_SETTINGS'] = 'DevelopmentConfig'

app = create_app()

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=int(app.config['PORT']))
