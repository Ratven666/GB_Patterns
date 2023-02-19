from quopri import decodestring


def parse_input_data(data: str):
    """Разбивает строки GET и POST запросов в словарь"""

    result = {}
    if data:
        params = data.split("&")
        for item in params:
            key, value = item.split("=")
            result[key] = value
    # исправляем проблемы с кодировкой сразу
    result = decode_value(result)
    return result


def decode_value(data):
    """Заменяет рпоблемные символы из кириллицы и приводит ее к нормальному виду"""
    new_data = {}

    def val_decoder(val):
        val = bytes(val.replace('%', '=').replace("+", " "), 'UTF-8')
        val_decode_str = decodestring(val).decode('UTF-8')
        return val_decode_str

    for key, value in data.items():
        key = val_decoder(key)
        value = val_decoder(value)

        new_data[key] = value
    return new_data
