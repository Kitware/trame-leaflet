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
            ("layer_type", "layerType"),
            "visible",
            "interactive",
            ("bubbling_mouse_events", "bubblingMouseEvents"),
            ("l_style", "lStyle"),
            "stroke",
            "color",
            "weight",
            "opacity",
            ("line_cap", "lineCap"),
            ("line_join", "lineJoin"),
            ("dash_array", "dashArray"),
            ("dash_offset", "dashOffset"),
            "fill",
            ("fill_color", "fillColor"),
            ("fill_opacity", "fillOpacity"),
            ("fill_rule", "fillRule"),
            ("class_name", "className"),
            "radius",
            "options",
            ("lat_lng", "latLng"),
        ]
        self._event_names += [("update_visible", "update:visible"), "ready"]


class LCircleMarker(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__("l-circle-marker", **kwargs)
        self._attr_names += [
            "pane",
            "attribution",
            "name",
            ("layer_type", "layerType"),
            "visible",
            "interactive",
            ("bubbling_mouse_events", "bubblingMouseEvents"),
            ("l_style", "lStyle"),
            "stroke",
            "color",
            "weight",
            "opacity",
            ("line_cap", "lineCap"),
            ("line_join", "lineJoin"),
            ("dash_array", "dashArray"),
            ("dash_offset", "dashOffset"),
            "fill",
            ("fill_color", "fillColor"),
            ("fill_opacity", "fillOpacity"),
            ("fill_rule", "fillRule"),
            ("class_name", "className"),
            "radius",
            "options",
            ("lat_lng", "latLng"),
        ]
        self._event_names += [("update_visible", "update:visible"), "ready"]


class LControl(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__("l-control", **kwargs)
        self._attr_names += [
            "position",
            "options",
            ("disable_click_propagation", "disableClickPropagation"),
            ("disable_scroll_propagation", "disableScrollPropagation"),
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
            ("auto_z_index", "autoZIndex"),
            ("hide_single_base", "hideSingleBase"),
            ("sort_layers", "sortLayers"),
            ("sort_function", "sortFunction"),
        ]
        self._event_names += ["ready"]


class LControlScale(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__("l-control-scale", **kwargs)
        self._attr_names += [
            "position",
            "options",
            ("max_width", "maxWidth"),
            "metric",
            "imperial",
            ("update_when_idle", "updateWhenIdle"),
        ]
        self._event_names += ["ready"]


class LControlZoom(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__("l-control-zoom", **kwargs)
        self._attr_names += [
            "position",
            "options",
            ("zoom_in_text", "zoomInText"),
            ("zoom_in_title", "zoomInTitle"),
            ("zoom_out_text", "zoomOutText"),
            ("zoom_out_title", "zoomOutTitle"),
        ]
        self._event_names += ["ready"]


class LFeatureGroup(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__("l-feature-group", **kwargs)
        self._attr_names += [
            "pane",
            "attribution",
            "name",
            ("layer_type", "layerType"),
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
            ("layer_type", "layerType"),
            "visible",
            "options",
            "geojson",
            ("options_style", "optionsStyle"),
        ]
        self._event_names += [("update_visible", "update:visible"), "ready"]


class LGridLayer(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__("l-grid-layer", **kwargs)
        self._attr_names += [
            "pane",
            "attribution",
            "name",
            ("layer_type", "layerType"),
            "visible",
            "opacity",
            ("z_index", "zIndex"),
            ("tile_size", "tileSize"),
            ("no_wrap", "noWrap"),
            "options",
            ("tile_component", "tileComponent"),
        ]
        self._event_names += [("update_visible", "update:visible"), "ready"]


class LIcon(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__("l-icon", **kwargs)
        self._attr_names += [
            ("icon_url", "iconUrl"),
            ("icon_retina_url", "iconRetinaUrl"),
            ("icon_size", "iconSize"),
            ("icon_anchor", "iconAnchor"),
            ("popup_anchor", "popupAnchor"),
            ("tooltip_anchor", "tooltipAnchor"),
            ("shadow_url", "shadowUrl"),
            ("shadow_retina_url", "shadowRetinaUrl"),
            ("shadow_size", "shadowSize"),
            ("shadow_anchor", "shadowAnchor"),
            ("bg_pos", "bgPos"),
            ("class_name", "className"),
            "options",
        ]


class LImageOverlay(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__("l-image-overlay", **kwargs)
        self._attr_names += [
            "pane",
            "attribution",
            "name",
            ("layer_type", "layerType"),
            "visible",
            "interactive",
            ("bubbling_mouse_events", "bubblingMouseEvents"),
            "url",
            "bounds",
            "opacity",
            "alt",
            ("cross_origin", "crossOrigin"),
            ("error_overlay_url", "errorOverlayUrl"),
            ("z_index", "zIndex"),
            ("class_name", "className"),
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
            ("layer_type", "layerType"),
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
            ("max_bounds", "maxBounds"),
            "zoom",
            ("min_zoom", "minZoom"),
            ("max_zoom", "maxZoom"),
            ("padding_bottom_right", "paddingBottomRight"),
            ("padding_top_left", "paddingTopLeft"),
            "padding",
            ("world_copy_jump", "worldCopyJump"),
            "crs",
            ("max_bounds_viscosity", "maxBoundsViscosity"),
            "inertia",
            ("inertia_deceleration", "inertiaDeceleration"),
            ("inertia_max_speed", "inertiaMaxSpeed"),
            ("ease_linearity", "easeLinearity"),
            ("zoom_animation", "zoomAnimation"),
            ("zoom_animation_threshold", "zoomAnimationThreshold"),
            ("fade_animation", "fadeAnimation"),
            ("marker_zoom_animation", "markerZoomAnimation"),
            ("no_blocking_animations", "noBlockingAnimations"),
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
            ("layer_type", "layerType"),
            "visible",
            "options",
            "draggable",
            ("lat_lng", "latLng"),
            "icon",
            "opacity",
            ("z_index_offset", "zIndexOffset"),
        ]
        self._event_names += [
            ("update_visible", "update:visible"),
            "ready",
            ("update_lat_lng", "update:latLng"),

        ]


class LPolygon(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__("l-polygon", **kwargs)
        self._attr_names += [
            "pane",
            "attribution",
            "name",
            ("layer_type", "layerType"),
            "visible",
            "interactive",
            ("bubbling_mouse_events", "bubblingMouseEvents"),
            ("l_style", "lStyle"),
            "stroke",
            "color",
            "weight",
            "opacity",
            ("line_cap", "lineCap"),
            ("line_join", "lineJoin"),
            ("dash_array", "dashArray"),
            ("dash_offset", "dashOffset"),
            "fill",
            ("fill_color", "fillColor"),
            ("fill_opacity", "fillOpacity"),
            ("fill_rule", "fillRule"),
            ("class_name", "className"),
            ("smooth_factor", "smoothFactor"),
            ("no_clip", "noClip"),
            "options",
            ("lat_lngs", "latLngs"),
        ]
        self._event_names += [("update_visible", "update:visible"), "ready"]


class LPolyline(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__("l-polyline", **kwargs)
        self._attr_names += [
            "pane",
            "attribution",
            "name",
            ("layer_type", "layerType"),
            "visible",
            "interactive",
            ("bubbling_mouse_events", "bubblingMouseEvents"),
            ("l_style", "lStyle"),
            "stroke",
            "color",
            "weight",
            "opacity",
            ("line_cap", "lineCap"),
            ("line_join", "lineJoin"),
            ("dash_array", "dashArray"),
            ("dash_offset", "dashOffset"),
            "fill",
            ("fill_color", "fillColor"),
            ("fill_opacity", "fillOpacity"),
            ("fill_rule", "fillRule"),
            ("class_name", "className"),
            ("smooth_factor", "smoothFactor"),
            ("no_clip", "noClip"),
            "options",
            ("lat_lngs", "latLngs"),
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
            ("layer_type", "layerType"),
            "visible",
            "interactive",
            ("bubbling_mouse_events", "bubblingMouseEvents"),
            ("l_style", "lStyle"),
            "stroke",
            "color",
            "weight",
            "opacity",
            ("line_cap", "lineCap"),
            ("line_join", "lineJoin"),
            ("dash_array", "dashArray"),
            ("dash_offset", "dashOffset"),
            "fill",
            ("fill_color", "fillColor"),
            ("fill_opacity", "fillOpacity"),
            ("fill_rule", "fillRule"),
            ("class_name", "className"),
            ("smooth_factor", "smoothFactor"),
            ("no_clip", "noClip"),
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
            ("layer_type", "layerType"),
            "visible",
            "opacity",
            ("z_index", "zIndex"),
            ("tile_size", "tileSize"),
            ("no_wrap", "noWrap"),
            "tms",
            "subdomains",
            ("detect_retina", "detectRetina"),
            "options",
            "url",
            ("tile_layer_class", "tileLayerClass"),
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
            ("layer_type", "layerType"),
            "visible",
            "opacity",
            ("z_index", "zIndex"),
            ("tile_size", "tileSize"),
            ("no_wrap", "noWrap"),
            "tms",
            "subdomains",
            ("detect_retina", "detectRetina"),
            "layers",
            "styles",
            "format",
            "transparent",
            "version",
            "crs",
            "uppercase",
            "options",
            ("base_url", "baseUrl"),
        ]
        self._event_names += [("update_visible", "update:visible"), "ready"]


class VGeosearch(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__("v-geosearch", **kwargs)
        self._attr_names += ["options"]
