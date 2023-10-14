def my_name():
    print("Hello world")


my_name()


def add_sum(a, b):
    answer = a + b
    return answer


print("Output", add_sum(30, 57))


def add_sums(*nums):
    _sum = 0
    for num in nums:
        _sum += num
    return _sum


print("Total sums:", add_sums(6, 12, 34, 56))


def add_ages(**ages):
    _age_sum = 0
    for k, v in ages.items():
        _age_sum += v
    return _age_sum


print("Total Ages", add_ages(angel=13, cecelia=56, emy=9))


def add_nums(a, b):
    answer = a + b

    def double_it():
        double = answer * 2
        print(double)

    double_it()
    return answer


print(add_nums(1, 49))

global_var = 13


def add_nums(a, b):
    total = a + b
    print("Global Variable:", global_var)
    double_it(total)  # Passing total as an argument to double_it


def double_it(total):
    double = total * 2
    print("Double:", double)


print("Global var in outer function:", global_var)
add_nums(5, 10)  # Calling add_nums function
