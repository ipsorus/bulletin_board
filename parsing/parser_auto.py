import requests
from bs4 import BeautifulSoup

def auto_parce():
    print('hello')
    auto_url = "https://auto.ru/moskva/cars/volvo/used/"
    params = {
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
    }
    try:
        result = requests.get(auto_url, params=params)
        result.raise_for_status()
        return result.text

    except(requests.RequestException, ValueError):
        print('Network error')
        return False

def auto_item():
    html = auto_parce()
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_cars = soup.find('div', class_="ListingCars-module__container ListingCars-module__list")
        result_news = []
        print(all_cars)
        for car in all_cars:
            title = car.find('a').text
            url = car.find('a')['href']
            #published = news.find('time').text
            result_news.append({
                'title': title,
                'url': url,
                #'published': published
            })
        print(result_news)
        return result_news
    return False

if __name__ == '__main__':
    print(auto_item())