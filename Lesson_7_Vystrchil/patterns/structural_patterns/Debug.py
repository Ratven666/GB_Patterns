
from timeit import timeit, default_timer


class Debug:

    def __init__(self, name, count_number=100):
        self.__name = name
        self.__count_number = count_number

    def __call__(self, cls):
        def time_test(method):
            '''
            нужен для того, чтобы декоратор класса wrapper обернул в time_test
            каждый метод декорируемого класса
            '''
            def timed(*args, **kw):
                start_time = default_timer()
                for _ in range(self.__count_number):
                    result = method(*args, **kw)
                func_time = (default_timer() - start_time) / self.__count_number
                print(f"Debug --> {self.__name} выполнялся {func_time}")
                return result
            return timed
        return time_test(cls)
