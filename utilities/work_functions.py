def greeting(name):
    return f'Hello, {name}'


def sort_array(arr):
    return sorted(arr)


def find_element(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
