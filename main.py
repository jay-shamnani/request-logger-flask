from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    print('Request Headers: \n', request.headers)
    print('Request Data: \n', request.data)
    print('Request Method: \n', request.method)
    print('Request Method 2: \n', request.method)
    return 'Web App with Python Flask!'

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
