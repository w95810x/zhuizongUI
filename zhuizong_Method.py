#coding=utf-8
from appium import webdriver
from time import sleep
import os
from shurufa import InputMethod
srf=InputMethod()

class My():
    def __init__(self,driver):
        self.driver=driver
        # proposal = {}
        # proposal['platformName'] = 'Android'
        # proposal['platformVersion'] = '6.0.1'
        # proposal['deviceName'] = 'M92QACQBT385K'
        # proposal['appPackage'] = 'com.beebee.tracing'
        # proposal['appActivity'] = 'com.beebee.tracing.ui.general.MainActivity'
        # proposal['unicodeKeyboard'] = 'true'
        # proposal['resetKeyboard'] = 'true'
        # proposal['orientation'] = 'PORTRAIT'
        # self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', proposal)

    def login(self,name,pwd):#正常登录
        try:
            sleep(2)
            self.driver.find_element_by_name('我的').click()
            sleep(1)
            self.driver.find_element_by_id('btnLogin').click()
            sleep(1)
            self.driver.find_element_by_id('inputAccount').click()
            sleep(2)
            srf.enableLatinIME()
            sleep(1)
            self.driver.find_element_by_id('inputAccount').send_keys(name)
            sleep(1)
            self.driver.find_element_by_id('inputPassword').click()
            sleep(1)
            self.driver.find_element_by_id('inputPassword').send_keys(pwd)
            sleep(1)
            srf.enableAppiumUnicodeIME()
            self.driver.find_element_by_id('btnConfirm').click()
        except:
            sleep(2)
            self.driver.find_element_by_name('我的').click()
            sleep(1)
            # zt = self.driver.find_element_by_id('textName').text
            self.driver.find_element_by_id('btnSetting').click()
            sleep(1)
            self.driver.find_element_by_name('退出登录').click()
            sleep(2)
            self.driver.find_element_by_id('btnLogin').click()
            sleep(1)
            self.driver.find_element_by_id('inputAccount').click()
            sleep(2)
            srf.enableLatinIME()
            sleep(1)
            self.driver.find_element_by_id('inputAccount').send_keys(name)
            sleep(1)
            self.driver.find_element_by_id('inputPassword').click()
            sleep(1)
            self.driver.find_element_by_id('inputPassword').send_keys(pwd)
            sleep(1)
            srf.enableAppiumUnicodeIME()
            self.driver.find_element_by_id('btnConfirm').click()

    def Eliminate(self):#清除缓存
        self.driver.keyevent(4)
        sleep(2)
        self.driver.find_element_by_name('我的').click()
        self.driver.find_element_by_id('btnSetting').click()
        sleep(1)
        self.driver.find_element_by_id('textClearSize').click()
        sleep(1)
        self.driver.find_element_by_id('btnConfirm').click()

    def wode_zongyi(self,name):#关注综艺
        sleep(2)
        self.driver.keyevent(4)
        self.driver.find_element_by_name('分类').click()
        sleep(1)
        self.driver.find_element_by_id('searchText').click()
        sleep(2)
        self.driver.find_element_by_id('inputText').send_keys(name)
        sleep(5)
        srf.enableLatinIME()
        sleep(1)
        self.driver.keyevent(66)
        sleep(5)
        self.driver.tap([(45,330)])
        sleep(1)
        self.driver.find_element_by_name('+ 关注').click()
        sleep(1)
        self.driver.find_element_by_id('btnToolbarBack').click()
        self.driver.keyevent(4)
        self.driver.find_element_by_name('我的').click()
        sleep(2)
        self.driver.find_element_by_name('综艺').click()

    def share(self, name):  # 分享
        if name == '微信':
            self.driver.find_element_by_name('微信').click()
            sleep(5)
            self.driver.find_element_by_name('文件传输助手').click()
            sleep(1)
            self.driver.find_element_by_name('分享').click()
            sleep(1)
            self.driver.find_element_by_name('返回追综').click()

        elif name == '微博':
            self.driver.find_element_by_name('微博').click()
            sleep(5)
            self.driver.find_element_by_name('发送').click()
        elif name == '朋友圈':
            self.driver.find_element_by_name('朋友圈').click()
            sleep(5)
            self.driver.find_element_by_name('发表').click()

    def wode_shoucang(self,name):#我的收藏
        sleep(2)
        self.driver.find_element_by_name('首页').click()
        sleep(2)
        self.driver.find_element_by_name('海外专场').click()
        sleep(2)
        self.driver.find_element_by_name(name).click()
        sleep(1)
        self.driver.find_element_by_id('imageCollect').click()
        sleep(1)
        self.driver.find_element_by_id('btnToolbarBack').click()
        sleep(1)
        self.driver.find_element_by_name('我的').click()
        sleep(2)
        self.driver.find_element_by_name('收藏').click()
        self.driver.find_element_by_name(name).click()
        sleep(1)
        self.driver.find_element_by_id('imageCollect').click()
        sleep(1)
        self.driver.find_element_by_id('btnToolbarBack').click()

    def wode_xinwen(self):
        sleep(2)
        self.driver.find_element_by_name('首页').click()
        self.driver.find_element_by_name('看点').click()
        sleep(2)
        s = self.driver.find_elements_by_id('textTitle')
        txt = s[0].text
        print txt
        s[0].click()
        sleep(1)
        self.driver.find_element_by_id('btnToolbarBack').click()
        sleep(1)
        self.driver.find_element_by_name('我的').click()
        sleep(1)
        self.driver.find_element_by_name('新闻').click()
        sleep(1)
        texts = self.driver.find_elements_by_id('textTitle')
        ts = texts[0].text
        if txt == ts:
            return True
        else:
            return False

