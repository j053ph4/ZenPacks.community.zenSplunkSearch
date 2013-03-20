from Products.ZenModel.RRDDataSource import RRDDataSource
from Products.ZenModel.ZenPackPersistence import ZenPackPersistence
from AccessControl import ClassSecurityInfo, Permissions
from Products.ZenUtils.ZenTales import talesCompile, getEngine
from Products.ZenUtils.Utils import binPath

'''
Args:  classname, datasourcename, zenpackname, eventClass, cycletime, timeout, cmdfile, dpoints, properties,_properties,datasourcename,datasourcename
'''

class SplunkSearchDataSource(ZenPackPersistence, RRDDataSource):
    DATASOURCE = 'SplunkSearch'
    ZENPACKID = 'ZenPacks.community.zenSplunkSearch'
    sourcetypes = (DATASOURCE,)
    sourcetype = DATASOURCE
    eventClass = '/Unknown'
    cycletime = 60
    timeout = 300
    component = '${here/alias}'
    cmdFile = 'check_splunk.py'
    provided = True
    dpoints = ['count']
    
    alias = '${here/alias}'
    user = '${here/user}'
    query = '${here/query}'
    password = '${here/password}'
    port = '${here/port}'
    server = '${here/server}'

    _properties = RRDDataSource._properties + (
    {'id': 'alias', 'type': 'string','mode': 'w', 'switch': 'None'},
    {'id': 'cycletime', 'type': 'int','mode': 'w', 'switch': 'None'},
    {'id': 'user', 'type': 'string','mode': 'w', 'switch': '-u'},
    {'id': 'timeout', 'type': 'string','mode': 'w', 'switch': '-t'},
    {'id': 'query', 'type': 'string','mode': 'w', 'switch': '-q'},
    {'id': 'password', 'type': 'string','mode': 'w', 'switch': '-w'},
    {'id': 'port', 'type': 'string','mode': 'w', 'switch': '-p'},
    {'id': 'server', 'type': 'string','mode': 'w', 'switch': '-s'},

    )
    
    _relations = RRDDataSource._relations + (
        )
        
    factory_type_information = (
    {
        'immediate_view' : 'editSplunkSearchDataSource',
        'actions'        :
        (
            { 'id'            : 'edit',
              'name'          : 'Data Source',
              'action'        : 'editSplunkSearchDataSource',
              'permissions'   : ( Permissions.view, ),
            },
        )
    },
    )

    security = ClassSecurityInfo()

    def __init__(self, id, title=None, buildRelations=True):
        RRDDataSource.__init__(self, id, title, buildRelations)
        self.addDataPoints()
    
    def getDescription(self):
        if self.sourcetype == self.DATASOURCE:
            return self.component
        return RRDDataSource.getDescription(self)
    
    def useZenCommand(self):
        return True
        
    def getCommand(self, context):
        '''
            generate the plugin command
        '''
        cmd = binPath(self.cmdFile)
        if self.provided == False:
            cmd = binPath(self.cmdFile)
        else:
            cmd = self.cmdFile
        parts = [cmd]
        endargs = ''
        props = getattr(context,'_properties')
        for p in props:
            ptype = p['type']
            switch = p['switch']
            value = getattr(context,p['id'])
            if value is not None and len(str(value)) > 0:
                if switch != 'None':
                    if ptype == 'boolean':
                        if value == True:
                            parts.append('%s' % switch)
                    elif ptype == 'list' or ptype == 'lines':
                        bySpace = value.split(' ')
                        byNewline = value.split('\n')
                        if len(bySpace) > len(byNewline):
                            endargs = '%s \"%s\"' % (switch, ' '.join(bySpace))
                        else:
                            endargs = '%s \"%s\"' % (switch, ' '.join(byNewline))
                    else:
                        if len(str(value)) > 0:
                            parts.append('%s \"%s\" ' % (switch, str(value)))
        parts.append(endargs)
        cmd = ' '.join(parts)
        cmd = RRDDataSource.getCommand(self, context, cmd)
        return cmd


    def checkCommandPrefix(self, context, cmd):
    	if self.provided == True:
            return self.getZenPack(context).path('libexec', cmd)
        else:
            return cmd
            
    def addDataPoints(self):
        for p in self.dpoints:
            if not self.datapoints._getOb(p, None):
                self.manage_addRRDDataPoint(p)
    
    def zmanage_editProperties(self, REQUEST=None):
        '''validation, etc'''
        if REQUEST:
            # ensure default datapoint didn't go away
            self.addDataPoints()
            # and eventClass
            if not REQUEST.form.get('eventClass', None):
                REQUEST.form['eventClass'] = self.__class__.eventClass
        return RRDDataSource.zmanage_editProperties(self, REQUEST)

