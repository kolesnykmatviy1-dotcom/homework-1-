import colorama
import inspect

print(hasattr(colorama, 'append'))

print(getattr(colorama, 'reverse'))
print(getattr(colorama, 'revers', None))
print(inspect.ismodule(colorama))
print(inspect.isclass(colorama))
for method in dir(colorama):
    print(method)
print(inspect.isfunction(colorama))
