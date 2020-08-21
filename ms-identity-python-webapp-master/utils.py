#-*-coding:utf-8-*-
import threading
import requests
import json
from requests.adapters import HTTPAdapter




class Adaptor:
    def __init__(self,dataList):
        self.dataList = dataList

    @property
    def run(self):
        postDataList,updateDataList=[],[]
        for data in self.dataList:
            tempData = {'emailAddresses': [], 'businessPhones': []}
            tempData['givenName'] = data.firstname
            tempData['surname'] = data.lastname
            tempData['emailAddresses'].append({"address": data.email, "name": data.firstname + " " + data.lastname})
            tempData['businessPhones'].append(data.otherphone)
            if not data.contact_id:
                tempData['id'] = data.id
                postDataList.append(tempData)
            else:
                tempData['contact_id'] =  data.contact_id
                updateDataList.append(tempData)
        return postDataList,updateDataList


class Handler:

    def __init__(self, postDataList,updataDataList,Token):

        self.postDataList = postDataList
        self.updataDataList = updataDataList
        self.headers ={'Authorization': 'Bearer ' + Token['access_token'],"Content-Type":"application/json"}
        self.postUrl = 'https://graph.microsoft.com/v1.0/me/contacts'
        self.updataUrl = 'https://graph.microsoft.com/v1.0/me/contacts/'
        self.request = requests.Session().mount('https://', HTTPAdapter(max_retries=3))

    def postData(self,data):
        from app import db
        from model import Contactor

        id = data['id']
        del data['id']
        headers = self.headers
        r = self.request.post(self.postUrl, headers = headers,data=json.dumps(data),timeout=1)
        dataObj = Contactor.query.get(id)
        dataObj.contact_id = r.json()['id']
        db.session.commit()


    def updateData(self,data):

        contact_id = data['contact_id']
        del data['contact_id']
        headers = self.headers
        self.request.patch(self.updataUrl+contact_id, headers=headers, data=json.dumps(data))



    def postDataWorker(self):
        while self.postDataList:
            data = self.postDataList.pop()
            postThreadObj = threading.Thread(target=self.postData,args=(data,))
            postThreadObj.start()


    def updateDataWorker(self):
        while self.updataDataList:
            data = self.updataDataList.pop()
            updateThreadObj = threading.Thread(target=self.updateData,args=(data,))
            updateThreadObj.start()

    @property
    def run(self):
        runnerPost = threading.Thread(target=self.postDataWorker)
        runnerUpdate = threading.Thread(target=self.updateDataWorker)
        runnerPost.start()
        runnerUpdate.start()
