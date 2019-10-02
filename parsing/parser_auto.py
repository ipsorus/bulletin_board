from datetime import datetime

import requests, time, csv
from bs4 import BeautifulSoup

def auto_parce(url):
    print('start parsing')
    auto_url = url
    '''params = {
        "sort": "fresh_relevance_1-desc",
        "year_from": 2014,
        "year_to": 2019,
        "engine_group": 'GASOLINE',
        "transmission": "AUTOMATIC",
        "displacement_to": 2800,
        "displacement_from": 1800,
        "pts_status": 1,
        "steering_wheel": "LEFT",
        "owners_count_group": "LESS_THAN_TWO",
        "price_to": 1500000,
        "price_from": 800000,
        "km_age_to": 80000
    }'''
    try:
        #result = requests.get(auto_url, params=params)
        result = requests.get(auto_url)
        result.raise_for_status()
        return result.text

    except(requests.RequestException, ValueError):
        print('Network error')
        return False

def all_auto_items(link_for_parce):
    html = auto_parce(link_for_parce)
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        #soup = soup.prettify()
        all_cars = soup.findAll('a', class_="item-description-title-link")
        result_news = []
        #print(all_cars)
        for car in all_cars:
            title = car.find('span').text
            try:
                url = car.attrs['href']
            except BaseException as e:
                print(e)

            result_news.append({
                'title': title,
                'url': url,
            })
        return result_news
    return False

def auto_item():
    auto_list = all_auto_items('https://www.avito.ru/moskva_i_mo/avtomobili/avtomat/benzin/levyy_rul/ne_bolee_dvuh/ne_bityy')
    #print(auto_list)
    time.sleep(10)
    car_full_info = []
    for item in auto_list:
        link = 'https://www.avito.ru'+ item['url']
        item_info = auto_parce(link)

        if item_info:
            soup = BeautifulSoup(item_info, 'html.parser')

            car_specs = []
            title = soup.find('span', class_="title-info-title-text")
            published = soup.find('div', class_="title-info-metadata-item-redesign")
            published = published.text
            try:
                published = datetime.strptime(published, '%Y-%m-%d')
            except(ValueError):
                published = datetime.now()

            price = soup.find('span', class_="js-item-price")
            seller = soup.find('span', class_="sticky-header-seller-text")
            phone = None
            all_specs = soup.find('ul', class_='item-params-list').findAll('li')
            for spec in all_specs:
                try:
                    car_spec = spec.text
                    car_specs.append(car_spec)
                except BaseException as e:
                    print(e)
            description = soup.find('div', class_="item-description-text")

            car_full_info.append({
                'title': title.text,
                'published': published,
                'price': price.text,
                'seller': seller.text,
                'phone': phone,
                'description': description.text,
                'car_specs': car_specs
                })
            print('ok!')
        time.sleep(180)
    return car_full_info
#return False


if __name__ == '__main__':
    result = auto_item()
    print(result)
    with open('export_cars.csv', 'w', encoding='utf-8', newline='') as f:
        fields = ['title', 'published', 'price', 'seller', 'phone', 'description', 'car_specs']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for auto in result:
            writer.writerow(auto)