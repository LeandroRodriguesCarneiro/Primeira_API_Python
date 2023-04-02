import json
#-*- coding: utf-8 -*-
def gerarJson(lista_nomes):
    pessoas = []
    counter = 0
    for nome in lista_nomes:
        base_senha = nome.split(' ')
        senha = f'{base_senha[0]}_{base_senha[1]}'
        pessoa ={
                "id_user": counter,
                "nome": nome,
                "email": nome.replace(" ","_")+"@example.com",
                "senha": senha
        }
        counter+=1
        pessoas.append(pessoa)
    json_object = json.dumps(pessoas,indent=4) 
    with open('base_dados\\pessoas.json','w',encoding='utf-8') as json_w: 
        json_w.write(str(json_object))
        json_w.close()

def updateJson(pessoas):
    json_object = json.dumps(pessoas,indent=4) 
    with open('base_dados\\pessoas.json','w',encoding='utf-8') as json_w: 
        json_w.write(str(json_object))
        json_w.close()
    return lerJson()

def lerJson():
    with open('base_dados\\pessoas.json','r',encoding='utf-8') as json_r:
        json_object = json.load(json_r)
        json_r.close()
    return json_object

def addJson(nome,email,senha):
    pessoas = lerJson()
    pessoa = {
            "id_user": len(pessoas)+1,
            "nome": nome,
            "email": email,
            "senha": senha
    }
    for data in pessoas:
        if data['nome'] == pessoa['nome'] or pessoa['nome']==' ':
            return 
        if data['email'] == pessoa['email'] or pessoa['email']==' ':
            return 
        if data['senha'] == pessoa['senha'] or pessoa['senha']==' ':
            return 
    pessoas.append(pessoa)
    json_objet = json.dumps(pessoas,indent=4)
    with open('base_dados\\pessoas.json','w',encoding='utf-8') as json_a:
        json_a.write(str(json_objet))
        json_a.close()
    return pessoas[(len(pessoas)-1)]

def lerjson_especifico(type_search,data):
    pessoas = lerJson()
    if type_search == 'id_user' or type_search == 'nome' or type_search == 'email':
        if not data == None:
            if type_search == 'id_user':
                for pessoa in pessoas:
                    if pessoa[type_search] == int(data):
                        return pessoa
            else:
                for pessoa in pessoas:
                    if pessoa[type_search] == data:
                        return pessoa
        else:
            return
    else:
        return

def alterarJson(dicionario):
    if type(dicionario) == dict:
        id_user = dicionario['id_user']
        pessoas = lerJson()
        count = 0
        for pessoa in pessoas:
            if pessoa['id_user'] == id_user:
                break
            count +=1
        keys = ['nome','email','senha']
        if not dicionario['nome'] == '' and dicionario['email'] == '' and dicionario['senha'] == '':
            if keys in dicionario.keys():
                pessoas[count] = dicionario
        json_object = json.dumps(pessoas,indent=4) 
        with open('base_dados\\pessoas.json','w',encoding='utf-8') as json_w: 
            json_w.write(str(json_object))
            json_w.close()
        pessoas = lerJson()
        return pessoas[count]
    else:
        return
