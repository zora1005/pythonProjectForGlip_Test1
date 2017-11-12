import requests
import json
#import urllib2



def getToken(ENV, userName, passWord, grant_Type):
    baseUrl = ENV + "/restapi/oauth/token"
    if ENV == 'https://platform-devfre.lab.rcch.ringcentral.com:8446':
        endCode ='MDJiNzI5MTgwMDRhOWVkMzM2YjlDRUJDNDhlNjAzOGJlM2YyMTk2NDI2MjFBODA0MjA3MmY5N2MyQzg0MkZBQTpGQkQzRENBMDk5N2JFQTlCMGI4MWY4NTZlY2NiOWNkMmIxOWQ2MDYwNzc3NmE4NjFDOUM0N2RiNWVkMDU0ODcy'
    elif ENV == 'http://api-up.lab.rcch.ringcentral.com': # or 'https://api-up.lab.rcch.ringcentral.com':
        endCode = 'TWtDZGxTVnFRMDZINmk3S1ljdjliZzo1X3RGQlhCUVRMV2FWY1BGNjFMVUdnbmdCZmM4S0dRQ2FaMF9VVHc4MHZzdw=='
    keyEndcode = 'Basic ' + endCode
    payload={'username':userName, 'password':passWord, 'grant_type':grant_Type}
    headers={'Authorization':keyEndcode, 'Accept':'application/json'}
    getTokenResponse=requests.post(baseUrl, data=payload, headers=headers)
    #print(getTokenResponse.text)
    data=getTokenResponse.json()
    if getTokenResponse.ok:
        access_token=data['token_type']+' '+data['access_token']
    else:
        print('Failed to get access token:'+str[data])
    return (access_token)

def getFavirutesID(ENV, userName):
    baseUrl=ENV + "/restapi/v1.0/account/~/extension/~/favorite"
    token=getToken(ENV, userName, "Test!123", "password")
    header1 = {'Authorization': token, 'Content-Type': 'application/json'}
    r = requests.get(baseUrl,headers=header1)
    favoritesRecord = r.json();
    return favoritesRecord



def addFavorites(ENV, userName, contactId):
    baseUrl=ENV + "/restapi/v1.0/account/~/extension/~/favorite"
    token=getToken(ENV, userName, "Test!123", "password")
    header2 = {'content-type': 'application/json', 'Authorization': token}
    paras = getFavirutesID(ENV, userName)
    paras['records'].append({'id':(len(paras['records'])+1),'contactId':contactId})
    payload = json.dumps(paras)
    addFavoritesResonse = requests.put(baseUrl, data=payload, headers=header2)
    newFavoriteList = addFavoritesResonse.json()
    #print(newFavoriteList)


    if addFavoritesResonse.ok:
        print('Add successfully!')
        print(newFavoriteList['records'])


    else:
        print('Add fail!')
    return addFavoritesResonse



def createNewContact(ENV, userName, firstName, lastName, mobilePhone):
    baseUrl=ENV+"/restapi/v1.0/account/~/extension/~/address-book/contact"
    token=getToken(ENV,userName, 'Test!123', 'password')
    paras = {'firstName': firstName, 'lastName': lastName, 'mobilePhone': mobilePhone}
    payload = json.dumps(paras)
    header1 = {'Authorization': token, 'Content-Type': 'application/json'}
    createNewContactResonse = requests.post(baseUrl, data=payload, headers=header1)
    #print(createNewContactResonse.json())
    #print(createNewContactResonse.status_code)
    if createNewContactResonse.ok:
        print('Create successfully!')
        print(firstName)
        print(lastName)
        data = createNewContactResonse.json()
        contactId = data['id']
        print (contactId)
        for index in range(0, 1):
            addFavorites(ENV, userName, contactId)

    else:
        print('Create fail!')
    return







def multipleCreate(n, ENV, userName, firstName, lastName, mobilePhone):
    count = 0
    while (count<n):
        createNewContact(ENV, userName, firstName, lastName, mobilePhone)
        count = count+1
    return


#getFavirutesID('http://api-up.lab.rcch.ringcentral.com','18773344444')
#addFavorites('http://api-up.lab.rcch.ringcentral.com','18773344444','1214605004')
#createNewContact('http://api-up.lab.rcch.ringcentral.com','18773344444','hello10','world10','6502358975')
#addFavorites('http://api-up.lab.rcch.ringcentral.com','18773344444')
#addFavorites('http://api-up.lab.rcch.ringcentral.com','18773344444','hello','world','6502358974')
#getToken("http://api-up.lab.rcch.ringcentral.com",'18773344444','Test!123','password')
multipleCreate(2,'http://api-up.lab.rcch.ringcentral.com','18773344444','hello10','world10','6502358975')