# Example rules_pyz project

This is a project that uses the [rules_pyz Bazel Python rules](https://github.com/TriggerMail/rules_pyz) to run a Python project that depends on some third-party libraries from PyPI. Notably, this is a demo based on a `rules_python` bug report, showing that third-party namespace packages work correctly: https://github.com/bazelbuild/rules_python/issues/14


## Usage

Run the command:

```bash
bazel run //:use_pypi_libs
```

You should see it print output. Most importantly, it manages to import the `google.cloud.*` APIs, which don't work with the native Bazel rules.
