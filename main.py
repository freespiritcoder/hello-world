
import sys
from .scripts import pre_test
from scripts.actions import constants

if sys.argv[1] == "pre-check":
    obj = pre_test.greet()
    print(constants.STATUS)
