from datetime import datetime

import django, time, os
from django.db import models
from bs4 import BeautifulSoup

import parser_lib, get_links, get_html, get_image

os.environ['DJANGO_SETTINGS_MODULE'] = 'bulletin.settings'
django.setup()


from db_create import db_create
from bulletin_board.models import Car

MAIN_LINK = 'https://www.avito.ru/moskva_i_mo/avtomobili/avtomat/benzin/levyy_rul/ne_bolee_dvuh/ne_bityy'

def get_auto_item():
    auto_list = get_links.get_all_links(MAIN_LINK)
    p = 2
    while len(auto_list) < 60:
        auto_list = get_links.get_all_links(MAIN_LINK, p)
        time.sleep(5)
        p += 1

    for item in auto_list:
        link = 'https://www.avito.ru'+ item['url']
        item_info = get_html.get_html_page(link)

        soup = BeautifulSoup(item_info, 'html.parser')

        avito_item_number = parser_lib.get_item_number(soup)
        title = parser_lib.get_title(soup)
        published = datetime.now()
        price = parser_lib.get_price(soup)
        seller = parser_lib.get_seller(soup)
        phone = parser_lib.get_phone(soup)
        description = parser_lib.get_description(soup)
        all_specs = parser_lib.get_all_specs(soup)


# Кирилл, я тебе данные для вноса в таблицу подготовил) перевел все в int, float, удалил все лишнее
        car_brand = all_specs['Марка']
        car_model = all_specs['Модель']
        car_generation = all_specs['Поколение']
        modif = all_specs['Модификация']
        year_of_manufacture = int(all_specs['Год выпуска'])
        car_mileage = int(all_specs['Пробег'].rstrip('\xa0км'))
        condition = all_specs['Состояние']
        owners = int(all_specs['Владельцев по ПТС'])
        vin_number = all_specs['VIN или номер кузова']
        type_chassis = all_specs['Тип кузова']
        doors = int(all_specs['Количество дверей'])
        engine_type = all_specs['Тип двигателя']
        transmission = all_specs['Коробка передач']
        drive = all_specs['Привод']
        steering_side = all_specs['Руль']
        color = all_specs['Цвет']
        equipment = all_specs['Комплектация']
        view_place = all_specs['Место осмотра']
        engine_volume = float(all_specs['Объём двигателя'].rstrip('\xa0л'))



        #Ниже функция записи в БД
        db_create(car_title=title, pub_date=published, price=price, seller=seller, phone=phone, car_description=description, car_specs=all_specs, avito_item=avito_item_number)
        
        images = parser_lib.get_image(soup)
        #Загрузка картинок на диск
        get_image.download_image(images, avito_item_number)


        #После тестирования этот блок удалить
        car_full_info = {
            'avito_item_number': avito_item_number,
            'title': title,
            'published': published,
            'price': price,
            'seller': seller,
            'phone': phone,
            'description': description,
            'car_specs': all_specs,
            'images': images
            }
        print(car_full_info)
        print('ok!')
        #

        time.sleep(60)
    return car_full_info


if __name__ == '__main__':
    result = get_auto_item()
    print(result)
