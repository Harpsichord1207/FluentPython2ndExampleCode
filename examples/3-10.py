from types import MappingProxyType


if __name__ == '__main__':
    d = {1: 'A'}
    d_proxy = MappingProxyType(d)
    print(d_proxy)
    try:
        d_proxy[2] = 'x'
    except TypeError:
        print("TypeError: 'mappingproxy' object does not support item assignment")

    d[1] = 'B'
    print(d_proxy)
