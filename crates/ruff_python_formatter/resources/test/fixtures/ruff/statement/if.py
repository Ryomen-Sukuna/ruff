# 1 leading if comment
if x == y:
    if y == z:
        ...

    # trailing else comment

...
# Don't drop this comment 1
x = 1

# Don't drop this comment 2
x = 2

# Don't drop this comment 3
x = 3


# Regression test for `last_child_in_body` special casing of `StmtIf`
# https://github.com/python/cpython/blob/aecf6aca515a203a823a87c711f15cbb82097c8b/Lib/test/test_pty.py#L260-L275
def f():
    pass

        # comment

if True:
    def f():
        pass
        # 1
elif True:
    def f():
        pass
        # 2
else:
    def f():
        pass
        # 3

if True: print("a") # 1
# Regression test for https://github.com/astral-sh/ruff/issues/5337
if parent_body:
    if current_body:
        child_in_body()
        last_child_in_current_body()  # may or may not have children on its own
# a
  # b
    # c
      # d
        # e
          #f
