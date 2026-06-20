from code_pathshala.labs.kata_advanced import count_calls, prime_generator


def test_count_calls_decorator():
    @count_calls
    def dummy_add(a, b):
        return a + b

    assert dummy_add.calls == 0
    assert dummy_add(10, 20) == 30
    assert dummy_add.calls == 1
    assert dummy_add(1, 2) == 3
    assert dummy_add(3, 4) == 7
    assert dummy_add.calls == 3


def test_prime_generator_simple():
    primes = list(prime_generator(10))
    assert primes == [2, 3, 5, 7]


def test_prime_generator_larger():
    primes = list(prime_generator(25))
    assert primes == [2, 3, 5, 7, 11, 13, 17, 19, 23]


def test_prime_generator_empty():
    primes = list(prime_generator(1))
    assert primes == []
