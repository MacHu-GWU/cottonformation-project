#!/bin/bash
# -*- coding: utf-8 -*-
#
# Python dev environment tools.
#
# This script should be sourced to use.
#
# This file is generated by cookiecutter-pygitrepo 0.0.5: https://github.com/MacHu-GWU/cookiecutter-pygitrepo/tree/0.0.5

if [ -n "${BASH_SOURCE}" ]
then
    dir_here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
else
    dir_here="$( cd "$(dirname "$0")" ; pwd -P )"
fi
dir_bin="$(dirname "${dir_here}")"
dir_project_root=$(dirname "${dir_bin}")

source ${dir_bin}/settings.sh
source ${dir_bin}/source/detect-os.sh
source ${dir_bin}/source/helpers.sh
source ${dir_bin}/aws/aws-env.sh

# Virtualenv Name
venv_name="${package_name}_venv"

# Full Python Version
py_version="${py_ver_major}.${py_ver_minor}.${py_ver_micro}"
py_version_major_and_minor="${py_ver_major}.${py_ver_minor}"


resolve_important_path()
{
    local tmp_dir_project_root=$1

    path_readme=${tmp_dir_project_root}/README.rst

    path_sphinx_doc=${tmp_dir_project_root}/docs
    path_sphinx_doc_source=${tmp_dir_project_root}/docs/source
    path_sphinx_doc_build=${tmp_dir_project_root}/docs/build

    path_sphinx_doc_build_html=${path_sphinx_doc_build}/html
    path_sphinx_index_html=${path_sphinx_doc_build}/html/index.html

    path_sphinx_config=${path_sphinx_doc_source}/conf.py

    path_version_file=${tmp_dir_project_root}/${package_name}/_version.py

    path_requirement_file=${tmp_dir_project_root}/requirements.txt
    path_dev_requirement_file=${tmp_dir_project_root}/requirements-dev.txt
    path_doc_requirement_file=${tmp_dir_project_root}/requirements-doc.txt
    path_test_requirement_file=${tmp_dir_project_root}/requirements-test.txt

    path_test_dir=${tmp_dir_project_root}/tests
    path_coverage_html_dir=${tmp_dir_project_root}/htmlcov
    path_tox_dir=${tmp_dir_project_root}/.tox

    path_auto_pep8_script=${tmp_dir_project_root}/fix_code_style.py

    path_build_dir=${tmp_dir_project_root}/build
    path_dist_dir=${tmp_dir_project_root}/dist
    path_egg_dir=${tmp_dir_project_root}/${package_name}.egg-info
    path_pytest_cache_dir=${tmp_dir_project_root}/.pytest_cache
}

resolve_important_path ${dir_project_root}


resolve_venv_bin()
{
    # python virtual environment bin directory
    local tmp_dir_venv_bin=$1

    bin_activate="${tmp_dir_venv_bin}/activate"
    bin_python="${tmp_dir_venv_bin}/python"
    bin_pip="${tmp_dir_venv_bin}/pip"
    bin_pytest="${tmp_dir_venv_bin}/pytest"
    bin_sphinx_start="${tmp_dir_venv_bin}/sphinx-quickstart"
    bin_twine="${tmp_dir_venv_bin}/twine"
    bin_tox="${tmp_dir_venv_bin}/tox"
    bin_jupyter="${tmp_dir_venv_bin}/jupyter"
    bin_aws="${tmp_dir_venv_bin}/aws"
}


resolve_other_venv_dir_on_windows()
{
    # python virtual environment directory
    local tmp_dir_venv=$1

    dir_venv_bin="${tmp_dir_venv}/Scripts"
    dir_venv_site_packages="${tmp_dir_venv}/Lib/site-packages"
    dir_venv_site_packages64="${tmp_dir_venv}/Lib64/site-packages"
}


resolve_other_venv_dir_on_darwin_or_linux()
{
    # python virtual environment directory
    local tmp_dir_venv=$1
    # python major and minor version, example: 2.7 or 3.6
    local tmp_py_version_major_and_minor=$2

    dir_venv_bin="${tmp_dir_venv}/bin"
    dir_venv_site_packages="${tmp_dir_venv}/lib/python${tmp_py_version_major_and_minor}/site-packages"
    dir_venv_site_packages64="${tmp_dir_venv}/lib64/python${tmp_py_version_major_and_minor}/site-packages"
}


