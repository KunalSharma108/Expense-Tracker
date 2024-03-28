import mysql.connector
import getDB
import getTTB
import time
import Nametime
import dateCount
from tabulate import tabulate

tb_name = getDB.getDate()


async def add_item():
    error_count = 0

    try:
        while True:
            try:
                day = input("Enter the date of the data you want to view : ")
                month = input(
                    "Enter the number of the month of the data you want to view : "
                )
                year = input("Enter the year of the data you want to view : ")
                try:
                    month = Nametime.nameMonth(int(month))

                except Exception as e:
                    error_count += 1
                    print(f"there was an error : {e}")
                    if error_count == 4:
                        print("Process interrupted because of too many errors...")
                        time.sleep(0.5)
                        print("\nRedirecting back to the menu...")
                        time.sleep(1.7)
                        break

                tb_name = f"{day}_{month}_{year}"

                result = await getTTB.check_tb(tb_name)
                print("\n")

                if result == True:
                    try:
                        mydb = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            password="",
                            database="expense_tracker",
                        )

                        item_name = input("Enter the name of the item : ")
                        item_quantity = input(
                            "Enter the quantity of the item purchased : "
                        )
                        item_price = input(
                            "Enter the price of one single item purchased : "
                        )

                        if not (item_name and item_quantity and item_price):
                            print("Any input can't be empty.")

                        else:
                            try:
                                row_count = await getTTB.getRow(tb_name)
                                total_price = int(item_quantity) * int(item_price)

                                print("adding data to the database...")
                                time.sleep(1)

                                add_command = f'INSERT INTO `{tb_name}` VALUES ({str(row_count + 1)}, "{item_name}", {item_quantity}, {item_price}, {total_price})'
                                mycursor = mydb.cursor()
                                mycursor.execute(add_command)
                                mydb.commit()

                                print("\nTask completed")
                                time.sleep(0.5)
                                print("\nredirecting back to menu.....")

                                time.sleep(1)
                                break

                            except mysql.connector.Error as e:
                                error_count += 1
                                print(f"There was an error: {e}")
                                if error_count == 4:
                                    print(
                                        "Process interrupted because of too many errors"
                                    )
                                    time.sleep(1.7)
                                    break

                    except Exception as e:

                        error_count += 1
                        print(f"There was an error: {e}")
                        if error_count == 4:
                            print("Process interrupted because of too many errors")
                            time.sleep(1.7)
                            break
                elif result == False :
                    print('Table doesnt exist')
                    print('\n')
                    
                    error_count += 1
                    if error_count == 4:
                        print("Process interrupted because of too many errors...")
                        time.sleep(0.5)
                        print("\nRedirecting back to the menu...")
                        time.sleep(1.7)
                        break

            except Exception as e:
                error_count += 1
                print(f"there was an error : {e}")
                if error_count == 4:
                    print("Process interrupted because of too many errors...")
                    time.sleep(0.5)
                    print("\nRedirecting back to the menu...")
                    time.sleep(1.7)
                    break

    except Exception as e:
        error_count += 1
        print(f"there was an error : {e}")
        if error_count == 4:
            print("Process interrupted because of too many errors...")
            time.sleep(0.5)
            print("\nRedirecting back to the menu...")
            time.sleep(1.7)
    
    mydb.close()



