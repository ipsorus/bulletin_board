import requests
from bs4 import BeautifulSoup

def auto_parce():
    print('hello')
    #auto_url = "https://auto.ru/moskva/cars/volvo/used/"
    auto_url = 'https://www.avito.ru/moskva_i_mo/avtomobili/avtomat/benzin/levyy_rul/ne_bolee_dvuh/ne_bityy'
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

def auto_item():
    html = auto_parce()
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        #soup = soup.prettify()
        all_cars = soup.findAll('a', class_="item-description-title-link")
        result_news = []
        print(all_cars)
        for car in all_cars:
            title = car.find('span').text
            try:
                url = car.attrs['href']
            except BaseException as e:
                print(e)

            #published = news.find('time').text
            result_news.append({
                'title': title,
                'url': url,
                #'published': published
            })
        return result_news
    return False

if __name__ == '__main__':
    print(auto_item())