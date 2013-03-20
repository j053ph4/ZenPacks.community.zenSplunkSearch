from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.component import ComponentInfo
<<<<<<< HEAD
from ZenPacks.community.zenSplunkSearch.interfaces import *

'''
args:  zenpack,compInfo,compInterface,infoProperties
'''

class SplunkSearchInfo(ComponentInfo):
    implements( ISplunkSearchInfo )
    server = ProxyProperty('server')
    alias = ProxyProperty('alias')
    user = ProxyProperty('user')
    query = ProxyProperty('query')
    password = ProxyProperty('password')
    port = ProxyProperty('port')


'''
args : zenpackname,zenpackname,dsclass,dsvolcclass,dsvolcvar,dsinfo,dsinterface,dsinfoproperties
'''
# datasource info
from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from zope.schema.vocabulary import SimpleVocabulary
from Products.Zuul.infos.template import RRDDataSourceInfo
from ZenPacks.community.zenSplunkSearch.interfaces import *
from ZenPacks.community.zenSplunkSearch.datasources.SplunkSearchDataSource import *

def SplunkSearchRedirectVocabulary(context):
    return SimpleVocabulary.fromValues(SplunkSearchDataSource.onRedirectOptions)

class SplunkSearchDataSourceInfo(RRDDataSourceInfo):
    implements(ISplunkSearchDataSourceInfo)
    alias = ProxyProperty('alias')
    cycletime = ProxyProperty('cycletime')
    user = ProxyProperty('user')
    timeout = ProxyProperty('timeout')
    query = ProxyProperty('query')
    password = ProxyProperty('password')
    port = ProxyProperty('port')
    server = ProxyProperty('server')

    @property
    def testable(self):
        ''''''
=======
from ZenPacks.community.zenSplunkSearch.interfaces import ISplunkSearchInfo,ISplunkDataSourceInfo
from Products.Zuul.infos import InfoBase

class SplunkSearchInfo(ComponentInfo):
    """
    Info adapter for SplunkSearch components.
    """
    implements(ISplunkSearchInfo)
    splunkSearch = ProxyProperty("splunkSearch")
    
class SplunkDataSourceInfo(InfoBase):
    implements(ISplunkDataSourceInfo)
    component = ProxyProperty('component')
    eventKey = ProxyProperty('eventKey')
    timeout = ProxyProperty('timeout')
    splunkServer = ProxyProperty('splunkServer')
    splunkPort = ProxyProperty('splunkPort')
    splunkUsername = ProxyProperty('splunkUsername')
    splunkPassword = ProxyProperty('splunkPassword')
    splunkSearch = ProxyProperty('splunkSearch')
    enabled = ProxyProperty('enabled')
    
    @property
    def testable(self):
        """
        We can NOT test this datsource against a specific device
        """
>>>>>>> 4d329403a84318cea7c3058767c0ddf937d76fdb
        return False

