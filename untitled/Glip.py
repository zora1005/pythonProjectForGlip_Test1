#coding:utf-8
from appium import webdriver
#from selenium import webdriver
from time import sleep
import os
import Login

desired_caps = {}
# desired_caps['platformName'] = 'Android'
# #desired_caps['platformVersion'] = '7.1.1' # 5x
# #desired_caps['deviceName'] = '010fce00f9add00c' #5x
# desired_caps['platformVersion'] = '6.0.1'  #Nexus 6P
# desired_caps['deviceName'] = '84B7N16523002983'    #Nexus 6P
# desired_caps['appPackage'] = 'com.glip.mobile'
# desired_caps['appActivity'] = 'com.glip.ui.app.SplashScreenActivity' # a special activity
desired_caps['platformName'] = 'iOS'
#desired_caps['platformVersion'] = '7.1.1' # 5x
#desired_caps['deviceName'] = '010fce00f9add00c' #5x
desired_caps['platformVersion'] = '10.3'  #Nexus 6P
desired_caps['deviceName'] = 'iPhone Simulator'    #iNexus 6P
desired_caps['appPackage'] = 'com.glip.mobile'
desired_caps['appActivity'] = 'com.glip.ui.app.SplashScreenActivity' # a special activity


dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

for i in range(1,4,1):  #range is 1,2,3
    Login.Gliplogin(dr,'vina.chenxn@gmail.com','Test!123')
    Login.Signout(dr)
    name=Login.Getusername(dr)
    print( name)

for i in range(1,2,1):
    Login.Gliplogin(dr, 'vina.chen91@gmail.com', 'Test!123')
    Login.Signout(dr)
    name=Login.Getusername(dr)
    print (name)



'''
if name=='Elena Vee':
    print 'success'
else:
    print 'error'
'''




