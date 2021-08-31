# build-conda-action
[![Test](https://github.com/skyworksinc/ids-actions-build-conda/actions/workflows/test.yml/badge.svg)](https://github.com/skyworksinc/ids-actions-build-conda/actions/workflows/test.yml)
![v0.1.0](https://img.shields.io/badge/v-0.1.0-blue)

A Github Action for building an IDS conda package using 
[conda-build](https://docs.conda.io/projects/conda-build/en/latest/index.html).  It supports both GitHub hosted and 
self-hosted runners.  When it is run on a self-hosted runner, it builds with both the ids and dev channels included. 

# Usage

> Inputs are **NOT** required when using this action. They all have basic defaults and are only there to allow for more customization.

**Best Practices**
- Place customized _build.yml_ file at 'envs/build.yml'
- Need a "conda-recipe" package in the repository - or another package name that needs to be specified in the ${RECIPE_PATH} input section.

**Example Usage**

`job-name:` <br/>
&ensp;&ensp;&ensp;`runs-on: ubuntu-latest`<br/>
&ensp;&ensp;&ensp;`steps:`<br/>
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;`# Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it`<br/>
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;`- uses: actions/checkout@v2`<br/>
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;`# Runs the action with the following inputs or defaults if not specified.`<br/>
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;`- uses: cascode-labs/build-conda-action/action.yml@1`<br/>
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;`with:`<br/>
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;`RECIPE_PATH: '{NEW_RECIPE_PATH}'`<br/>
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;`BASE_ENV_PREFIX: '{NEW_BASE_PREFIX}'`<br/>
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;`PACKAGE_ARTIFACT_NAME: '{NEW_PACKAGE_NAME}'`<br/>
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;`TEST_RESULTS_ARTIFACT_NAME: '{NEW_TEST_RESULTS_NAME}'`<br/>
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;`BUILD_OPTIONS: '{NEW_CHANNELS_TO_USE}'`<br/>
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;`CONDA_BUILD_ENV_FILEPATH: '{NEW_BUILD_ENV_PATH}`<br/>
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;`- uses: actions/download-artifact@v2`

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