import os
from http.server import HTTPServer, CGIHTTPRequestHandler
os.chdir('.')



# # Create server object listening the port 80
# server_object = HTTPServer(
#     server_address=('', 80), 
#     RequestHandlerClass=CGIHTTPRequestHandler
#     #The second argument is the request handler class. 
#     #Here we use CGIHTTPRequestHandler that we have already imported.
# )

# server_object.serve_forever()
from flask import Flask

app = Flask(__name__)
def your_func():
    print('hello')
    return ('hello')
@app.route('/run')
def run_command():
    your_func()
    return 'Executed your function!'

if __name__ == '__main__':
    app.run(debug=False, port=8080)