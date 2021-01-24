""" https://jsonplaceholder.typicode.com/ """

class JsonSiteMethods:

    @staticmethod
    def ids_list():
        """ Возвращает int список ids, для передачи в запросы """
        post_ids = list(range(1, 10))
        return post_ids

    @staticmethod
    def headers_data():
        """ Возвращает значения headers, для передачи в запросы """
        headers = {
            "Content-type": "application/json; charset=UTF-8"
        }
        return headers
