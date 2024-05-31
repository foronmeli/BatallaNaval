import sys
sys.path.append("src")

from View import vista_usuarios 
from flask import Flask, request
from flask import render_template

app = Flask(__name__)

app.register_blueprint( vista_usuarios.blueprint )

if __name__ == '__main__':
    app.run(debug=True)