async def delete_item():
    error_count = 1

    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="expense_tracker",
        )

        while True:
            try:
                day = input("Enter the date of the data you want to view : ")
                month = input(
                    "Enter the number of the month of the data you want to view : "
                )
                year = input("Enter the year of the data you want to view : ")
                try:
                    month = Nametime.nameMonth(int(month))

                except Exception as e:
                    error_count += 1
                    print(f"there was an error : {e}")
                    if error_count == 4:
                        print("Process interrupted because of too many errors...")
                        time.sleep(0.5)
                        print("\nRedirecting back to the menu...")
                        time.sleep(1.7)
                        break

                tb_name = f"{day}_{month}_{year}"

                result = await getTTB.check_tb(tb_name)
                print("\n")

                if result == True:
                    item_no = input(
                        "Enter the item_no of the item you want to delete: "
                    )

                    if item_no.isdigit():
                        choice = input(
                            "\nAre you sure you want to delete the item from the database forever? (y/n): "
                        )

                        if choice.lower() == "n":
                            print("Cancelling the process...")
                            time.sleep(0.7)
                            break

                        elif choice.lower() == "y":
                            print("Deleting the item...")
                            print(
                                "\nNote - if the Item No. doesnt exist it will not return any error."
                            )

                            time.sleep(1.5)

                            try:

                                command = f"DELETE FROM `{tb_name}` WHERE `Item_no` = {int(item_no)};"
                                mycursor = mydb.cursor()
                                mycursor.execute(command)
                                mydb.commit()

                                print("The item has been deleted.")
                                time.sleep(0.5)
                                print("\nRedirecting back to the menu...")
                                time.sleep(1.7)
                                break

                            except Exception as e:
                                error_count += 1
                                print(f"there was an error : {e}")
                                if error_count == 4:
                                    print(
                                        "Process interrupted because of too many errors..."
                                    )
                                    time.sleep(0.5)
                                    print("\nRedirecting back to the menu...")
                                    time.sleep(1.7)
                                    break

                        else:
                            print("Invalid input.")
                            error_count += 1
                            if error_count == 4:
                                print(
                                    "Process interrupted because of too many errors..."
                                )
                                time.sleep(0.5)
                                print("\nRedirecting back to the menu...")
                                time.sleep(1.7)
                                break
                    else:
                        print(
                            "Invalid item number format. Please enter a valid integer."
                        )
                        error_count += 1
                        if error_count == 4:
                            print("Process interrupted because of too many errors...")
                            time.sleep(0.5)
                            print("\nRedirecting back to the menu...")
                            time.sleep(1.7)
                            break
                else:
                    print("the table doesnt exist try again...")
                    error_count += 1
                    if error_count == 4:
                        print("Process interrupted because of too many errors...")
                        time.sleep(0.5)
                        print("\nRedirecting back to the menu...")
                        time.sleep(1.7)
                        break

            except Exception as e:
                error_count += 1
                print(f"there was an error : {e}")
                if error_count == 4:
                    print("Process interrupted because of too many errors...")
                    time.sleep(0.5)
                    print("\nRedirecting back to the menu...")
                    time.sleep(1.7)
                    break

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        mydb.close()


