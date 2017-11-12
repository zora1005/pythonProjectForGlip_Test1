#!/usr/bin/python
print "你好，世界";


import requests
import json

def getToken(ENV,userName, passWord, grant_Type):
    baseUrl=ENV + "/restapi/oauth/token"
    if ENV == 'https://platform-devfre.lab.rcch.ringcentral.com:8446':
        endCode='MDJiNzI5MTgwMDRhOWVkMzM2YjlDRUJDNDhlNjAzOGJlM2YyMTk2NDI2MjFBODA0MjA3MmY5N2MyQzg0MkZBQTpGQkQzRENBMDk5N2JFQTlCMGI4MWY4NTZlY2NiOWNkMmIxOWQ2MDYwNzc3NmE4NjFDOUM0N2RiNWVkMDU0ODcy'
    elif ENV=='https://platform-up.lab.rcch.ringcentral.com':
        endCode='MDJiNzI5MTgwMDRhOWVkMzM2YjlDRUJDNDhlNjAzOGJlM2YyMTk2NDI2MjFBODA0MjA3MmY5N2MyQzg0MkZBQTpGQkQzRENBMDk5N2JFQTlCMGI4MWY4NTZlY2NiOWNkMmIxOWQ2MDYwNzc3NmE4NjFDOUM0N2RiNWVkMDU0ODcyIA=='
    keyEndcode='Basic '+ endCode
    payload={'username':userName, 'password':passWord, 'grant_type':grant_Type}
    headers={'Authorization':keyEndcode, 'Accept':'application/json'}
    getTokenResponse=requests.post(baseUrl,data=payload, headers=headers)
    print(getTokenResponse.text)
    data=getTokenResponse.json()
    if getTokenResponse.ok:
        access_token=data['token_type']+' '+data['access_token']
    else:
        print('Failed to get access token:'+str[data])
    return (access_token)




def createNewContact(ENV1,userName1,firstname,mobilephone,lastname):
    baseUrl="http://api-devfre.lab.rcch.ringcentral.com/restapi/v1.0/account/~/extension/~/address-book/contact"
    token=getToken(ENV1,userName1, 'Test!123','password')  #'18668180001',
    print(token)
    paras={'firstName':firstname,'mobilePhone':mobilephone,'lastName':lastname}
    payload=json.dumps(paras)
    headers={'Authorization':token,'Content-Type':'application/json'}
    createNewContactResonse=requests.post(baseUrl,data=payload,headers=headers)
    print(createNewContactResonse.json())
    print(createNewContactResonse.status_code)
    if createNewContactResonse.ok:
        print('create successfully')
    else:
        print('create fail')
    return


def multipleCreate(n,ENV1,userName1,firstname,mobilephone,lastname):
    count=0
    while (count<n):
        createNewContact(ENV1,userName1,firstname,mobilephone,lastname)
        count=count+1
    return






createNewContact('https://platform-devfre.lab.rcch.ringcentral.com:8446','18668180001','3hhhh','6502358974','yyyy')
#getToken("https://platform-devfre.lab.rcch.ringcentral.com:8446",'18668180001','Test!123','password')
#multipleCreate(2,'https://platform-devfre.lab.rcch.ringcentral.com:8446','18668180001','c','6502358974','d')