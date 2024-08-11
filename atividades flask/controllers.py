from flask import Blueprint, render_template, request, redirect, url_for
from models import tarefas, addTarefa

tarefas_controller = Blueprint('tarefa', __name__)

@tarefas_controller.route('/')
def index():
    return render_template('index.html', tarefas=tarefas)


@tarefas_controller.route('/add', methods=['POST'])
def add():
    descricao = request.form['descricao']
    addTarefa(descricao)
    return redirect(url_for('tarefa.index'))
