__author__='wilmarguerra'
import requests #tem que instalar
import json

link_banco = "https://chatbot-aefd1-default-rtdb.firebaseio.com/Marcacao"
from flask import Flask, request, jsonify, render_template


##################################################################################################
def verifica_vagas_danier():
    requisicao = requests.get(f'{link_banco}/.json')
    print("Requisição .json -->  ", requisicao.json())
    dic_pyt_requisicao = requisicao.json()
    print("Número de pacientes Danier: ", len(dic_pyt_requisicao["medicos"]["especialidade"]["clinicoGeral"]["danier"]["pacientes"]))
    pacientes_marcados = len(dic_pyt_requisicao["medicos"]["especialidade"]["clinicoGeral"]["danier"]["pacientes"])

    print("vagas Danier: ", dic_pyt_requisicao["medicos"]["especialidade"]["clinicoGeral"]["danier"]["vagas"])
    vagas = dic_pyt_requisicao["medicos"]["especialidade"]["clinicoGeral"]["danier"]["vagas"]
    if pacientes_marcados < vagas:
        return True
    else:
        return False
        


def marca_para_danier(data, nome, prontuario, telefone):
    dados = {'nome': nome, 'prontuario': prontuario, 'telefone':telefone}
    dados = json.dumps(dados)
    requisicao = requests.post(f'{link_banco}/medicos/especialidade/clinicoGeral/danier/pacientes/.json', \
    data=dados)
    #print(requisicao, "  ", requisicao.text)
    


    data['fulfillmentText'] = f"Ok Sr(a) {nome}, sua consulta para o Dr. Danier foi marcada e seu prontuário é o {prontuario} e o telefone é o {telefone}. \n ATENÇÃO: Em breve entraremos em contato através do telefone informado para lhe informar o dia e a hora da sua consulta"

##################################################################################################
def verifica_vagas_jorge():
    requisicao = requests.get(f'{link_banco}/.json')
    print("Requisição .json -->  ", requisicao.json())
    dic_pyt_requisicao = requisicao.json()
    print("Número de pacientes Danier: ", len(dic_pyt_requisicao["medicos"]["especialidade"]["clinicoGeral"]["jorge"]["pacientes"]))
    pacientes_marcados = len(dic_pyt_requisicao["medicos"]["especialidade"]["clinicoGeral"]["jorge"]["pacientes"])

    print("vagas jorge: ", dic_pyt_requisicao["medicos"]["especialidade"]["clinicoGeral"]["jorge"]["vagas"])
    vagas = dic_pyt_requisicao["medicos"]["especialidade"]["clinicoGeral"]["jorge"]["vagas"]
    if pacientes_marcados < vagas:
        return True
    else:
        return False
        


def marca_para_jorge(data, nome, prontuario, telefone):
    dados = {'nome': nome, 'prontuario': prontuario, 'telefone':telefone}
    dados = json.dumps(dados)
    requisicao = requests.post(f'{link_banco}/medicos/especialidade/clinicoGeral/jorge/pacientes/.json', \
    data=dados)
    #print(requisicao, "  ", requisicao.text)
    


    data['fulfillmentText'] = f"Ok Sr(a) {nome}, sua consulta para o Dr. Jorge Camargo foi marcada e seu prontuário é o {prontuario} e o telefone é o {telefone}. \n ATENÇÃO: Em breve entraremos em contato através do telefone informado para lhe informar o dia e a hora da sua consulta"
##################################################################################################
def verifica_vagas_fabio():
    requisicao = requests.get(f'{link_banco}/.json')
    print("Requisição .json -->  ", requisicao.json())
    dic_pyt_requisicao = requisicao.json()
    print("Número de pacientes Fabio: ", len(dic_pyt_requisicao["medicos"]["especialidade"]["cardiologia"]["fabio"]["pacientes"]))
    pacientes_marcados = len(dic_pyt_requisicao["medicos"]["especialidade"]["cardiologia"]["fabio"]["pacientes"])

    print("vagas fabio: ", dic_pyt_requisicao["medicos"]["especialidade"]["cardiologia"]["fabio"]["vagas"])
    vagas = dic_pyt_requisicao["medicos"]["especialidade"]["cardiologia"]["fabio"]["vagas"]
    if pacientes_marcados < vagas:
        return True
    else:
        return False

