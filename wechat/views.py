# -*- coding: utf-8 -*-
from lxml import etree

from django.http import HttpResponse
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt

import hashlib

from wechat import receive, reply
from wechat.models import Article


@csrf_exempt
def wechat(request):
    # 这里我当时写成了防止跨站请求伪造，其实不是这样的，恰恰相反。因为django默认是开启了csrf防护中间件的
    # 所以这里使用@csrf_exempt是单独为这个函数去掉这个防护功能。
    if request.method == 'GET':
        # 下面这四个参数是在接入时，微信的服务器发送过来的参数
        signature = request.GET.get('signature', None)
        timestamp = request.GET.get('timestamp', None)
        nonce = request.GET.get('nonce', None)
        echostr = request.GET.get('echostr', None)

        # 这个token是我们自己来定义的，并且这个要填写在开发文档中的Token的位置
        token = 'LvsanerHJ0119'

        # 把token，timestamp, nonce放在一个序列中，并且按字符排序
        hashlist = [token, timestamp, nonce]
        hashlist.sort()

        # 将上面的序列合成一个字符串
        hashstr = ''.join([s for s in hashlist])

        # 通过python标准库中的sha1加密算法，处理上面的字符串，形成新的字符串。
        hashstr = hashlib.sha1(hashstr.encode('utf-8')).hexdigest()

        # 把我们生成的字符串和微信服务器发送过来的字符串比较，
        # 如果相同，就把服务器发过来的echostr字符串返回去
        if hashstr == signature:
            return HttpResponse(echostr)
    if request.method == 'POST':
        data = smart_str(request.body)
        xml = etree.fromstring(data)
        print('**********收到的XML***********\n')
        print(data)
        recMsg = receive.parse_xml(xml)
        if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
            if recMsg.Content == 'xx':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                content = "From "+fromUser+"to "+toUser+recMsg.Content
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return HttpResponse(replyMsg.send())
            elif recMsg.Content == 'wz':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                articles = Article.objects.all()
                count = len(articles)
                # content = "From " + fromUser + "to " + toUser + recMsg.Content
                replyMsg = reply.NewsMsg(toUser, fromUser, count,articles)
                return HttpResponse(replyMsg.send())
            else:
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                content = recMsg.Content
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return HttpResponse(replyMsg.send())
        else:
            print("暂且不处理")
            return HttpResponse('success')

