import time


def log(filename=None):
    """
    Декоратор для логирования времени выполнения функции и её результата.

    :param filename: Имя файла для записи логов. Если None, выводит в консоль.
    """

    def my_decorator(func):
        """
        Декоратор для обёртки функции, добавляющий логирование.

        :param func: Функция, которую нужно обернуть.
        """

        def wrapper(*args, **kwargs):
            """
            Обертывающая функция, которая записывает логи.

            :param args: Позиционные аргументы функции.
            :param kwargs: Именованные аргументы функции.
            :return: Результат выполнения оригинальной функции.
            """
            try:
                time_1 = time.time()
                result = func(*args, **kwargs)
                time_2 = time.time()
                name_func = func.__name__
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(
                            f"Начало: {time_1} \nФункция {name_func} ок. Результат: {result}\nКонец: {time_2}\n\n"
                        )
                        file.close()
                else:
                    print(
                        f"Начало: {time_1} \nФункция {name_func} ок. Результат: {result}\nКонец: {time_2}"
                    )
                return result
            except Exception as e:
                name_func = func.__name__
                if filename:
                    file = open(filename, "a", encoding="utf-8")
                    file.write(f"{name_func} error: {e}. Inputs: {args}, {kwargs}")
                    file.close()
                    return f"{name_func} error: {e}. Inputs: {args}, {kwargs}"
                else:
                    print(f"{name_func} error: {e}. Inputs: {args}, {kwargs}")
                raise

        return wrapper

    return my_decorator


@log(filename="mylog.txt")
@log()
def my_function(x, y):
    return x + y


@log()
def second_fun(x, y):
    return x / y


second_fun(5, 1)
