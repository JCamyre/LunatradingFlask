def outer_function(func):
    def modifier():
        return func() * 3 + 1

    return modifier

@outer_function
def inner_function():
    return 3

print(inner_function())
print(outer_function(lambda: 1)())