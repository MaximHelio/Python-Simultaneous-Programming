import requests


def io_bound_func():
    result = requests.get("https://google.com")
    return result


if __name__ == "___main__":
    for i in range(10):
        result = io_bound_func()
        result = io_bound_func()
        result = io_bound_func()
        result = io_bound_func()
        result = io_bound_func()
        result = io_bound_func()
        result = io_bound_func()
        result = io_bound_func()
        result = io_bound_func()
        print(result)