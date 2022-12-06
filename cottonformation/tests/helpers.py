# -*- coding: utf-8 -*-

import json
import subprocess

from .paths import dir_project_root, bin_pytest, dir_htmlcov


def jprint(data):
    print(json.dumps(data, indent=4))


def run_cov_test(test_file: str, module: str):
    args = [
        bin_pytest,
        "-s",
        "--tb=native",
        f"--rootdir={dir_project_root}",
        f"--cov={module}",
        "--cov-report",
        "term-missing",
        "--cov-report",
        f"html:{dir_htmlcov}",
        f"{test_file}",
    ]
    subprocess.run(args)
