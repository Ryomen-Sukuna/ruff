foo_tuple = (1, 2, 3)
foo_list = [1, 2, 3]
foo_set = {1, 2, 3}
foo_dict = {1: 2, 3: 4}
foo_int = 123

import itertools

for _ in itertools.product(foo_int):
    pass
