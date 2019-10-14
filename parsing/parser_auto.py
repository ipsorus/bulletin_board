from datetime import datetime

import requests, time, csv, os
from bs4 import BeautifulSoup

import parser_lib

ALL_LINKS = [] #Для записи всех ссылок на объявления (чтобы не обнулялся список после прохода по второй и далее страницам)

def get_html_page(url, page = None):
    print('start parsing')
    auto_url = url
    params = {
            "p": page
        }
    try:
        result = requests.get(auto_url, params=params)
        result.raise_for_status()
        return result.text

    except(requests.RequestException, ValueError):
        print('Network error')
        return False

def get_all_links(link_for_parce, page = None):
    html = get_html_page(link_for_parce, page)
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_cars = soup.findAll('a', class_="item-description-title-link")
        all_links = ALL_LINKS
        for car in all_cars:
            try:
                url = car.attrs['href']
            except BaseException as e:
                print('Something wrong in get_all_links', e)

            all_links.append({
                'url': url,
            })
        return all_links
    return False

def get_auto_item():
    auto_list = get_all_links('https://www.avito.ru/moskva_i_mo/avtomobili/avtomat/benzin/levyy_rul/ne_bolee_dvuh/ne_bityy')
    p = 2
    while len(auto_list) < 60:
        auto_list = get_all_links('https://www.avito.ru/moskva_i_mo/avtomobili/avtomat/benzin/levyy_rul/ne_bolee_dvuh/ne_bityy', p)
        time.sleep(5)
        p += 1

    for item in auto_list:
        link = 'https://www.avito.ru'+ item['url']
        item_info = get_html_page(link)

        soup = BeautifulSoup(item_info, 'html.parser')

        avito_item_number = parser_lib.get_item_number(soup)
        title = parser_lib.get_title(soup)
        published = datetime.now().strftime('%d.%m.%Y %H:%M')
        price = parser_lib.get_price(soup)
        seller = parser_lib.get_seller(soup)
        phone = parser_lib.get_phone(soup)
        description = parser_lib.get_description(soup)
        all_specs = parser_lib.get_all_specs(soup)

        images = parser_lib.get_image(soup)

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

        image_name_index = 0
        image_lib = car_full_info['images']
        image_name = car_full_info['avito_item_number']
        
        path = car_full_info['avito_item_number']
        try:
            os.mkdir(path)
        except OSError:
            print ("Создать директорию %s не удалось" % path)
        else:
            print ("Успешно создана директория %s " % path)

        for link in image_lib:
            image_name = image_name + str(image_name_index)
            parser_lib.load_image(link, image_name, path)
            image_name_index += 1

        time.sleep(60)
    return car_full_info


if __name__ == '__main__':
    result = get_auto_item()
    print(result)
