import sys

from app import app


if __name__ == '__main__':
    if len(sys.argv) == 1 and sys.argv[1] == 'debug':
        app.run('0.0.0.0', debug=True, port=5000)
    app.run(debug=True)
