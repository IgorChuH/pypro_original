from datetime import datetime


def filter_by_state(list_of_dict: list, state="EXECUTED") -> list:
    filtered_list = []
    for i in list_of_dict:
        if i.get("state") == state:
            filtered_list.append(i)
        else:
            continue
    return filtered_list


def sort_by_date(list_of_dict: list) -> list:

    return sorted(
        list_of_dict, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f")
    )