def marca_para_fabio(data, nome, prontuario, telefone):
    dados = {'nome': nome, 'prontuario': prontuario, 'telefone':telefone}
    dados = json.dumps(dados)
    requisicao = requests.post(f'{link_banco}/medicos/especialidade/cardiologia/fabio/pacientes/.json', \
    data=dados)
    #print(requisicao, "  ", requisicao.text)
    


    data['fulfillmentText'] = f"Ok Sr(a) {nome}, sua consulta para o Dr. Fabio Dhein foi marcada e seu prontuário é o {prontuario} e o telefone é o {telefone}. \n ATENÇÃO: Em breve entraremos em contato através do telefone informado para lhe informar o dia e a hora da sua consulta"


##################################################################################################
def verifica_vagas_felipe():
    requisicao = requests.get(f'{link_banco}/.json')
    print("Requisição .json -->  ", requisicao.json())
    dic_pyt_requisicao = requisicao.json()
    print("Número de pacientes Felipe: ", len(dic_pyt_requisicao["medicos"]["especialidade"]["cardiologia"]["felipe"]["pacientes"]))
    pacientes_marcados = len(dic_pyt_requisicao["medicos"]["especialidade"]["cardiologia"]["felipe"]["pacientes"])

    print("vagas felipe: ", dic_pyt_requisicao["medicos"]["especialidade"]["cardiologia"]["felipe"]["vagas"])
    vagas = dic_pyt_requisicao["medicos"]["especialidade"]["cardiologia"]["felipe"]["vagas"]
    if pacientes_marcados < vagas:
        return True
    else:
        return False
        


def marca_para_felipe(data, nome, prontuario, telefone):
    dados = {'nome': nome, 'prontuario': prontuario, 'telefone':telefone}
    dados = json.dumps(dados)
    requisicao = requests.post(f'{link_banco}/medicos/especialidade/cardiologia/felipe/pacientes/.json', \
    data=dados)
    #print(requisicao, "  ", requisicao.text)
    


    data['fulfillmentText'] = f"Ok Sr(a) {nome}, sua consulta para o Dr. Felipe Moraes foi marcada e seu prontuário é o {prontuario} e o telefone é o {telefone}. \n ATENÇÃO: Em breve entraremos em contato através do telefone informado para lhe informar o dia e a hora da sua consulta"
##################################################################################################
def verifica_vagas_clovis():
    requisicao = requests.get(f'{link_banco}/.json')
    print("Requisição .json -->  ", requisicao.json())
    dic_pyt_requisicao = requisicao.json()
    print("Número de pacientes Clóvis: ", len(dic_pyt_requisicao["medicos"]["especialidade"]["angiologia"]["clovis"]["pacientes"]))
    pacientes_marcados = len(dic_pyt_requisicao["medicos"]["especialidade"]["angiologia"]["clovis"]["pacientes"])

    print("vagas Clóvis: ", dic_pyt_requisicao["medicos"]["especialidade"]["angiologia"]["clovis"]["vagas"])
    vagas = dic_pyt_requisicao["medicos"]["especialidade"]["angiologia"]["clovis"]["vagas"]
    if pacientes_marcados < vagas:
        return True
    else:
        return False
        


def marca_para_clovis(data, nome, prontuario, telefone):
    dados = {'nome': nome, 'prontuario': prontuario, 'telefone':telefone}
    dados = json.dumps(dados)
    requisicao = requests.post(f'{link_banco}/medicos/especialidade/angiologia/clovis/pacientes/.json', \
    data=dados)
    #print(requisicao, "  ", requisicao.text)
    


    data['fulfillmentText'] = f"Ok Sr(a) {nome}, sua consulta para o Dr. Clóvis Aragão foi marcada e seu prontuário é o {prontuario} e o telefone é o {telefone}. \n ATENÇÃO: Em breve entraremos em contato através do telefone informado para lhe informar o dia e a hora da sua consulta"

##################################################################################################
def verifica_vagas_flavioMonteiro():
    requisicao = requests.get(f'{link_banco}/.json')
    print("Requisição .json -->  ", requisicao.json())
    dic_pyt_requisicao = requisicao.json()
    print("Número de pacientes Clóvis: ", len(dic_pyt_requisicao["medicos"]["especialidade"]["bucomaxilo"]["flavioMonteiro"]["pacientes"]))
    pacientes_marcados = len(dic_pyt_requisicao["medicos"]["especialidade"]["bucomaxilo"]["flavioMonteiro"]["pacientes"])

    print("vagas Clóvis: ", dic_pyt_requisicao["medicos"]["especialidade"]["bucomaxilo"]["flavioMonteiro"]["vagas"])
    vagas = dic_pyt_requisicao["medicos"]["especialidade"]["bucomaxilo"]["flavioMonteiro"]["vagas"]
    if pacientes_marcados < vagas:
        return True
    else:
        return False
        