async def change_data():
    error_count = 0
    try:
        while True:
            try:
                day = input("Enter the date of the data you want to change : ")
                month = input(
                    "Enter the number of the month of the data you want to change : "
                )
                year = input("Enter the year of the data you want to change : ")
                try:
                    month = Nametime.nameMonth(int(month))

                except Exception as e:
                    error_count += 1
                    print(f"there was an error : {e}")
                    if error_count == 4:
                        print("Process interrupted because of too many errors...")
                        time.sleep(0.5)
                        print("\nRedirecting back to the menu...")
                        time.sleep(1.7)
                        break

                tb_name = f"{day}_{month}_{year}"

                result = await getTTB.check_tb(tb_name)

                if result == True:
                    print("Opening Table....")
                    time.sleep(0.5)

                    print("\n  \n \n")
                    print(f"-----------------------------------------")
                    print(f"1. Name of Item.")
                    print(f"-----------------------------------------")
                    print(f"2. Quantity of the Item.")
                    print(f"-----------------------------------------")
                    print(f"3. Price of the Item.")
                    print(f"-----------------------------------------")

                    Choice = input("Enter Your Choice : ") or None
                    item_no = input("Enter the item_no of that Item : ") or None
                    new_value = input("Enter the New Value : ") or None

                    if (
                        Choice != None
                        and item_no != None
                        and new_value != None
                        and int(item_no)
                    ):
                        try:
                            mydb = mysql.connector.connect(
                                host="localhost",
                                user="root",
                                password="",
                                database="expense_tracker",
                            )

                            cursor = mydb.cursor()

                            if Choice == "1":
                                command = f"UPDATE `{tb_name}` SET `Item_name` = '{new_value}' WHERE Item_no = {item_no};"
                                cursor.execute(command)
                                print("Changed Item Name")
                                time.sleep(0.5)
                                print("\nRedirecting back to the menu...")
                                time.sleep(1.7)
                                break

                            elif Choice == "2":
                                command = f"UPDATE `{tb_name}` SET `Item_quantity` = '{new_value}' WHERE Item_no = {item_no};"
                                cursor.execute(command)
                                print("Changed Item quantity")
                                time.sleep(0.5)
                                print("\nRedirecting back to the menu...")
                                time.sleep(1.7)
                                break

                            elif Choice == "3":
                                command = f"UPDATE `{tb_name}` SET `Item_price` = '{new_value}' WHERE Item_no = {item_no};"
                                cursor.execute(command)

                                print("Changed Item price")
                                time.sleep(0.5)
                                print("\nRedirecting back to the menu...")
                                time.sleep(1.7)
                                break

                            else:
                                error_count += 1
                                print(f"Invalid input")
                                if error_count == 4:
                                    print(
                                        "Process interrupted because of too many errors..."
                                    )
                                    time.sleep(0.5)
                                    print("\nRedirecting back to the menu...")
                                    time.sleep(1.7)
                                    break

                        except Exception as e:
                            error_count += 1
                            print(f"there was an error : {e}")
                            if error_count == 4:
                                print(
                                    "Process interrupted because of too many errors..."
                                )
                                time.sleep(0.5)
                                print("\nRedirecting back to the menu...")
                                time.sleep(1.7)
                                break

                        finally:
                            cursor.execute(
                                f"UPDATE `{tb_name}` SET `Total_price` = `Item_quantity` * `Item_price` ;"
                            )
                            mydb.commit()
                            mydb.close()

                    else:
                        error_count += 1
                        print(f"there was an error")
                        if error_count == 4:
                            print("Process interrupted because of too many errors...")
                            time.sleep(0.5)
                            print("\nRedirecting back to the menu...")
                            time.sleep(1.7)
                            break

                elif result == False:
                    error_count += 1
                    print("Table doesnt exst")
                    if error_count == 4:
                        print("Process interrupted because of too many errors...")
                        time.sleep(0.5)
                        print("\nRedirecting back to the menu...")
                        time.sleep(1.7)
                        break

                else:
                    print("Table doesnt exst")
                    error_count += 1
                    if error_count == 4:
                        print("Process interrupted because of too many errors...")
                        time.sleep(0.5)
                        print("\nRedirecting back to the menu...")
                        time.sleep(1.7)
                        break

            except Exception as e:
                error_count += 1
                print(f"there was an error : {e}")
                if error_count == 4:
                    print("Process interrupted because of too many errors...")
                    time.sleep(0.5)
                    print("\nRedirecting back to the menu...")
                    time.sleep(1.7)
                    break

    except Exception as e:
        error_count += 1
        print(f"there was an error : {e}")
        if error_count == 4:
            print("Process interrupted because of too many errors...")
            time.sleep(0.5)
            print("\nRedirecting back to the menu...")
            time.sleep(1.7)


