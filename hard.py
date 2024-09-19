data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(*args):
    if len(args[0]) == 0:
        return 0

    result = 0
    entry = args[0]

    for i in entry:
        if isinstance(i, list | tuple | set):
            result += calculate_structure_sum(i)
        elif isinstance(i, dict):
            result += calculate_structure_sum(list(zip(i.keys(), i.values())))
        elif isinstance(i, int):
            result += i
        elif isinstance(i, str):
            result += len(i)

    return result


print(calculate_structure_sum(data_structure))