# --- resolve venv
resolve_windows_venv()
{
    local tmp_venv_name=$1
    local tmp_py_version_major_and_minor=$2

    local tmp_dir_envs="${HOMEPATH}/venvs/python/${tmp_py_version_major_and_minor}"
    mkdir -p ${tmp_dir_envs}
    dir_venv="${tmp_dir_envs}/${tmp_venv_name}"
    resolve_other_venv_dir_on_windows ${dir_venv}
    resolve_venv_bin ${dir_venv_bin}
}


resolve_mac_pyenv()
{
    local tmp_venv_name=$1
    local tmp_py_version=$2
    local tmp_py_version_major_and_minor=$3

    dir_venv="${HOME}/.pyenv/versions/${tmp_py_version}/envs/${tmp_venv_name}"
    resolve_other_venv_dir_on_darwin_or_linux ${dir_venv} ${tmp_py_version_major_and_minor}
    resolve_venv_bin ${dir_venv_bin}
}


resolve_mac_venv()
{
    local tmp_venv_name=$1
    local tmp_py_version=$2
    local tmp_py_version_major_and_minor=$3

    local tmp_dir_envs="${HOME}/venvs/python/${tmp_py_version}"
    mkdir -p ${tmp_dir_envs}
    dir_venv="${tmp_dir_envs}/${tmp_venv_name}"
    resolve_other_venv_dir_on_darwin_or_linux ${dir_venv} ${tmp_py_version_major_and_minor}
    resolve_venv_bin ${dir_venv_bin}
}


resolve_linux_pyenv() {
    resolve_mac_pyenv $1 $2 $3
}


resolve_linux_venv() {
    resolve_mac_venv $1 $2 $3
}


if [ "${os_is_windows}" = "Y" ]
then
    bin_global_python="/c/Python${py_ver_major}${py_ver_minor}/python.exe"
    resolve_windows_venv ${venv_name} ${py_version_major_and_minor}
elif [ "${os_is_darwin}" = "Y" ]
then
    bin_global_python="python${py_ver_major}.${py_ver_minor}"
    bin_global_python="$(which ${bin_global_python})"
    if [ "${use_pyenv}" = "Y" ]
    then
        resolve_mac_pyenv ${venv_name} ${py_version} ${py_version_major_and_minor}
    else
        resolve_mac_venv ${venv_name} ${py_version} ${py_version_major_and_minor}
    fi
elif [ "${os_is_linux}" = "Y" ]
then
    bin_global_python="python${py_ver_major}.${py_ver_minor}"
    bin_global_python="$(which ${bin_global_python})"
    if [ "${use_pyenv}" = "Y" ]
    then
        resolve_linux_pyenv ${venv_name} ${py_version} ${py_version_major_and_minor}
    else
        resolve_linux_venv ${venv_name} ${py_version} ${py_version_major_and_minor}
    fi
fi


# Doc Relative Variables
package_version=$(python ${path_version_file})

rtd_url="https://${rtd_project_name}.readthedocs.io/"
rtd_project_url="https://readthedocs.org/projects/${package_name}/"
s3_uri_doc_versioned="s3://${s3_bucket_doc_host}/docs/${package_name}/${package_version}"
s3_uri_doc_latest="s3://${s3_bucket_doc_host}/docs/${package_name}/latest"
s3_doc_url="${s3_bucket_doc_host}.s3.amazonaws.com/docs/${package_name}/latest/index.html"


# Deploy sphinx generated html doc to s3 bucket
deploy_doc_to_s3() {
    local tmp_path_sphinx_doc_build_html="$1" # html doc dir
    local tmp_s3_uri_doc="$2" # uri of dir on s3

    echo "remove existing doc on ${tmp_s3_uri_doc}"
    aws s3 rm ${tmp_s3_uri_doc} \
        --recursive \
        --only-show-errors \
        ${aws_cli_profile_arg}

    echo "upload doc to ${tmp_s3_uri_doc}"
    aws s3 sync ${tmp_path_sphinx_doc_build_html} ${tmp_s3_uri_doc} \
        --only-show-errors \
        ${aws_cli_profile_arg}
}
