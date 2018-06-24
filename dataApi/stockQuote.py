import csv
import requests

URL = 'https://app.quotemedia.com/quotetools/getHistoryDownload.csv?&webmasterId=501&startDay=01&startMonth=05&startYear=2018&endDay=31&endMonth=05&endYear=2018&isRanged=true&symbol='

def getData(ticker):
    r = requests.get(URL+ticker)
    data = r.text
    res = {
        ticker: [],
        'over2count': 0
    }
    for line in csv.DictReader(data.splitlines(), skipinitialspace=True):
        if((float(line['high'])-float(line['low']))/float(line['low'])>0.05):
            res['over2count']=res['over2count']+1
        res[ticker].append(line)
    return res