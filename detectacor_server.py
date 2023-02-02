from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from detectacor import analisaImagem

app = Flask(__name__)
api = Api(app)
CORS(app)

@app.route('/getcolor', methods=['GET'])
def getColor():
    _, _, string64, cor = analisaImagem()
    return {'cor': cor, 'imagem': string64}, 200

if __name__ == '__main__':
    app.run(host='10.113.163.132', port=5000)