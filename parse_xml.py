from xml.etree.ElementTree import fromstring

from bs4 import BeautifulSoup
import requests
from lxml import etree


def parse_xml():
  url = "http://upload.itcollege.ee/~aleksei/test.xml"
  xml_content = requests.get(url).content
  soup = BeautifulSoup(xml_content, 'xml')
  
  # your code here

  result = ""

  x = soup.get_text("</data>")
  y = soup.getText("</data>")

  return x.split()[1].strip()


print(parse_xml())
