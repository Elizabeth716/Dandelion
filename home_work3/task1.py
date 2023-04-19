def cache(times: int) -> int:

    def outer(func):
        count = 0 #amount hom much out func was called
        cache_value = None

        def wrapper(*args, **kwargs):
            nonlocal cache_value
            nonlocal count
            if count == 0:
                count += 1
                cache_value = func(*args, **kwargs)
                return cache_value
            if count >= times - 1:
                count = 0
                return cache_value
            if count < times:
                count += 1
                return cache_value

        return wrapper

    return outer
