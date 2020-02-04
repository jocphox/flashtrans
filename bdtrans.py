import http.client
import hashlib
import urllib
import random
import json

def bdtranscn(text):
    return bdtrans(text,'zh')

def bdtransen(text):
    return bdtrans(text,'en')

def bdtrans(text,toLang='zh'):
    httpClient = None
    myurl = '/api/trans/vip/translate'
    appid = '20190911000333775'  # 填写你的appid
    secretKey = 'G5QDL9ZBgZpoltVwwMQa'  # 填写你的密钥
    if toLang=='zh':
        fromLang = 'en'   #原文语种
    else:
        fromLang='zh'
    salt = random.randint(32768, 65536)
    q=text
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
    salt) + '&sign=' + sign
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
      # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)
        trans=result['trans_result']
        an=lambda x:x['dst']
        return "\t".join(list(map(an, trans)))
        #print(result.type)
    except Exception as e:
        print (e)
    finally:
        if httpClient:
            httpClient.close()
if __name__ == '__main__':
    text="""
    Monkey likes banana very much.
	an apple.
    """

    bdtrans(text)