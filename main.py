data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(*data_structure):
    summa_ = 0
    if data_structure:
        return
    if isinstance(data_structure, dict):
        for key, value in data_structure.items():
            summa_ += calculate_structure_sum(len(key))
            summa_ += calculate_structure_sum(value)

    if isinstance(data_structure, list):
        for list[:-1] in data_structure:
            summa_ += calculate_structure_sum(list)

    if isinstance(data_structure, str):
        for str[:-1] in data_structure:
            summa_ += calculate_structure_sum(len(str))

    if isinstance(data_structure, int):
        i = int
        for i in data_structure:
            summa_ += calculate_structure_sum(i)

    return summa_


result = calculate_structure_sum(data_structure)
print(result)




















