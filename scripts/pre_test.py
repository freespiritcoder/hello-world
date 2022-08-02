
from bs4 import BeautifulSoup
import actions.constants as CT
import requests

def greet():
    res = requests.post("http://10.200.0.251:8445/query?db=psr&q=show+databases")
    if res.status_code == 200:
        print(res.json())
    else:
        raise RuntimeError("API called with error: {}".format(res.content))
    print("Hello, how was your day?!")
    print(CT.STATUS)

if __name__ == "__main__":
    greet()
