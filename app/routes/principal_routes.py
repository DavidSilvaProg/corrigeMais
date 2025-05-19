from flask import Blueprint, render_template, request, redirect, url_for, session

bp_tarefa = Blueprint('tarefa', __name__)

#Página inicial
@bp_tarefa.route('/')
def index():
    return redirect(url_for("tarefa.cadastarTarefa"))

#Página de solicitações de compra
@bp_tarefa.route('/cadastarTarefa')
def cadastarTarefa():
    return render_template('cadastraTarefa.html')