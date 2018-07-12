import urllib2
import re
print "This is a fetch test"

response = urllib2.urlopen('https://www.azlyrics.com/lyrics/drake/inmyfeelings.html')
html = response.read()


def cleanhtml(raw_html):
    print "Cleaning text"
    cleanr1 = re.compile(r"(<.*?>|\[.*?\]|.*\(.*?\).*|\{((.|\n)*)\}|.*?;|\".*?\"|lyrics|.*\.com.*|[\{\}\(\)])", re.IGNORECASE) #removes HTML tags
    cleantext1 = re.sub(cleanr1, '', raw_html)
    empty_lines = re.compile(r"(\s){2}")
    cleantext2 = re.sub(empty_lines, ' ', cleantext1)
    print "Text Cleaned"
    return cleantext2

clean_text = cleanhtml(html)
print clean_text