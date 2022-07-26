
import sys
import scripts.pre-test
from scripts.actions import constants

if sys.argv[1] == "pre-check":
    obj = pre-test.greet()
    print(constants.STATUS)
