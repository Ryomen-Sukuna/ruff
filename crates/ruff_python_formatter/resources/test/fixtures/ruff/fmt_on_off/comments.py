a +   b # a trailing comment

# in between comments

# function comment
def test():
  # under indent

    def nested():
        ...

        # trailing comment that falls into the verbatim range
      # trailing outer comment
  # fmt: on

a +   b

def test():
    pass
    # fmt: off
    # a trailing comment

