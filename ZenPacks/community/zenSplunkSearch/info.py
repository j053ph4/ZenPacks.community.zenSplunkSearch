from ZenPacks.community.ConstructionKit.ClassHelper import *

def SplunkSearchgetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class SplunkSearchInfo(ClassHelper.SplunkSearchInfo):
    ''''''

from ZenPacks.community.zenSplunkSearch.datasources.SplunkSearchDataSource import *
def SplunkSearchRedirectVocabulary(context):
    return SimpleVocabulary.fromValues(SplunkSearchDataSource.onRedirectOptions)

class SplunkSearchDataSourceInfo(ClassHelper.SplunkSearchDataSourceInfo):
    ''''''


