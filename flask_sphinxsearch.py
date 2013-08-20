try:
    import sphinxapi as sphinxsearch
except ImportError:
    import sphinxsearch
from flask import current_app

# Find the stack on which we want to store the database connection.
# Starting with Flask 0.9, the _app_ctx_stack is the correct one,
# before that we need to use the _request_ctx_stack.
try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack


class Sphinx(object):
    """
    Simple wrapper around the `SphinxClient` object.

    Usage:

    from flask.ext.sphinxsearch import Sphinx
    from myapp import app

    sphinx = Sphinx(myapp)
    print sphinx.client.Query("query")
    """
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        app.config.setdefault('SPHINX_HOST', 'localhost')
        app.config.setdefault('SPHINX_PORT', 3312)

    def connect(self):
        client = sphinxsearch.SphinxClient()
        client.SetServer(
            current_app.config['SPHINX_HOST'],
            current_app.config['SPHINX_PORT'])
        return client

    @property
    def client(self):
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx, 'sphinxclient'):
                ctx.sphinxclient = self.connect()
            return ctx.sphinxclient


# set constants on the Sphinx object, for ease of use
for key in dir(sphinxsearch):
    if key == key.upper():
        setattr(Sphinx, key,
                getattr(sphinxsearch, key))
