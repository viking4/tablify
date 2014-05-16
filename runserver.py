from approot import app

# Options: DevConfig, ProdConfig, TestConfig
app.config.from_object('approot.config.DevConfig')


if __name__ == '__main__':
    app.run()
