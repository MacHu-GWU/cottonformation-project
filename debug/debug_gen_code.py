# -*- coding: utf-8 -*-

"""
This script generate the code for ``cottonformation/res/...`` directory and
try to import everything. If there's any syntax error, we can catch it here.

Also this is part of the testing workflow. **Before we push code to CI,
We should run this script locally, and run test locally before commit the code.**
"""

from cottonformation.code.spec import remove_all_file, gen_code

# remove_all_file()
# gen_code(dry_run=False)

import cottonformation.res._imp
_ = cottonformation.res._imp