def marca_para_flavioMonteiro(data, nome, prontuario, telefone):
    dados = {'nome': nome, 'prontuario': prontuario, 'telefone':telefone}
    dados = json.dumps(dados)
    requisicao = requests.post(f'{link_banco}/medicos/especialidade/bucomaxilo/flavioMonteiro/pacientes/.json', \
    data=dados)
    #print(requisicao, "  ", requisicao.text)
    


    data['fulfillmentText'] = f"Ok Sr(a) {nome}, sua consulta para o Dr. Flávio Monteiro foi marcada e seu prontuário é o {prontuario} e o telefone é o {telefone}. \n ATENÇÃO: Em breve entraremos em contato através do telefone informado para lhe informar o dia e a hora da sua consulta"
##################################################################################################
def verifica_vagas_flavioSpohde():
    requisicao = requests.get(f'{link_banco}/.json')
    print("Requisição .json -->  ", requisicao.json())
    dic_pyt_requisicao = requisicao.json()
    print("Número de pacientes Clóvis: ", len(dic_pyt_requisicao["medicos"]["especialidade"]["bucomaxilo"]["flavioSpohde"]["pacientes"]))
    pacientes_marcados = len(dic_pyt_requisicao["medicos"]["especialidade"]["bucomaxilo"]["flavioSpohde"]["pacientes"])

    print("vagas Clóvis: ", dic_pyt_requisicao["medicos"]["especialidade"]["bucomaxilo"]["flavioSpohde"]["vagas"])
    vagas = dic_pyt_requisicao["medicos"]["especialidade"]["bucomaxilo"]["flavioSpohde"]["vagas"]
    if pacientes_marcados < vagas:
        return True
    else:
        return False
        


def marca_para_flavioSpohde(data, nome, prontuario, telefone):
    dados = {'nome': nome, 'prontuario': prontuario, 'telefone':telefone}
    dados = json.dumps(dados)
    requisicao = requests.post(f'{link_banco}/medicos/especialidade/bucomaxilo/flavioSpohde/pacientes/.json', \
    data=dados)
    #print(requisicao, "  ", requisicao.text)
    


    data['fulfillmentText'] = f"Ok Sr(a) {nome}, sua consulta para o Dr. Flávio Spohde foi marcada e seu prontuário é o {prontuario} e o telefone é o {telefone}. \n ATENÇÃO: Em breve entraremos em contato através do telefone informado para lhe informar o dia e a hora da sua consulta"
##################################################################################################
def verifica_vagas_michele():
    requisicao = requests.get(f'{link_banco}/.json')
    print("Requisição .json -->  ", requisicao.json())
    dic_pyt_requisicao = requisicao.json()
    print("Número de pacientes Clóvis: ", len(dic_pyt_requisicao["medicos"]["especialidade"]["dermatologia"]["michele"]["pacientes"]))
    pacientes_marcados = len(dic_pyt_requisicao["medicos"]["especialidade"]["dermatologia"]["michele"]["pacientes"])

    print("vagas Clóvis: ", dic_pyt_requisicao["medicos"]["especialidade"]["dermatologia"]["michele"]["vagas"])
    vagas = dic_pyt_requisicao["medicos"]["especialidade"]["dermatologia"]["michele"]["vagas"]
    if pacientes_marcados < vagas:
        return True
    else:
        return False
        


def marca_para_michele(data, nome, prontuario, telefone):
    dados = {'nome': nome, 'prontuario': prontuario, 'telefone':telefone}
    dados = json.dumps(dados)
    requisicao = requests.post(f'{link_banco}/medicos/especialidade/dermatologia/michele/pacientes/.json', \
    data=dados)
    #print(requisicao, "  ", requisicao.text)
    


    data['fulfillmentText'] = f"Ok Sr(a) {nome}, sua consulta para a Dr. Michele foi marcada e seu prontuário é o {prontuario} e o telefone é o {telefone}. \n ATENÇÃO: Em breve entraremos em contato através do telefone informado para lhe informar o dia e a hora da sua consulta"

##################################################################################################
def verifica_vagas_roberto():
    requisicao = requests.get(f'{link_banco}/.json')
    print("Requisição .json -->  ", requisicao.json())
    dic_pyt_requisicao = requisicao.json()
    print("Número de pacientes Clóvis: ", len(dic_pyt_requisicao["medicos"]["especialidade"]["gastrologia"]["roberto"]["pacientes"]))
    pacientes_marcados = len(dic_pyt_requisicao["medicos"]["especialidade"]["gastrologia"]["roberto"]["pacientes"])

    print("vagas Clóvis: ", dic_pyt_requisicao["medicos"]["especialidade"]["gastrologia"]["roberto"]["vagas"])
    vagas = dic_pyt_requisicao["medicos"]["especialidade"]["gastrologia"]["roberto"]["vagas"]
    if pacientes_marcados < vagas:
        return True
    else:
        return False
        


