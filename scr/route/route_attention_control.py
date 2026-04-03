from flask import Blueprint, render_template
from scr.models.model_Attention_control import model_Attention_Control
main = Blueprint('attention_ctrl_bp',__name__)
#select
@main.route('/')
def index():
    data=model_Attention_Control.get_attention_control_list()
    #print(data)
    return render_template('index.html',attention=data)

#insert
@main.route('/insert',methods=['POST'])
def insert():
    return render_template('index.html', attention=data)


#update
@main.route('/update',methods=['POST'])
def update():
    return render_template('index.html', attention=data)


#delete
@main.route('/delete/<string:id>')
def delete():
    return render_template('index.html', attention=data)
