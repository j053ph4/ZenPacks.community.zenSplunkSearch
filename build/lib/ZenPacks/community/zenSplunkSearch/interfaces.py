<<<<<<< HEAD

'''
args: componentInterface,comopnentInterfaceproperties,componentIFacade,iFacadeMethodName
'''

from Products.Zuul.form import schema
from Products.Zuul.interfaces.component import IComponentInfo
from Products.Zuul.interfaces import IFacade

from Products.Zuul.utils import ZuulMessageFactory as _t

from Products.ZenModel.ZVersion import VERSION as ZENOSS_VERSION
from Products.ZenUtils.Version import Version
if Version.parse('Zenoss ' + ZENOSS_VERSION) >= Version.parse('Zenoss 4'):
    SingleLineText = schema.TextLine
    MultiLineText = schema.Text
else:
    SingleLineText = schema.Text
    MultiLineText = schema.TextLine


class ISplunkSearchInfo(IComponentInfo):
    server = SingleLineText(title=_t(u'Server'))
    alias = SingleLineText(title=_t(u'Alias'))
    user = SingleLineText(title=_t(u'User'))
    query = SingleLineText(title=_t(u'Query'))
    password = SingleLineText(title=_t(u'Password'))
    port = SingleLineText(title=_t(u'Port'))



class IzenSplunkSearchFacade(IFacade):
    def addSplunkSearch(self, ob, **kwargs):
        ''''''

'''
args : dsinterface,dsinterfaceproperties
'''

# datasource interface
from Products.Zuul.interfaces import IRRDDataSourceInfo
from Products.Zuul.form import schema
from Products.Zuul.utils import ZuulMessageFactory as _t

if Version.parse('Zenoss ' + ZENOSS_VERSION) >= Version.parse('Zenoss 4'):
    SingleLineText = schema.TextLine
    MultiLineText = schema.Text
else:
    SingleLineText = schema.Text
    MultiLineText = schema.TextLine

class ISplunkSearchDataSourceInfo(IRRDDataSourceInfo):
    alias = SingleLineText(title=_t(u'Alias'))
    cycletime = schema.Int(title=_t(u'Cycle Time (s)'))
    user = SingleLineText(title=_t(u'User'))
    timeout = SingleLineText(title=_t(u'Timeout (s)'))
    query = SingleLineText(title=_t(u'Query'))
    password = SingleLineText(title=_t(u'Password'))
    port = SingleLineText(title=_t(u'Port'))
    server = SingleLineText(title=_t(u'Server'))


=======
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
        
>>>>>>> 4d329403a84318cea7c3058767c0ddf937d76fdb