class PersonalInformation():

    def __init__(self, driver):
        self.driver = driver
        # proposal = {}
        # proposal['platformName'] = 'Android'
        # proposal['platformVersion'] = '6.0.1'
        # proposal['deviceName'] = 'M92QACQBT385K'
        # proposal['appPackage'] = 'com.beebee.tracing'
        # proposal['appActivity'] = 'com.beebee.tracing.ui.general.MainActivity'
        # proposal['unicodeKeyboard'] = 'true'
        # proposal['resetKeyboard'] = 'true'
        # proposal['orientation'] = 'PORTRAIT'
        # self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', proposal)

    def HeadPortrait(self):#头像
        sleep(2)
        self.driver.find_element_by_name('我的').click()
        self.driver.find_element_by_id('imageAvatar').click()
        sleep(1)
        self.driver.find_element_by_name('头像').click()
        sleep(1)
        self.driver.find_element_by_name('从手机相册选择').click()
        s=self.driver.find_elements_by_class_name('android.widget.ImageView')
        s[5].click()
        sleep(1)
        self.driver.find_element_by_id('image_cropper_save').click()
        self.driver.keyevent(4)

    def name(self,name):#nicheng
        sleep(2)
        self.driver.find_element_by_name('我的').click()
        self.driver.find_element_by_id('imageAvatar').click()
        sleep(1)
        self.driver.find_element_by_id('textName').click()
        srf.enableAppiumUnicodeIME()
        self.driver.find_element_by_id('inputText').clear()
        self.driver.find_element_by_id('inputText').send_keys(name)
        self.driver.find_element_by_id('btnToolbarBack').click()

    def BriefIntroduction(self,text):#简介
        sleep(2)
        self.driver.find_element_by_name('我的').click()
        self.driver.find_element_by_id('imageAvatar').click()
        sleep(1)
        self.driver.find_element_by_name('简介').click()
        self.driver.find_element_by_id('inputText').send_keys(text)
        self.driver.find_element_by_id('menuText').click()

    def sex(self):#选择性别
        sleep(2)
        self.driver.find_element_by_name('我的').click()
        self.driver.find_element_by_id('imageAvatar').click()
        sleep(1)
        self.driver.find_element_by_name('性别').click()
        sleep(1)
        self.driver.find_element_by_name('男').click()

    def Birthday(self):#选择生日
        sleep(2)
        self.driver.find_element_by_name('我的').click()
        self.driver.find_element_by_id('imageAvatar').click()
        sleep(1)
        self.driver.find_element_by_name('生日').click()
        self.driver.swipe(10,1900,10,1800)
        sleep(1)
        self.driver.swipe(380, 1900, 380, 1800)
        sleep(1)
        self.driver.swipe(750, 1900, 750, 1800)
        sleep(1)
        self.driver.find_element_by_name('确定').click()
    def region(self):#选择地区
        sleep(2)
        self.driver.find_element_by_name('我的').click()
        self.driver.find_element_by_id('imageAvatar').click()
        sleep(1)
        self.driver.find_element_by_name('地区').click()
        sleep(1)
        self.driver.swipe(10, 1900, 10, 1800)
        sleep(1)
        self.driver.swipe(380, 1900, 380, 1800)
        sleep(1)
        self.driver.swipe(750, 1900, 750, 1800)
        sleep(1)
        self.driver.find_element_by_id('dialog_confirm').click()

