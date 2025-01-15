import re
def removeHTML(text):
    return re.sub(r'\<[^>]*\>', '', text)
from urllib import request
connect = request.urlopen("https://www.cbr.ru/key-indicators/")
text = connect.read().decode()
what = '<td class="value td-w-4 _bold _end mono-num">'
start = text.find(what)
end = text.find("<", start+len(what))

text1 = text[start:end]
print("Курс ЕВРО =", removeHTML(text1))