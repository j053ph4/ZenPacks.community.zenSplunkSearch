(function() {
<<<<<<< HEAD
        
            function getPageContext() {
                return Zenoss.env.device_uid || Zenoss.env.PARENT_CONTEXT;
            }
        
            Ext.ComponentMgr.onAvailable('component-add-menu', function(config) {
                var menuButton = Ext.getCmp('component-add-menu');
                menuButton.menuItems.push({
                    xtype: 'menuitem',
                    text: _t('Add Splunk Search') + '...',
                    hidden: Zenoss.Security.doesNotHavePermission('Manage Device'),
                    handler: function() {
                        var win = new Zenoss.dialog.CloseDialog({
                            width: 300,
                            title: _t('Add Splunk Search'),
                            items: [{
                                xtype: 'form',
                                buttonAlign: 'left',
                                monitorValid: true,
                                labelAlign: 'top',
                                footerStyle: 'padding-left: 0',
                                border: false,
                                items: [
                {
                xtype: 'textfield',
                name: 'alias',
                fieldLabel: _t('Alias'),
                id: "aliasField",
                width: 260,
                allowBlank: false,
                },
                
                {
                xtype: 'textfield',
                name: 'query',
                fieldLabel: _t('Query'),
                id: "queryField",
                width: 260,
                allowBlank: false,
                },
                ],
                                buttons: [{
                                    xtype: 'DialogButton',
                                    id: 'zenSplunkSearch-submit',
                                    text: _t('Add'),
                                    formBind: true,
                                    handler: function(b) {
                                        var form = b.ownerCt.ownerCt.getForm();
                                        var opts = form.getFieldValues();
                                        Zenoss.remote.zenSplunkSearchRouter.addSplunkSearchRouter(opts,
                                        function(response) {
                                            if (response.success) {
                                                new Zenoss.dialog.SimpleMessageDialog({
                                                    title: _t('Splunk Search Added'),
                                                    message: response.msg,
                                                    buttons: [{
                                                        xtype: 'DialogButton',
                                                        text: _t('OK')
                                                    }]
                                                }).show();
                                            }
                                            else {
                                                new Zenoss.dialog.SimpleMessageDialog({
                                                    message: response.msg,
                                                    buttons: [{
                                                        xtype: 'DialogButton',
                                                        text: _t('OK')
                                                    }]
                                                }).show();
                                            }
                                        });
                                    }
                                }, Zenoss.dialog.CANCEL]
                            }]
                        });
                        win.show();
                    }
                });
            });
        }()
);

=======

/**
* On the device details page the uid is
* Zenoss.env.device_uid and on most other pages it is set with
* the environmental variable PARENT_CONTEXT;
**/
    function getPageContext() {
        return Zenoss.env.device_uid || Zenoss.env.PARENT_CONTEXT;
    }

    Ext.ComponentMgr.onAvailable('component-add-menu', function(config) {
        var menuButton = Ext.getCmp('component-add-menu');
        menuButton.menuItems.push({
			xtype: 'menuitem',
            text: _t('Add Splunk Search') + '...',
            hidden: Zenoss.Security.doesNotHavePermission('Manage Device'),
            handler: function() {
                var win = new Zenoss.dialog.CloseDialog({
                    width: 300,
                    title: _t('Add Splunk Search'),
                    items: [{
                        xtype: 'form',
                        buttonAlign: 'left',
                        monitorValid: true,
                        labelAlign: 'top',
                        footerStyle: 'padding-left: 0',
                        border: false,
                        items: [{
                        	xtype: 'textfield',
                            name: 'splunkSearch',
                            fieldLabel: _t('Search'),
                            id: "splunkSearchField",
                            width: 260,
                            allowBlank: false
                        }],
                        buttons: [{
                            xtype: 'DialogButton',
                            id: 'zenSplunkSearch-submit',
                            text: _t('Add'),
                            formBind: true,
                            handler: function(b) {
                                var form = b.ownerCt.ownerCt.getForm();
                                var opts = form.getFieldValues();
                                Zenoss.remote.zenSplunkSearchRouter.addSplunkSearchRouter(opts,
                                function(response) {
                                    if (response.success) {
                                        new Zenoss.dialog.SimpleMessageDialog({
                                            title: _t('Search Added'),
                                            message: response.msg,
                                            buttons: [{
                                                xtype: 'DialogButton',
                                                text: _t('OK')
                                            }]
                                        }).show();
                                    }
                                    else {
                                        new Zenoss.dialog.SimpleMessageDialog({
                                            message: response.msg,
                                            buttons: [{
                                                xtype: 'DialogButton',
                                                text: _t('OK')
                                            }]
                                        }).show();
                                    }
                                });
                            }
                        }, Zenoss.dialog.CANCEL]
                    }]
                });
                win.show();
            }
        });
    });
}());
>>>>>>> 4d329403a84318cea7c3058767c0ddf937d76fdb
