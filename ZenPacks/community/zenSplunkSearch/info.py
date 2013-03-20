from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.component import ComponentInfo
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
        return False

