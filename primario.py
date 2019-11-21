import principal.secundario

from importlib import import_module


p = "principal.secundario"
m = "function_one"

mod = import_module(p)
met = getattr(mod, m)
# my_method = getattr(the_module, "my_method")

res = met(2, 5)
print(res)


