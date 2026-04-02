from scr.models.entities.Attention_Control import Attention_control
from scr.models.model_Attention_control import model_Attention_Control


#attention_control = Attention_control("2026-04-02","luis giraldo","10:18:00","12:18:45",True,True,"Si")
#model_Attention_Control.add_attention_control(attention_control)

#probar update
#attention_control = Attention_control("2026-04-02","luis garcia","10:18:00","12:18:45",False,False,"Si",23)
#model_Attention_Control.update_attention_control(attention_control)
#probar delete

model_Attention_Control.delete_attention_control(23)
print("dato eliminado")