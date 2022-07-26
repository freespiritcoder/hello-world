
import sys
from scripts import pre-test
from scripts.actions import constants

if sys.argv[1] == "pre-check":
    obj = pre-test.greet()
    print(constants.STATUS)
