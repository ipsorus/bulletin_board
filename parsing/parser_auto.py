from datetime import datetime

import requests, time, csv
from bs4 import BeautifulSoup

import parser_lib


def auto_parce(url):
    print('start parsing')
    auto_url = url
    try:
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
        all_cars = soup.findAll('a', class_="item-description-title-link")
        result_news = []
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
    time.sleep(10)
    car_full_info = []
    for item in auto_list:
        link = 'https://www.avito.ru'+ item['url']
        item_info = auto_parce(link)

        if item_info:
            soup = BeautifulSoup(item_info, 'html.parser')

            avito_item_number = parser_lib.get_item_number(soup)
            title = parser_lib.get_title(soup)
            published = datetime.now().strftime('%d.%m.%Y %H:%M')
            price = parser_lib.get_price(soup)
            seller = parser_lib.get_seller(soup)
            phone = parser_lib.get_phone(soup)
            description = parser_lib.get_description(soup)
            all_specs = parser_lib.get_all_specs(soup)

            car_full_info.append({
                'avito_item_number': avito_item_number,
                'title': title,
                'published': published,
                'price': price,
                'seller': seller,
                'phone': phone,
                'description': description,
                'car_specs': all_specs
                })
            print(car_full_info)
            print('ok!')
            time.sleep(180)     
    return car_full_info


if __name__ == '__main__':
    result = auto_item()
    print(result)
    with open('export_cars.csv', 'w', encoding='utf-8', newline='') as f:
        fields = ['title', 'published', 'price', 'seller', 'phone', 'description', 'car_specs']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for auto in result:
            writer.writerow(auto)