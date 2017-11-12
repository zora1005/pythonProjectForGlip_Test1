import requests
import json
import time
import base64

header = {'content-type': 'application/json'}

def getGlipBaseUrl(portID):
    glipBaseUrl= "https://aws21-g43-udp01.asialab.glip.net:" + portID
    return glipBaseUrl



def getRCToken(ENV,userName,extNum,passWord,grant_Type): #定义方法，传env,用户名，密码，认证方式
    baseUrl = ENV + "/restapi/oauth/token" #定义字符串变量
    if ENV == 'http://api-up.lab.rcch.ringcentral.com' or 'https://api-up.lab.rcch.ringcentral.com':
        rcSecurtyCode = 'TWtDZGxTVnFRMDZINmk3S1ljdjliZzo1X3RGQlhCUVRMV2FWY1BGNjFMVUdnbmdCZmM4S0dRQ2FaMF9VVHc4MHZzdw=='
    elif ENV == 'https://api.ringcentral.com':
        rcSecurtyCode = 'MDJiNzI5MTgwMDRhOWVkMzM2YjlDRUJDNDhlNjAzOGJlM2YyMTk2NDI2MjFBODA0MjA3MmY5N2MyQzg0MkZBQTpGQkQzRENBMDk5N2JFQTlCMGI4MWY4NTZlY2NiOWNkMmIxOWQ2MDYwNzc3NmE4NjFDOUM0N2RiNWVkMDU0ODcy'
    rcAuthCode = 'Basic ' + rcSecurtyCode #定义字符串变量
    payload = {'username':userName, 'password':passWord, 'extension':extNum,'grant_type':grant_Type} #定义一个json的map结构的对象（key：value）
    header = {'content-type':'application/x-www-form-urlencoded','authorization':rcAuthCode} #定义一个json的map结构的对象（key：value）
    getRCTokenresponse=requests.post(baseUrl, data= payload, headers=header) #调用api，获取请求结果
    print(getRCTokenresponse.text) #在控制台打印请求对象结果，使用对象的文本属性
    rcTokenJsonText = getRCTokenresponse.json() #取得json结构的结果
    rcTokenText = getRCTokenresponse.text #取得文本结果
    if getRCTokenresponse.ok: #如果请求是成功，取得acess_token, 并做base64位加密
        rc_access_token_data =str(base64.b64encode(bytes(rcTokenText,encoding="utf-8")),encoding="utf-8")
        print(rc_access_token_data)
    else:
        print("failed to get access_token, the reason is" + json.dumps(rcTokenJsonText)) #
    return rc_access_token_data




def glipLogin(ENV, userName, rc_access_token, portID):
    token = getRCToken(ENV, userName,104, "Test!123", "password")
    baseUrl = getGlipBaseUrl(portID) + "/api/login"
    payload = {'rc_access_token_data':rc_access_token,'mobile': True, 'for_mobile': True}
    header = {'content-type':'application/json'}
    glipLoginResponse = requests.put(baseUrl,data=json.dumps(payload),headers=header)
    if glipLoginResponse.ok:
        print(glipLoginResponse.text)
        print( glipLoginResponse.headers)
        tk = glipLoginResponse.headers['X-Authorization']
        creator_id = glipLoginResponse.json()['user_id']
        loginUserInfo = {'tk':tk,'creator_id':creator_id} #定义数组对象，保存获取的glip token和user_id
    else:
        print("failed to get glipLoginResponse, the reason is " + glipLoginResponse.text)
    return loginUserInfo


def replyPost(ENV, userName, portID, txtContent):


    baseUrl = getGlipBaseUrl(portID) + "/api/post"

    paras = {'new_version':3701094196333632,'source':'mobile','group_id':32776198,'tk':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ0b2tlbl9pZCI6MTQ5ODcxODE3NjAyMiwidHlwZSI6IndlYiIsInVpZCI6MTU0MjIyNTk1LCJpYXQiOjE0OTg3MTgxNzYsImlzcyI6ImF3czIxLWc0My11ZHAwMS5hc2lhbGFiLmdsaXAubmV0Iiwic3ViIjoiZ2xpcCJ9.Qr0DRbAAww1_t9WXF42IjrlOE43yYhiGX8lEEPQGFJ3E0R9JVjd4n1M-KvaxwCgVTXpM5b5qkXmi9lMK-a7r3Q','created_at':1490503643832,'creator_id':154222595,'is_new':True,'text':txtContent,'version':3701094196333632}
    payload=json.dumps(paras)
    replyPost = requests.post(baseUrl,data=payload, headers=header)
    #print(replyPost.json())
    #print(replyPost.status_code)
    if replyPost.ok:
        print('The Sent Text is: ' )
        print(txtContent)
    else:
        print('Failed to reply post, the status code is ' + str(replyPost.status_code))
    return



# def run(ENV,userName,extNum,passWord,portID, textContent, messageCount):
#     rc_access_token = getRCToken(ENV,userName,extNum,passWord,'password')
#     glip_token = glipLogin(rc_access_token, portID)
#     for index in range(0, messageCount):
#
#         replyPost(glip_token['tk'],portID,messageCount)
#         time.sleep(0.1)

# replyPost('http://api-up.lab.rcch.ringcentral.com','18002491122','23304',"Test")

def mulReply(n, ENV, userName, portID, txtContent):
    for index in range(0, n):
        replyPost(ENV, userName,portID, txtContent+str(index))

        time.sleep(0.15)
    return



mulReply (50,'http://api-up.lab.rcch.ringcentral.com','18002491122','23304',"Testl0")

