from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return "Index Page!"


@app.route('/hello/')
def hello():
    return "Hello World!"


# converters: any,default,float,int,path,string
@app.route('/hello/<string:username>')
def hello_user(username):
    return "Hello {}".format(username)


# HTTP methods: GET,HEAD,POST,PUT,DELETE,OPTIONS
# default: OPTIONS, GET, HEAD
@app.route('/users/<string:username>', methods=['GET', 'POST'])
def users(username):
    if request.method == 'POST':
        return "Create user: {}".format(username)
    else:
        return "Show user: {}".format(username)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
