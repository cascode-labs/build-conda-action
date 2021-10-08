import pathlib
import subprocess
from invoke import Context
from conda_api import info
from json import JSONDecoder
from typing import Union


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


def select_build_env_file(build_env_filepath: str, default_env_filepath=None) -> str:
    print("\nSelecting Build Env yml File")
    if (build_env_filepath == 'action_default') or \
       (not pathlib.Path(build_env_filepath).exists()):
        print("Using the default conda configuration")
        build_env_filepath = default_env_filepath
    print(f"CONDA_BUILD_ENV_FILE: {build_env_filepath}")
    print("Contents:")
    with open(build_env_filepath, 'r') as file:
        print(file.read())
    return build_env_filepath


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Error: Wrong number of inputs to combine_release_notes.py!")
        print(sys.argv)
        print("\nNumber of inputs:")
        print(len(sys.argv))
        sys.exit(1)
    else:
        release_notes_folder_path = sys.argv[1]
        release_notes_summary_path = sys.argv[2]
    build_conda_package()