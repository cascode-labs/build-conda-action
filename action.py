import pathlib
import subprocess
from json import JSONDecoder

import conda


def check_conda_recipe(recipe_path: str) -> None:
    print("\nChecking for the Conda recipe")
    recipe_path = pathlib.Path(recipe_path)
    if recipe_path.exists():
        print(f"Building the conda recipe at {recipe_path}")
    else:
        print(f"ERROR: Unable to locate the conda recipe at ${recipe_path}")
        print("  Skipping the build of the conda package")
        exit(1)


def select_build_env_file(build_env_filepath: str) -> None:
    print("\nSelecting Build Env yml File")
    if (build_env_filepath == 'action_default') or \
       (not pathlib.Path(build_env_filepath).exists()):
        print("Using the default conda configuration")
        build_env_filepath = "${{ github.action_path }}/envs/build.yml"
    print(f"CONDA_BUILD_ENV_FILE: {build_env_filepath}")
    print("Contents:")
    with open(build_env_filepath, 'r') as file:
        print(file.read())

def check_conda_env(base_env_prefix: str) -> None:
    print("Checking that Conda is Initialized")
    try:
        info = subprocess.call(["conda", "info", "--json"])
        if info.returncode == 0:
            info = JSONDecoder(info.stdout)
        else:
            print("ERROR: Cannot find 'conda' command. "
                  "Conda is not initialized")
            raise FileNotFoundError()
        info.
    except FileNotFoundError:
        print("Conda must be initialized before calling Python")


def create_conda_env():
    if json
    echo "Conda is not setup.  Attempting to set it up."
    echo 'source ${{ inputs.base_env_prefix }}/etc/profile.d/conda.sh'
    source ${{ inputs.base_env_prefix }}/etc/profile.d/conda.sh
    if ! command -v conda &> /dev/null; then
    echo "ERROR: Failed to setup setup Conda"
    exit 1
    fi
    fi
    echo "  Conda is initialized"