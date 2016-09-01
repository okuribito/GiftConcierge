import urllib.request as urlreq
import urllib.parse
from bs4 import BeautifulSoup

def morpheme(string):
    url = "http://jlp.yahooapis.jp/MAService/V1/parse?"
    appid = ""
    query = "&results=ma,uniq&uniq_filter=9%7C10"
    sentence = "&sentence=" + urllib.parse.quote(string)
    
    morphemelist = urlreq.urlopen(url+ appid + query + sentence)
    text = morphemelist.read().decode("utf-8")
    
    soup = BeautifulSoup(text)
    wordlist = soup.find_all("surface")
    morphlist = soup.find_all("pos")
    returnlist = []
    for i in range(len(wordlist)):
        morph = str(morphlist[i].string)
        if  morph == "名詞" or morph == "形容詞":
            #print("true",i, str(morphlist[i].string))
            returnlist.append(str(wordlist[i].string))
    
    return returnlist
~
~
~
~
~
~
~
~
~
