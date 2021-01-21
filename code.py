from flask import flask
from flask import request

sample = Flask(__name__)

@sample.router("/")
def main():
    return "You are calling me from " + request.remote_addr

if __name__ == "__main__":
    smaple.run(port=8080, host ="0.0.0.0")
