from Products.Zuul.form import schema
from Products.Zuul.interfaces.component import IComponentInfo
from Products.Zuul.interfaces import IFacade
from Products.Zuul.interfaces import IInfo
from Products.Zuul.utils import ZuulMessageFactory as _t

class ISplunkSearchInfo(IComponentInfo):
    """
    Info adapter for SplunkSearch components.
    """
    splunkSearch = schema.Text(title=u"Search")

class ISplunkDataSourceInfo(IInfo):
    timeout = schema.Int(title=_t(u"Timeout (seconds)"))
    component = schema.Text(title=_t(u"Component"))
    eventKey = schema.Text(title=_t(u"Event Key"))

    splunkServer = schema.Text(title=_t(u"Splunk Server"),
                               group=_t('Splunk'))
    splunkUsername = schema.Text(title=_t(u"Splunk Username"),
                                 group=_t('Splunk'))
    splunkPort = schema.Text(title=_t(u"Splunk Port"),
                            group=_t('Splunk'))
    splunkPassword = schema.Password(title=_t(u"Splunk Password"),
                                     group=_t('Splunk'))
    splunkSearch = schema.Text(title=_t(u"Search"),
                               group=_t('Splunk'))

class IzenSplunkSearchFacade(IFacade):
    
    def addSplunkSearch(self, ob, splunkSearch):
        """  add Splunk Search Component to device
        """
        
