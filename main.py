#downloading an image using python code
import random
import urllib.request
def download_web_image(url):
    name = random.randrange(1, 100)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)
download_web_image("https://static3.bigstockphoto.com/1/2/3/large2/321033145.jpg")
