from flask import Flask
from config import config
from scr.models.model_Attention_control import model_Attention_Control
from scr.route import route_attention_control
app = Flask(__name__)

if __name__ == "__main__":
    #model_Attention_Control.get_attention_control_list()
    app.config.from_object(config['development'])

    #blueprint
    app.register_blueprint(route_attention_control.main, url_prefix='/')

    app.run()