def marca_para_roberto(data, nome, prontuario, telefone):
    dados = {'nome': nome, 'prontuario': prontuario, 'telefone':telefone}
    dados = json.dumps(dados)
    requisicao = requests.post(f'{link_banco}/medicos/especialidade/gastrologia/roberto/pacientes/.json', \
    data=dados)
    #print(requisicao, "  ", requisicao.text)
    


    data['fulfillmentText'] = f"Ok Sr(a) {nome}, sua consulta para o Dr. Roberto Lemos foi marcada e seu prontuário é o {prontuario} e o telefone é o {telefone}. \n ATENÇÃO: Em breve entraremos em contato através do telefone informado para lhe informar o dia e a hora da sua consulta"

##################################################################################################
def verifica_vagas_caroline():
    requisicao = requests.get(f'{link_banco}/.json')
    print("Requisição .json -->  ", requisicao.json())
    dic_pyt_requisicao = requisicao.json()
    print("Número de pacientes Clóvis: ", len(dic_pyt_requisicao["medicos"]["especialidade"]["ginecologia"]["caroline"]["pacientes"]))
    pacientes_marcados = len(dic_pyt_requisicao["medicos"]["especialidade"]["ginecologia"]["caroline"]["pacientes"])

    print("vagas Clóvis: ", dic_pyt_requisicao["medicos"]["especialidade"]["ginecologia"]["caroline"]["vagas"])
    vagas = dic_pyt_requisicao["medicos"]["especialidade"]["ginecologia"]["caroline"]["vagas"]
    if pacientes_marcados < vagas:
        return True
    else:
        return False
        


def marca_para_caroline(data, nome, prontuario, telefone):
    dados = {'nome': nome, 'prontuario': prontuario, 'telefone':telefone}
    dados = json.dumps(dados)
    requisicao = requests.post(f'{link_banco}/medicos/especialidade/ginecologia/caroline/pacientes/.json', \
    data=dados)
    #print(requisicao, "  ", requisicao.text)
    


    data['fulfillmentText'] = f"Ok Sr(a) {nome}, sua consulta para a Dra. Caroline Mombaque foi marcada e seu prontuário é o {prontuario} e o telefone é o {telefone}. \n ATENÇÃO: Em breve entraremos em contato através do telefone informado para lhe informar o dia e a hora da sua consulta"

##################################################################################################
def verifica_vagas_maria():
    requisicao = requests.get(f'{link_banco}/.json')
    print("Requisição .json -->  ", requisicao.json())
    dic_pyt_requisicao = requisicao.json()
    print("Número de pacientes Clóvis: ", len(dic_pyt_requisicao["medicos"]["especialidade"]["ginecologia"]["maria"]["pacientes"]))
    pacientes_marcados = len(dic_pyt_requisicao["medicos"]["especialidade"]["ginecologia"]["maria"]["pacientes"])

    print("vagas Clóvis: ", dic_pyt_requisicao["medicos"]["especialidade"]["ginecologia"]["maria"]["vagas"])
    vagas = dic_pyt_requisicao["medicos"]["especialidade"]["ginecologia"]["maria"]["vagas"]
    if pacientes_marcados < vagas:
        return True
    else:
        return False
        


def marca_para_maria(data, nome, prontuario, telefone):
    dados = {'nome': nome, 'prontuario': prontuario, 'telefone':telefone}
    dados = json.dumps(dados)
    requisicao = requests.post(f'{link_banco}/medicos/especialidade/ginecologia/maria/pacientes/.json', \
    data=dados)
    #print(requisicao, "  ", requisicao.text)
    


    data['fulfillmentText'] = f"Ok Sr(a) {nome}, sua consulta para a Dra. Maria Aparecida foi marcada e seu prontuário é o {prontuario} e o telefone é o {telefone}. \n ATENÇÃO: Em breve entraremos em contato através do telefone informado para lhe informar o dia e a hora da sua consulta"

