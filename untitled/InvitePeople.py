import requests
import json
import time
import base64

header = {'content-type': 'application/json'}
source = 'mobile'

def getGlipBaseUrl(portID):
    glipBaseUrl= "https://aws13-g04-uds01.asialab.glip.net:" + portID
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
    #print(getRCTokenresponse.text) #在控制台打印请求对象结果，使用对象的文本属性
    rcTokenJsonText = getRCTokenresponse.json() #取得json结构的结果
    rcTokenText = getRCTokenresponse.text #取得文本结果
    rc_access_token_data = "";
    if getRCTokenresponse.ok: #如果请求是成功，取得acess_token, 并做base64位加密
        rc_access_token_data =str(base64.b64encode(bytes(rcTokenText,encoding="utf-8")),encoding="utf-8")
        #print(rc_access_token_data)
    else:
        print("failed to get access_token, the reason is" + json.dumps(rcTokenJsonText)) #
    return rc_access_token_data




def glipLogin(rc_access_token, portID):
    baseUrl = getGlipBaseUrl(portID) + "/api/login"
    payload = {'rc_access_token_data':rc_access_token,'mobile': True, 'for_mobile': True}
    header = {'content-type':'application/json'}
    glipLoginResponse = requests.put(baseUrl,data=json.dumps(payload),headers=header)

    if glipLoginResponse.ok:
        #print(glipLoginResponse.text)
        #print( glipLoginResponse.headers)
        tk = glipLoginResponse.headers['X-Authorization']
        creator_id = glipLoginResponse.json()['user_id']
        loginUserInfo = {'tk':tk,'creator_id':creator_id} #定义数组对象，保存获取的glip token和user_id
    else:
        print("failed to get glipLoginResponse, the reason is " + glipLoginResponse.text)
    return loginUserInfo



def invitePeople(tk, portID, creator_id,email):
    baseUrl = getGlipBaseUrl(portID) +"/api/person"
    paras = {'invite_id': creator_id, 'email': email, 'tk': tk}
    payload=json.dumps(paras)
    invitePeople = requests.post(baseUrl,data=payload, headers=header)
    #print(createTeamResonse.json())
    #print(createTeamResonse.status_code)19701766

    if invitePeople.ok:
        print('Invited People: ')
        print(email)
    else:
        print('Failed to invite people, the status_code is' +str(createTeamResonse.status_code))
    return



def run(ENV,userName,extNum,passWord,portID, createTeamCount):
    rc_access_token = getRCToken(ENV,userName,extNum,passWord,'password')
    glip_token = glipLogin(rc_access_token, portID)

    for index in range(0, createTeamCount):
        emailpre = "test7"
        invitePeople(glip_token['tk'],portID, glip_token['creator_id'], emailpre+str(index)+"@acmec2.com")
        time.sleep(0.15)


run('http://api-up.lab.rcch.ringcentral.com','18002491122','106','Test!123','23304',2)
#run('http://api-up.lab.rcch.ringcentral.com','18003396668','102','Test!123','23304',50,50, 'task')