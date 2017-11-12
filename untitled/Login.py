#coding:utf-8
from appium import webdriver
from selenium import webdriver
from time import sleep
import os

def Gliplogin(dr,username,pswd):
    dr.find_element_by_id('com.glip.mobile:id/sign_in_button').click()
    dr.find_element_by_id('com.glip.mobile:id/common_email_edit').clear()
    dr.find_element_by_id('com.glip.mobile:id/common_email_edit').send_keys(username)
    dr.find_element_by_id('com.glip.mobile:id/common_password_edit').send_keys(pswd)
    dr.find_element_by_id('com.glip.mobile:id/sign_form_post_button').click()
    sleep(10)

def Gotoprofile(dr):
    dr.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Open navigation drawer']").click()

def Getusername(dr):
    name= dr.find_element_by_id('com.glip.mobile:id/navigation_header_item_title_view').text
    return name

def Signout(dr):
    Gotoprofile(dr)
    dr.find_element_by_name('Settings').click()
    sleep(5)
    dr.find_element_by_name('Sign Out').click()
    sleep(4)


