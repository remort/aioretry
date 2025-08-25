import asyncio
from aioretry_decorator import retry

FAIL_MSG = 'Fail'
CB_STRING = 'callback was called'

async def failing_coro_1():
    await asyncio.sleep(0.1)
    raise RuntimeError(FAIL_MSG)

async def failing_coro_2(results: list):
    results.append(1)
    await asyncio.sleep(0.1)
    raise RuntimeError('Fail')

async def success_coro_1(results: list):
    results.append(1)
    await asyncio.sleep(0.1)

def callback_func(results: list):
    results.append(CB_STRING)

async def async_callback_func(results: list):
    await asyncio.sleep(0.01)
    results.append(CB_STRING)

def run_tests():
    results_holder = []
    try:
        asyncio.run(retry(3, intervals=(1,))(failing_coro_1)())
    except RuntimeError as exc:
        assert str(exc) == FAIL_MSG, str(exc)
        print('test 1 done')

    retries = 3
    deco = retry(retries, (RuntimeError,), tuple(x / 10 for x in range(1, retries + 1)))
    asyncio.run(deco(failing_coro_2)(results_holder))
    assert results_holder == [1 for x in range(0, 3)], results_holder
    print('test 2 done')

    results_holder = []
    asyncio.run(retry(3, (RuntimeError,), (0.2, 0.5), callback_func)(failing_coro_2)(results_holder))
    assert results_holder == [1 for x in range(0, 3)] + [CB_STRING], results_holder
    print('test 3 done')

    results_holder = []
    asyncio.run(retry(1, (RuntimeError,))(failing_coro_2)(results_holder))
    assert results_holder == [1], results_holder
    print('test 4 done')

    results_holder = []
    asyncio.run(retry(10)(success_coro_1)(results_holder))
    assert results_holder == [1], results_holder
    print('test 5 done')

    results_holder = []
    asyncio.run(retry(10, (RuntimeError,), (0,1))(success_coro_1)(results_holder))
    assert results_holder == [1], results_holder
    print('test 6 done')

    results_holder = []
    asyncio.run(
        retry(3, (RuntimeError,), (0,1), async_callback_func)(failing_coro_2)(results_holder)
    )
    assert results_holder == [1 for x in range(0, 3)] + [CB_STRING], results_holder
    print('test 7 done')

    print('All checks passed')


if __name__ == '__main__':
    run_tests()
