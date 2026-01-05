from flask import Flask

'''
It creates an instance of the Flask class, which will be your WSGI (Web Server Gateway Interface) application.
'''

def main():
    return "Hello World"


app = Flask(__name__)

if __name__ == "__main__":
    app.run()

