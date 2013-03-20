========================================
ZenPacks.community.zenSplunkSearch
========================================

Developed by
============
Joseph Anderson

Description:
===========
This ZenPack provides a "Splunk Search" component and allows for the execution
of 
Splunk Searches within Zenoss.  

Each "Splunk Search" component has a "query" property that contains the query
string.

Connection parameters are defined in zProperties, but can be overriden on a
per component basis

The component data is passed to a "check_splunk.py" script that was
copied/modified from an earlier 
community ZenPack that no longer seems to be available.


Components
==========
  Component and Datasource class properties are specified in the provided
"Definition.py" file.
	A basic RRD Template is also provided that executes the
check_splunk.py script (provided) and graphs the output (result count).

Installation
============
Describe the install process if anything is needed before or after standard
ZenPack installation.

Requirements
============
    Zenoss Versions Supported: 3.x, 4.x
    External Dependencies: None
    ZenPack Dependencies: ZenPacks.community.ConstructionKit
    Installation Notes: zopectl restart; zenhub restart after installation
    Configuration: None

History
=======
Change History:

1.0 initial release

2.0
    added Zenoss 4.X support
    new dependency on "ConstructionKit" ZenPack to simplify current/future
development
    <https://github.com/j053ph4/ZenPacks.community.ConstructionKit>

Tested
======
This ZenPack was tested with versions 3.2.1, 4.2.3

Source
======
https://github.com/j053ph4/ZenPacks.community.zenSplunkSearch

Known issues
============
None  
