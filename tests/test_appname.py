#! ../env/bin/python
# -*- coding: utf-8 -*-
from appname import create_app
from appname.models import User


class TestConfig:
    def test_dev_config(self):
        app = create_app('appname.settings.DevConfig', 'dev')

        assert app.config['DEBUG'] == True
        assert app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite://example.db'
        assert app.config['SQLALCHEMY_ECHO'] == True
        assert app.config['CACHE_TYPE'] == 'null'


    def test_prod_config(self):
        app = create_app('appname.settings.ProdConfig', 'prod')

        assert app.config['SQLALCHEMY_DATABASE_URI'] == 'postgresql://localhost/example'
        assert app.config['CACHE_TYPE'] == 'simple'


class TestModels:
    def test_user(self):
        admin = User('admin', 'supersafepassword')

        assert admin.username == 'admin'
        assert admin.password == 'supersafepassword'