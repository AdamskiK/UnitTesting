def test():
    print("hello world")


def test_my_function(benchmark):
    result = benchmark(test)


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test", number=100))



