from bulletin_board.models import Car

#TODO

def db_create(car_title='',pub_date='', price='', seller='', phone='', car_description='', avito_item='', car_brand='', car_model='', car_generation='', 
modification='', year_of_manufacture='', car_mileage='', condition='', owners='',vin_number='', type_chassis='', doors='', engine_type='', transmission='', drive='',
steering_side='', color='', equipment='', view_place='', engine_volume='' ):

    sale_announcement = Car(car_title=car_title, pub_date=pub_date, price=price, seller=seller,phone=phone, car_description=car_description, avito_item=avito_item, 
    car_brand=car_brand, car_model=car_model, car_generation=car_generation, modif=modification, year_of_manufacture=year_of_manufacture, car_mileage=car_mileage, condition=condition,
    owners=owners, vin_number=vin_number, type_chassis=type_chassis, doors=doors, engine_type=engine_type, transmission=transmission, drive=drive, steering_side=steering_side, 
    color=color, equipment=equipment, view_place=view_place, engine_volume=engine_volume)

    sale_announcement.save()
    return print('Объявление занесено в базу данных')
