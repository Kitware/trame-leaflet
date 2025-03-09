.. |pypi_download| image:: https://img.shields.io/pypi/dm/trame-leaflet

trame-leaflet |pypi_download|
===========================================================================

trame-leaflet extends trame **widgets** with components from vue-leaflet.

This package is under the same MIT License as `Vue-Leaflet <https://github.com/vue-leaflet/Vue2Leaflet/blob/master/LICENSE>`_ which that library embeds.

Leaflet integration in trame allows you to create map views with useful widgets.


How to use it?
```````````````````````````````````````````````````````````

Using the Python library

.. code-block:: python

    # for vue2
    from trame.widgets import leaflet2 as leaflet

    # for vue3
    from trame.widgets import leaflet3 as leaflet

    with leaflet.LMap(zoom=("zoom", 15), center=("center", [51.505, -0.159])):
        leaflet.LTileLayer(url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png")
        leaflet.LMarker(lat_lng=("markerLatLng", [51.504, -0.159]))


JavaScript dependency
-----------------------------------------------------------

This Python package bundle the ``leaflet@1.8.0`` and ``vue2-leaflet@2.7.1`` JavaScript libraries. 
For vue3 we also bundle ``@vue-leaflet/vue-leaflet@0.10.1`` JavaScript librarie.
If you would like us to upgrade it, `please reach out <https://www.kitware.com/trame/>`_.