##################################################################################################
def verifica_vagas_renata():
    requisicao = requests.get(f'{link_banco}/.json')
    print("Requisição .json -->  ", requisicao.json())
    dic_pyt_requisicao = requisicao.json()
    print("Número de pacientes Clóvis: ", len(dic_pyt_requisicao["medicos"]["especialidade"]["nutricionista"]["renata"]["pacientes"]))
    pacientes_marcados = len(dic_pyt_requisicao["medicos"]["especialidade"]["nutricionista"]["renata"]["pacientes"])

    print("vagas Clóvis: ", dic_pyt_requisicao["medicos"]["especialidade"]["nutricionista"]["renata"]["vagas"])
    vagas = dic_pyt_requisicao["medicos"]["especialidade"]["nutricionista"]["renata"]["vagas"]
    if pacientes_marcados < vagas:
        return True
    else:
        return False
        


def marca_para_renata(data, nome, prontuario, telefone):
    dados = {'nome': nome, 'prontuario': prontuario, 'telefone':telefone}
    dados = json.dumps(dados)
    requisicao = requests.post(f'{link_banco}/medicos/especialidade/nutricionista/renata/pacientes/.json', \
    data=dados)
    #print(requisicao, "  ", requisicao.text)
    


    data['fulfillmentText'] = f"Ok Sr(a) {nome}, sua consulta para a Dra. Renata foi marcada e seu prontuário é o {prontuario} e o telefone é o {telefone}. \n ATENÇÃO: Em breve entraremos em contato através do telefone informado para lhe informar o dia e a hora da sua consulta"

##################################################################################################
def verifica_vagas_paulo():
    requisicao = requests.get(f'{link_banco}/.json')
    print("Requisição .json -->  ", requisicao.json())
    dic_pyt_requisicao = requisicao.json()
    print("Número de pacientes Clóvis: ", len(dic_pyt_requisicao["medicos"]["especialidade"]["pediatria"]["paulo"]["pacientes"]))
    pacientes_marcados = len(dic_pyt_requisicao["medicos"]["especialidade"]["pediatria"]["paulo"]["pacientes"])

    print("vagas Clóvis: ", dic_pyt_requisicao["medicos"]["especialidade"]["pediatria"]["paulo"]["vagas"])
    vagas = dic_pyt_requisicao["medicos"]["especialidade"]["pediatria"]["paulo"]["vagas"]
    if pacientes_marcados < vagas:
        return True
    else:
        return False
        


def marca_para_paulo(data, nome, prontuario, telefone):
    dados = {'nome': nome, 'prontuario': prontuario, 'telefone':telefone}
    dados = json.dumps(dados)
    requisicao = requests.post(f'{link_banco}/medicos/especialidade/pediatria/paulo/pacientes/.json', \
    data=dados)
    #print(requisicao, "  ", requisicao.text)
    


    data['fulfillmentText'] = f"Ok Sr(a) {nome}, sua consulta para o Dr. Paulo Maldonado foi marcada e seu prontuário é o {prontuario} e o telefone é o {telefone}. \n ATENÇÃO: Em breve entraremos em contato através do telefone informado para lhe informar o dia e a hora da sua consulta"

##################################################################################################
def verifica_vagas_manuelCrossetti():
    requisicao = requests.get(f'{link_banco}/.json')
    print("Requisição .json -->  ", requisicao.json())
    dic_pyt_requisicao = requisicao.json()
    print("Número de pacientes Clóvis: ", len(dic_pyt_requisicao["medicos"]["especialidade"]["reumatologia"]["manuel"]["pacientes"]))
    pacientes_marcados = len(dic_pyt_requisicao["medicos"]["especialidade"]["reumatologia"]["manuel"]["pacientes"])

    print("vagas Clóvis: ", dic_pyt_requisicao["medicos"]["especialidade"]["reumatologia"]["manuel"]["vagas"])
    vagas = dic_pyt_requisicao["medicos"]["especialidade"]["reumatologia"]["manuel"]["vagas"]
    if pacientes_marcados < vagas:
        return True
    else:
        return False
        


def marca_para_manuelCrossetti(data, nome, prontuario, telefone):
    dados = {'nome': nome, 'prontuario': prontuario, 'telefone':telefone}
    dados = json.dumps(dados)
    requisicao = requests.post(f'{link_banco}/medicos/especialidade/reumatologia/manuel/pacientes/.json', \
    data=dados)
    #print(requisicao, "  ", requisicao.text)
    


    data['fulfillmentText'] = f"Ok Sr(a) {nome}, sua consulta para o Dr. Manuel Crossetti foi marcada e seu prontuário é o {prontuario} e o telefone é o {telefone}. \n ATENÇÃO: Em breve entraremos em contato através do telefone informado para lhe informar o dia e a hora da sua consulta"
