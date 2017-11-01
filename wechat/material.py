import json

import requests

from wechat.base import Basic


class Material(object):

    # 获取素材列表
    def batch_get(self, accessToken, mediaType, offset=0, count=20):
        postUrl = 'https://api.weixin.qq.com/cgi-bin/material/batchget_material?access_token='+accessToken
        postData = {"type":mediaType,"offset":offset,"count":count}
        urlResp = requests.post(postUrl,postData)
        print(urlResp.content)


if __name__ == '__main__':
    myMaterial = Material()
    accessToken = Basic().get_access_token()
    print(accessToken)
    mediaType = "news"
    myMaterial.batch_get(accessToken, mediaType)