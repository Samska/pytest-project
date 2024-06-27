import os
import sys

#Include parent directory of conftest making project root visible
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))