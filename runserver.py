from approot import app
from werkzeug.contrib.fixers import ProxyFix

# Options: DevConfig, ProdConfig, TestConfig
app.config.from_object('approot.config.ProdConfig')

app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    app.run()
