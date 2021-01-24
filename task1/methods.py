""" https://dog.ceo/api/breed/ """
import requests


class DogSiteMethods:

    @staticmethod
    def request_breed_image(breed_item):
        """ Метод запрашивает изображение для указанной породы собак. """
        response = requests.get('https://dog.ceo/api/breed/' + breed_item + '/images/random')
        return response

    @staticmethod
    def get_all_breeds():
        """ Метод возвращает список названий всех пород собак в формате list """

        response = requests.get('https://dog.ceo/api/breeds/list/all')
        all_breeds = list(response.json()['message'])
        return all_breeds
