load(
    "@com_bluecore_rules_pyz//rules_python_zip:rules_python_zip.bzl",
    "pyz_binary",
    "pyz_library",
    "pyz_test",
)

pyz_binary(
    name = "use_pypi_libs",
    srcs = ["use_pypi_libs.py"],
    deps = [
        "//third_party/pypi:google_cloud_bigquery",
        "//third_party/pypi:google_cloud_storage",
    ],
)

pyz_binary(
    name = "grpc_helloworld_client",
    srcs = [
        "grpc_helloworld_client.py",
        "helloworld_pb2.py",
        "helloworld_pb2_grpc.py",
    ],
    deps = [
        "//third_party/pypi:grpcio",
    ],
)

pyz_binary(
    name = "grpc_helloworld_server",
    srcs = [
        "grpc_helloworld_server.py",
        "helloworld_pb2.py",
        "helloworld_pb2_grpc.py",
    ],
    deps = [
        "//third_party/pypi:grpcio",
    ],
)

pyz_test(
    name = "example_test",
    srcs = ["example_test.py"],
)
