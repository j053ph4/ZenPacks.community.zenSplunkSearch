################################################################################
#
# This program is part of the zenHttpComponent Zenpack for Zenoss.
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
################################################################################
from Products.ZenModel.OSComponent import OSComponent
from Products.ZenModel.ZenPackPersistence import ZenPackPersistence
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne
   
class SplunkSearch(OSComponent, ManagedEntity, ZenPackPersistence):
    """
    SplunkSearch contains the basic properties of a SplunkSearch
    """
    portal_type = meta_type = 'SplunkSearch'
    
    splunkSearch = ''

    _properties = (
        {'id':'splunkSearch', 'type':'string', 'mode':''},
        )

    _relations = OSComponent._relations + (
        ("os", ToOne(ToManyCont, "Products.ZenModel.OperatingSystem", "splunkComponents")),
        )

    
    isUserCreatedFlag = True
    def isUserCreated(self):
        return self.isUserCreatedFlag
    
    def viewName(self):
        return self.splunkSearch
    titleOrId = name = viewName

    def primarySortKey(self):
        return self.splunkSearch
    
#    def getStatus(self):
#        return self.statusMap()
#    
#    def statusMap(self):
#        """ map run state to zenoss status
#        """
#        self.status = 0
#        return self.status


