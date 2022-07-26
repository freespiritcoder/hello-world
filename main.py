
import sys
import scripts.pre_test as PT

if sys.argv[1] == "pre-check":
    obj = PT.greet()
    print(constants.STATUS)
