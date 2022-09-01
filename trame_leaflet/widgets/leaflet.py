from trame_client.widgets.core import AbstractElement
from .. import module


class HtmlElement(AbstractElement):
    def __init__(self, _elem_name, children=None, **kwargs):
        super().__init__(_elem_name, children, **kwargs)
        if self.server:
            self.server.enable_module(module)


class LCircle(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__("l-circle", **kwargs)
        self._attr_names += [
            "pane",
            "attribution",
            "name",
            "layerType",
            "visible",
            "interactive",
            "bubblingMouseEvents",
            "lStyle",
            "stroke",
            "color",
            "weight",
            "opacity",
            "lineCap",
            "lineJoin",
            "dashArray",
            "dashOffset",
            "fill",
            "fillColor",
            "fillOpacity",
            "fillRule",
            "className",
            "radius",
            "options",
            "latLng",
        ]
        self._event_names += [("update_visible", "update:visible"), "ready"]


class LCircleMarker(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__("l-circle-marker", **kwargs)
        self._attr_names += [
            "pane",
            "attribution",
            "name",
            "layerType",
            "visible",
            "interactive",
            "bubblingMouseEvents",
            "lStyle",
            "stroke",
            "color",
            "weight",
            "opacity",
            "lineCap",
            "lineJoin",
            "dashArray",
            "dashOffset",
            "fill",
            "fillColor",
            "fillOpacity",
            "fillRule",
            "className",
            "radius",
            "options",
            "latLng",
        ]
        self._event_names += [("update_visible", "update:visible"), "ready"]


class LControl(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__("l-control", **kwargs)
        self._attr_names += [
            "position",
            "options",
            "disableClickPropagation",
            "disableScrollPropagation",
        ]
        self._event_names += ["ready"]


class LControlAttribution(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__("l-control-attribution", **kwargs)
        self._attr_names += ["position", "options", "prefix"]
        self._event_names += ["ready"]


class LControlLayers(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__("l-control-layers", **kwargs)
        self._attr_names += [
            "position",
            "options",
            "collapsed",
            "autoZIndex",
            "hideSingleBase",
            "sortLayers",
            "sortFunction",
        ]
        self._event_names += ["ready"]


class LControlScale(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__("l-control-scale", **kwargs)
        self._attr_names += [
            "position",
            "options",
            "maxWidth",
            "metric",
            "imperial",
            "updateWhenIdle",
        ]
        self._event_names += ["ready"]


class LControlZoom(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__("l-control-zoom", **kwargs)
        self._attr_names += [
            "position",
            "options",
            "zoomInText",
            "zoomInTitle",
            "zoomOutText",
            "zoomOutTitle",
        ]
        self._event_names += ["ready"]


class LFeatureGroup(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__("l-feature-group", **kwargs)
        self._attr_names += [
            "pane",
            "attribution",
            "name",
            "layerType",
            "visible",
            "options",
        ]
        self._event_names += [("update_visible", "update:visible"), "ready"]


class LGeoJson(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__("l-geo-json", **kwargs)
        self._attr_names += [
            "pane",
            "attribution",
            "name",
            "layerType",
            "visible",
            "options",
            "geojson",
            "optionsStyle",
        ]
        self._event_names += [("update_visible", "update:visible"), "ready"]


class LGridLayer(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__("l-grid-layer", **kwargs)
        self._attr_names += [
            "pane",
            "attribution",
            "name",
            "layerType",
            "visible",
            "opacity",
            "zIndex",
            "tileSize",
            "noWrap",
            "options",
            "tileComponent",
        ]
        self._event_names += [("update_visible", "update:visible"), "ready"]


class LIcon(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__("l-icon", **kwargs)
        self._attr_names += [
            "iconUrl",
            "iconRetinaUrl",
            "iconSize",
            "iconAnchor",
            "popupAnchor",
            "tooltipAnchor",
            "shadowUrl",
            "shadowRetinaUrl",
            "shadowSize",
            "shadowAnchor",
            "bgPos",
            "className",
            "options",
        ]


class LImageOverlay(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__("l-image-overlay", **kwargs)
        self._attr_names += [
            "pane",
            "attribution",
            "name",
            "layerType",
            "visible",
            "interactive",
            "bubblingMouseEvents",
            "url",
            "bounds",
            "opacity",
            "alt",
            "crossOrigin",
            "errorOverlayUrl",
            "zIndex",
            "className",
            "options",
        ]
        self._event_names += [("update_visible", "update:visible"), "ready"]


class LLayerGroup(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__("l-layer-group", **kwargs)
        self._attr_names += [
            "pane",
            "attribution",
            "name",
            "layerType",
            "visible",
            "options",
        ]
        self._event_names += [("update_visible", "update:visible"), "ready"]


class LMap(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__("l-map", **kwargs)
        self._attr_names += [
            "center",
            "bounds",
            "maxBounds",
            "zoom",
            "minZoom",
            "maxZoom",
            "paddingBottomRight",
            "paddingTopLeft",
            "padding",
            "worldCopyJump",
            "crs",
            "maxBoundsViscosity",
            "inertia",
            "inertiaDeceleration",
            "inertiaMaxSpeed",
            "easeLinearity",
            "zoomAnimation",
            "zoomAnimationThreshold",
            "fadeAnimation",
            "markerZoomAnimation",
            "noBlockingAnimations",
        ]
        self._event_names += [
            "ready",
            ("update_zoom", "update:zoom"),
            ("update_center", "update:center"),
            ("update_bounds", "update:bounds"),
        ]


class LMarker(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__("l-marker", **kwargs)
        self._attr_names += [
            "pane",
            "attribution",
            "name",
            "layerType",
            "visible",
            "options",
            "draggable",
            "latLng",
            ("lat_lng", "latLng"),
            "icon",
            "opacity",
            "zIndexOffset",
        ]
        self._event_names += [
            ("update_visible", "update:visible"),
            "ready",
            ("update_latLng", "update:latLng"),
            ("update_lat_lng", "update:lat-lng"),
        ]


class LPolygon(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__("l-polygon", **kwargs)
        self._attr_names += [
            "pane",
            "attribution",
            "name",
            "layerType",
            "visible",
            "interactive",
            "bubblingMouseEvents",
            "lStyle",
            "stroke",
            "color",
            "weight",
            "opacity",
            "lineCap",
            "lineJoin",
            "dashArray",
            "dashOffset",
            "fill",
            "fillColor",
            "fillOpacity",
            "fillRule",
            "className",
            "smoothFactor",
            "noClip",
            "options",
            "latLngs",
        ]
        self._event_names += [("update_visible", "update:visible"), "ready"]


class LPolyline(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__("l-polyline", **kwargs)
        self._attr_names += [
            "pane",
            "attribution",
            "name",
            "layerType",
            "visible",
            "interactive",
            "bubblingMouseEvents",
            "lStyle",
            "stroke",
            "color",
            "weight",
            "opacity",
            "lineCap",
            "lineJoin",
            "dashArray",
            "dashOffset",
            "fill",
            "fillColor",
            "fillOpacity",
            "fillRule",
            "className",
            "smoothFactor",
            "noClip",
            "options",
            "latLngs",
        ]
        self._event_names += [("update_visible", "update:visible"), "ready"]


class LPopup(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__("l-popup", **kwargs)
        self._attr_names += ["content", "options", "latLng"]
        self._event_names += ["ready"]


class LRectangle(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__("l-rectangle", **kwargs)
        self._attr_names += [
            "pane",
            "attribution",
            "name",
            "layerType",
            "visible",
            "interactive",
            "bubblingMouseEvents",
            "lStyle",
            "stroke",
            "color",
            "weight",
            "opacity",
            "lineCap",
            "lineJoin",
            "dashArray",
            "dashOffset",
            "fill",
            "fillColor",
            "fillOpacity",
            "fillRule",
            "className",
            "smoothFactor",
            "noClip",
            "options",
            "bounds",
        ]
        self._event_names += [("update_visible", "update:visible"), "ready"]


class LTileLayer(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__("l-tile-layer", **kwargs)
        self._attr_names += [
            "pane",
            "attribution",
            "name",
            "layerType",
            "visible",
            "opacity",
            "zIndex",
            "tileSize",
            "noWrap",
            "tms",
            "subdomains",
            "detectRetina",
            "options",
            "url",
            "tileLayerClass",
        ]
        self._event_names += [("update_visible", "update:visible"), "ready"]


class LTooltip(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__("l-tooltip", **kwargs)
        self._attr_names += ["content", "options"]
        self._event_names += ["ready"]


class LWMSTileLayer(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__("l-wms-tile-layer", **kwargs)
        self._attr_names += [
            "pane",
            "attribution",
            "name",
            "layerType",
            "visible",
            "opacity",
            "zIndex",
            "tileSize",
            "noWrap",
            "tms",
            "subdomains",
            "detectRetina",
            "layers",
            "styles",
            "format",
            "transparent",
            "version",
            "crs",
            "uppercase",
            "options",
            "baseUrl",
        ]
        self._event_names += [("update_visible", "update:visible"), "ready"]


class VGeosearch(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__("v-geosearch", **kwargs)
        self._attr_names += ["options"]
