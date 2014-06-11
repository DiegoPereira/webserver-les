import json

from flask import Flask, make_response, request
from bd_agent import ServerData

app = Flask(__name__)
server_data = ServerData()

@app.route('/get_db')
def get_db():
    user_id = request.args.get('user_id')
    resp = make_response(server_data.get_db(user_id))
    resp.headers['Access-Control-Allow-Origin'] = "*"

    return resp

@app.route('/save_db')
def save_db():
    ano = json.loads(request.args.get('ano'))
    atividade = request.args.get('atividade')
    data = request.args.get('data')
    prioridade = request.args.get('prioridade')
    semanaDoAno = request.args.get('semanaDoAno')
    tempo = request.args.get('tempo')
    tipo = request.args.get('tipo')
    user_id = request.args.get('user_id')
    
    #status = server_data.insert_bd(ano,atividade,data,prioridade,semanaDoAno, tempo, tipo, user_id)
    list = [ano,atividade,data,prioridade,semanaDoAno, tempo, tipo, user_id]
    #status = ano
    #if status:
     #   resp = 'True'
   # else:
   #     resp = 'None'
    return json.dumps(list)


if __name__ == '__main__':
    app.debug = True    
    app.run(host='0.0.0.0', port=8080)

