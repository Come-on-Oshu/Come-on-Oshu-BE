import os
import secret
import requests
import django

from datetime import date, timedelta, datetime
from dateutil import relativedelta
import xmltodict as xmltodict
from rest_framework.utils import json

# declare before bring models.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Oshu.settings')
django.setup()

# bring models.py(use absolute path)
from oshuApp.models import EventInformation, EventLocation

# request an openAPI and receive a list of events response
# return the list of events for the current month
def requestEvent(stDate, edDate, eventstate):
    # open api url
    url = 'http://www.kopis.or.kr/openApi/restful/pblprfr'

    # open api request parameters
    params = {'service': secret.key, 'stdate': stDate, 'eddate': edDate, 'cpage': 1, 'rows': 50, 'prfstate': eventstate,
              'signgucode': 30}

    # open api request
    response = requests.get(url, params=params)

    # xml to json
    xpars = xmltodict.parse(response.text)
    jsonDump = json.dumps(xpars)
    jsonBody = json.loads(jsonDump)

    contents = jsonBody['dbs']['db']
    return contents


# request an openAPI using EventID and receive detailed information about the Event
# find LocationID in detailed information
# return LocationID
def requestLocationID(conid):
    url = 'http://www.kopis.or.kr/openApi/restful/pblprfr/'
    url = url + conid
    params = {'service': secret.key}

    response = requests.get(url, params=params)

    xpars = xmltodict.parse(response.text)
    jsonDump = json.dumps(xpars)
    jsonBody = json.loads(jsonDump)

    contents = jsonBody['dbs']['db']

    return contents['mt10id']


# request an openAPI using LocationID and receive detailed information about the location
# return the detailed information about the location
def requestLocationDetail(LocationID):
    url = 'http://www.kopis.or.kr/openApi/restful/prfplc/'
    url = url + LocationID
    params = {'service': secret.key}

    response = requests.get(url, params=params)
    xpars = xmltodict.parse(response.text)
    jsonDump = json.dumps(xpars)
    jsonBody = json.loads(jsonDump)

    contents = jsonBody['dbs']['db']
    return contents


def updateDB(contents):
    print("Insert data to EventLoaction table...")
    for item in contents:
        try:
            LocationID = requestLocationID(item['mt20id'])
            detailContents = requestLocationDetail(LocationID)

            EL = EventLocation()
            EL.LocationID = detailContents['mt10id']
            item['LocationID'] = detailContents['mt10id']
            EL.LocationName = detailContents['fcltynm']
            EL.Telno = detailContents['telno']
            EL.SiteUrl = detailContents['relateurl']
            EL.address = detailContents['adres']
            EL.la = detailContents['la']
            EL.lo = detailContents['lo']

            EL.save()
        except:
            print("중복 처리")

    print("Insertion complete")

    print("Insert data to EventInformation table...")
    for item in contents:
        EI = EventInformation()

        stDate = item['prfpdfrom']
        edDate = item['prfpdto']
        Date_format = '%Y.%m.%d'

        stDate = datetime.strptime(stDate, Date_format)
        stDate = stDate.strftime('%Y-%m-%d')
        edDate = datetime.strptime(edDate, Date_format)
        edDate = edDate.strftime('%Y-%m-%d')

        LocationID = item['LocationID']
        eventlocation = EventLocation.objects.get(LocationID=LocationID)

        district = eventlocation.address.split()

        try:
            EI.EventID = item['mt20id']
            # EI.District = district[1]
            district = district[1]
            if district == '서구':
                EI.District = 1
            elif district == '유성구':
                EI.District = 2
            elif district == '중구':
                EI.District = 3
            elif district == '동구':
                EI.District = 4
            elif district == '대덕구':
                EI.District = 5

            EI.EventName = item['prfnm']
            EI.isFestival = 1
            EI.ImgUrl = item['poster']
            EI.stDate = stDate
            EI.edDate = edDate
            EI.Organization = item['fcltynm']
            EI.lid = eventlocation
            EI.save()
        except:
            print("중복 처리")

    print("Insertion complete")


if __name__ == "__main__":

    # find the first and last date based on current date
    today = date.today()

    stDate = today.replace(day=1)
    nextenDate = stDate + relativedelta.relativedelta(months=1)
    edDate = nextenDate - timedelta(days=1)

    stDate = today
    edDate = edDate.strftime('%Y%m%d')

    # request open api
    contents = requestEvent(stDate, edDate, '01')  # List of events in the current month
    updateDB(contents)

    contents = requestEvent(stDate, edDate, '02')  # List of events in the current month
    updateDB(contents)