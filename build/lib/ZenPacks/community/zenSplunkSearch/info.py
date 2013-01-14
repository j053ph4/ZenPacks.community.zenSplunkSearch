from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.component import ComponentInfo
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
        return False

