import requests
from bs4 import BeautifulSoup


class GetInfo:
    def __init__(self, number_of_function):
        if number_of_function == '1':
            self.closest_events()
        elif number_of_function == '2':
            self.services()
        elif number_of_function == '3':
            self.how_to_be_a_resident()
        elif number_of_function == '4':
            pass
        elif number_of_function == '5':
            pass
        elif number_of_function == '6':
            pass

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

    def how_to_be_a_resident(self):
        print('Как стать резидентом?')
        print('Всего пять шагов!')
        print('1)Сформулировать идею и заполнить анкету')
        print('2)Подать заявку в Технопарк на проведение экспертизы проекта')
        print('3)Получить положительное заключение на проект и направить заявление на получение статуса резидента*')
        print('4)Успешно защитить свой проект на заседании Экспертной комиссии')
        print('5)Подписать договор о предоставлении статуса резидента Технопарка', end='\n\n')
        print('*При соблюдении условий, указанных в Положении о резидентной политике')
        print('Скачать анкету: https://www.tp86.ru/upload/medialibrary/588/9vp1xwgvz29gk1siueugb9qi5p2h3cr5/zayavlenie-proektnaya-initsiativa.docx')
        print('Подробнее: https://www.tp86.ru/residents/add/')

    def accelerator_of_technological_startups_competition(self):
        pass

    def umnik_competition(self):
        pass

    def young_developer_competition(self):
        pass
