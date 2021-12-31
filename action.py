import pathlib
import subprocess
from invoke import Context
from conda_api import info
from json import JSONDecoder
from typing import Union

PathLike = Union[str, Path]

def check_conda_recipe(recipe_path: PathLike) -> None:
    recipe_path = Path(recipe_path)
    if recipe_path.exists():
        print(f"Building the conda recipe at {recipe_path}")
    else:
        raise RuntimeError(f"ERROR: Unable to locate the conda \
                           recipe at ${recipe_path}")

def setup_build_env(ctx: Context, required_env_name: str,
                    build_env_filepath: str) -> None:
    info_result = info(ctx)
    if info_result["active_prefix_name"] == required_env_name:
        return
    elif find_env(info, required_env_name) is not None:
        update_env(build_env_file)
        return
    else:
        create_env(build_env_file)


def select_build_env_file(build_env_filepath: PathLike, 
                          action_path: str) -> Path:
    if build_env_filepath == 'action_default':
        print("Using the default conda environment definition")
        build_env_filepath = Path(action_path) / "envs" / "build.yml"
    elif Path(build_env_filepath).exists():
        print(f"Using the supplied build env yml file")
        build_env_filepath = Path(build_env_filepath)
    else:
        raise RuntimeError(f"Could not find build_env_filepath={build_env_filepath}")
    print(f"CONDA_BUILD_ENV_FILE: {build_env_filepath}")
    print("Contents:")
    with open(build_env_filepath, 'r') as file:
        print(file.read())
    return build_env_filepath

def select_build_env_name(build_env_name: str, build_env_filepath: PathLike, 
                          repo_name:str) -> str:
    if (build_env_name == 'action_default') and \
       (build_env_filepath == 'action_default') :

        print("Using the default conda environment ")
        build_env_name = "build-conda-action"
    elif (build_env_name == 'action_default') and \
         (build_env_filepath != 'action_default') :

        print("Using the default conda environment name with a custom env yml")
        build_env_name = f"{repo_name}-build"
    return build_env_name
  
if __name__ == '__main__':
    input_args = (
        "recipe_path",
        "conda_build_env_filepath",
        "conda_build_env_name",
        "build_options",
        "action_path",
        "repository_name",
        "runner_temp_folder",
        )
    if len(sys.argv) != len(input_args):
        print("Error: Wrong number of inputs!")
        print(f"\nNumber of inputs:{len(sys.argv)}")
        print(f"Inputs:\n {sys.argv}")
        sys.exit(1)
    else:
        pass
    build_conda_package()
