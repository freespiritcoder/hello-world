
import sys
import scripts.pre_test as PT
import scripts.actions.constants as CONST

if sys.argv[1] == "pre-check":
    obj = PT.greet()
    print(CONST.STATUS)
