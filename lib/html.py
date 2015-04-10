from HTMLParser import HTMLParser
from re import sub
from urllib import urlopen
#=========================================================================================
class HTMLParserT(HTMLParser):
    """this class finds the text in a page by overwritting handlers methods
        and return the text by getText method."""
    def __init__(self):
        
        HTMLParser.__init__(self)
        self.text = []

    def handle_data(self, data):
        text = data.strip()
        if len(text) > 0:
            text = sub('[ \t\r\n]+', ' ', text)
            self.text.append(text + ' ')

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.text.append('\n\n')
        elif tag == 'br':
            self.text.append('\n')

    def handle_startendtag(self, tag, attrs):
        if tag == 'br':
            self.text.append('\n\n')

    def getText(self):
        "returns the text in a page"
        return ''.join(self.text).strip()


def findText(text):
    """creates an  object from htmlparsert and returns the text"""
    try:
        parser = HTMLParserT()
        parser.feed(text)
        parser.close()
        return parser.getText()
    except:
        return 'text not found !'