class Setting():

    def __init__(self, driver):
        self.driver = driver

    def changepwd(self, pwd, Newpwd):  # 修改密码
        sleep(2)
        self.driver.keyevent(4)
        self.driver.find_element_by_name('我的').click()
        self.driver.find_element_by_id('btnSetting').click()
        sleep(1)
        self.driver.find_element_by_id('btnUpdatePwd').click()
        self.driver.find_element_by_id('inputOldPassword').click()
        self.driver.find_element_by_id('inputOldPassword').send_keys(pwd)
        sleep(1)
        self.driver.find_element_by_id('inputPassword').click()
        self.driver.find_element_by_id('inputPassword').send_keys(Newpwd)
        sleep(2)
        self.driver.find_element_by_id('btnConfirm').click()
        sleep(2)

    def BindOnAccount(self):#账号绑定
        sleep(2)
        self.driver.find_element_by_name('我的').click()
        self.driver.find_element_by_id('btnSetting').click()
        sleep(1)
        self.driver.find_element_by_name('账号绑定').click()
        Mb=self.driver.find_element_by_id('btnUpdateMobile').text
        wx=self.driver.find_element_by_id('textWechat').text
        if Mb=='未绑定':
            pass

class Classification():
    def __init__(self, driver):
        self.driver = driver
        # proposal = {}
        # proposal['platformName'] = 'Android'
        # proposal['platformVersion'] = '6.0.1'
        # proposal['deviceName'] = 'M92QACQBT385K'
        # proposal['appPackage'] = 'com.beebee.tracing'
        # proposal['appActivity'] = 'com.beebee.tracing.ui.general.MainActivity'
        # proposal['unicodeKeyboard'] = 'true'
        # proposal['resetKeyboard'] = 'true'
        # proposal['orientation'] = 'PORTRAIT'
        # self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', proposal)

    def fenlei_shaixuan(self):#分类筛选
        sleep(2)
        self.driver.find_element_by_name('分类').click()
        sleep(1)
        self.driver.find_element_by_name('中国大陆').click()
        sleep(1)
        self.driver.find_element_by_name('体验').click()
        sleep(1)
        self.driver.find_element_by_name('2018').click()
        sleep(1)
        self.driver.find_element_by_name('追综线路').click()
        sleep(1)

    def fenlei_sousuo(self,name):#分类搜索
        sleep(2)
        self.driver.find_element_by_name('分类').click()
        sleep(1)
        self.driver.find_element_by_id('searchText').click()
        srf.enableAppiumUnicodeIME()
        sleep(2)
        self.driver.find_element_by_id('inputText').send_keys(name)
        sleep(1)
        srf.enableLatinIME()
        self.driver.keyevent(66)
        sleep(3)
