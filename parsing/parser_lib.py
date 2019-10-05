from datetime import datetime

import requests, time, csv
from bs4 import BeautifulSoup

def get_item_number(get_item_number_text):
    try:
        item = get_item_number_text.find('div', class_="item-view-search-info-redesign").find('span').text
        print(item)
        item = item.split(' ')[1]
    except (ValueError, AttributeError):
        item = None
    return item

def get_title(title_text):
    try:
        title = title_text.find('span', class_="title-info-title-text").text
    except (ValueError, AttributeError):
        title = None
    return title

def get_price(price_text):
    try:
        price = price_text.find('span', class_="js-item-price").text
    except (ValueError, AttributeError):
        price = None
    return price

def get_seller(seller_text):
    try:
        seller = seller_text.find('span', class_="sticky-header-seller-text").text
    except (ValueError, AttributeError):
        seller = None
    return seller

def get_phone(phone_text):
    try:
        phone = phone_text.find('div', class_="sticky-header-prop sticky-header-contacts").text
    except (ValueError, AttributeError):
        phone = None
    return phone

def get_description(description_text):
    try:
        description = description_text.find('div', class_="item-description").text
    except (ValueError, AttributeError):
        description = None
    return description

def get_all_specs(all_specs_text):
    car_specs = dict()
    try:
        all_specs = all_specs_text.find('ul', class_='item-params-list').findAll('li')
        for spec in all_specs:
            car_spec = spec.text.split(':')
            car_specs[car_spec[0]] = car_spec[1]
    except (ValueError, AttributeError):
        all_specs = None
    return car_specs