##################################################################################################
def verifica_vagas_fernando():
    requisicao = requests.get(f'{link_banco}/.json')
    print("Requisição .json -->  ", requisicao.json())
    dic_pyt_requisicao = requisicao.json()
    print("Número de pacientes Clóvis: ", len(dic_pyt_requisicao["medicos"]["especialidade"]["traumatologia"]["fernando"]["pacientes"]))
    pacientes_marcados = len(dic_pyt_requisicao["medicos"]["especialidade"]["traumatologia"]["fernando"]["pacientes"])

    print("vagas Clóvis: ", dic_pyt_requisicao["medicos"]["especialidade"]["traumatologia"]["fernando"]["vagas"])
    vagas = dic_pyt_requisicao["medicos"]["especialidade"]["traumatologia"]["fernando"]["vagas"]
    if pacientes_marcados < vagas:
        return True
    else:
        return False
        


def marca_para_fernando(data, nome, prontuario, telefone):
    dados = {'nome': nome, 'prontuario': prontuario, 'telefone':telefone}
    dados = json.dumps(dados)
    requisicao = requests.post(f'{link_banco}/medicos/especialidade/traumatologia/fernando/pacientes/.json', \
    data=dados)
    #print(requisicao, "  ", requisicao.text)
    


    data['fulfillmentText'] = f"Ok Sr(a) {nome}, sua consulta para o Dr. Fernando Barros foi marcada e seu prontuário é o {prontuario} e o telefone é o {telefone}. \n ATENÇÃO: Em breve entraremos em contato através do telefone informado para lhe informar o dia e a hora da sua consulta"

##################################################################################################
def verifica_vagas_fabricio():
    requisicao = requests.get(f'{link_banco}/.json')
    print("Requisição .json -->  ", requisicao.json())
    dic_pyt_requisicao = requisicao.json()
    print("Número de pacientes Clóvis: ", len(dic_pyt_requisicao["medicos"]["especialidade"]["urologia"]["fabricio"]["pacientes"]))
    pacientes_marcados = len(dic_pyt_requisicao["medicos"]["especialidade"]["urologia"]["fabricio"]["pacientes"])

    print("vagas Clóvis: ", dic_pyt_requisicao["medicos"]["especialidade"]["urologia"]["fabricio"]["vagas"])
    vagas = dic_pyt_requisicao["medicos"]["especialidade"]["urologia"]["fabricio"]["vagas"]
    if pacientes_marcados < vagas:
        return True
    else:
        return False
        


def marca_para_fabricio(data, nome, prontuario, telefone):
    dados = {'nome': nome, 'prontuario': prontuario, 'telefone':telefone}
    dados = json.dumps(dados)
    requisicao = requests.post(f'{link_banco}/medicos/especialidade/urologia/fabricio/pacientes/.json', \
    data=dados)
    #print(requisicao, "  ", requisicao.text)
    


    data['fulfillmentText'] = f"Ok Sr(a) {nome}, sua consulta para o Dr. Fabricio Lemos foi marcada e seu prontuário é o {prontuario} e o telefone é o {telefone}. \n ATENÇÃO: Em breve entraremos em contato através do telefone informado para lhe informar o dia e a hora da sua consulta"
##################################################################################################
def verifica_vagas_manoelAntunes():
    requisicao = requests.get(f'{link_banco}/.json')
    print("Requisição .json -->  ", requisicao.json())
    dic_pyt_requisicao = requisicao.json()
    print("Número de pacientes Clóvis: ", len(dic_pyt_requisicao["medicos"]["especialidade"]["urologia"]["manoel"]["pacientes"]))
    pacientes_marcados = len(dic_pyt_requisicao["medicos"]["especialidade"]["urologia"]["manoel"]["pacientes"])

    print("vagas Clóvis: ", dic_pyt_requisicao["medicos"]["especialidade"]["urologia"]["manoel"]["vagas"])
    vagas = dic_pyt_requisicao["medicos"]["especialidade"]["urologia"]["manoel"]["vagas"]
    if pacientes_marcados < vagas:
        return True
    else:
        return False
        


def marca_para_manoelAntunes(data, nome, prontuario, telefone):
    dados = {'nome': nome, 'prontuario': prontuario, 'telefone':telefone}
    dados = json.dumps(dados)
    requisicao = requests.post(f'{link_banco}/medicos/especialidade/urologia/manoel/pacientes/.json', \
    data=dados)
    #print(requisicao, "  ", requisicao.text)
    


    data['fulfillmentText'] = f"Ok Sr(a) {nome}, sua consulta para o Dr. Manoel Antunes foi marcada e seu prontuário é o {prontuario} e o telefone é o {telefone}. \n ATENÇÃO: Em breve entraremos em contato através do telefone informado para lhe informar o dia e a hora da sua consulta"