class Timetable():
    def __init__(self, driver):
        self.driver = driver
        # proposal = {}
        # proposal['platformName'] = 'Android'
        # proposal['platformVersion'] = '6.0.1'
        # proposal['deviceName'] = 'M92QACQBT385K'
        # proposal['appPackage'] = 'com.beebee.tracing'
        # proposal['appActivity'] = 'com.beebee.tracing.ui.general.MainActivity'
        # proposal['unicodeKeyboard'] = 'true'
        # proposal['resetKeyboard'] = 'true'
        # proposal['orientation'] = 'PORTRAIT'
        # self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', proposal)
    def guanzhu(self):#加关注
        sleep(2)
        self.driver.find_element_by_name('时间表').click()
        z=self.driver.find_elements_by_id('btnFocus')
        z[0].click()
        s=self.driver.find_elements_by_id('textTitle')
        s[0].click()
        sleep(2)
        g=self.driver.find_element_by_id('btnFocus').text
        if g=='+ 关注':
            self.driver.find_element_by_id('btnFocus').click()
            sleep(1)
            self.driver.find_element_by_id('btnToolbarBack').click()
        else:
            self.driver.find_element_by_id('btnToolbarBack').click()

    def remind(self):#时间表通知时间
        sleep(2)
        self.driver.find_element_by_name('时间表').click()
        sleep(1)
        self.driver.find_element_by_name('关注').click()
        sleep(1)
        t = self.driver.find_element_by_id('textNotification').text
        if t == '去设置':
            self.driver.find_element_by_id('textNotification').click()
            sleep(1)
            self.driver.swipe(500, 1900, 500, 1800)
            sleep(1)
            self.driver.find_element_by_name('确定').click()
        else:
            self.driver.find_element_by_id('textNotification').click()
            sleep(1)
            self.driver.swipe(500,1700,500,1900)
            sleep(1)
            self.driver.find_element_by_name('确定').click()
            sleep(1)
            self.driver.find_element_by_id('textNotification').click()
            sleep(1)
            self.driver.swipe(500, 1900, 500, 1800)
            sleep(1)
            self.driver.find_element_by_name('确定').click()

class HomePage():
    def __init__(self, driver):
        self.driver = driver
        # proposal = {}
        # proposal['platformName'] = 'Android'
        # proposal['platformVersion'] = '6.0.1'
        # proposal['deviceName'] = 'M92QACQBT385K'
        # proposal['appPackage'] = 'com.beebee.tracing'
        # proposal['appActivity'] = 'com.beebee.tracing.ui.general.MainActivity'
        # proposal['unicodeKeyboard'] = 'true'
        # proposal['resetKeyboard'] = 'true'
        # proposal['orientation'] = 'PORTRAIT'
        # self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', proposal)
    def jianji_pinglun(self,text):#剪辑评论
        sleep(2)
        self.driver.find_element_by_name('首页').click()
        s = self.driver.find_elements_by_id('imageCover')
        s[1].click()
        sleep(2)
        self.driver.find_element_by_id('btnComment').click()
        sleep(2)
        srf.enableAppiumUnicodeIME()
        self.driver.find_element_by_id('inputComment').send_keys(text)
        sleep(2)
        self.driver.find_element_by_name('发布').click()
        sleep(1)

    def jianji_dianzan(self):#剪辑点赞
        sleep(2)
        self.driver.find_element_by_name('首页').click()
        s = self.driver.find_elements_by_id('imageCover')
        s[1].click()
        sleep(2)
        self.driver.find_element_by_id('btnPraise').click()
        sz = self.driver.find_element_by_id('btnPraise').text
        self.driver.find_element_by_id('btnToolbarBack').click()
        shuliang = self.driver.find_elements_by_id('textPraise')
        s = shuliang[0].text
        print s
        if sz == s:
            return True
        else:
            return False

    def jianji_danmu(self,text):#剪辑弹幕
        sleep(2)
        self.driver.find_element_by_name('首页').click()
        s = self.driver.find_elements_by_id('imageCover')
        s[1].click()
        self.driver.find_element_by_id('btnDanmuInput').click()
        srf.enableAppiumUnicodeIME()
        self.driver.find_element_by_id('btnDanmuInput').send_keys(text)
        srf.enableLatinIME()
        self.driver.keyevent(66)
    def sy_pl(self,text):#首页封面视频评论
        self.driver.find_element_by_id('imageCover').click()
        self.driver.find_element_by_id('btnComment').click()
        sleep(1)
        srf.enableAppiumUnicodeIME()
        self.driver.find_element_by_id('inputComment').send_keys(text)
        sleep(1)
        self.driver.find_element_by_name('发布').click()
        srf.enableLatinIME()

    def sy_dz(self):#首页长视频点赞
        self.driver.find_element_by_id('btnPraise').click()

    def sy_sx(self):#往期G点筛选
        self.driver.find_element_by_name('首页').click()
        self.driver.swipe(500, 1700, 500, 1000)
        sleep(1)
        self.driver.find_element_by_id('btnRecommend').click()
        sleep(2)
        self.driver.find_element_by_id('menuIcon').click()
        sleep(1)
        self.driver.find_element_by_name('户外').click()
        sleep(1)




