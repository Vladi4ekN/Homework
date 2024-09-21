def apply_all_func(int_list, *functions):
    results = {}

    for func in functions:
        func_name = func.__name__
        results[func_name] = func(int_list)

    return results

int_list = [5, 1, 3, 4, 2]

results = apply_all_func(int_list, min, max, len, sum, sorted)

print(results)