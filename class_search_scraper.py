import urllib.request
from bs4 import BeautifulSoup

def get_class_data(classNum):
    url = "https://webapp4.asu.edu/catalog/classlist?t=2197&k=" + classNum + "&k=" + classNum +" &hon=F&promod=F&e=all&page=1"
