from functools import wraps


def chekc_free_cells(content):
    def check_func(func):
        def cheker(*args):
            for a in args:
                if content[a.x][a.y].name != 'Empty':
                    raise IndexError
            return func(*args)
        return cheker
    return check_func
