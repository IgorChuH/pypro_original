def get_date(data_main: str) -> str:
    """
        Преобразует дату в формате 'YYYY-MM-DD' в формат 'DD.MM.YYYY'.

        Параметры:
        data_main (str): Дата в виде строки, содержащая дату и время.

        Возвращает:
        str: Дата в формате 'DD.MM.YYYY'.
        """
    just_date = data_main[: data_main.find("T")].split("-")
    just_date.reverse()
    return ".".join(just_date)


result = "2024-03-11T02:26:18.671407"
print(get_date(result))
