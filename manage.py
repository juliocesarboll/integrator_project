from app import app
from app.models import Equipamento
from flask import request, render_template, jsonify

class Caixa:
   def __init__(self, nome, descricao, valor):
      self.nome = nome
      self.descricao = descricao
      self.valor = valor

caixas = []

@app.route('/')
def login():
   return render_template('login.html')

@app.route('/', methods=['POST'])
def toHome():
   return render_template('home.html', valorCaixa = len(caixas))

@app.route('/home')
def home():
   return render_template('home.html', valorCaixa = len(caixas))

@app.route('/cadastro')
def cadastrarCaixa():
   caixa1 = Caixa(request.args.get('nome', ''), request.args.get('descricao', ''), request.args.get('valor', ''))
   caixas.append(caixa1)

   return jsonify({"data": "success"})

@app.route('/cadastra-caixa')
def cadastroCaixa():
   return render_template('cadastro.html')

@app.route('/exit')
def exit():
   return render_template('login.html')

@app.route('/search-caixa')
def searchCaixa():
   descricao = request.args.get('descricao', '')
   resultados = search(descricao)

   return resultados

def populaCaixa():
   caixa = []
   for x in range(1,5):
      caixas.append(Caixa("Caixa {x}", "Caixote", 12.99))

   for x in range(1,5):
      caixas.append(Caixa("Caixa {x}", "Degrau", 10.99))

def search(palavra_chave):
   resultados = [caixa.__dict__ for caixa in caixas if palavra_chave.lower() in caixa.descricao.lower()]

   return resultados

if __name__ == "__main__":
   app.run(host='0.0.0.0')