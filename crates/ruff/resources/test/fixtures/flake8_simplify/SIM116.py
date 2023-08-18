# Errors
a = "hello"

# OK
def no_return_in_else(platform):
    if platform == "linux":
        return "auditwheel repair -w {dest_dir} {wheel}"
    elif platform == "macos":
        return "delocate-wheel --require-archs {delocate_archs} -w {dest_dir} -v {wheel}"
    elif platform == "windows":
        return ""
    else:
        msg = f"Unknown platform: {platform!r}"
        raise ValueError(msg)
