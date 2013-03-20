<<<<<<< HEAD
(function(){
            var ZC = Ext.ns('Zenoss.component');
        
            function render_link(ob) {
                if (ob && ob.uid) {
                    return Zenoss.render.link(ob.uid);
                } else {
                    return ob;
                }
            }
        
            ZC.SplunkSearchPanel = Ext.extend(ZC.ComponentGridPanel, {
                constructor: function(config) {
                    config = Ext.applyIf(config||{}, {
                        componentType: 'SplunkSearch',
                        fields: [
            {name: 'uid'},
            {name: 'severity'},
            {name: 'status'},
            {name: 'name'},{name: 'alias'},
                {name: 'query'},
                
            {name: 'usesMonitorAttribute'},
            {name: 'monitor'},
            {name: 'monitored'},
            {name: 'locking'},
            ]
        ,
                        columns:[{
            id: 'severity',
            dataIndex: 'severity',
            header: _t('Events'),
            renderer: Zenoss.render.severity,
            sortable: true,
            width: 50
        },{
            id: 'name',
            dataIndex: 'name',
            header: _t('Name'),
            sortable: true,
            width: 70
        },{
                    id: 'alias',
                    dataIndex: 'alias',
                    header: _t('Alias'),
                    sortable: true,
                    width: 266
                },{
                    id: 'query',
                    dataIndex: 'query',
                    header: _t('Query'),
                    sortable: true,
                    width: 266
                },{
            id: 'monitored',
            dataIndex: 'monitored',
            header: _t('Monitored'),
            sortable: true,
            width: 65
        },{
            id: 'locking',
            dataIndex: 'locking',
            header: _t('Locking'),
            renderer: Zenoss.render.locking_icons,
            sortable: true,
            width: 65
        }]
                    });
                    ZC.SplunkSearchPanel.superclass.constructor.call(this, config);
                }
            });
            
            Ext.reg('SplunkSearchPanel', ZC.SplunkSearchPanel);
            ZC.registerName('SplunkSearch', _t('Splunk Search'), _t('Splunk Searches'));
            
            })(); 
=======
/*
 * Based on the configuration in ../../configure.zcml this JavaScript will only
 * be loaded when the user is looking at an ExampleDevice in the web interface.
 */

(function(){

var ZC = Ext.ns('Zenoss.component');

function render_link(ob) {
    if (ob && ob.uid) {
        return Zenoss.render.link(ob.uid);
    } else {
        return ob;
    }
}

ZC.SplunkSearchPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'SplunkSearch',
            fields: [
                {name: 'uid'},
                {name: 'severity'},
                {name: 'status'},
                {name: 'name'},
                {name: 'splunkSearch'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'locking'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                sortable: true
            },{
                id: 'splunkSearch',
                dataIndex: 'splunkSearch',
                header: _t('Search'),
                sortable: true,
                width: 150
            },{
                id: 'status',
                dataIndex: 'status',
                header: _t('Status'),
                width: 70
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                sortable: true,
                width: 65
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons,
                sortable: true,
                width: 65
            }
			]
        });
        ZC.SplunkSearchPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('SplunkSearchPanel', ZC.SplunkSearchPanel);
ZC.registerName('SplunkSearch', _t('Splunk Search'), _t('Splunk Searches'));

})();
>>>>>>> 4d329403a84318cea7c3058767c0ddf937d76fdb

