from flask import Flask
from controllers import tarefas_controller

app = Flask(__name__)
app.register_blueprint(tarefas_controller)

if __name__=="__main__":
    app.run(debug=True)