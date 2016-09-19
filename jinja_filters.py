def dayofweek(number):
    return {
        1: "Понедельник",
        2: "Вторник",
        3: "Среда",
        4: "Четверг",
        5: "Пятница",
        6: "Суббота",
    }.get(number, "")


def parainfo(number):
    return {
        1: "08:15",
        2: "09:55",
        3: "11:35",
        4: "13:45",
        5: "15:25",
        6: "17:05",
        7: "18:40",
        8: "20:00",
    }.get(number, "")


def lesson_type_class(nt):
    return {
        1: "lect",
        2: "lab",
        3: "pract",
    }.get(nt)


def is_list(value):
    return isinstance(value, list)