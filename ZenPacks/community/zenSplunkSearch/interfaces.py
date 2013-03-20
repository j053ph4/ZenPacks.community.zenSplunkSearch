
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


