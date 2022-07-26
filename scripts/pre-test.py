from .actions import greet

hello = greet.Greet()
print("Pre-checks status: {}".format(hello.greeting()))
