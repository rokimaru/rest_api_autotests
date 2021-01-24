"""  https://api.openbrewerydb.org/ """

import requests


class BrewerySiteMethods:


    @staticmethod
    def get_all_breweries_id():
        """ Метод возвращает список id пивоварен на 1 странице"""
        response = requests.get('https://api.openbrewerydb.org/breweries').json()
        breweries_id = []
        for item in response:
            breweries_id.append(item['id'])
        return breweries_id

    @staticmethod
    def get_all_breweries_name():
        """ Метод возвращает список name пивоварен на 1 странице """
        response = requests.get('https://api.openbrewerydb.org/breweries').json()
        breweries_name = []
        for item in response:
            breweries_name.append(item['name'])
        return breweries_name

    @staticmethod
    def request_brewery_information(brewery_id):
        """ Метод запрашивает информацию по id пивоварни """
        response = requests.get('https://api.openbrewerydb.org/breweries/' + str(brewery_id))
        return response