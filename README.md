
[![Test](https://github.com/cascode-labs/build-conda-action/actions/workflows/test.yml/badge.svg)](https://github.com/cascode-labs/build-conda-action/actions/workflows/test.yml)
![v0.1.4](https://img.shields.io/badge/v-0.1.4-blue)

<br />
<p align="center">
  <a href="https://github.com/cascode-labs/build-conda-action">
    <img src="images/conda_logo.png" alt="Conda Logo">
  </a>

  <h1 align="center">build-conda-action</h1>

  <p align="center">
    A GitHub action that builds a Conda recipe
    <br />
    <br />
    <a href="https://github.com/marketplace/actions/build-conda">Action Marketplace</a>
    ·
    <a href="https://github.com/cascode-labs/conda-build-action/issues">Report Bug</a>
    ·
    <a href="https://github.com/cascode-labs/conda-build-action/issues">Request Feature</a>
  </p>
</p>

A Github Action for building a [Conda](https://docs.conda.io/en/latest/) 
package stored in the project using 
[conda-build](https://docs.conda.io/projects/conda-build/en/latest/index.html).
It is meant to be simple to use with reasonable defaults that should work 
without any inputs when your project Conda configuration is setup according to 
the guidelines. However it also supports powerful customization of the conda 
build configuration through the inputs. It supports both GitHub hosted and 
self-hosted runners by setting the "base_env_prefix" input.

## Getting Started

> All inputs are optional. Just Follow the project configuration guidelines 
> below

### Standard Conda Configuration for Basic Operation

- Name the conda recipe folder "conda-recipe"
- Place any test result, lint, or other build outputs you'd like uploaded as 
  artifacts in a "test_results" folder
- The build environment will contain Conda, Conda-build, and Conda-verify by
  default.  
  > The build environment can be customized using the 
  > _conda_build_env_filepath_ input.  Include just the packages needed to 
  > **build** the package.  Packages required to test or run the project are 
  > specified in the recipe's meta.yml.
  
### Basic Usage

```yaml
job-name:
  runs-on: 'ubuntu-latest'
  steps:
    - uses: actions/checkout@v4
    # Builds the package using the standard configuration
    - uses: cascode-labs/build-conda-action/action.yml@v0
```

## Custom Configuration

### Inputs

- **recipe_path**: The path to the Conda recipe from the repo root.  
  Default: 'conda-recipe' 
- **conda_build_env_filepath**: Path to a custom build 
  [yml env definition file](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#create-env-file-manually)
  > Best Practice: If you need to customize the build environment, place a
  > customized _build.yml_ file at 'envs/build.yml'
- **base_env_prefix**:  The prefix of the base Conda environment.  
  Default: '/usr/share/miniconda'
  > Use this input for initializing the base environment of a self-hosted 
  > runner by providing the base environment prefix of the runner
- **package_artifact_name**:  The display name of the uploaded package 
  artifact.  
  Default: 'conda_package'
- **test_results_artifact_name**:  The display name of the uploaded test 
  results artifact.  
  Default: 'test_results'
- **build_options**: Options to be passed to conda-build to customize the build
  configuration.  For example, you can provide a different set of channels.  
  Default: '-c defaults -c conda-forge'
  
### Outputs

- **package-filepath**: The file path of the generated package.  It will 
  return "None" if no package was created.
  > The folder "built_package_outputs" is reserved for the build process.
  > It is used to assemble the package to be uploaded as artifacts

### Artifacts Uploaded

The following are uploaded to the run as artifacts.

- **Conda packages**: The built Conda packages
- **Test Results**:  Any additional testing or build artifacts that are copied
  into the _test_results_ folder.  Examples include test results, test reports, 
  lint reports or coverage reports.

### Example customized workflow

```yaml
job-name:
  runs-on: 'ubuntu-latest'
  steps:
    - uses: actions/checkout@v4
    # Initializes Conda on a GitHub hosted Runner
    - uses: conda-incubator/setup-miniconda@v2
      with:
        python-version: 3.7
    # Runs the action with the following inputs or defaults if not specified.
    - uses: cascode-labs/build-conda-action/action.yml@v0
      with:
        recipe_path: '{NEW_RECIPE_PATH}'
        base_env_prefix: '{NEW_BASE_PREFIX}'
        package_artifact_name: '{NEW_PACKAGE_NAME}'
        test_results_artifact_name: '{NEW_TEST_RESULTS_NAME}'
        build_options: '{NEW_CHANNELS_TO_USE}'
        conda_build_env_filepath: '{NEW_BUILD_ENV_PATH}'
```

## Roadmap

See the 
[open issues](https://github.com/cascode-labs/build-conda-action/issues)
for a list of proposed features (and known issues).
[Milestones](https://github.com/cascode-labs/build-conda-action/milestones)
outline the release version of each issue.

## Contributing

Contributions are what make the open source community such an amazing place to 
learn, inspire, and create. Any contributions you make are 
**greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Testing

This repo contains a test workflow with each job of the workflow as a different
test case.
