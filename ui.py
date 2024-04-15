from typing import Tuple


def enter_user_account() -> Tuple:
    user_name = input('User Name, Please!:\n')
    user_password = input('User Password, Please:\n')
    return user_name, user_password


def edit_user_type_data_mongo():
    edit_user_type_mongo = input('Please, edit user type mongo!\n')
    return edit_user_type_mongo


def buy_car_part_mongo() -> Tuple:
    buy_car_model_type = input('Please, enter the car model type!\n')
    buy_car_part_model = input('Please, enter the car part model!\n')
    num_buy_parts = int(input('Please, enter the quantity of the parts!\n'))
    return buy_car_model_type, buy_car_part_model, num_buy_parts


def delete_data_mongo():
    delete_user_line_num = input("Please, enter the name to delete mongo!\n")
    return delete_user_line_num
