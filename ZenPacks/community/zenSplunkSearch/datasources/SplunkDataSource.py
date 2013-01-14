#from Products.ZenModel.RRDDataSource import RRDDataSource
from Products.ZenModel.BasicDataSource import BasicDataSource
from Products.ZenModel.ZenPackPersistence import ZenPackPersistence


class SplunkDataSource(ZenPackPersistence, BasicDataSource):

    ZENPACKID = 'ZenPacks.community.zenSplunkSearch'

    SPLUNK = 'Splunk'
    sourcetypes = (SPLUNK,)
    sourcetype = SPLUNK
    
    timeout = 60
    eventClass = '/App/Splunk'
    component = "${here/splunkSearch}"
    server = "${dev/zSplunkServer}"
    
    splunkServer = "${dev/zSplunkServer}"
    splunkPort = "${dev/zSplunkPort}"
    splunkUsername = "${dev/zSplunkUsername}"
    splunkPassword = "${dev/zSplunkPassword}"
    splunkSearch = "${here/splunkSearch}"

    _properties = BasicDataSource._properties + (
        {'id': 'command', 'type': 'string'},
        )

    def getDescription(self):
        return self.component

    def useZenCommand(self):
        return True

    def getCommand(self, context):
        parts = ['check_splunk.py']
        if self.splunkServer:
            parts.append("-s %s" % self.splunkServer)
        if self.splunkPort:
            parts.append("-p %s" % self.splunkPort)
        if self.splunkUsername:
            parts.append("-u '%s'" % self.splunkUsername)
        if self.splunkPassword:
            parts.append("-w '%s'" % self.splunkPassword)
        if self.splunkSearch:
            parts.append("'%s'" % self.splunkSearch)
        return BasicDataSource.getCommand(self, context, ' '.join(parts))


    def checkCommandPrefix(self, context, cmd):
        return self.getZenPack(context).path('libexec', cmd)


