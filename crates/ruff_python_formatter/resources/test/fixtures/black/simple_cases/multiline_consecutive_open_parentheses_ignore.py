# This is a regression test. Issue #3737

a = 6

b = 6

print(   "111") # type: ignore
print(   "111"                         ) # type: ignore
print(   "111"       ) # type: ignore
