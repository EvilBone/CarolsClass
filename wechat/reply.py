import time
from lxml import etree
from lxml.etree import CDATA


class Msg(object):
    def __init__(self):
        pass

    def send(self):
        return "success"

class TextMsg(Msg):
    def __init__(self, toUserName, fromUserName, content):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Content'] = content

    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{Content}]]></Content>
        </xml>
        """
        return XmlForm.format(**self.__dict)

class NewsMsg(Msg):
    def __init__(self, toUserName, fromUserName, count,articles):
        self.__dict = dict()
        self.__dict['ToUserName'] = CDATA(toUserName)
        self.__dict['FromUserName'] = CDATA(fromUserName)
        self.__dict['CreateTime'] = str(int(time.time()))
        self.__dict['MsgType'] = CDATA('news')
        self.__dict['ArticleCount'] = str(count)
        self.__dict['Articles'] = articles


    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[image]]></MsgType>
        <Image>
        <MediaId><![CDATA[{MediaId}]]></MediaId>
        </Image>
        </xml>
        """
        # 创建根节点
        news = etree.Element('xml')
        # 创建子节点，并添加数据
        tousername = etree.SubElement(news, "ToUserName")
        tousername.text = self.__dict['ToUserName']
        fromusername = etree.SubElement(news, "FromUserName")
        fromusername.text = self.__dict['FromUserName']
        createTime = etree.SubElement(news, "CreateTime")
        createTime.text = self.__dict['CreateTime']
        msgType = etree.SubElement(news, "MsgType")
        msgType.text = self.__dict['MsgType']
        count = etree.SubElement(news, "ArticleCount")
        count.text = self.__dict['ArticleCount']
        articles = etree.SubElement(news, "Articles")
        for item in self.__dict['Articles']:
            article = etree.SubElement(articles, "item")
            title = etree.SubElement(article, "Title")
            title.text = CDATA(item.title)
            des = etree.SubElement(article,'Description')
            des.text =CDATA(item.des)
            picurl = etree.SubElement(article,'PicUrl')
            picurl.text = CDATA(item.picurl)
            url = etree.SubElement(article,'Url')
            url.text =  CDATA(item.url)
        return etree.tostring(news,encoding="utf-8")


class ImageMsg(Msg):
    def __init__(self, toUserName, fromUserName, mediaId):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['MediaId'] = mediaId

    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[image]]></MsgType>
        <Image>
        <MediaId><![CDATA[{MediaId}]]></MediaId>
        </Image>
        </xml>
        """
        return XmlForm.format(**self.__dict)