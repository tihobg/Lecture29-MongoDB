import pymongo


import pandas as pd
from ui import enter_user_account, buy_car_part_mongo

# mongo_client = connect_to_mongo_local_cluster()
# # account_data = mongo_client.accounts_find({}, {"_id": 0})
# print(mongo_client["name"], mongo_client["password"])

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client.python_course


print('Welcome to our car store!')
main_question = input('Do you want to enter the car store?\n')
while main_question == 'yes':
    reg_question = input('Do you have a registration?\n')
    if reg_question == 'yes':
        user_account = enter_user_account()
        if user_account[0] == "admin" and user_account[1] == "admin":
            print('This is MONGO administrator account?\n')

            all_records = db.accounts.find({}, {"_id": 0, "linenumber": 0})
            list_cursor = list(all_records)
            table_accounts = pd.DataFrame(list_cursor)
            print(table_accounts)

            edit_option = input("Do you want to edit anyone of the users' accounts?\n")
            while edit_option == "yes":
                edit_user_name = input("Please, enter the name for edit!\n")

                db.accounts.update_one(
                    {"name": edit_user_name},
                    {
                        "$set":
                            {
                                "name": input('Please, enter the new name or enter the old one!\n'),
                                "password": input('Please, enter the new password or enter the old one!\n'),
                                "usertype": input('Please, enter the new user type or enter the old one!\n')
                            }
                    }
                )

                all_records = db.accounts.find({}, {"_id": 0, "linenumber": 0})
                list_cursor = list(all_records)
                table_accounts = pd.DataFrame(list_cursor)
                print(table_accounts)

                delete_user = input('Do you want to delete any user?\n')
                if delete_user == 'yes':
                    # doc_num = delete_data_mongo()
                    delete_user_name = input("Please, enter the name to delete mongo!\n")
                    db.accounts.delete_one({"name": delete_user_name})

                all_records = db.accounts.find({}, {"_id": 0, "linenumber": 0})
                list_cursor = list(all_records)
                table_accounts = pd.DataFrame(list_cursor)
                print(table_accounts)

                add_user = input('Do you want to add a new user?\n')
                if add_user == 'yes':
                    add_new_account = enter_user_account()
                    db.accounts.insert_one(
                        {
                            # "linenumber": db.accounts.count_documents({}) + 1,
                            "name": add_new_account[0],
                            "password": add_new_account[1],
                            "usertype": "reguser"
                        }
                    )
                all_records = db.accounts.find({}, {"_id": 0, "linenumber": 0})
                list_cursor = list(all_records)
                table_accounts = pd.DataFrame(list_cursor)
                print(table_accounts)
                edit_option = input("Do you want to edit anyone of the users' accounts?\n")

            main_question = input('Do you want to enter the car store?\n')
            if main_question == 'yes':
                car_parts_list = db.car_part_store.find({}, {"_id": 0})
                table_car_parts = pd.DataFrame(list(car_parts_list))
                print(table_car_parts)
                edit_car_model_question = input('Do you want to edit anyone of the car model parts!\n')
                while edit_car_model_question == 'yes':
                    update_car_model_question = input('Do you want to update anyone of the car model parts!\n')
                    if update_car_model_question == 'yes':
                        db.car_part_store.update_one(
                            {
                                "Car Model": input('Enter the name of the car model for edit!\n'),
                                "Car Part": input('Enter the name of the car part for edit!\n')
                            },
                            {
                                "$set":
                                    {
                                        "Car Model": input('Please, enter new car model or enter the old one!\n'),
                                        "Car Part": input('Please, enter the new car part or enter the old one!\n'),
                                        "Price": input('Please, enter the new price or enter the old one!\n')
                                    }
                            }
                        )

                        car_parts_list = db.car_part_store.find({}, {"_id": 0})
                        table_car_parts = pd.DataFrame(list(car_parts_list))
                        print(table_car_parts)

                    delete_car_part_question = input('Do you want to delete any car part model?\n')
                    if delete_car_part_question == 'yes':
                        delete_car_model = input('Enter the name of the car model to delete!\n')
                        delete_car_part = input('Enter the name of the car part to delete!\n')
                        db.car_part_store.delete_one({"Car Model": delete_car_model, "Car Part": delete_car_part})

                        car_parts_list = db.car_part_store.find({}, {"_id": 0})
                        table_car_parts = pd.DataFrame(list(car_parts_list))
                        print(table_car_parts)

                    add_car_part_question = input('Do you want to add a new car part?\n')
                    if add_car_part_question == 'yes':
                        add_car_model = input('Enter the name of the car model to add!\n')
                        add_car_part = input('Enter the name of the car part to add!\n')
                        add_car_part_price = int(input('Enter the price of the car part!\n'))
                        db.car_part_store.insert_one(
                            {
                                "Car Model": add_car_model,
                                "Car Part": add_car_part,
                                "Price": add_car_part_price
                            }
                        )

                        car_parts_list = db.car_part_store.find({}, {"_id": 0})
                        table_car_parts = pd.DataFrame(list(car_parts_list))
                        print(table_car_parts)

                    edit_car_model_question = input('Do you want to edit anyone of the car model parts!\n')
                else:
                    exit()

        else:
            current_user_account = db.accounts.find_one({"name": user_account[0], "password": user_account[1]})
            print(current_user_account["usertype"])
            if current_user_account["usertype"] == "reguser":
                print('This is registered MONGO user account!\n')
                total_purchase = 0
                buy_question = input('Do you want to purchase any car part?\n')

                while buy_question == "yes":

                    car_parts_list = db.car_part_store.find({}, {"_id": 0})
                    table_car_parts = pd.DataFrame(list(car_parts_list))
                    print(table_car_parts)

                    car_data = buy_car_part_mongo()
                    car_part_mongo = db.car_part_store.find_one(
                        {
                            "Car Model": car_data[0],
                            "Car Part": car_data[1]
                        }
                    )
                    print(car_data[0], car_data[1])
                    total_purchase = total_purchase + car_data[2] * car_part_mongo["Price"]
                    print(total_purchase)

                    buy_question = input('Do you want to purchase any car part?\n')

                save_transaction = db.transactions.insert_one(
                    {
                        "Name": user_account[0],
                        "Password": user_account[1],
                        "Total Price": total_purchase
                    }
                )
            elif current_user_account["usertype"] == "nonreg":
                print('This is non-registered MONGO user!\n')
                print('Please, wait the user account MONGO validation!\n')
                exit()
    else:
        registration_question = input('Do you want to make a MONGO registration?\n')
        if registration_question == "yes":
            print('Please, register!\n')
            add_new_account = enter_user_account()
            db.accounts.insert_one(
                {
                    "name": add_new_account[0],
                    "password": add_new_account[1],
                    "usertype": "nonreg"
                })
            print("Wait the creation of MONGO account!\n")
            break
        else:
            exit()

else:
    exit()
