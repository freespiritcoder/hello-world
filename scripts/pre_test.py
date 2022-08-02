
import actions.constants as CT
import requests

def greet():
    if res.status_code == 200:
        print(res.json())
    else:
        raise RuntimeError("API called with error: {}".format(res.content))
    print("Hello, how was your day?!")
    print(CT.STATUS)

if __name__ == "__main__":
    greet()
