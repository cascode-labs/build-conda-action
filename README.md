# build-conda-action
[![Test](https://github.com/skyworksinc/ids-actions-build-conda/actions/workflows/test.yml/badge.svg)](https://github.com/skyworksinc/ids-actions-build-conda/actions/workflows/test.yml)
![v0.1.0](https://img.shields.io/badge/v-0.1.0-blue)

A Github Action for building an IDS conda package using 
[conda-build](https://docs.conda.io/projects/conda-build/en/latest/index.html).  It supports both GitHub hosted and 
self-hosted runners.  When it is run on a self-hosted runner, it builds with both the ids and dev channels included. 

# Usage
TODO: 

# Inputs
- **recipe_path**: The path to the recipe from the repo root.  Optional, default: 'conda-recipe'
- **base_env_prefix**:  The prefix of the base Conda environment.  Optional, default: '/prj/ids/ids-conda/envs/anaconda'
- **package_artifact_name**:  The display name of the uploaded package artifact.  Optional, default: 'conda_package'
- **test_results_artifact_name**:  The display name of the uploaded test results artifact.  Optional, default: 'test_results'

# Outputs:
- **package-filepath**: The file path of the generated package.  It will return "None" if no package was created.

# Project Requirements
The Conda recipe's tests should copy their results, including any test or lint reports to the "test_results" folder.
Then the folder will be uploaded as an artifact.

The project also needs to have a build environment definition file at "envs/build.yml".  This should include all the 
packages required to build the package.

# Contributing

## Testing
This repo contains a test workflow with each job of the workflow as a different test case.