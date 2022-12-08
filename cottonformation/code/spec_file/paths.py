# -*- coding: utf-8 -*-

from pathlib_mate import Path

dir_project_root = Path.dir_here(__file__).parent.parent.parent
assert dir_project_root.joinpath("Makefile").exists()

path_cft_spec_json = dir_project_root / "cft-spec.json"
