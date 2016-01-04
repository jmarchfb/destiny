#!/bin/python

import sys
import os
import requests
import time

from pprint import pprint as pp

from destiny.exceptions import *


class DestinyClient:

    HEADERS = {"X-API-Key": "PUT_API_KEY_HERE"}
    PLATFORM = {'XBOX': 1, 'PSN': 2}
    MODE = {'TOO' : 14}

    URL = 'http://www.bungie.net/Platform/Destiny/{0}'
    ENDPOINT = {
        # m_type, m_id, c_id, mode, page, count
        'ActivityHistory' : '/Stats/ActivityHistory/{0}/{1}/{2}/?mode={3}&page={4}&count={5}',
        # i_id  
        'PostGameCarnageReport' : '/Stats/PostGameCarnageReport/{0}/',
        # m_type, d_name
        'GetMembershipIdByDisplayName' : '/{0}/Stats/GetMembershipIdByDisplayName/{1}/',
        # m_type, displayName
        'SearchDestinyPlayer': '/SearchDestinyPlayer/{0}/{1}/',
        # m_type, m_id
        'GetAccount' : '/{0}/Account/{1}/',
    }

    def __getattr__(self, method):
        def f(*args):
            url = DestinyClient.URL.format(DestinyClient.ENDPOINT[method].format(*args))
            st = time.time()
            tries = 0
            while tries < 5:
              tries += 1

              resp = requests.get(url, headers=DestinyClient.HEADERS).json()

              if resp['ErrorStatus'] == 'PerEndpointRequestThrottleExceeded':
                  time.sleep(1)
                  continue

              if resp['ErrorStatus'] == 'Success':
                  break

              raise_destiny_exception(resp['ErrorCode'])

            if tries == 5:
                raise Exception("Too many retries")

            end = time.time()

            # print('method: %s %s %0.2f %d %d %s %s' % (
            #       method, args, end-st,
            #       resp['ThrottleSeconds'], resp['ErrorCode'],
            #       resp['ErrorStatus'], resp['MessageData']))

            if resp['ErrorStatus'] == 'Success':
                return resp['Response']

            return None
        return f
