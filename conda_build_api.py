import pathlib
from conda_api import Ctx


def build_conda_package(ctx: Ctx, recipe_path: str, input_options: str = None):
    """Builds a conda package with the given recipe and input options."""
    print(f"Building recipe at:\n  {recipe_path}")
    check_conda_recipe(recipe_path)
    if check_conda_recipe(recipe_path):
        if (input_options is not None) or \
           (input_options != "None"):
            ctx.run(f"conda build {recipe_path}")
        else:
            ctx.run(f"conda build {input_options} {recipe_path}")
    else:
        print(f"ERROR: Cannot find conda recipe at:\n  {recipe_path}")
        raise FileNotFoundError()


def check_conda_recipe(recipe_path: str) -> bool:
    print(f"Checking the existence of the Conda recipe at:\n  {recipe_path}\n")
    recipe_path = pathlib.Path(recipe_path)
    result = recipe_path.exists()
    if not result:
        print("ERROR: Conda recipe does not exist!")
    return result
