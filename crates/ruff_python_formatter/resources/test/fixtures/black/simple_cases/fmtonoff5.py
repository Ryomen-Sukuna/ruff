# Regression test for https://github.com/psf/black/issues/3129.
setup(
    entry_points={
        # fmt: off
        "console_scripts": [
            "foo-bar"
            "=foo.bar.:main",
        # fmt: on
            ]  # Includes an formatted indentation.
    },
)


# Regression test for https://github.com/psf/black/issues/2015.
run(
    # fmt: off
    [
        "ls",
        "-la",
    ]
    # fmt: on
    + path,
    check=True,
)


# Regression test for https://github.com/psf/black/issues/3026.
def test_func():
    # yapf: disable
    if  unformatted(  args  ):
        return True
    # yapf: enable
    elif b:
        return True

    return False


# Regression test for https://github.com/psf/black/issues/2567.
# fmt: off
for _ in range( 1 ):
    # fmt: on
    print ( "This won't be formatted" )
print ( "This won't be formatted either" )


# Regression test for https://github.com/psf/black/issues/3184.
class A:
    async def call(self):
        if self:
            # fmt: off
            if self[:4] in ("ABCD", "EFGH"):
                # fmt: on
                print ( "This won't be formatted" )

            elif self[:4] in ("ZZZZ",):
                print ( "This won't be formatted either" )

        print ( "This will be formatted" )


# Regression test for https://github.com/psf/black/issues/2985.
class Named(t.Protocol):
    # fmt: off
    @property
    def  this_wont_be_formatted ( self ) -> str: ...

class Factory(t.Protocol):
    def  this_will_be_formatted ( self, **kwargs ) -> Named: ...
    # fmt: on


# Regression test for https://github.com/psf/black/issues/3436.
if x:
    pass
elif   unformatted:
# fmt: on
    will_be_formatted  ()
