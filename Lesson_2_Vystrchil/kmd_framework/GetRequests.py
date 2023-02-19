from .common.utils import parse_input_data


class GetRequests:

    @staticmethod
    def get_request_params(environ):
        # получаем параметры запроса
        query_string = environ["QUERY_STRING"]
        # превращаем параметры в словарь
        request_params = parse_input_data(query_string)
        return request_params
