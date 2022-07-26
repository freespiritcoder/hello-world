
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from scripts import pre_test

if sys.argv[1] == "pre-check":
    obj = pre_test.greet()
    print(constants.STATUS)
