.. _map-view:

********
Map View
********

.. autoclass:: tethys_sdk.gizmos.MapView

MVLayer
-------

.. autoclass:: tethys_sdk.gizmos.MVLayer

MVLegendClass
-------------

.. autoclass:: tethys_sdk.gizmos.MVLegendClass

MVDraw
------

.. autoclass:: tethys_sdk.gizmos.MVDraw

MVView
------

.. autoclass:: tethys_sdk.gizmos.MVView

JavaScript API
--------------

For advanced features, the JavaScript API can be used to interact with the OpenLayers map object that is generated by the Map View JavaScript library.

TETHYS_MAP_VIEW.getMap()
++++++++++++++++++++++++

This method returns the OpenLayers map object. You can use the `OpenLayers Map API version 3.5.0 <http://openlayers.org/en/v3.5.0/apidoc/ol.Map.html>`_ to perform operations on this object such as adding layers and custom controls.

::

    var ol_map = TETHYS_MAP_VIEW.map;
    ol_map.addLayer(...);
    ol_map.setView(...);

.. caution::

    The Map View Gizmo is powered by OpenLayers version 3.5.0. When referring to the OpenLayers documentation, ensure that you are browsing the correct version of documentation (see the URL of the documentation page).