def get_date(data_main):
    just_date = data_main[:data_main.find("T")].split('-')
    just_date.reverse()
    return '.'.join(just_date)

result = '2024-03-11T02:26:18.671407'
print(get_date(result))