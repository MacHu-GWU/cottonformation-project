#!/bin/bash
# -*- coding: utf-8 -*-

dir_here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
dir_bin="$(dirname "${dir_here}")"
dir_project_root=$(dirname "${dir_bin}")

source ${dir_bin}/py/python-env.sh

print_colored_line $color_cyan "[DOING] Run code coverage tests in ${path_test_dir} ..."
cd ${dir_project_root}
rm -r ${path_coverage_html_dir}
${bin_pytest} ${path_test_dir} -s --cov=${package_name} --cov-report term-missing --cov-report html:${path_coverage_html_dir}