class Public():
    def __init__(self, driver):
        self.driver = driver
        # proposal = {}
        # proposal['platformName'] = 'Android'
        # proposal['platformVersion'] = '6.0.1'
        # proposal['deviceName'] = 'M92QACQBT385K'
        # proposal['appPackage'] = 'com.beebee.tracing'
        # proposal['appActivity'] = 'com.beebee.tracing.ui.general.MainActivity'
        # proposal['unicodeKeyboard'] = 'true'
        # proposal['resetKeyboard'] = 'true'
        # proposal['orientation'] = 'PORTRAIT'
        # self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', proposal)

    def xunzhao(self, by, locator):
        try:
            if by == 'id':
                self.driver.find_element_by_id(locator)
                return True
            elif by == 'name':
                self.driver.find_element_by_name(locator)
                return True
            elif by == 'content':
                self.driver.find_element_by_accessibility_id(locator)
        except:
            return False

    def fenxiang(self, name):
        if name=='微信':
            self.driver.find_element_by_name('微信').click()
            sleep(5)
            self.driver.find_element_by_name('文件传输助手').click()
            sleep(1)
            self.driver.find_element_by_name('分享').click()
            sleep(1)
            self.driver.find_element_by_name('返回追综').click()

        elif name=='微博':
            self.driver.find_element_by_name('微博').click()
            sleep(5)
            self.driver.find_element_by_name('发送').click()
        elif name=='朋友圈':
            self.driver.find_element_by_name('朋友圈').click()
            sleep(5)
            self.driver.find_element_by_name('发表').click()

    def fanhui(self):
        self.driver.find_element_by_id('btnToolbarBack').click()

    def jinrubangdan(self):
        sleep(2)
        self.driver.find_element_by_name('首页').click()
        self.driver.swipe(500,1700,500,1000)
        sleep(1)
        self.driver.find_element_by_id('btnRank').click()

    def jinruzongyibaike(self):
        self.driver.find_element_by_name('首页').click()
        self.driver.swipe(500, 1700, 500, 1100)
        sleep(1)
        self.driver.find_element_by_id('btnRank').click()
        s=self.driver.find_elements_by_id('textSchedule')
        s[0].click()
        self.driver.find_element_by_name('选集').click()
        sleep(5)

    def fabiaodanmu(self,text):
        self.driver.find_element_by_id('btnDanmuInput').click()
        srf.enableAppiumUnicodeIME()
        sleep(1)
        self.driver.find_element_by_id('btnDanmuInput').send_keys(text)
        sleep(1)
        srf.enableLatinIME()
        sleep(1)
        self.driver.keyevent(66)
    def sy_sousuo(self,text):#首页搜索
        self.driver.find_element_by_id('menuIcon').click()
        sleep(1)
        srf.enableAppiumUnicodeIME()
        sleep(1)
        self.driver.find_element_by_id('inputText').send_keys(text)
        sleep(1)
        srf.enableLatinIME()
        sleep(1)
        self.driver.keyevent(66)
    def jinru_zhuanchangneiye(self):#进入专场内页
        self.driver.find_element_by_name('海外专场').click()
        sleep(2)
        ts = self.driver.find_elements_by_id('textTitle')
        ts[0].click()

    def shurukuang_pinglun(self, text):  # 输入框评论
        self.driver.find_element_by_id('inputComment').click()
        srf.enableAppiumUnicodeIME()
        self.driver.find_element_by_id('inputComment').send_keys(text)
        sleep(2)
        self.driver.find_element_by_name('发布').click()
    def kandian_xinwen(self):#进入看点新闻
        self.driver.find_element_by_name('看点').click()
        sleep(2)

    def fengxiangdy(self):#分享断言
        s=self.driver.find_element_by_id('btnShare').text






















