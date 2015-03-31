from ZenPacks.community.ConstructionKit.BasicDefinition import *
from ZenPacks.community.ConstructionKit.Construct import *


SplunkDefinition = type('SplunkDefinition', (BasicDefinition,), {
        'version' : Version(2, 1, 1),
        'zenpackbase': "zenSplunkSearch",
        'component' : 'SplunkSearch',
        'componentData' : {
                          'singular': 'Splunk Search',
                          'plural': 'Splunk Searches',
                          'displayed': 'alias', # component field in Event Console
                          'primaryKey': 'alias',
                          'properties': {
                                # Basic settings
                                'alias' : addProperty('Alias', optional='false'),
                                'query' : addProperty('Query',switch='-q',optional='false'),
                                'server': addProperty('Server','zSplunkServer', switch='-s',override=True, isReference=True),
                                'port': addProperty('Port','zSplunkPort', switch='-p',override=True, isReference=True),
                                'user': addProperty('User','zSplunkUsername', switch='-u',override=True, isReference=True),
                                'password': addProperty('Password','zSplunkPassword', switch='-w',override=True, isReference=True),
                                'productKey' : getProductClass('Splunk'),
                                },
                          },
        'addManual' : True,
        'cmdFile' : 'check_splunk.py',
        'createDS' : True,
        'datapoints' : ['count'],
        'packZProperties' : [
                            ('zSplunkServer', 'default', 'string'),
                            ('zSplunkPort', '8089', 'string'),
                            ('zSplunkUsername', 'default', 'string'),
                            ('zSplunkPassword', 'default', 'password'),
                            ],
        'saveOld': True,
        'loadOld': True,         
        },
)

