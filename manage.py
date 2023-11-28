from app import app
from app.models import Equipamento
from flask import request, render_template

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

@app.route('/cadastrar-caixa')
def cadastrarCaixa():
   caixa1 = Caixa(request.form['name'], request.form['descricao'], request.form['valor'])
   caixas.extend(caixa1)

   return render_template('home.html', valorCaixa = len(caixas))

@app.route('/cadastro-caixa')
def cadastroCaixa():
   return render_template('cadastro.html')

@app.route('/exit')
def exit():
   return render_template('login.html')

@app.route('/search-caixa/<palavra_chave>')
def searchCaixa(palavra_chave):
   dados = request.get_json()
   resultados = search(palavra_chave)

   return render_template('home.html', valorCaixa = len(caixas), resultado = resultados)

def search(palavra_chave):
   resultados = [caixa.__dict__ for caixa in caixas if palavra_chave.lower() in caixa.descricao.lower()]

   return resultados

if __name__ == "__main__":
   app.run(host='0.0.0.0')