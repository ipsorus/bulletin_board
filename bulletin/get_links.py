from bs4 import BeautifulSoup

import get_html

ALL_LINKS = [] #Для записи всех ссылок на объявления (чтобы не обнулялся список после прохода по второй и далее страницам)

def get_all_links(link_for_parce, page = None):
    html = get_html.get_html_page(link_for_parce, page)
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