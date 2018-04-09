# Dependencies required for rules_pyz
git_repository(
    name = "com_bluecore_rules_pyz",
    commit = "b65da7c4cd2d845e216539c12ea586bdb9f30820",
    remote = "https://github.com/TriggerMail/rules_pyz.git",
)

load("//third_party/pypi:pypi_rules.bzl", "pypi_repositories")
pypi_repositories()

load("@com_bluecore_rules_pyz//rules_python_zip:rules_python_zip.bzl", "pyz_repositories")

pyz_repositories()

# Dependencies needed to use PyPI rules
load("@com_bluecore_rules_pyz//pypi:pip.bzl", "pip_repositories")

pip_repositories()


