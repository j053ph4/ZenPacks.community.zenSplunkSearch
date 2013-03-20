import Globals
from Products.ZenModel.ZenPack import ZenPack as ZenPackBase
<<<<<<< HEAD
from Products.ZenModel.OperatingSystem import OperatingSystem
from Products.ZenUtils.Utils import unused
from Definition import *

unused(Globals)

c = Construct(Definition)
c.addDeviceRelation()

# copied from HttpMonitor
def onCollectorInstalled(ob, event):
    zpFriendly = c.componentClass
    errormsg = '{0} binary cannot be found on {1}. This is part of the nagios-plugins ' + \
               'dependency, and must be installed before {2} can function.'
    verifyBin = c.cmdFile
    code, output = ob.executeCommand('zenbincheck %s' % verifyBin, 'zenoss', needsZenHome=True)
    if code:
        log.warn(errormsg.format(verifyBin, ob.hostname, zpFriendly))

class ZenPack(ZenPackBase):
    """ Zenpack install
    """
    
    packZProperties = c.d.packZProperties
    
    def updateRelations(self):
        for d in self.dmd.Devices.getSubDevices():
            d.os.buildRelations()  

    def install(self, app):
        c.buildZenPackFiles()
        ZenPackBase.install(self, app)
        self.updateRelations()

    def remove(self, app, leaveObjects=False):
        ZenPackBase.remove(self, app, leaveObjects)
        if not leaveObjects:
            OperatingSystem._relations = tuple([x for x in OperatingSystem._relations if x[0] not in (c.relname)])
            self.updateRelations()
=======
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
>>>>>>> 4d329403a84318cea7c3058767c0ddf937d76fdb
