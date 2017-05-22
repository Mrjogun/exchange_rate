import time
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

def 환율(last,ex):
    url = "http://info.finance.naver.com/marketindex/exchangeDegreeCountQuote.nhn?marketindexCd=FX_"+ex+"KRW_SHB"
    html = urlopen(url)
    soup = bs(html,"html.parser")
    tbody = soup.find('tbody')
    now = tbody.find('tr').findAll('td')
    times = str(now[0]).split(">")[1].split("<")[0]
    if last !=times:
        last = times
        매매기준율 = str(now[1]).split(">")[1].split("<")[0].split(",")
        살때 = str(now[3]).split(">")[1].split("<")[0].split(",")
        if len(매매기준율) == 2:
            매매기준율 = float(매매기준율[0] + 매매기준율[1])
        else:
            매매기준율 = float(매매기준율[0])
        if len(살때) == 2:
            살때 = round(매매기준율 + (float(살때[0] + 살때[1]) - 매매기준율) * 0.1,2)
        else:
            살때 = round(매매기준율 + (float(살때[0]) - 매매기준율) * 0.1,2)
        print(times+"차\n매매기준율:", 매매기준율, "\t살때:", 살때)
    html.close()
    return last

last = "0회"
last = 환율(last,"JPY")
while True:
    time.sleep(15)
    last = 환율(last,"JPY")
