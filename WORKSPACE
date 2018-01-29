# Dependencies required for rules_pyz
git_repository(
    name = "com_bluecore_rules_pyz",
    remote = "https://github.com/TriggerMail/rules_pyz.git",
    commit = "a539c6c938db75fa871e8611764f41fc0c35254b",
)
load("@com_bluecore_rules_pyz//rules_python_zip:rules_python_zip.bzl", "pyz_repositories")
pyz_repositories()

# Dependencies needed to use PyPI rules
load("@com_bluecore_rules_pyz//pypi:pip.bzl", "pip_repositories")
pip_repositories()
load("//third_party/pypi:pypi_rules.bzl", "pypi_repositories")
pypi_repositories()
