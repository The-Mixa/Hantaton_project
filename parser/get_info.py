import requests
from bs4 import BeautifulSoup


class GetInfo:
    def __init__(self, number_of_function):
        if number_of_function == '1':
            self.closest_events()
        elif number_of_function == '2':
            self.services()

    def closest_events(self):
        events = ['']
        response = requests.get('https://www.tp86.ru/press-centr/events/')
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.findAll('a', class_='grid events__list_item')
        for el in data:
            event = ''
            date = el.find('p', class_='day text-color-black font-montserrat-weight-700 font-size-36').text.strip()
            month = el.find('p', class_='month').text.strip()
            text = el.find('p', class_='prew-text text-color-black font-myriad-pro-weight-600 font-size-24 '
                                       'text-color-dark-purple events__list_item_prew-text').text.strip()
            more_info_url = el['href']
            event += date + ' ' + month + '\n'
            event += text + '\n'
            event += f'https://www.tp86.ru{more_info_url}' + '\n\n'
            events += event
        with open('texts/events.txt', 'w', encoding='utf8') as f:
            for event in events:
                f.write(event)

    def services(self):
        response = requests.get('https://www.tp86.ru/services/services/')
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.findAll('a', class_='service-element bg-color-full-white')

        for el in data:
            name_of_service = el.find('p', class_='font-myriad-pro-weight-400 text-color-black font-size-17').text.strip()
            service_info_url = el['href']
            print(name_of_service)
            print(f'https://www.tp86.ru{service_info_url}', end='\n\n')
