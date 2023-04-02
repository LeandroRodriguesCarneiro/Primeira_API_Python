from flask import Flask,render_template,request,url_for
#-*- coding: utf-8 -*-

from base_dados.base_dados import gerarJson,lerJson,addJson,lerjson_especifico,alterarJson,updateJson
app = Flask(__name__, template_folder='templates')

# para rodar pela primeira vez usar gerarJson com uma lista de nomes a fim de construir uma base 
# para iniciar o uso dos endpoints ou adicionar com endpoint '/adicionar-usuario'

@app.get('/')
def index():
    return render_template('index.html'),200

@app.get('/todos')
def dados_get():
    return lerJson(),200

@app.post('/adicionar-usuario')
def adicionar():
    request_data = request.get_json()
    nome = None
    email = None
    senha = None
    if request_data:
        if 'nome' in request_data:
            nome = request_data['nome']
        if 'email' in request_data:
            email = request_data['email']
        if 'senha' in request_data:
            senha = request_data['senha']
        data = addJson(nome,email,senha)
        if not data == None:
            return data,200
        else:
            return 'Houve um problema na requisição',400

@app.get('/consulta-especifica')
def consulta_especifica():
    type_search =  request.args.get('typeSearch')
    data = request.args.get('data')
    consulta = lerjson_especifico(type_search,data)
    if not consulta == None:
        data_return ={
                        "email": consulta['email'],
                        "senha": consulta['senha']
                    }
        return data_return,200
    else:
        return 'consulta errada',400

@app.post('/alterar-user')
def alterar():
    type_search =  request.args.get('typeSearch')
    data = request.args.get('data')
    consulta = lerjson_especifico(type_search,data)
    if not consulta == None:
        request_data = request.get_json()
        if request_data:
            if 'nome' in request_data:
                nome = request_data['nome']
            else:
                return 'faltou chave nome no diocionario',400
            if 'email' in request_data:
                email = request_data['email']
            else:
                return 'faltou chave email no diocionario',400
            if 'senha' in request_data:
                senha = request_data['senha']
            else:
                return 'faltou chave senha no diocionario',400
            data_user ={
                        "id_user": consulta['id_user'],
                        "nome":  nome,
                        "email": email,
                        "senha": senha
                    }
            data = alterarJson(data_user)
            if not data == None:
                return data,200
            else:
                return 'Houve um problema na requisição',400
        else:
            return 'Houve um problema na requisição',400
    else:
        return 'não foi encontrado nenhum usuario',400

@app.delete('/apaga-user')
def delete():
    type_search =  request.args.get('typeSearch')
    data = request.args.get('data')
    consulta = lerjson_especifico(type_search,data)
    if not consulta == None:
        pessoas = lerJson()
        position =  pessoas.index(consulta)
        cont = 0
        for pessoa in pessoas:
            if cont>position:
                if not cont == len(pessoas):
                    pessoas[cont-1]=pessoas[cont]
                else:
                    break 
            cont +=1
        remover = pessoas[len(pessoas)-1]
        pessoas.remove(remover)
        return updateJson(pessoas),200
    else:
        return 'Não foi encontrado nenhum usuario',400

app.run(debug=True)