def info_kwargs(**kwargs):
    result = sorted(kwargs.items())
    for i in result:
        a, b = i
    print(f"{a} = {b}")

print(info_kwargs(first_name="John", last_name="Doe", age=33))

print("Hello, world")


pass

pass
pass