import mysql.connector


#DB MYSQL
def get_connection():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="attention_control"
        )

    except mysql.connector.Error as err:
        raise err

