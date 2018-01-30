# Dependencies required for rules_pyz
git_repository(
    name = "com_bluecore_rules_pyz",
    commit = "a7322c7b32a7e5f924d5f90369384b2dc63abe70",
    remote = "https://github.com/TriggerMail/rules_pyz.git",
)

load("@com_bluecore_rules_pyz//rules_python_zip:rules_python_zip.bzl", "pyz_repositories")

pyz_repositories()

# Dependencies needed to use PyPI rules
load("@com_bluecore_rules_pyz//pypi:pip.bzl", "pip_repositories")

pip_repositories()

load("//third_party/pypi:pypi_rules.bzl", "pypi_repositories")

pypi_repositories()
