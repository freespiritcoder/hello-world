
hello = greet.Greet()
print("Pre-checks status: {}".format(hello.greeting()))

if __name__ == "__main__":
    if __package__ is None:
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from actions import greet
    else:
        from .actions import greet
