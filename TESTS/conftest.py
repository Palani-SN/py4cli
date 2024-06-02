"""
    Dummy conftest.py for sampleproject.

    If you don't know what this is for, just leave it empty.
    Read more about conftest.py under:
    - https://docs.pytest.org/en/stable/fixture.html
    - https://docs.pytest.org/en/stable/writing_plugins.html
"""

# import pytest
DEBUG = True

import os
import shutil

if not os.path.exists('res_files'):
    os.makedirs('res_files', exist_ok=True)
else:
    shutil.rmtree(f'res_files{os.sep}')
    os.makedirs('res_files', exist_ok=True)

if not os.path.exists('ref_files'):
    os.makedirs('ref_files', exist_ok=True)
