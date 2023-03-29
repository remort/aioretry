import asyncio
import logging
import typing as t

TargetFunction = t.Callable[..., t.Awaitable]
CallbackFunction = t.Callable[..., t.Any]
Intervals = t.Tuple[int | float, ...]

log = logging.getLogger('retry_decorator')


def retry(
        tries: int,
        intervals: Intervals,
        fail_cb: CallbackFunction,
        allowed_exceptions: t.Tuple[t.Type[Exception], ...],
        logger: logging.Logger = log,
) -> t.Callable[[TargetFunction], TargetFunction]:
    def wrapper(fn: TargetFunction) -> TargetFunction | CallbackFunction:
        async def wrapped(*args, **kwargs) -> t.Any:
            for try_idx in range(0, tries):
                if try_idx > 0:
                    logger.info(f'Try to run {fn.__name__} for the {try_idx} retry.')

                try:
                    result = await fn(*args, **kwargs)
                    if try_idx > 0:
                        logger.debug(f'Got result from the {try_idx} retry.')
                    return result
                except allowed_exceptions:
                    try:
                        interval = intervals[try_idx]
                    except IndexError:
                        interval = intervals[-1]

                    if try_idx > 0:
                        logger.debug(f'Sleep {interval} seconds before retry.')
                    await asyncio.sleep(interval)

            logger.info(f'Failed to get result for the callable {fn}. Call a callback {fail_cb} and return.')
            return fail_cb(*args, **kwargs)

        return wrapped

    return wrapper
