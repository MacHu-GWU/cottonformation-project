# -*- coding: utf-8 -*-

import sys
from pathlib_mate import Path

dir_project_root = Path.dir_here(__file__).parent.parent

# ------------------------------------------------------------------------------
# Virtual Environment Related
# ------------------------------------------------------------------------------
dir_venv = Path(sys.executable).parent.parent
dir_venv_bin = dir_venv / "bin"

# virtualenv executable paths
bin_pytest = dir_venv_bin / "pytest"

# test related
dir_htmlcov = dir_project_root / "htmlcov"
dir_unit_test = dir_project_root / "tests"
dir_int_test = dir_project_root / "tests_int"
