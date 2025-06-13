import sys
import types

# Stub for flask if not installed
try:
    import flask  # noqa: F401
except ModuleNotFoundError:
    flask_stub = types.ModuleType('flask')

    class Redirect:
        def __init__(self, location):
            self.location = location

    class Response:
        def __init__(self, data='', status_code=200, headers=None):
            self.data = data.encode() if isinstance(data, str) else data
            self.status_code = status_code
            self.headers = headers or {}

    def redirect(location):
        return Redirect(location)

    import os
    def render_template(template):
        path = os.path.join(os.path.dirname(__file__), '..', 'app', 'templates', template)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return f'render:{template}'

    def url_for(endpoint):
        if endpoint == 'tarefa.cadastarTarefa':
            return '/cadastarTarefa'
        return '/' + endpoint.split('.')[-1]

    session = {}
    request = types.SimpleNamespace()

    class Blueprint:
        def __init__(self, name, import_name):
            self.name = name
            self.routes = {}

        def route(self, rule):
            def decorator(func):
                self.routes[rule] = func
                return func
            return decorator

    class Flask:
        def __init__(self, name):
            self.name = name
            self.routes = {}

        def route(self, rule):
            def decorator(func):
                self.routes[rule] = func
                return func
            return decorator

        def register_blueprint(self, bp):
            for rule, func in bp.routes.items():
                self.routes[rule] = func

        def test_client(self):
            app = self

            class Client:
                def get(self, path, follow_redirects=False):
                    rv = app.routes[path]()
                    if isinstance(rv, Redirect):
                        if follow_redirects:
                            return self.get(rv.location, follow_redirects)
                        return Response('', 302, {'Location': rv.location})
                    return Response(rv)

            return Client()

    flask_stub.Flask = Flask
    flask_stub.Blueprint = Blueprint
    flask_stub.redirect = redirect
    flask_stub.url_for = url_for
    flask_stub.render_template = render_template
    flask_stub.session = session
    flask_stub.request = request

    sys.modules['flask'] = flask_stub

# Stub for dotenv if not installed
try:
    from dotenv import load_dotenv  # noqa: F401
except ModuleNotFoundError:
    dotenv_stub = types.ModuleType('dotenv')

    def load_dotenv():
        pass

    dotenv_stub.load_dotenv = load_dotenv
    sys.modules['dotenv'] = dotenv_stub

# Stub for mysql.connector if not installed
try:
    import mysql.connector  # noqa: F401
except ModuleNotFoundError:
    mysql_stub = types.ModuleType('mysql')
    connector_stub = types.ModuleType('mysql.connector')

    class Connection:
        def cursor(self, dictionary=False):
            return types.SimpleNamespace(
                execute=lambda query, params=None: None,
                executemany=lambda query, params=None: None,
                fetchall=lambda: [],
                lastrowid=1,
                close=lambda: None,
            )

        def commit(self):
            pass

        def rollback(self):
            pass

        def close(self):
            pass

    def connect(**kwargs):
        return Connection()

    connector_stub.connect = connect
    mysql_stub.connector = connector_stub

    sys.modules['mysql'] = mysql_stub
    sys.modules['mysql.connector'] = connector_stub
