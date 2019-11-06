import django, time, os, requests
from django.db import models
from django.utils import timezone
from bs4 import BeautifulSoup

import parser_lib, get_links, get_html

os.environ['DJANGO_SETTINGS_MODULE'] = 'bulletin.settings'
django.setup()


from db_create import db_create
from bulletin_board.models import Car

MAIN_LINK = 'https://www.avito.ru/moskva_i_mo/avtomobili/ne_bolee_dvuh/ne_bityy'

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
        price = parser_lib.get_price(soup)
        #seller_id = 1
        phone = parser_lib.get_phone(soup)
        description = parser_lib.get_description(soup)
        all_specs = parser_lib.get_all_specs(soup)

        #Разбор словаря
        car_brand = all_specs.get('Марка', '')
        car_model = all_specs.get('Модель', '')
        car_generation = all_specs.get('Поколение', '')
        modif = all_specs.get('Модификация', '')
        year_of_manufacture = all_specs.get('Год выпуска')
        if year_of_manufacture:
            year_of_manufacture = int(year_of_manufacture)
        car_mileage = all_specs.get('Пробег')
        if car_mileage:
            car_mileage = int(car_mileage.rstrip('\xa0км'))
        condition = all_specs.get('Состояние', '')
        owners = all_specs.get('Владельцев по ПТС')
        if owners:
            owners = int(owners)
        vin_number = all_specs.get('VIN или номер кузова', '')
        type_chassis = all_specs.get('Тип кузова', '')
        doors = all_specs.get('Количество дверей')
        if doors:
            doors = int(doors)
        engine_type = all_specs.get('Тип двигателя', '')
        transmission = all_specs.get('Коробка передач', '')
        drive = all_specs.get('Привод', '')
        steering_side = all_specs.get('Руль', '')
        color = all_specs.get('Цвет', '')
        equipment = all_specs.get('Комплектация', '')
        view_place = all_specs.get('Место осмотра', '')
        engine_volume = all_specs.get('Объём двигателя')
        if engine_volume:
            if '+' in engine_volume:
                engine_volume = float(engine_volume.rstrip('+\xa0л'))
            else:
                engine_volume = float(engine_volume.rstrip('\xa0л'))


        
        images = parser_lib.get_image(soup)

        #Ниже функция записи в БД, TODO
        db_create(car_title=title, price=price, phone=phone, car_description=description, avito_item=avito_item_number, car_brand=car_brand,
        car_model=car_model, car_generation=car_generation, modification=modif, year_of_manufacture=year_of_manufacture, car_mileage=car_mileage, condition=condition, owners=owners,
        vin_number=vin_number, type_chassis=type_chassis, doors=doors, engine_type=engine_type, transmission=transmission, drive=drive, steering_side=steering_side, color=color,
        equipment=equipment, view_place=view_place, engine_volume=engine_volume, images=images )


        print('Парсинг закончен успешно!')
        
        time.sleep(30)


if __name__ == '__main__':
    get_auto_item()
    