##################################################################################################
def verifica_vagas_marcosLemos():
    requisicao = requests.get(f'{link_banco}/.json')
    print("Requisição .json -->  ", requisicao.json())
    dic_pyt_requisicao = requisicao.json()
    print("Número de pacientes Clóvis: ", len(dic_pyt_requisicao["medicos"]["especialidade"]["urologia"]["marcos"]["pacientes"]))
    pacientes_marcados = len(dic_pyt_requisicao["medicos"]["especialidade"]["urologia"]["marcos"]["pacientes"])

    print("vagas Clóvis: ", dic_pyt_requisicao["medicos"]["especialidade"]["urologia"]["marcos"]["vagas"])
    vagas = dic_pyt_requisicao["medicos"]["especialidade"]["urologia"]["marcos"]["vagas"]
    if pacientes_marcados < vagas:
        return True
    else:
        return False
        


def marca_para_marcosLemos(data, nome, prontuario, telefone):
    dados = {'nome': nome, 'prontuario': prontuario, 'telefone':telefone}
    dados = json.dumps(dados)
    requisicao = requests.post(f'{link_banco}/medicos/especialidade/urologia/marcos/pacientes/.json', \
    data=dados)
    #print(requisicao, "  ", requisicao.text)
    


    data['fulfillmentText'] = f"Ok Sr(a) {nome}, sua consulta para o Dr. Marcos Lemos foi marcada e seu prontuário é o {prontuario} e o telefone é o {telefone}. \n ATENÇÃO: Em breve entraremos em contato através do telefone informado para lhe informar o dia e a hora da sua consulta"

##################################################################################################
def verifica_vagas_nehemias():
    requisicao = requests.get(f'{link_banco}/.json')
    print("Requisição .json -->  ", requisicao.json())
    dic_pyt_requisicao = requisicao.json()
    print("Número de pacientes Clóvis: ", len(dic_pyt_requisicao["medicos"]["especialidade"]["urologia"]["nehemias"]["pacientes"]))
    pacientes_marcados = len(dic_pyt_requisicao["medicos"]["especialidade"]["urologia"]["nehemias"]["pacientes"])

    print("vagas Clóvis: ", dic_pyt_requisicao["medicos"]["especialidade"]["urologia"]["nehemias"]["vagas"])
    vagas = dic_pyt_requisicao["medicos"]["especialidade"]["urologia"]["nehemias"]["vagas"]
    if pacientes_marcados < vagas:
        return True
    else:
        return False
        


def marca_para_nehemias(data, nome, prontuario, telefone):
    dados = {'nome': nome, 'prontuario': prontuario, 'telefone':telefone}
    dados = json.dumps(dados)
    requisicao = requests.post(f'{link_banco}/medicos/especialidade/urologia/nehemias/pacientes/.json', \
    data=dados)
    #print(requisicao, "  ", requisicao.text)
    


    data['fulfillmentText'] = f"Ok Sr(a) {nome}, sua consulta para o Dr. Nehemias Lemos foi marcada e seu prontuário é o {prontuario} e o telefone é o {telefone}. \n ATENÇÃO: Em breve entraremos em contato através do telefone informado para lhe informar o dia e a hora da sua consulta"

##################################################################################################


def vagas_preenchidas(data, nome):
    data['fulfillmentText'] = f"Ops! Sr.(a) {nome}, infelizmente as vagas já foram preenchidas para este(a) especialista.\n\
        para voltar ao início digite início"


app = Flask(__name__)

#.com/Marcacao/medicos/especialidade/clinicoGeral/danier/pacientes
@app.route('/')
def main():
    return render_template("index.html")

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json(silent=True)
    
    #print(data)
    intentName = data['queryResult']['intent']['displayName']
    nome = data['queryResult']['parameters']['nome']
    prontuario=data['queryResult']['parameters']['prontuario']
    telefone=data['queryResult']['parameters']['telefone']

##########################################################################
    if intentName == "1 - marcacao - 1 clinicogeral - 1 danier":
        if verifica_vagas_danier() == True:
            marca_para_danier(data, nome, prontuario, telefone)
        else:
            vagas_preenchidas(data, nome)
############################################################################       
    if intentName == "1 - marcacao - 1 clinicogeral - 2 jorge":
        if verifica_vagas_jorge() == True:
            marca_para_jorge(data, nome, prontuario, telefone)
        else:
            vagas_preenchidas(data, nome)