async def total():
    error_count = 0
    try:
        while True:
            try:
                print(
                    "To calculate your expenses, please provide the start and end dates."
                )

                print("\n\nGive the Following data of start dates : ")
                start_date = int(input("\nEnter the Starting date : "))
                start_month = int(input("\nEnter the starting month : "))
                start_year = int(input("\nEnter the starting year : "))

                print("\n\nGive the following data of end dates : ")
                end_date = int(input("\nEnter ending date : "))
                end_month = int(input("\nEnter ending month : "))
                end_year = int(input("\nEnter endin year : "))

                full_starting_date = f"{start_date}_{start_month}_{start_year}"
                full_ending_date = f"{end_date}_{end_month}_{end_year}"

                try:
                    full_date_list = await dateCount.dateCount(
                        full_starting_date, full_ending_date
                    )

                except Exception as e:
                    error_count += 1
                    print(f"there was an error : {e}")
                    if error_count == 4:
                        print("Process interrupted because of too many errors...")
                        time.sleep(0.5)
                        print("\nRedirecting back to the menu...")
                        time.sleep(1.7)
                        break

                try:
                    print("\nfetching data...")
                    time.sleep(1.5)

                    mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="expense_tracker",
                    )

                    cursor = mydb.cursor()
                    rows = []

                    for dates in full_date_list:
                        try:
                            cursor.execute(f"SELECT * FROM {dates};")

                            row = cursor.fetchall()
                            rows.append(row)

                        except Exception as e:
                            pass

                    total_expense = 0
                    total_items = 0
                    total_quantity = 0

                    for row in rows:
                        try:
                            for i in row:
                                total_expense += i[4]
                                total_items += 1
                                total_quantity += i[2]

                        except Exception as e:
                            print(f"There was an error : {e}")

                    print("\nAlmost done...")
                    time.sleep(0.7)
                    print("\nCalculating Data")
                    time.sleep(0.4)

                    print("\n  \n \n")
                    print(
                        f"-----------------------------------------------------------------------------"
                    )
                    print(
                        f"---------------This Data Shows The Stats Of Past {len(rows)} Day(s).-------------------"
                    )
                    print(
                        f"-----------------------------------------------------------------------------"
                    )
                    print(f"1. Your Total Spending Was : {total_expense}")
                    print(
                        f"-----------------------------------------------------------------------------"
                    )
                    print(
                        f"2. Your Average Spending Per Day Is : {total_expense / len(rows)}"
                    )
                    print(
                        f"-----------------------------------------------------------------------------"
                    )
                    print(f"3. Your Total Items Purchased Are : {total_items}")
                    print(
                        f"-----------------------------------------------------------------------------"
                    )
                    print(
                        f"4. Your Average Items Brought Per Day Is : {total_items / len(rows)}"
                    )
                    print(
                        f"-----------------------------------------------------------------------------"
                    )
                    print(f"5. Your Total Quanitity Purchased Is : {total_quantity}")
                    print(
                        f"-----------------------------------------------------------------------------"
                    )
                    print(
                        f"6. Your Average Quantity Brought Per Day Is : {total_quantity / len(rows)}"
                    )
                    print(
                        f"-----------------------------------------------------------------------------"
                    )

                    mydb.close()

                    input("Press Enter to continue......")

                    print("\n\nredirecting back to meny , Please Wait.....")
                    time.sleep(1.2)
                    break

                except Exception as e:
                    error_count += 1
                    print(f"there was an error : {e}")
                    if error_count == 4:
                        print("Process interrupted because of too many errors...")
                        time.sleep(0.5)
                        print("\nRedirecting back to the menu...")
                        time.sleep(1.7)
                        break

            except Exception as e:
                error_count += 1
                print(f"there was an error : {e}")
                if error_count == 4:
                    print("Process interrupted because of too many errors...")
                    time.sleep(0.5)
                    print("\nRedirecting back to the menu...")
                    time.sleep(1.7)
                    break

    except Exception as e:
        error_count += 1
        print(f"there was an error : {e}")
        if error_count == 4:
            print("Process interrupted because of too many errors...")
            time.sleep(0.5)
            print("\nRedirecting back to the menu...")
            time.sleep(1.7)


