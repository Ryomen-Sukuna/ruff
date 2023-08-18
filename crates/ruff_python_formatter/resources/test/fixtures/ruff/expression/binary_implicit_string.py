
raise ImproperlyConfigured(
    "The app module %r has multiple filesystem locations (%r); "
    "you must configure this app with an AppConfig subclass "
    "with a 'path' class attr                               ibute." % (module, paths)
)

def test():
    return (
        "\n%(modified_count)s %(identifier)s %(action)s"
        "%(destination)s%(unmodified)s%(post_processed)s."
        % {
            "modified_count": modified_count,
            "identifier": "static file" + ("" if modified_count == 1 else "s"),
            "action": "symlinked" if self.symlink else "copied",
            "destination": f" to '{destination_path}'"
            if destination_path
            else "",
            "unmodified": f", {unmodified_count} unmodified"
            if collected["unmodified"]
            else "",
            "post_processed": collected["post_processed"]
            and f", {post_processed_count} post-processed"
            or "",
        }
    )

# trailing expression comment
self._assert_skipping(
    SkipTestCase("test_foo").test_foo,
    ValueError,
    "skipUnlessDBFeature cannot be used on test_foo (test_utils.tests."
    "SkippingTestCase.test_skip_unless_db_feature.<locals>.SkipTestCase%s) "
    "as SkippingTestCase.test_skip_unless_db_feature.<locals>.SkipTestCase "
    "doesn't allow queries against the 'default' database."
    # Python 3.11 uses fully qualified test name in the output.
    % (".test_foo" if PY311 else ""),
    )

# dangling operator comment
self._assert_skipping(
    SkipTestCase("test_foo").test_foo,
    ValueError,
    "skipUnlessDBFeature cannot be used on test_foo (test_utils.tests."
    "SkippingTestCase.test_skip_unless_db_feature.<locals>.SkipTestCase%s) "
    "as SkippingTestCase.test_skip_unless_db_feature.<locals>.SkipTestCase "
    "doesn't allow queries against the 'default' database."
    % # Python 3.11 uses fully qualified test name in the output.
    (".test_foo" if PY311 else ""),
    )

# Black keeps as many operands as fit on the same line as the `%`. Ruff does not. This is intentional as these are rare and complicated things significantly
(
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    "bbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    "cccccccccccccccccccccccccc"
    % aaaaaaaaaaaa
    + x
)

(
    b + c + d +
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    "bbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    "cccccccccccccccccccccccccc"
    % aaaaaaaaaaaa
    + x
)

(
    b < c > d <
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    "bbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    "cccccccccccccccccccccccccc"
    % aaaaaaaaaaaa
    > x
)


self.assertEqual(
    response.status_code,
    status_code,
    msg_prefix + "Couldn't retrieve content: Response code was %d"
                 " (expected %d)" % (response.status_code, status_code),
)

def test():
    return (
       "((TIME_TO_SEC(%(lhs)s) * 1000000 + MICROSECOND(%(lhs)s)) -"
       " (TIME_TO_SEC(%(rhs)s) * 1000000 + MICROSECOND(%(rhs)s)))"
   ) % {"lhs": lhs_sql, "rhs": rhs_sql}, tuple(lhs_params) * 2 + tuple(rhs_params) * 2

def test2():
    return (
        f'RETURNING {", ".join(field_names)} INTO {", ".join(["%s"] * len(params))}',
        tuple(params),
    )

def test3():
    return (
               "(CASE WHEN JSON_TYPE(%s, %%s) IN (%s) "
               "THEN JSON_TYPE(%s, %%s) ELSE JSON_EXTRACT(%s, %%s) END)"
           ) % (lhs, datatype_values, lhs, lhs), (tuple(params) + (json_path,)) * 3
