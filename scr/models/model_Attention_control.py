from scr.db.dbconnect import *

class model_Attention_Control:
    @classmethod #convierte una funcion para que sea el metodo de clase
    #llamar
    def get_attention_control_list(cls):
        connection = get_connection()
        with connection.cursor() as cursor:
            SQL="SELECT ID, FECHA, NOMBRES, HORA_INGRESO, HORA_SALIDA, POLO_GIFT, KEYCHAIN_GIFT, CATALOG_BOOK   FROM Attention_Control"
            cursor.execute(SQL)

            listattention_ctrl = cursor.fetchall()
            connection.close()
            #print (listattention_ctrl)
            return listattention_ctrl

    #insertar
    @classmethod
    def add_attention_control(cls,attention_control):
        connection = get_connection()
        with connection.cursor() as cursor:
            SQLINSERT="INSERT INTO Attention_Control(FECHA,NOMBRES, HORA_INGRESO, HORA_SALIDA, POLO_GIFT, KEYCHAIN_GIFT, CATALOG_BOOK)"\
                    "VALUES(%s,%s,%s,%s,%s,%s,%s)"#SQLINJECTION EVITA LA OCNSULTA PARAMETRISADSA
            values = (attention_control.fecha, attention_control.nombres,
                      attention_control.hora_ingreso, attention_control.hora_salida,
                      attention_control.polo_gift, attention_control.keychain_gift,
                      attention_control.catalog_book)
            cursor.execute(SQLINSERT,values)
            affected_row = cursor.rowcount
            connection.commit()
        return affected_row

    #actualizar
    @classmethod
    def update_attention_control(cls,attention_control):
        connection = get_connection()
        with connection.cursor() as cursor:
            SQLUPDATE="UPDATE Attention_Control SET FECHA=%s,NOMBRES=%s, HORA_INGRESO=%s, HORA_SALIDA=%s, POLO_GIFT=%s, KEYCHAIN_GIFT=%s, CATALOG_BOOK=%s WHERE ID=%s"
            values =(attention_control.fecha, attention_control.nombres,
                      attention_control.hora_ingreso, attention_control.hora_salida,
                      attention_control.polo_gift, attention_control.keychain_gift,
                      attention_control.catalog_book,attention_control.id)
            cursor.execute(SQLUPDATE,values)
            connection.commit()#confirmar los cambios

    #eliminar
    @classmethod
    def delete_attention_control(cls,id):
        connection = get_connection()
        with connection.cursor() as cursor:
            SQLDelete ="DELETE FROM Attention_Control WHERE ID=%s"
            cursor.execute(SQLDelete,(id,))
            affected_row = cursor.rowcount
            connection.commit()
        return affected_row