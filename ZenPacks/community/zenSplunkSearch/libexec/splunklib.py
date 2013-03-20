######################################################################
#
# Copyright 2009 Zenoss, Inc.  All Rights Reserved.
#
######################################################################

from httplib import HTTPSConnection
from urllib import urlencode
from xml.dom.minidom import parseString


class Unauthorized(Exception): pass
class Failure(Exception): pass
class NotFinished(Exception): pass


class Connection:
    _server = None
    _port = None
    _credentials = None
    _sessionkey = None

<<<<<<< HEAD
    def __init__(self, server, port, username, password):
        self._server = server
        self._port = port
        self._credentials = urlencode({
                                       'username':username, 
                                       'password':password
                                       })
=======

    def __init__(self, server, port, username, password):
        self._server = server
        self._port = port
        self._credentials = urlencode(
            {'username':username, 'password':password})

>>>>>>> 4d329403a84318cea7c3058767c0ddf937d76fdb

    def setSessionKey(self, sessionkey):
        self._sessionkey = sessionkey

<<<<<<< HEAD
=======

>>>>>>> 4d329403a84318cea7c3058767c0ddf937d76fdb
    def getSessionKey(self):
        if self._sessionkey:
            return self._sessionkey

        h = HTTPSConnection(self._server, self._port)
        h.request('POST', '/services/auth/login/', self._credentials)
        r = h.getresponse()
        content = r.read()
<<<<<<< HEAD
        
=======

>>>>>>> 4d329403a84318cea7c3058767c0ddf937d76fdb
        if r.status != 200:
            raise Unauthorized('Server responded with code %s' % r.status)

        if len(content) < 1:
            raise Unauthorized('No response to authentication attempt')

        xml = parseString(content)
        elements = xml.getElementsByTagName('sessionKey')
        if len(elements) < 1:
            raise Unauthorized('No session key returned from authentication')

        self._sessionkey = elements[0].firstChild.nodeValue
        return self._sessionkey

<<<<<<< HEAD
=======

>>>>>>> 4d329403a84318cea7c3058767c0ddf937d76fdb
    def getHeaders(self):
        return {
            'Authorization': 'Splunk %s' % self.getSessionKey(),
            'Content-type': 'application/x-www-form-urlencoded',
            }

<<<<<<< HEAD
=======

>>>>>>> 4d329403a84318cea7c3058767c0ddf937d76fdb
    def _request(self, method, url, body=None):
        h = HTTPSConnection(self._server, self._port)
        h.request(method, url, body, self.getHeaders())
        r = h.getresponse()
        return r, r.read()

<<<<<<< HEAD
=======

>>>>>>> 4d329403a84318cea7c3058767c0ddf937d76fdb
    def createSearch(self, search, **kwargs):
        kwargs.update({'search': search})
        body = urlencode(kwargs)
        r, content = self._request('POST', '/services/search/jobs/', body)

        if r.status == 401:
            raise Unauthorized('Server responded with code %s' % r.status)
        elif r.status != 201:
            raise Failure('Server responded with code %s' % r.status)

        if len(content) < 1:
            raise Failure('No response to job creation attempt')

        xml = parseString(content)
        elements = xml.getElementsByTagName('sid')
        if len(elements) < 1:
            raise Failure('No sid returned from job creation')

        return elements[0].firstChild.nodeValue

<<<<<<< HEAD
    def getSearchResults(self, sid, **kwargs):
        params = urlencode(kwargs)
        if params:
            params = '?%s' % params
        r, content = self._request('GET', '/services/search/jobs/%s/results%s?output_mode=xml' % (sid, params))
=======

    def getSearchResults(self, sid, **kwargs):
        #print "getting results for ",sid
        params = urlencode(kwargs)
        if params:
            params = '?%s' % params
            #print " using params",params
        
        #print "request",'/services/search/jobs/%s/results%s' % (sid, params)
        r, content = self._request('GET',
            '/services/search/jobs/%s/results%s?output_mode=xml' % (sid, params))
        #print "status",r.status
        #print "reason",r.reason
        #print "data",r.read()
        #print "content",content
        #print "result",r,content
        
>>>>>>> 4d329403a84318cea7c3058767c0ddf937d76fdb
        if r.status == 204:
            raise NotFinished('Job still processing. Try again later')
        elif r.status != 200:
            raise Failure('Server returned code %s' % r.status)
<<<<<<< HEAD
        if len(content) < 1:
            raise Failure('No response for job results')
        return content

=======
        #if r.status == 200 and len(content) < 1:
         #   content = ""
            
        if len(content) < 1:
            raise Failure('No response for job results')

        return content


>>>>>>> 4d329403a84318cea7c3058767c0ddf937d76fdb
    def deleteSearch(self, sid):
        r, content = self._request('DELETE', '/services/search/jobs/%s' % sid)
