# coding=utf-8
import HTMLTestRunner
from appium import webdriver
from time import sleep
import time
import unittest
from zhuizong_Method import *
from shurufa import InputMethod
srf = InputMethod()


class Test_case(unittest.TestCase):

    def setUp(self):
        proposal = {}
        proposal['platformName'] = 'Android'
        proposal['platformVersion'] = '6.0.1'
        proposal['deviceName'] = 'M92QACQBT385K'
        proposal['appPackage'] = 'com.beebee.tracing'
        proposal['appActivity'] = 'com.beebee.tracing.ui.general.MainActivity'
        proposal['unicodeKeyboard'] = 'true'
        proposal['resetKeyboard'] = 'true'
        proposal['orientation'] = 'PORTRAIT'
        proposal['chromeOptions']={'androidProcess':'com.beebee.tracing'}
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', proposal)
        self.xinxi=PersonalInformation(self.driver)
        self.setting=Setting(self.driver)
        self.my=My(self.driver)
        self.fenlei=Classification(self.driver)
        self.public=Public(self.driver)
        self.timetable=Timetable(self.driver)
        self.homepage=HomePage(self.driver)

    def test_login(self):  # 登录
        self.my.login('15097475275', '123456')
        sleep(1)
        user = self.my.driver.find_element_by_id('textName').text
        self.assertEqual(user, u'秋风扫落叶')
        sleep(1)

    def test_Eliminate(self):  # 清除缓存
        sleep(1)
        self.my.Eliminate()
        t = self.my.driver.find_element_by_id('textClearSize').text
        self.assertEqual(t, '0M')
        sleep(2)
        self.driver.keyevent(4)

    def test_my_weibofx(self):#我的微博分享
        self.driver.keyevent(4)
        self.driver.find_element_by_name('我的').click()
        sleep(3)
        self.driver.find_element_by_name('分享追综').click()
        sleep(2)
        self.my.share('微博')
    def test_my_weixinfx(self):#我的微信分享
        self.driver.keyevent(4)
        self.driver.find_element_by_name('我的').click()
        sleep(3)
        self.driver.find_element_by_name('分享追综').click()
        sleep(2)
        self.my.share('微信')

    def test_my_pengyouquanfx(self):  # 我的微信朋友圈分享
        self.driver.keyevent(4)
        self.driver.find_element_by_name('我的').click()
        sleep(3)
        self.driver.find_element_by_name('分享追综').click()
        sleep(2)
        self.my.share('朋友圈')
    def test_wode_zongyi(self):#我的综艺
        sleep(2)
        self.my.wode_zongyi(u'向往的生活 第二季')
        dy=self.driver.find_element_by_name('向往的生活 第二季').text
        self.assertEqual(dy,u'向往的生活 第二季')
        self.driver.find_element_by_name('向往的生活 第二季').click()
        sleep(2)
        self.driver.find_element_by_name('√ 已关注').click()
        self.driver.find_element_by_id('btnToolbarBack').click()
        z=self.driver.find_element_by_id('plus_content_view').text
        self.assertNotIn(u'向往的生活 第二季',z)
    def test_wode_shoucang(self):#我的收藏
        sleep(2)
        self.my.wode_shoucang('长江后浪推前浪，前浪还在沙滩上')#暂时写死后期优化
        d=self.driver.find_element_by_id('textTitle').text
        sleep(1)
        self.assertNotIn(u'长江后浪推前浪，前浪还在沙滩上',d)
    def test_wode_xinwen(self):#我的新闻
        sleep(2)
        self.my.wode_xinwen()

    def test_UpHeadPortrait(self):#更换头像
        self.xinxi.HeadPortrait()
    def test_UPname(self):
        self.xinxi.name(u'秋风扫落叶')
        x=self.driver.find_element_by_id('textName').text
        self.assertEqual(x,'秋风扫落叶')
        sleep(1)
        self.driver.keyevent(4)
    def test_BriefIntroduction(self):#简介
        self.xinxi.BriefIntroduction(u'好好好好好好好好好好好好好好好好好好好好')
        j=self.driver.find_element_by_id('textSignature').text
        self.assertEqual(j,'好好好好好好好好好好好好好好好好好好好好')
        sleep(1)
        self.driver.keyevent(4)
    def test_UPsex(self):#修改性别
        self.xinxi.sex()
        x=self.driver.find_element_by_id('textSex').text
        self.assertEqual(x,'男')
        sleep(1)
        self.driver.keyevent(4)
    def test_birthday(self):#修改生日暂时先不做断言后期优化后加断言
        self.xinxi.Birthday()
        sleep(1)
        self.driver.keyevent(4)
    def test_Region(self):#修改地区暂时先不做断言后期优化后加断言
        self.xinxi.region()
        sleep(1)
        self.driver.keyevent(4)
    def test_fenlei_shaixuan(self):#分类筛选
        self.fenlei.fenlei_shaixuan()
        self.driver.swipe(1000, 1500, 1000, 500)
        t1=self.driver.find_element_by_id('textCategory1').text
        t2=self.driver.find_element_by_id('textCategory2').text
        t3=self.driver.find_element_by_id('textCategory3').text
        t4=self.driver.find_element_by_id('textCategory4').text
        t5=self.driver.find_element_by_name('最新排序').text
        self.assertEqual(t1,'中国大陆')
        self.assertEqual(t2,'体验')
        self.assertEqual(t3,'2018')
        self.assertEqual(t4,'追综线路')
        self.assertEqual(t5,'最新排序')
        sleep(1)
    def test_fenlei_search(self):#分类搜索
        self.fenlei.fenlei_sousuo(u'坑王驾到 第二季')
        sleep(1)
        s=self.driver.find_element_by_name('坑王驾到 第二季').text
        self.assertEqual(s,'坑王驾到 第二季')
        sleep(1)
        self.driver.keyevent(4)
    def test_fenlei_delete(self):#删除搜索记录
        self.fenlei.fenlei_sousuo(u'坑王驾到 第二季')
        self.driver.find_element_by_id('inputText').click()
        sleep(1)
        self.driver.find_element_by_id('btnClear').click()
        sleep(1)
        dl=self.driver.find_elements_by_id('btnDelete')
        dl[0].click()
        text=self.driver.find_elements_by_id('textContent')
        self.assertNotEqual('坑王驾到 第二季',text)
        sleep(1)
        self.driver.find_element_by_id('btnClearHistory').click()
        self.driver.keyevent(4)
    def test_time_weiboshare(self):#时间表微博分享
        self.driver.find_element_by_name('时间表').click()
        sleep(2)
        self.driver.find_element_by_id('btnShare').click()
        self.public.fenxiang('微博')
    def test_time_weishare(self):#时间表微信分享
        self.driver.find_element_by_name('时间表').click()
        sleep(2)
        self.driver.find_element_by_id('btnShare').click()
        sleep(1)
        self.public.fenxiang('微信')

    def test_time_pengyouquan(self):#时间表朋友圈分享
        self.driver.find_element_by_name('时间表').click()
        sleep(2)
        self.driver.find_element_by_id('btnShare').click()
        sleep(1)
        self.public.fenxiang('朋友圈')
    def test_Default(self):#时间表默认值
        self.driver.find_element_by_name('时间表').click()
        s=self.driver.find_element_by_id('text4').text
        self.assertEqual(s,'今')
        sleep(1)
        self.driver.find_element_by_id('text7').click()
        sleep(1)
        self.driver.find_element_by_name('首页').click()
        sleep(2)
        self.driver.find_element_by_name('时间表').click()
        self.driver.find_element_by_name('时间表').click()
        s = self.driver.find_element_by_id('text4').text
        self.assertEqual(s, '今')
    def test_time_follow(self):#加关注
        self.timetable.guanzhu()
        s = self.driver.find_elements_by_id('textTitle')
        s[0].click()
        sleep(1)
        g = self.driver.find_element_by_id('btnFocus').text
        self.assertEqual(g,'√ 已关注')
        sleep(1)
        self.driver.find_element_by_id('btnFocus').click()
        self.public.fanhui()
    def test_time_remind(self):#设置更新推送时间
        self.timetable.remind()
        t=self.driver.find_element_by_id('textNotification').text
        self.assertEqual(t,'午饭提醒')
    def test_janji_pinglun(self): #剪辑评论
        self.homepage.jianji_pinglun('666')
        sleep(1)
        txt=self.driver.find_element_by_xpath(xpath="//android.widget.TextView[@text='666']").text
        self.assertEqual(txt,'666')
        self.public.fanhui()
    def test_jianjidianzan(self):#剪辑点赞
        self.homepage.jianji_dianzan()
    def test_jianji_weinxinfx(self):#剪辑微信分享
        sleep(2)
        self.driver.find_element_by_name('首页').click()
        s = self.driver.find_elements_by_id('imageCover')
        s[1].click()
        sleep(1)
        s = self.driver.find_element_by_id('btnShare').text
        self.driver.find_element_by_id('btnShare').click()
        self.public.fenxiang('微信')
        s2 = self.driver.find_element_by_id('btnShare').text
        s3 = int(s2)
        s1 = int(s) + 1
        self.assertEqual(s3, s1)
        sleep(1)
        self.driver.keyevent(4)

    def test_jianji_weinbofx(self):  # 剪辑微博分享
        sleep(2)
        self.driver.find_element_by_name('首页').click()
        s = self.driver.find_elements_by_id('imageCover')
        s[1].click()
        sleep(1)
        s = self.driver.find_element_by_id('btnShare').text
        self.driver.find_element_by_id('btnShare').click()
        self.public.fenxiang('微博')
        s2 = self.driver.find_element_by_id('btnShare').text
        s3 = int(s2)
        s1 = int(s) + 1
        self.assertEqual(s3, s1)
        sleep(1)
        self.driver.keyevent(4)

    def test_jianji_pengyouquanfx(self):  # 剪辑微信朋友圈分享
        sleep(2)
        self.driver.find_element_by_name('首页').click()
        s = self.driver.find_elements_by_id('imageCover')
        s[1].click()
        sleep(1)
        s = self.driver.find_element_by_id('btnShare').text
        self.driver.find_element_by_id('btnShare').click()
        self.public.fenxiang('朋友圈')
        s2 = self.driver.find_element_by_id('btnShare').text
        s3 = int(s2)
        s1 = int(s) + 1
        self.assertEqual(s3, s1)
        sleep(1)
        self.driver.keyevent(4)
    def test_jianji_Barrage(self):#剪辑发布弹幕
        self.homepage.jianji_danmu('666')
        self.public.fanhui()
    def test_phb_wxfx(self):#排行榜微信分享
        self.public.jinrubangdan()
        self.driver.find_element_by_id('menuIcon').click()
        self.public.fenxiang('微信')
        sleep(1)
        self.public.fanhui()

    def test_phb_wbfx(self):  # 排行榜微博分享
        self.public.jinrubangdan()
        self.driver.find_element_by_id('menuIcon').click()
        self.public.fenxiang('微博')
        sleep(1)
        self.public.fanhui()

    def test_phb_pyqfx(self):  # 排行榜微信朋友圈分享
        self.public.jinrubangdan()
        self.driver.find_element_by_id('menuIcon').click()
        self.public.fenxiang('朋友圈')
        sleep(1)
        self.public.fanhui()
    def test_baike_wxfx(self):#综艺百科微信分享
        self.public.jinruzongyibaike()
        sleep(1)
        self.driver.find_element_by_id('menuIcon').click()
        self.public.fenxiang('微信')
        self.public.fanhui()
        sleep(1)
        self.public.fanhui()

    def test_baike_wbfx(self):#综艺百科微博分享
        self.public.jinruzongyibaike()
        sleep(1)
        self.driver.find_element_by_id('menuIcon').click()
        self.public.fenxiang('微博')
        self.public.fanhui()
        sleep(1)
        self.public.fanhui()

    def test_baike_pyqfx(self):#综艺百科朋友圈分享
        self.public.jinruzongyibaike()
        sleep(1)
        self.driver.find_element_by_id('menuIcon').click()
        self.public.fenxiang('朋友圈')
        self.public.fanhui()
        sleep(1)
        self.public.fanhui()
    def test_shouye_comment(self):#首页长视频评论
        self.homepage.sy_pl('666')
        t=self.driver.find_elements_by_id('textContent')
        texts=t[0].text
        self.assertEqual(texts,'666')
        self.public.fanhui()
    def test_shouye_dz(self):#首页点赞
        self.driver.find_element_by_id('imageCover').click()
        sleep(2)
        s=self.driver.find_element_by_id('btnPraise').text
        s1=int(s)
        self.homepage.sy_dz()
        s2 = self.driver.find_element_by_id('btnPraise').text
        s3= int(s2)
        s4=s1+1
        self.assertEqual(s3,s4)
        self.public.fanhui()
    def test_shouye_wxfx(self):#长视频微信分享
        self.driver.find_element_by_id('imageCover').click()
        sleep(1)
        s = self.driver.find_element_by_id('btnShare').text
        self.driver.find_element_by_id('btnShare').click()
        sleep(1)
        self.public.fenxiang('微信')
        sleep(1)
        s2=self.driver.find_element_by_id('btnShare').text
        s3=int(s2)
        s1=int(s)+1
        self.assertEqual(s3,s1)
        sleep(1)
        self.public.fanhui()
    def test_shouye_wbfx(self):#长视频微博分享
        self.driver.find_element_by_id('imageCover').click()
        sleep(1)
        s = self.driver.find_element_by_id('btnShare').text
        self.driver.find_element_by_id('btnShare').click()
        sleep(1)
        self.public.fenxiang('微博')
        sleep(1)
        s2 = self.driver.find_element_by_id('btnShare').text
        s3 = int(s2)
        s1 = int(s) + 1
        self.assertEqual(s3, s1)
        sleep(1)
        self.public.fanhui()
    def test_shouye_pyqfx(self):#长视频朋友圈分享
        self.driver.find_element_by_id('imageCover').click()
        sleep(1)
        s = self.driver.find_element_by_id('btnShare').text
        self.driver.find_element_by_id('btnShare').click()
        sleep(1)
        self.public.fenxiang('朋友圈')
        sleep(1)
        s2 = self.driver.find_element_by_id('btnShare').text
        s3 = int(s2)
        s1 = int(s) + 1
        self.assertEqual(s3, s1)
        sleep(1)
        self.public.fanhui()
    def test_shouye_danmu(self):
        self.driver.find_element_by_id('imageCover').click()
        sleep(1)
        self.public.fabiaodanmu('666666')
        sleep(1)
        self.public.fanhui()
    def test_wqGd_sx(self):#往期G点筛选
        self.homepage.sy_sx()
        sleep(1)
        self.public.fanhui()
    def test_shouye_sousuo(self):#首页搜索明星
        self.public.sy_sousuo(u'郭德纲')
        sleep(1)
        t=self.driver.find_element_by_id('textKeyword').text
        sleep(1)
        self.assertEqual(t,'郭德纲')
        sleep(1)
        self.driver.find_element_by_name('热度').click()
        sleep(2)
        self.driver.find_element_by_id('btnCancel').click()
    def test_zc_pl(self):#专场评论
        self.public.jinru_zhuanchangneiye()
        sleep(1)
        self.public.shurukuang_pinglun('666')
        t=self.driver.find_elements_by_id('textContent')
        ts=t[0].text
        sleep(1)
        self.assertEqual(ts,'666')
        sleep(1)
        self.public.fanhui()
    def test_zc_dz(self):#专场点赞(暂时没做断言后期补上)
        self.public.jinru_zhuanchangneiye()
        sleep(1)
        s=self.driver.find_elements_by_class_name('android.widget.ImageView')
        s[-2].click()
    def test_zc_wxfx(self):#专场微信分享
        self.public.jinru_zhuanchangneiye()
        sleep(1)
        self.driver.find_element_by_id('btnShare').click()
        sleep(1)
        self.public.fenxiang('微信')
        self.public.fanhui()
    def test_zc_wbfx(self):#专场微博分享
        self.public.jinru_zhuanchangneiye()
        sleep(1)
        self.driver.find_element_by_id('btnShare').click()
        sleep(1)
        self.public.fenxiang('微博')
        self.public.fanhui()
    def test_zc_pyqfx(self):#专场微信朋友圈分享
        self.public.jinru_zhuanchangneiye()
        sleep(1)
        self.driver.find_element_by_id('btnShare').click()
        sleep(1)
        self.public.fenxiang('朋友圈')
        self.public.fanhui()
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(Test_case("test_login"))
    testunit.addTest(Test_case("test_Eliminate"))
    testunit.addTest(Test_case("test_my_weibofx"))
    testunit.addTest(Test_case("test_my_weixinfx"))
    testunit.addTest(Test_case("test_my_pengyouquanfx"))
    testunit.addTest(Test_case("test_wode_zongyi"))
    testunit.addTest(Test_case("test_wode_shoucang"))
    testunit.addTest(Test_case("test_wode_xinwen"))
    testunit.addTest(Test_case("test_UpHeadPortrait"))
    testunit.addTest(Test_case("test_UPname"))
    testunit.addTest(Test_case("test_BriefIntroduction"))
    testunit.addTest(Test_case("test_birthday"))
    testunit.addTest(Test_case("test_Region"))
    testunit.addTest(Test_case("test_fenlei_shaixuan"))
    testunit.addTest(Test_case("test_fenlei_search"))
    testunit.addTest(Test_case("test_fenlei_delete"))
    testunit.addTest(Test_case("test_time_weiboshare"))
    testunit.addTest(Test_case("test_time_weishare"))
    testunit.addTest(Test_case("test_time_pengyouquan"))
    testunit.addTest(Test_case("test_Default"))#20
    testunit.addTest(Test_case("test_time_follow"))
    testunit.addTest(Test_case("test_time_remind"))
    testunit.addTest(Test_case("test_janji_pinglun"))
    testunit.addTest(Test_case("test_jianjidianzan"))
    testunit.addTest(Test_case("test_jianji_weinxinfx"))
    testunit.addTest(Test_case("test_jianji_weinbofx"))
    testunit.addTest(Test_case("test_jianji_pengyouquanfx"))
    testunit.addTest(Test_case("test_jianji_Barrage"))
    testunit.addTest(Test_case("test_phb_wxfx"))
    testunit.addTest(Test_case("test_phb_wbfx"))
    testunit.addTest(Test_case("test_phb_pyqfx"))
    testunit.addTest(Test_case("test_baike_wxfx"))
    testunit.addTest(Test_case("test_baike_wbfx"))
    testunit.addTest(Test_case("test_baike_pyqfx"))
    testunit.addTest(Test_case("test_shouye_comment"))
    testunit.addTest(Test_case("test_shouye_dz"))
    testunit.addTest(Test_case("test_shouye_wxfx"))
    testunit.addTest(Test_case("test_shouye_wbfx"))
    testunit.addTest(Test_case("test_shouye_pyqfx"))
    testunit.addTest(Test_case("test_shouye_danmu"))
    testunit.addTest(Test_case("test_wqGd_sx"))
    testunit.addTest(Test_case("test_shouye_sousuo"))
    testunit.addTest(Test_case("test_zc_pl"))
    testunit.addTest(Test_case("test_zc_dz"))
    testunit.addTest(Test_case("test_zc_wxfx"))
    testunit.addTest(Test_case("test_zc_wbfx"))
    testunit.addTest(Test_case("test_zc_pyqfx"))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    #HtmlFile = "F:\\result\\" + now + "HTMLtemplate.html"
    #print HtmlFile
    filename = '\Users\lenovo\PycharmProjects\zhuizong' + now + '.html'  # 这个路径改成自己的目录路径
    fp = open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"追综测试报告", description=u"用例测试执行情况")
    runner.run(testunit)
    fp.close()