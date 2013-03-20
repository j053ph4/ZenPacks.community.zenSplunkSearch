from ZenPacks.community.ConstructionKit.Construct import *
from Products.ZenModel.migrate.Migrate import Version
import os

class Definition():
    """
    """
    version = Version(2, 0, 0)
    zenpackroot = "ZenPacks.community" # ZenPack Root
    zenpackbase = "zenSplunkSearch" # ZenaPack Name
    cwd = os.path.dirname(os.path.realpath(__file__)) # ZenPack files directory
    #dictionary of components
    packZProperties = [
        ('zSplunkServer', 'default', 'string'),
        ('zSplunkPort', '8089', 'string'),
        ('zSplunkUsername', 'default', 'string'),
        ('zSplunkPassword', 'default', 'password'),
        ]
    
    component = 'SplunkSearch'
    componentData = {
                  'singular': 'Splunk Search',
                  'plural': 'Splunk Searches',
                  'displayed': 'alias', # component field in Event Console
                  'primaryKey': 'alias',
                  'properties': { 
                        # Basic settings
                        'alias' : addProperty('Alias','Basic', optional='false'),
                        'query' : addProperty('Query','Basic', switch='-q',optional='false'),
                        'server': addProperty('Server','Basic','zSplunkServer', switch='-s',override=True, isReference=True),
                        'port': addProperty('Port','Basic','zSplunkPort', switch='-p',override=True, isReference=True),
                        'user': addProperty('User','Basic','zSplunkUsername', switch='-u',override=True, isReference=True),
                        'password': addProperty('Password','Basic','zSplunkPassword', switch='-w',override=True, isReference=True),
                        },
                  }
    cmdFile = 'check_splunk.py'
    provided = True # cmdFile provided by ZenPack (in /libexec)
    cycleTime = 300
    timeout = 60
    datapoints = ['count']                  
                            
