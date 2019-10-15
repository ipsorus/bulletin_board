from bulletin_board.models import Car

def db_create(car_title='',pub_date='', price='', seller='', phone='', car_description='', car_specs='', avito_item=''):
    sale_announcement = Car(car_title=car_title, pub_date=pub_date, price=price, seller=seller, phone=phone, car_description=car_description, car_specs=car_specs, avito_item=avito_item)
    sale_announcement.save()
    return print('Объявление занесено в базу данных')
