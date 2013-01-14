from Products.ZenUtils.Ext import DirectRouter, DirectResponse
from Products import Zuul


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
