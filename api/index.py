from app.server import app

# For WSGI compatibility
def handler(request):
    return app(request)