"""
Append the parent directory to the system path.

This ensures that modules from the parent directory can be imported when
tests or scripts are run from a sub-directory.
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
