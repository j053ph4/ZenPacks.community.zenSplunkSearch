import Globals
from Products.ZenModel.ZenPack import ZenPack as ZenPackBase
from Products.ZenUtils.Utils import unused
import os,re
skinsDir = os.path.join(os.path.dirname(__file__), 'skins')
from Products.CMFCore.DirectoryView import registerDirectory
if os.path.isdir(skinsDir):
    registerDirectory(skinsDir, globals())


unused(Globals)
""" Add device relations
"""
from Products.ZenModel.OperatingSystem import OperatingSystem
from Products.ZenRelations.RelSchema import *
OperatingSystem._relations += (("splunkComponents", ToManyCont(ToOne,
                                    "ZenPacks.community.zenSplunkSearch.SplunkSearch", "os")),
                            )


from Products.ZenUtils.Utils import monkeypatch,prepId

@monkeypatch('Products.ZenModel.Device.Device')
def manage_addSplunkSearch(self, search=''):
    """make a Splunk Search component"""
    from SplunkSearch import SplunkSearch
    newId = self.id + '_' + re.sub('[^A-Za-z0-9]+', '', search)
    hcid = prepId(newId)
    splunksearch = SplunkSearch(hcid)
    self.os.splunkComponents._setObject(splunksearch.id, search)
    splunksearch = self.os.splunkComponents._getOb(splunksearch.id)
    splunksearch.splunkSearch = search
    return splunksearch

class ZenPack(ZenPackBase):
    """ Splunk Search Component
    """
    
    packZProperties = [
        ('zSplunkServer', 'default', 'string'),
        ('zSplunkPort', '8089', 'string'),
        ('zSplunkUsername', 'default', 'string'),
        ('zSplunkPassword', 'default', 'password'),
        ]
            
    def updateRelations(self):
        for d in self.dmd.Devices.getSubDevices():
            d.os.buildRelations()
            
    def install(self, app):
        ZenPackBase.install(self, app)
        self.updateRelations()
        
    def upgrade(self, app):
        ZenPackBase.upgrade(self, app)
        self.updateRelations()
        
    def remove(self, app, leaveObjects=False):
        ZenPackBase.remove(self, app, leaveObjects=leaveObjects)
        OperatingSystem._relations = tuple([x for x in OperatingSystem._relations if x[0] not in ('splunkComponents')])
        self.updateRelations()
