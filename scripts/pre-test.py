
def greet():
    hello = greet.Greet()
    print("Pre-checks status: {}".format(hello.greeting()))

if __name__ == "__main__":
    if __package__ is None:
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        print(sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) ))
        from actions.greet import Greet
    else:
        from .actions import greet
    
    greet()
