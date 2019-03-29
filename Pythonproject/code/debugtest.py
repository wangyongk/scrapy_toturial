def foo(bar=None):
    if not bar:
        bar = []
        bar.append('baz')
    return bar
print(foo())
print(foo())