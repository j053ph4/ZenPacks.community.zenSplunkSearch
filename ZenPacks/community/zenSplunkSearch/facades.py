'''
args:  compFacade,compClass,facadeName,iFacadeName,facadeMethodName, createMethod, singular
'''

import os,re
import logging
log = logging.getLogger('zen.zenSplunkSearchFacade')

from zope.interface import implements
from Products.Zuul.facades import ZuulFacade
from Products.Zuul.utils import ZuulMessageFactory as _t
from SplunkSearch import *
from .interfaces import *

class zenSplunkSearchFacade(ZuulFacade):
    implements(IzenSplunkSearchFacade)
    
    def addSplunkSearch(self, ob, **kwargs):
    	target = ob
    
        from Products.ZenUtils.Utils import prepId
        from ZenPacks.community.zenSplunkSearch.SplunkSearch import SplunkSearch
        import re
        cid = ''
        for k,v in kwargs.iteritems():
            if type(v) != bool:
                cid += str(v)
        cid = re.sub('[^A-Za-z0-9]+', '_', cid)
        id = prepId(cid)
        component = SplunkSearch(id)
        relation = target.os.splunkSearchs
        relation._setObject(component.id, component)
        component = relation._getOb(component.id)
        for k,v in kwargs.iteritems():
            setattr(component,k,v) 
        
        setattr(component,"server",target.zSplunkServer)
        setattr(component,"user",target.zSplunkUsername)
        setattr(component,"password",target.zSplunkPassword)
        setattr(component,"port",target.zSplunkPort)
    
    
    

    	return True, _t("Added Splunk Search for device " + target.id)

