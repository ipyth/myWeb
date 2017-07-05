from flask import Flask, request

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    return "Index Page!"


# converters: any,default,float,int,path,string
@app.route('/hello/', defaults={'username': 'flask'})
@app.route('/hello/<string:username>')
def hello_user(username):
    return "Hello {}".format(username)


# HTTP methods: GET,HEAD,POST,PUT,DELETE,OPTIONS
# default: OPTIONS, GET, HEAD
@app.route('/users/', methods=['GET', 'POST'], defaults={'username': 'flask'})
@app.route('/users/<string:username>', methods=['GET', 'POST'])
def users(username):
    if request.method == 'POST':
        return "Create user: {}".format(username)
    else:
        return "Show user: {}".format(username)

"""
# add_url_rule(self, rule, endpoint=None, view_func=None, **options)
# werkzeug.routing.Rule()
#   param: string,defaults,subdomain,methods,build_only,endpoint,strict_slashes,redirect_to,alias,host
"""
# app.add_url_rule('/', 'index', index)
# app.add_url_rule('/index/', 'index', index)
# app.add_url_rule(rule='/hello/', view_func=hello_user, defaults={'username': 'flask'})
# app.add_url_rule(rule='/hello/<string:username>', endpoint='hello user', view_func=hello_user)
# app.add_url_rule('/users/<string:username>', 'users', users, defaults={'username': 'flask'}, methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
