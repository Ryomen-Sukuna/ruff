for aVeryLongNameThatSpillsOverToTheNextLineBecauseItIsExtremelyLongAndGoesOnAndOnAndOnAndOnAndOnAndOnAndOnAndOnAndOn in anotherVeryLongNameThatSpillsOverToTheNextLineBecauseItIsExtremelyLongAndGoesOnAndOnAndOnAndOnAndOnAndOnAndOnAndOnAndOn: # trailing comment
    pass

else:
    ...

for (
    x,
    y,
    ) in z: # comment
    ...


# remove brackets around x,y but keep them around z,w
for (x, y) in (z, w):
    ...


# type comment
for _ in ():
    ...
