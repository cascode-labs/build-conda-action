from conda_api import info, find_env
# noinspection PyPackageRequirements
from invoke.context import Context


def test_info():
    ctx = Context()
    result = info(ctx)
    assert isinstance(result, dict)


def test_find_env():
    ctx = Context()
    result = find_env(ctx, "build-conda-action")
    assert isinstance(result, str)
