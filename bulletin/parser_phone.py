from selenium import webdriver
from time import sleep

class Bot:
    def __init__(self):
        self.driver = webdriver.Safari()
        self.navigate()
    
    def take_screenshot(self):
        self.driver.save_screenshot('avito_phone.png')

    def navigate(self):
        self.driver.get('https://www.avito.ru/moskva/avtomobili/mercedes-benz_glk-klass_2012_1814208232')

        a = self.driver.find_element_by_xpath('//a[@class="button item-phone-button js-item-phone-button button-origin button-origin-blue button-origin_full-width button-origin_large-extra item-phone-button_hide-phone item-phone-button_card js-item-phone-button_card"]')
        a.click()
        
        sleep(3)

        self.take_screenshot()



def main():
    b = Bot()

if __name__ == '__main__':
    main()