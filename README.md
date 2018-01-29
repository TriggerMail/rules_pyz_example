# Example rules_pyz project

This is a project that uses the [rules_pyz Bazel Python rules](https://github.com/TriggerMail/rules_pyz) to run a Python project that depends on some third-party libraries from PyPI. Notably, this is a demo based on a `rules_python` bug report, showing that third-party namespace packages work correctly: https://github.com/bazelbuild/rules_python/issues/14


## Demo usage

Run the command:

```bash
bazel run //:use_pypi_libs
```

You should see it print output. Most importantly, it manages to import the `google.cloud.*` APIs, which don't work with the native Bazel rules.


## Native libraries

This example depends on gRPC, which uses native code wheels. The pip_generate tool generates select statements in `third_party/pypi/pypi_rules.bzl` which work for Mac and Linux. To try it, run:

```bash
bazel build //...
./bazel-bin/grpc_helloworld_server

# in another shell:
./bazel-bin/grpc_helloworld_client
```

This should print: `Greeter client received: Hello, you!` which used the `grpcio` Pip native code wheels.
