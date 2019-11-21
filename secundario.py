


class dispatcher:
    name = 'dispatcher'
    def __init__(self, function_to_exec):
        self.function = function_to_exec
        return self.function

    def get_name(self):
        return self.name


def function_one(a,b):
    return a + b

def function_two():
    return 'function two'