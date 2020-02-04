from aip import AipOcr
import configparser
from getnewrow import newrow
import baiduAPIPassword as pd
class BaiduAPI:
    'using baidu api'
    def __init__(self):
        app_id= pd.APP_ID
        api_key = pd.API_KEY
        secret_key = pd.SECRET_KEY
        self.client = AipOcr(app_id, api_key, secret_key)

    def pic2text(self,filepath):
        image=BaiduAPI.getfileContent(filepath)
        texts=self.client.basicGeneral(image)
        if int(texts['words_result_num']) != 0:
            newlist=list(map(lambda x: x['words'], texts['words_result']))
            newlist=newrow(newlist)
            return "".join(newlist)

    @staticmethod
    def getfileContent(filepath):
        with open(filepath,'rb') as fp:
            return fp.read()

if __name__ == '__main__':
    pass