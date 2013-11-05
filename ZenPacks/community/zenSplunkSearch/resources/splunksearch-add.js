
(function() {
        
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
                                items:                         [
                            {
                                fieldLabel: 'Alias', 
                                allowBlank: 'false', 
                                name: 'alias', 
                                width: 260, 
                                id: 'aliasField', 
                                xtype: 'textfield'
                            }, 
                            {
                                fieldLabel: 'Query', 
                                allowBlank: 'false', 
                                name: 'query', 
                                width: 260, 
                                id: 'queryField', 
                                xtype: 'textfield'
                            }
                        ]

                                ,
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
                                                        text: _t('OK'),
                                                        handler: function() { 
                                                            window.top.location.reload();
                                                            }
                                                        }]
                                                }).show();
                                            }
                                            else {
                                                new Zenoss.dialog.SimpleMessageDialog({
                                                    message: response.msg,
                                                    buttons: [{
                                                        xtype: 'DialogButton',
                                                        text: _t('OK'),
                                                        handler: function() { 
                                                            window.top.location.reload();
                                                            }
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

