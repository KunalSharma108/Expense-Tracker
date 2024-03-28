import mysql.connector


async def getTables():
    try:
        mydb = mysql.connector.connect(
            host="localhost", user="root", password="", database="expense_tracker"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SHOW TABLES")
        tables = mycursor.fetchall()

        real_tables = []

        for table in tables:
            for i in table:
                real_tables.append(i)

        return real_tables
    except:
        print("there was an error")


async def getRow(tb_name):
    try:
        mydb = mysql.connector.connect(
            host="localhost", user="root", password="", database="expense_tracker"
        )
        mycursor = mydb.cursor()
        mycursor.execute(f"SELECT MAX(`Item_no`) FROM `{tb_name}`")
        rows = mycursor.fetchall()

        if rows[0][0] == None:
            return int('0')
        else:
            return int(rows[0][0])
        

    except:
        return "there was an error"


async def check_item_no(item_no, tb_name):
    try:
        mydb = mysql.connector.connect(
            host="localhost", user="root", password="", database="expense_tracker"
        )
        mycursor = mydb.cursor()
        mycursor.execute(f"SELECT * FROM {tb_name} WHERE `Item_no` = {item_no}")
        rows = mycursor.fetchall()

        return len(rows) == 1 

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False 

    finally:
        mycursor.close()
        mydb.close()


async def check_tb(tb_name):
    try:
        mydb = mysql.connector.connect(
            host="localhost", user="root", password="", database="expense_tracker"
        )
        mycursor = mydb.cursor()
        mycursor.execute(f"SELECT * FROM `{tb_name}`")
        tables = mycursor.fetchall()

        if tables:
            return True

    except mysql.connector.Error as err:
        return False

    finally:
        mycursor.close()
        mydb.close()