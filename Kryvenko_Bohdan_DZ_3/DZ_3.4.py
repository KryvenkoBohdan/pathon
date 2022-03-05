'''
4. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия»
и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме предыдущего
задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:
thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": ["Петр Алексеев"]
    },
    "И": {
        "И": ["Илья Иванов"]
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"],
        "А": ["Анна Савельева"]
    }
}
Как поступить, если потребуется сортировка по ключам?
'''


def thesaurus_adv(*args):
    """
    :param args:list of first and last names (список из имен и фамилий)
    :return:a dictionary where the key is the first letter of the last name, and the value is a dictionary
    where the key is the first letter of the first name, and the value is a list of names starting with that letter
    (словарь в котором ключ это первая буква фамилии, а значение это словарь в которам ключ это первая буква имени,
    а значение это список состоящий из имен начинающихся на эту букву)
    """
    name_dict = {}
    for i in args:
        key = i.split()[1][0]
        if not key in name_dict:
            name_dict[key] = {}
        new_key = i[0]
        if not new_key in name_dict[key]:
            name_dict[key][new_key] = [i]
        else:
            name_dict[key][new_key].append(i)
    return name_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))