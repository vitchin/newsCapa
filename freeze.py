from flask_frozen import Freezer
from flask import Flask # 'app' é sua instância Flask

app = Flask(__name__)
freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