async def view():
    error_count = 0
    try:
        while True:
            try:
                day = input("Enter the date of the data you want to view : ")
                month = input(
                    "Enter the number of the month of the data you want to view : "
                )
                year = input("Enter the year of the data you want to view : ")
                try:
                    month = Nametime.nameMonth(int(month))

                except Exception as e:
                    error_count += 1
                    print(f"there was an error : {e}")
                    if error_count == 4:
                        print("Process interrupted because of too many errors...")
                        time.sleep(0.5)
                        print("\nRedirecting back to the menu...")
                        time.sleep(1.7)
                        break

                tb_name = f"{day}_{month}_{year}"

                result = await getTTB.check_tb(tb_name)

                if result == True:
                    print("Opening Table....")
                    time.sleep(0.5)

                    try:
                        mydb = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            password="",
                            database="expense_tracker",
                        )
                        mycursor = mydb.cursor()

                        mycursor.execute(f"SELECT * FROM `{tb_name}`;")

                        table_data = mycursor.fetchall()

                        headers = [
                            "Item No.",
                            "Item Name",
                            "Item Quantity",
                            "Item Price",
                            "Total",
                        ]
                        print("\n\n")
                        print(tabulate(table_data, headers=headers, tablefmt="grid"))

                        input("Press Enter to proceed......")
                        print("\nRedirecting back to the menu...")
                        time.sleep(1.7)
                        break

                    except Exception as e:
                        error_count += 1
                        print(f"there was an error : {e}")
                        if error_count == 4:
                            print("Process interrupted because of too many errors...")
                            time.sleep(0.5)
                            print("\nRedirecting back to the menu...")
                            time.sleep(1.7)
                            break

                elif result == False:
                    print("\nError : The Table doesnt exist.")
                    error_count += 1
                    if error_count == 4:
                        print("Process interrupted because of too many errors...")
                        time.sleep(0.5)
                        print("\nRedirecting back to the menu...")
                        time.sleep(1.7)
                        break

            except Exception as e:
                error_count += 1
                print(f"there was an error : {e}")
                if error_count == 4:
                    print("Process interrupted because of too many errors...")
                    time.sleep(0.5)
                    print("\nRedirecting back to the menu...")
                    time.sleep(1.7)
                    break

    except Exception as e:
        error_count += 1
        print(f"there was an error : {e}")
        if error_count == 4:
            print("Process interrupted because of too many errors...")
            time.sleep(0.5)
            print("\nRedirecting back to the menu...")
            time.sleep(1.7)


async def choose():
    try:
        while True:
            print("\n\nChoose from the options below : ")
            print("\n")
            print(f"-----------------------------------------")
            print(f"1. Add an item.")
            print(f"-----------------------------------------")
            print(f"2. Delete an item.")
            print(f"-----------------------------------------")
            print(f"3. change a data of an item.")
            print(f"-----------------------------------------")
            print(f"4. Find the total expense.")
            print(f"-----------------------------------------")
            print(f"5. View the Table of a specefic date.")
            print(f"-----------------------------------------")
            print(f"6. Quite the program.")
            print(f"-----------------------------------------")
            Choice = input("Enter Your Choice : ")

            if Choice == "1":
                print("please wait..")
                time.sleep(1.5)
                await add_item()

            elif Choice == "2":
                print("please wait..")
                time.sleep(1.5)
                await delete_item()

            elif Choice == "3":
                print("please wait..")
                time.sleep(1.5)
                await change_data()

            elif Choice == "4":
                print("please wait..")
                time.sleep(1.5)
                await total()

            elif Choice == "5":
                print("please wait..")
                time.sleep(1.5)
                await view()

            elif Choice == "6":
                break
            else:
                print("Invalid input, try again")

    except Exception as e:
        print(f"there was an error : {e}")


async def start():
    try:
        tables = await getTTB.getTables()
        if tb_name in tables:
            await choose()

        elif tb_name not in tables:
            try:
                print("Setting up....")
                time.sleep(0.9)
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="expense_tracker",
                )
                mycursor = mydb.cursor()

                mycursor.execute(
                    f"CREATE TABLE {tb_name} (Item_no INT UNIQUE, Item_name VARCHAR(255), Item_quantity INT, Item_price INT, Total_price INT)"
                )

                print("Set up Done..")
                print("Starting..")
                time.sleep(1.4)
                await choose()
            except:
                print("there was an error")
    except:
        print("There was an error")


if __name__ == "__main__":
    import asyncio

    asyncio.run(start())
