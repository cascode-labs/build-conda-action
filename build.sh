#!/bin/bash

recipe_path=$1
conda_build_env_filepath=$2
base_env_prefix=$3
build_options=$4
action_path=$5
repository_name=$6
echo "recipe_path: ${recipe_path}"
echo "conda_build_env_filepath: ${conda_build_env_filepath}"
echo "base_env_prefix: ${base_env_prefix}"
echo "build_options: ${build_options}"
echo "action_path: ${action_path}"
echo "repository_name: ${repository_name}"

echo "::set-output name=PACKAGE_PATH::$(echo "None")"
echo "CHECKS"
echo "------"
echo "Checking for the Conda recipe"
if [ -d "${recipe_path}" ]; then
  echo "Building the conda recipe at ${recipe_path}"
else
  echo "Unable to locate the conda recipe at ${recipe_path}.
  Skipping the build of the conda package."
  exit 0
fi

echo ""
echo "Selecting Build Env yml File"
if [ "${conda_build_env_filepath}" = 'action_default' ]; then
  echo "Using the default conda configuration"
  CONDA_BUILD_ENV_FILE="${action_path}/envs/build.yml"
  BUILD_ENV_NAME="build-conda-action"
elif [ -f "${conda_build_env_filepath}" ]; then
  CONDA_BUILD_ENV_FILE=${conda_build_env_filepath}
  BUILD_ENV_NAME="${repository_name}-build"
else
  echo "Using the default conda configuration"
  CONDA_BUILD_ENV_FILE="${action_path}/envs/build.yml"
  BUILD_ENV_NAME="build-conda-action"
fi
echo "BUILD_ENV_NAME: ${BUILD_ENV_NAME}"
echo "CONDA_BUILD_ENV_FILE: ${CONDA_BUILD_ENV_FILE} ="
cat "${CONDA_BUILD_ENV_FILE}"


echo "Checking that Conda is Initialized"
if ! command -v conda &> /dev/null; then
  echo "Conda is not setup.  Attempting to set it up."
  echo "source ${base_env_prefix}/etc/profile.d/conda.sh"
  source "${base_env_prefix}/etc/profile.d/conda.sh"
  if ! command -v conda &> /dev/null; then
    echo "ERROR: Failed to setup setup Conda"
    exit 1
  fi
fi
echo "  Conda is initialized"

echo ""
echo "SETUP BUILD ENV"
echo "Set source"
echo "-----------------"
echo "Setting up ${BUILD_ENV_NAME} environment"
conda env update --name ${BUILD_ENV_NAME} \
                  --file "${CONDA_BUILD_ENV_FILE}"  || \
    conda env create -f "${CONDA_BUILD_ENV_FILE}"
conda activate ${BUILD_ENV_NAME}
echo "conda info"
conda info
echo ""
echo "conda list"
conda list

echo ""
echo "BUILD PACKAGE"
echo "-------------"
mkdir "test_results"
echo "the input for build options: ${build_options}"
echo "setting build options"
read -r -a BUILD_OPTIONS <<< "${build_options}"
echo "finished setting build options"
echo "BUILD_OPTIONS: " "${BUILD_OPTIONS[@]}"
OUT=$(conda build --output "${BUILD_OPTIONS[@]}" ${recipe_path})
echo "::set-output name=PACKAGE_PATH::$(echo $OUT)"
echo ""
echo "Package output path:"
echo "  $OUT"
echo ""
echo "conda build " "${BUILD_OPTIONS[@]}" "${recipe_path}"
conda build "${BUILD_OPTIONS[@]}" "${recipe_path}"
mkdir "${{runner.temp}/package_outputs"
cp -f "$OUT" "${{runner.temp}/package_outputs"
