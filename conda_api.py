import pprint
import json
import pathlib
# noinspection PyPackageRequirements
from invoke.context import Context
# noinspection PyPackageRequirements
from fabric.connection import Connection
from typing import Union, Dict, Any
# noinspection PyPackageRequirements
from fabric.runners import Result

Ctx = Union[Context, Connection]


def info(ctx: Ctx) -> Dict[str, Any]:
    """Provides information about the conda environment"""
    result = ctx.run("conda info --json")
    if result.ok:
        return _load_json(result)
    else:
        print("ERROR: conda info failed")
        raise Exception("conda info failed")


def list_packages(ctx: Ctx, env_name: str = None) -> Dict[str, Any]:
    if env_name is None:
        result = ctx.run(f"conda list --json")
    else:
        result = ctx.run(f"conda list -n {env_name} --json")
    if result.ok:
        return _load_json(result)
    else:
        print("ERROR: conda info failed")
        raise Exception("conda info failed")


def find_env(ctx: Ctx, env_name: str) -> Union[str, None]:
    """Returns the prefix of the named environment"""
    info_result = info(ctx)
    prefixes = {}
    for env_prefix in info_result["envs"]:
        name = pathlib.Path(env_prefix).parts[-1]
        prefixes[name] = env_prefix
    if env_name in prefixes.keys():
        return prefixes[env_name]
    else:
        return None


def create_env(ctx: Ctx, env_file_path: str) -> Dict[str, Any]:
    result = ctx.run(f"conda env create -f {env_file_path} --json")
    if result.ok:
        return _load_json(result)
    else:
        print("ERROR: Could not create conda environment!")
        raise Exception()


def _load_json(result: Result) -> Dict[str, Any]:
    stdout = result.stdout
    stdout = stdout[stdout.find("{"):stdout.rfind("}")+1]
    return json.loads(stdout)


def update_env(ctx: Ctx, env_file_path: str):
    cmd = f"conda env update -f {env_file_path}"
    result = ctx.run(cmd)
    print(result.stdout)
    if result.returncode == 0:
        return
    else:
        print("ERROR: Could not update conda environment!")
        raise Exception()


if __name__ == '__main__':
    context = Context()
    pp = pprint.PrettyPrinter()
    pp.pprint(info(context))
