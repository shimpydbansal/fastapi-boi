"""
Append the parent directory to the system path.

This ensures that modules from the parent directory can be imported when
tests or scripts are run from a sub-directory.
"""

import sys
import os

# Add the directory containing the main application to the system path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.append(parent_dir)
