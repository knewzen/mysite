import sys

from app import app, db
from app.models import User, Post


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}


if __name__ == '__main__':
    if len(sys.argv) == 1 and sys.argv[1] == 'debug':
        app.run('0.0.0.0', debug=True, port=5000)
    app.run()
