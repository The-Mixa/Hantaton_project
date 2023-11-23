import requests
from bs4 import BeautifulSoup


class GetInfo:
    def __init__(self, number_of_function):
        if number_of_function == 1:
            self.closest_events()
        elif number_of_function == 2:
            self.services()
        elif number_of_function == 3:
            self.news()

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
        with open('../texts/events.txt', 'w', encoding='utf8') as f:
            for event in events:
                f.write(event)

    def services(self):
        services = ['']
        response = requests.get('https://www.tp86.ru/services/services/')
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.findAll('a', class_='service-element bg-color-full-white')

        for el in data:
            service = ''
            name_of_service = el.find('p',
                                      class_='font-myriad-pro-weight-400 text-color-black font-size-17').text.strip()
            service_info_url = el['href']
            service += name_of_service + '\n'
            service += f'https://www.tp86.ru{service_info_url}\n\n'
            services += service
        with open('../texts/public_services.txt', 'w', encoding='utf8') as f:
            for service in services:
                f.write(service)

    def news(self):
        finish_news = ['']

        response_all_news = requests.get('https://www.tp86.ru/press-centr/news/')
        soup_all_news = BeautifulSoup(response_all_news.text, 'html.parser')
        all_news = soup_all_news.find('a', class_='news-element news__list_item')

        href = 'https://www.tp86.ru' + all_news['href']
        img_src = 'https://www.tp86.ru' + all_news.find('img')['src']
        finish_news += f'{img_src}\n'

        response_news = requests.get(href)
        soup_news = BeautifulSoup(response_news.text, 'html.parser')

        name = soup_news.findAll('h2', class_='uppercase mb-40 container-p-adaptive')

        name = name[0].text.strip()
        finish_news += f'*{name}*\n'

        paragraphs_find = soup_news.find('div', class_='news-detail__block_text line-height-200').findAll('p')
        for paragraph in paragraphs_find[:3]:
            text = paragraph.text.strip()
            finish_news += f'{text}\n'

        finish_news += (f'Если заинтересовала новость, то можете прочитать её полностью на [оффициальном сайте]'
                        f'({href})')

        with open('../texts/relevant_news.txt', 'w', encoding='utf8') as f:
            for line in finish_news:
                f.write(line)

GetInfo(3)