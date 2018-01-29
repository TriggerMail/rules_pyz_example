load("@com_bluecore_rules_pyz//rules_python_zip:rules_python_zip.bzl",
    "pyz_binary", "pyz_library", "pyz_test",
)

pyz_binary(
    name="use_pypi_libs",
    srcs=["use_pypi_libs.py"],
    deps=[
        "//third_party/pypi:google_cloud_bigquery",
        "//third_party/pypi:google_cloud_storage",
    ],
)