############################################################################       
    if intentName == "2 - marcacao - 2 cardiologia - 1 fabio":
        if verifica_vagas_fabio() == True:
            marca_para_fabio(data, nome, prontuario, telefone)
        else:
            vagas_preenchidas(data, nome)
############################################################################       
    if intentName == "2 - marcacao - 2 cardiologia - 2 felipe":
        if verifica_vagas_felipe() == True:
            marca_para_felipe(data, nome, prontuario, telefone)
        else:
            vagas_preenchidas(data, nome)
############################################################################       
    if intentName == "2 - marcacao - 3 angiologia - 1 clovis":
        if verifica_vagas_clovis() == True:
            marca_para_clovis(data, nome, prontuario, telefone)
        else:
            vagas_preenchidas(data, nome)
############################################################################       
    if intentName == "2 - marcacao - buco - 1 flavioMonteiro":
        if verifica_vagas_flavioMonteiro() == True:
            marca_para_flavioMonteiro(data, nome, prontuario, telefone)
        else:
            vagas_preenchidas(data, nome)
############################################################################       
    if intentName == "2 - marcacao - buco - 2 flavioSpohde":
        if verifica_vagas_flavioSpohde() == True:
            marca_para_flavioSpohde(data, nome, prontuario, telefone)
        else:
            vagas_preenchidas(data, nome)
############################################################################       
    if intentName == "2 - marcacao - 5 dermato - 1 michele":
        if verifica_vagas_michele() == True:
            marca_para_michele(data, nome, prontuario, telefone)
        else:
            vagas_preenchidas(data, nome)
############################################################################       
    if intentName == "2 - marcacao - 6 gastroenterologia - 1 roberto":
        if verifica_vagas_roberto() == True:
            marca_para_roberto(data, nome, prontuario, telefone)
        else:
            vagas_preenchidas(data, nome)
############################################################################       
    if intentName == "2 - marcacao - 7 ginecologia - 1 caroline":
        if verifica_vagas_caroline() == True:
            marca_para_caroline(data, nome, prontuario, telefone)
        else:
            vagas_preenchidas(data, nome)
############################################################################       
    if intentName == "2 - marcacao - 7 ginecologia - 2 maria":
        if verifica_vagas_maria() == True:
            marca_para_maria(data, nome, prontuario, telefone)
        else:
            vagas_preenchidas(data, nome)
############################################################################       
    if intentName == "2 - marcacao - 8 Nutricionista - 1 renata":
        if verifica_vagas_renata() == True:
            marca_para_renata(data, nome, prontuario, telefone)
        else:
            vagas_preenchidas(data, nome)
############################################################################       
    if intentName == "2 - marcacao - 9 pediatria - 1 paulo":
        if verifica_vagas_paulo() == True:
            marca_para_paulo(data, nome, prontuario, telefone)
        else:
            vagas_preenchidas(data, nome)
############################################################################       
    if intentName == "2 - marcacao - 10 Reumatologia - 1 manuel":
        if verifica_vagas_manuelCrossetti() == True:
            marca_para_manuelCrossetti(data, nome, prontuario, telefone)
        else:
            vagas_preenchidas(data, nome)
############################################################################       
    if intentName == "2 - marcacao - 11 traumatologia - 1 fernando":
        if verifica_vagas_fernando() == True:
            marca_para_fernando(data, nome, prontuario, telefone)
        else:
            vagas_preenchidas(data, nome)
############################################################################       
    if intentName == "2 - marcacao - 12 urologia - 1 fabricio":
        if verifica_vagas_fabricio() == True:
            marca_para_fabricio(data, nome, prontuario, telefone)
        else:
            vagas_preenchidas(data, nome)
############################################################################       
    if intentName == "2 - marcacao - 12 urologia - 2 manoel antunes":
        if verifica_vagas_manoelAntunes() == True:
            marca_para_manoelAntunes(data, nome, prontuario, telefone)
        else:
            vagas_preenchidas(data, nome)
############################################################################       
    if intentName == "2 - marcacao - 12 urologia - 3 marcos lemos":
        if verifica_vagas_marcosLemos() == True:
            marca_para_marcosLemos(data, nome, prontuario, telefone)
        else:
            vagas_preenchidas(data, nome)
############################################################################       
    if intentName == "2 - marcacao - 12 urologia - 4 nehemias lemos":
        if verifica_vagas_nehemias() == True:
            marca_para_nehemias(data, nome, prontuario, telefone)
        else:
            vagas_preenchidas(data, nome)
############################################################################
    print("Print", jsonify(data))
    return jsonify(data)

# run Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)