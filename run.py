from app.setup import create_app  # NOQA


app = create_app()

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=int(app.config['PORT']))
