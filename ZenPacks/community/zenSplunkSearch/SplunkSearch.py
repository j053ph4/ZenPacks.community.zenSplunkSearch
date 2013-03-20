<<<<<<< HEAD
from Products.ZenModel.OSComponent import OSComponent
from Products.ZenModel.ZenPackPersistence import ZenPackPersistence
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenRelations.RelSchema import *

'''
args:  classname,classname,properties,_properties,relname,sortkey,viewname
'''

class SplunkSearch(OSComponent, ManagedEntity, ZenPackPersistence):
    '''
    	basic Component class
    '''
    
    portal_type = meta_type = 'SplunkSearch'
    
    server = ''
    alias = None
    user = ''
    query = None
    password = ''
    port = ''

    _properties = (
    {'id': 'server', 'type': 'string','mode': '', 'switch': '-s' },
    {'id': 'alias', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'user', 'type': 'string','mode': '', 'switch': '-u' },
    {'id': 'query', 'type': 'string','mode': '', 'switch': '-q' },
    {'id': 'password', 'type': 'string','mode': '', 'switch': '-w' },
    {'id': 'port', 'type': 'string','mode': '', 'switch': '-p' },

    )
    
    _relations = OSComponent._relations + (
        ('os', ToOne(ToManyCont, 'Products.ZenModel.OperatingSystem', 'splunkSearchs')),
        )

    isUserCreatedFlag = True
    def isUserCreated(self):
        return self.isUserCreatedFlag
        
    def statusMap(self):
        self.status = 0
        return self.status
    
    def getStatus(self):
        return self.statusMap()
    
    def primarySortKey(self):
        return self.alias
    
    def viewName(self):
        return self.alias
    
    name = titleOrId = viewName
=======
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
>>>>>>> 4d329403a84318cea7c3058767c0ddf937d76fdb


