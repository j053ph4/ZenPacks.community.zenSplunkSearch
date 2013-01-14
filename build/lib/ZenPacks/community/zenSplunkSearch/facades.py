import os,re
import logging
log = logging.getLogger('zen.zenSplunkSearchfacade')

from zope.interface import implements
from Products.Zuul.facades import ZuulFacade
from Products.Zuul.utils import ZuulMessageFactory as _t
from SplunkSearch import SplunkSearch
from .interfaces import IzenSplunkSearchFacade


class zenSplunkSearchFacade(ZuulFacade):
    implements(IzenSplunkSearchFacade)

    def addSplunkSearch(self, ob, search=''):
        """ Adds SplunkSearch Component"""
        id = ob.id + '_' + re.sub('[^A-Za-z0-9]+', '', search)
        splunksearch = SplunkSearch(id)
        ob.os.splunkComponents._setObject(splunksearch.id, splunksearch)
        splunksearch = ob.os.splunkComponents._getOb(splunksearch.id)
        splunksearch.splunkSearch = search

        return True, _t(" Added Splunk Search for device %s" % (ob.id))
