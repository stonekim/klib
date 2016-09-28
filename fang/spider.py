# -*- coding:utf-8 -*-
import os
import sys
import urllib
import requests

import handle as h


headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en,zh-CN;q=0.8,zh;q=0.6',
    'Cookie': 'ASP.NET_SessionId=tuj51x45wc4vkm45jmqd5n45; ASP.NET_SessionId_NS_Sig=oenCV6md3Xt641G_; countrytabs=0',
    'Referer': 'http://ris.szpl.gov.cn/credit/showcjgs/ysfcjgs.aspx?cjType=0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36',
    'X-MicrosoftAjax': 'Delta=true',
    'Host': 'ris.szpl.gov.cn',
    'Connection': 'keep-alive',
    'Cache-Control': 'no-cache',
    'Origin': 'http://ris.szpl.gov.cn',
    'Content-Type': 'application/x-www-form-urlencoded'
}


params = 'ctl00$ContentPlaceHolder1$scriptManager1=ctl00$ContentPlaceHolder1$updatepanel1|ctl00$ContentPlaceHolder1$hypYt&__EVENTTARGET=ctl00%24ContentPlaceHolder1%24hypYt&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=FatRHC4AyepRp3nKAdpN7VfgTCWp6KFqIE9DeK3bueiV8zHyoPeU%2FqTok%2FBnpNov7%2B%2FzhaNSYRNLrQOrY9GvFCmj%2F2naGQF0yOaTlyI0RlS0%2FXMZy4%2FXDtDRqklqfSKMaeW9IGASUrLITLyOxCNisDDoZD9ygoqelMz3cpBAUu6MNYn1OvKhBZT%2BHyaxlDREVOSdR%2BSBpZdSeVpuu0HgSvSkwetlThAqY1vERBKcPA7qQDh%2FB3tpxofD42F0bxnLFD%2BLn1TpRTtyrXgfmcE6E83zdUQBsQNPiUoGEFnl4j0aWxejagSyDHh2%2BKQWicCWNAtbu9bsgSs1DY5HVTEiQnwfQR6TjghwcEP3WBgeYMyRbuypVQ8%2F3ArWV4AvA6JmkxUZ%2FwbCzojn0tSl0%2BhtQ%2F%2FMx14PiPNicysHDQQgTTkvBnhNu0h6C5RkMyWGodct%2BZorIZq87aIsE7fT8BLZQU6%2BYKrAMCAvdu%2F1YBzkOebkbL6dJ%2FmXZPZ3lda%2BYV0sJi44UVlRGtDhJOWNa%2Be45%2BOY3dfWPA81M%2BZxfpWIPX5CHShepkuiISYq8TXKka3mGfBbAd%2BGigChs7Q6EfoBH4ffOJOdQHh0rowMF2znayvCS3BPhHuj8L1RL2kkHXi0zK2WP7OsI12M0LGFStlYWUmPiEx%2FOnBZBEi0czJKHHMmn%2F0UerLVYu7yoS5CH8Knc04kcZtCjDTpywmMl6hGZ1ui%2FsWw8ab27QzDi2%2BRyAQdnQZVGD3h28N4T9rDx43pnPUqBgc4Gj%2BFR3zUJycc2FldGHGTiSaYRd%2Bzr4jGSt%2FOKgf4UXCOIo4EGMevnJwNdGeA32PtVlFylYvBnRX6UoLcnA1BiKD943UL235KWKYqWoMNaKH%2FVzZvbanfviIL8SAfFThmXsPeiouOwq9EDmAzkDcCnTbYowoGa00pVwUdurQW602Yr%2FBYTtqoPJX8nUXOeDZvNsMf8KKcyN27PGcZw7iXSuEXgOQzMe6K4aE1uRdsp3lw7r7KqHaGknbuBZd3%2BsVExvf7f0HWCGayTKsysCKfk1Ij1bL35Mf1FokeziJ9rqKSbuPMuvcQ9%2BSurHJ0w84YizH788C2JRtPWtSd3srgl5bC3Wqs119UkyhgqE%2BzE44AwnQc0%2F6zkuD9ju2e9W8n20%2BSgYAtsRfnYh%2BqAfr1gDSdsj7zDFi9Kx9eMkt9Y0iPvEW8%2Bdv5RR8oSh389o3D8asOsT9vdEyAb6lsrI5VjIEh%2FwZxSk1YqhjpTl5L8jh8Z5zEkYMsoTX%2FcmwLkbOH%2B%2BnvQAfulkDpSQuUvuK4tGjfHcYL9x2tXOJpG2By3kUA4rQzjOiyEMEh1cOlWxR3n%2FZMHW3kKrukyIyEWuiwH2qvj%2B61apdQ%2FKTrOC1mtbGTr6%2FAde3igyxYU2qybvVz9GSIgWM%2FYq80SsmtCzZ5aRahPgCFpmEr1vuB68vQEWdKPrFTeSIAwmcoMP82DPPJwW9gpb4VznBa8OuRxep28nZu6duSN9KQwwLanXdx8yLBCDH4%2FscboBV9V6ND%2FETM%2BnL%2B5XUGTBlFT%2BG7ETGazhEQHnHYLNHNCgaExZ9yWtd4jBwK215KNRdUBX7vVl41XyMJeYk3KvcQGyG56wZv3ECzFO2YZ5D%2FeVNMMwv%2BMaMkgOBQ4ersBERLQkYXDmKD2VN86f%2Bz2y9pOIMLfAO3l4ei5tqnk2C31SjiB910L%2FcgsCogBzsAM44caUVaug%3D%3D&__VIEWSTATEGENERATOR=9030114A&__VIEWSTATEENCRYPTED=&__EVENTVALIDATION=5FNWEGWX9fnpyCBM%2FgIafmyLIaovbokrkCijw1B2G8eWRAgAucMBmN%2FRGUJspDCdAvpZqedMuBmvsbFPMTlq%2BdhRq8jEzfergWvEYqxwz14SOqfojWy4ecATo3fPgxVZECidS5kuawehPEG5IUq0%2B8yMP7bR7in0RiifANg%2BIr5GTsQ3&ctl00$ContentPlaceHolder1$radSelect=0&'

districts = ['Ns', 'Ba', 'Lg', 'Yt', 'Lh', 'Ft', 'All']
url = 'http://ris.szpl.gov.cn/credit/showcjgs/ysfcjgs.aspx?cjType=0'

for dis in districts:
    r = requests.post(url, data=params.replace('Yt', dis), headers=headers)
    with open(dis, 'w') as fp:
        fp.writelines(r.text.encode('utf8'))       
    h.fetch_data(dis)
