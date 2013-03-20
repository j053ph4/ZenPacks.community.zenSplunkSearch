from Products.ZenUtils.Ext import DirectRouter, DirectResponse
from Products import Zuul

<<<<<<< HEAD
'''
args: routername,adaptername,routerMethodName, createMethodName
'''

class zenSplunkSearchRouter(DirectRouter):
    def _getFacade(self):
    	return Zuul.getFacade('zenSplunkSearchAdapter', self.context)
    
    def addSplunkSearchRouter(self, **kwargs):
    	from Products.ZenUtils.Ext import DirectResponse
    	facade = self._getFacade()
    	ob = self.context
    	success, message = facade.addSplunkSearch(ob, **kwargs)
    	if success:
    		return DirectResponse.succeed(message)
    	else:
    		return DirectResponse.fail(message)

=======

class zenSplunkSearchRouter(DirectRouter):
    def _getFacade(self):
        return Zuul.getFacade('zenSplunkSearchAdapter', self.context)

    def addSplunkSearchRouter(self, splunkSearch):
        
        facade = self._getFacade()
        ob = self.context
        success, message = facade.addSplunkSearch(ob, splunkSearch)
        if success:
            return DirectResponse.succeed(message)
        else:
            return DirectResponse.fail(message) 
>>>>>>> 4d329403a84318cea7c3058767c0ddf937d76fdb
