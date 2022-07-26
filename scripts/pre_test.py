
from bs4 import BeautifulSoup
import actions.constants as CT

def greet():
    print("Hello, how was your day?!")
    print(CT.STATUS)

if __name__ == "__main__":
    greet()
