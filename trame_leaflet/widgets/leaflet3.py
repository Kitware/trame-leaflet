from trame_client.widgets.core import AbstractElement, Template  # noqa
from ..module import leaflet3


class HtmlElement(AbstractElement):
    def __init__(self, _elem_name, children=None, **kwargs):
        super().__init__(_elem_name, children, **kwargs)
        if self.server:
            self.server.enable_module(leaflet3)


class LCircle(HtmlElement):
    """
    Component LCircle with the following properties

    Args:
      attribution:

      bubbling_mouse_events:

      class_name:

      color:

      dash_array:

      dash_offset:

      fill:

      fill_color:

      fill_opacity:

      fill_rule:

      interactive:

      lat_lng:

      layer_type:

      line_cap:

      line_join:

      name:

      opacity:

      options:

      pane:

      radius:

      stroke:

      visible:

      weight:

      attribution (event):

      bubbling_mouse_events (event):

      class_name (event):

      color (event):

      dash_array (event):

      dash_offset (event):

      fill (event):

      fill_color (event):

      fill_opacity (event):

      fill_rule (event):

      interactive (event):

      lat_lng (event):

      layer_type (event):

      line_cap (event):

      line_join (event):

      name (event):

      opacity (event):

      options (event):

      pane (event):

      radius (event):

      stroke (event):

      visible (event):

      weight (event):


    """

    def __init__(self, children=None, **kwargs):
        super().__init__("l-circle", children, **kwargs)
        self._attr_names += [
            "attribution",
            ("bubbling_mouse_events", "bubblingMouseEvents"),
            ("class_name", "className"),
            "color",
            ("dash_array", "dashArray"),
            ("dash_offset", "dashOffset"),
            "fill",
            ("fill_color", "fillColor"),
            ("fill_opacity", "fillOpacity"),
            ("fill_rule", "fillRule"),
            "interactive",
            ("lat_lng", "latLng"),
            ("layer_type", "layerType"),
            ("line_cap", "lineCap"),
            ("line_join", "lineJoin"),
            "name",
            "opacity",
            "options",
            "pane",
            "radius",
            "stroke",
            "visible",
            "weight",
        ]
        self._event_names += [
            "ready",
        ]


class LCircleMarker(HtmlElement):
    """
    Component LCircleMarker with the following properties

    Args:
      attribution:

      bubbling_mouse_events:

      class_name:

      color:

      dash_array:

      dash_offset:

      fill:

      fill_color:

      fill_opacity:

      fill_rule:

      interactive:

      lat_lng:

      layer_type:

      line_cap:

      line_join:

      name:

      opacity:

      options:

      pane:

      radius:

      stroke:

      visible:

      weight:

      attribution (event):

      bubbling_mouse_events (event):

      class_name (event):

      color (event):

      dash_array (event):

      dash_offset (event):

      fill (event):

      fill_color (event):

      fill_opacity (event):

      fill_rule (event):

      interactive (event):

      lat_lng (event):

      layer_type (event):

      line_cap (event):

      line_join (event):

      name (event):

      opacity (event):

      options (event):

      pane (event):

      radius (event):

      stroke (event):

      visible (event):

      weight (event):


    """

    def __init__(self, children=None, **kwargs):
        super().__init__("l-circle-marker", children, **kwargs)
        self._attr_names += [
            "attribution",
            ("bubbling_mouse_events", "bubblingMouseEvents"),
            ("class_name", "className"),
            "color",
            ("dash_array", "dashArray"),
            ("dash_offset", "dashOffset"),
            "fill",
            ("fill_color", "fillColor"),
            ("fill_opacity", "fillOpacity"),
            ("fill_rule", "fillRule"),
            "interactive",
            ("lat_lng", "latLng"),
            ("layer_type", "layerType"),
            ("line_cap", "lineCap"),
            ("line_join", "lineJoin"),
            "name",
            "opacity",
            "options",
            "pane",
            "radius",
            "stroke",
            "visible",
            "weight",
        ]
        self._event_names += [
            "ready",
        ]


class LControl(HtmlElement):
    """
    Component LControl with the following properties

    Args:
      disable_click_propagation:

      disable_scroll_propagation:

      options:

      position:

      disable_click_propagation (event):

      disable_scroll_propagation (event):

      options (event):

      position (event):


    """

    def __init__(self, children=None, **kwargs):
        super().__init__("l-control", children, **kwargs)
        self._attr_names += [
            ("disable_click_propagation", "disableClickPropagation"),
            ("disable_scroll_propagation", "disableScrollPropagation"),
            "options",
            "position",
        ]
        self._event_names += [
            "ready",
        ]


class LControlAttribution(HtmlElement):
    """
    Component LControlAttribution with the following properties

    Args:
      options:

      position:

      prefix:

      options (event):

      position (event):

      prefix (event):


    """

    def __init__(self, children=None, **kwargs):
        super().__init__("l-control-attribution", children, **kwargs)
        self._attr_names += [
            "options",
            "position",
            "prefix",
        ]
        self._event_names += [
            "ready",
        ]


class LControlLayers(HtmlElement):
    """
    Component LControlLayers with the following properties

    Args:
      auto_zindex:

      collapsed:

      hide_single_base:

      options:

      position:

      sort_function:

      sort_layers:

      auto_zindex (event):

      collapsed (event):

      hide_single_base (event):

      options (event):

      position (event):

      sort_function (event):

      sort_layers (event):


    """

    def __init__(self, children=None, **kwargs):
        super().__init__("l-control-layers", children, **kwargs)
        self._attr_names += [
            ("auto_zindex", "autoZIndex"),
            "collapsed",
            ("hide_single_base", "hideSingleBase"),
            "options",
            "position",
            ("sort_function", "sortFunction"),
            ("sort_layers", "sortLayers"),
        ]
        self._event_names += [
            "ready",
        ]


class LControlScale(HtmlElement):
    """
    Component LControlScale with the following properties

    Args:
      imperial:

      max_width:

      metric:

      options:

      position:

      update_when_idle:

      imperial (event):

      max_width (event):

      metric (event):

      options (event):

      position (event):

      update_when_idle (event):


    """

    def __init__(self, children=None, **kwargs):
        super().__init__("l-control-scale", children, **kwargs)
        self._attr_names += [
            "imperial",
            ("max_width", "maxWidth"),
            "metric",
            "options",
            "position",
            ("update_when_idle", "updateWhenIdle"),
        ]
        self._event_names += [
            "ready",
        ]


class LControlZoom(HtmlElement):
    """
    Component LControlZoom with the following properties

    Args:
      options:

      position:

      zoom_in_text:

      zoom_in_title:

      zoom_out_text:

      zoom_out_title:

      options (event):

      position (event):

      zoom_in_text (event):

      zoom_in_title (event):

      zoom_out_text (event):

      zoom_out_title (event):


    """

    def __init__(self, children=None, **kwargs):
        super().__init__("l-control-zoom", children, **kwargs)
        self._attr_names += [
            "options",
            "position",
            ("zoom_in_text", "zoomInText"),
            ("zoom_in_title", "zoomInTitle"),
            ("zoom_out_text", "zoomOutText"),
            ("zoom_out_title", "zoomOutTitle"),
        ]
        self._event_names += [
            "ready",
        ]


class LFeatureGroup(HtmlElement):
    """
    Component LFeatureGroup with the following properties

    Args:
      attribution:

      layer_type:

      name:

      options:

      pane:

      visible:

      attribution (event):

      layer_type (event):

      name (event):

      options (event):

      pane (event):

      visible (event):


    """

    def __init__(self, children=None, **kwargs):
        super().__init__("l-feature-group", children, **kwargs)
        self._attr_names += [
            "attribution",
            ("layer_type", "layerType"),
            "name",
            "options",
            "pane",
            "visible",
        ]
        self._event_names += [
            "ready",
        ]


class LGeoJson(HtmlElement):
    """
    Component LGeoJson with the following properties

    Args:
      attribution:

      geojson:

      layer_type:

      name:

      options:

      options_style:

      pane:

      visible:

      attribution (event):

      geojson (event):

      layer_type (event):

      name (event):

      options (event):

      options_style (event):

      pane (event):

      visible (event):


    """

    def __init__(self, children=None, **kwargs):
        super().__init__("l-geo-json", children, **kwargs)
        self._attr_names += [
            "attribution",
            "geojson",
            ("layer_type", "layerType"),
            "name",
            "options",
            ("options_style", "optionsStyle"),
            "pane",
            "visible",
        ]
        self._event_names += [
            "ready",
        ]


class LGridLayer(HtmlElement):
    """
    Component LGridLayer with the following properties

    Args:
      attribution:

      child_render:

      class_name:

      layer_type:

      max_zoom:

      min_zoom:

      name:

      no_wrap:

      opacity:

      options:

      pane:

      tile_size:

      visible:

      zindex:

      attribution (event):

      child_render (event):

      class_name (event):

      layer_type (event):

      max_zoom (event):

      min_zoom (event):

      name (event):

      no_wrap (event):

      opacity (event):

      options (event):

      pane (event):

      tile_size (event):

      visible (event):

      zindex (event):


    """

    def __init__(self, children=None, **kwargs):
        super().__init__("l-grid-layer", children, **kwargs)
        self._attr_names += [
            "attribution",
            ("child_render", "childRender"),
            ("class_name", "className"),
            ("layer_type", "layerType"),
            ("max_zoom", "maxZoom"),
            ("min_zoom", "minZoom"),
            "name",
            ("no_wrap", "noWrap"),
            "opacity",
            "options",
            "pane",
            ("tile_size", "tileSize"),
            "visible",
            ("zindex", "zIndex"),
        ]
        self._event_names += [
            "ready",
        ]


class LIcon(HtmlElement):
    """
    Component LIcon with the following properties

    Args:
      bg_pos:

      class_name:

      icon_anchor:

      icon_retina_url:

      icon_size:

      icon_url:

      options:

      popup_anchor:

      shadow_anchor:

      shadow_retinaUrl:

      shadow_size:

      shadow_url:

      tooltip_anchor:

      bg_pos (event):

      class_name (event):

      icon_anchor (event):

      icon_retina_url (event):

      icon_size (event):

      icon_url (event):

      options (event):

      popup_anchor (event):

      shadow_anchor (event):

      shadow_retinaUrl (event):

      shadow_size (event):

      shadow_url (event):

      tooltip_anchor (event):


    """

    def __init__(self, children=None, **kwargs):
        super().__init__("l-icon", children, **kwargs)
        self._attr_names += [
            ("bg_pos", "bgPos"),
            ("class_name", "className"),
            ("icon_anchor", "iconAnchor"),
            ("icon_retina_url", "iconRetinaUrl"),
            ("icon_size", "iconSize"),
            ("icon_url", "iconUrl"),
            "options",
            ("popup_anchor", "popupAnchor"),
            ("shadow_anchor", "shadowAnchor"),
            ("shadow_retinaUrl", "shadowRetinaUrl"),
            ("shadow_size", "shadowSize"),
            ("shadow_url", "shadowUrl"),
            ("tooltip_anchor", "tooltipAnchor"),
        ]
        self._event_names += [
            "ready",
        ]


class LImageOverlay(HtmlElement):
    """
    Component LImageOverlay with the following properties

    Args:
      alt:

      attribution:

      bounds:

      class_name:

      cross_origin:

      error_overlay_url:

      interactive:

      layer_type:

      name:

      opacity:

      options:

      pane:

      url:

      visible:

      zindex:

      alt (event):

      attribution (event):

      bounds (event):

      class_name (event):

      cross_origin (event):

      error_overlay_url (event):

      interactive (event):

      layer_type (event):

      name (event):

      opacity (event):

      options (event):

      pane (event):

      url (event):

      visible (event):

      zindex (event):


    """

    def __init__(self, children=None, **kwargs):
        super().__init__("l-image-overlay", children, **kwargs)
        self._attr_names += [
            "alt",
            "attribution",
            "bounds",
            ("class_name", "className"),
            ("cross_origin", "crossOrigin"),
            ("error_overlay_url", "errorOverlayUrl"),
            "interactive",
            ("layer_type", "layerType"),
            "name",
            "opacity",
            "options",
            "pane",
            "url",
            "visible",
            ("zindex", "zIndex"),
        ]
        self._event_names += [
            "ready",
        ]


class LLayerGroup(HtmlElement):
    """
    Component LLayerGroup with the following properties

    Args:
      attribution:

      layer_type:

      name:

      options:

      pane:

      visible:

      attribution (event):

      layer_type (event):

      name (event):

      options (event):

      pane (event):

      visible (event):


    """

    def __init__(self, children=None, **kwargs):
        super().__init__("l-layer-group", children, **kwargs)
        self._attr_names += [
            "attribution",
            ("layer_type", "layerType"),
            "name",
            "options",
            "pane",
            "visible",
        ]
        self._event_names += [
            "ready",
        ]


class LMap(HtmlElement):
    """
    Component LMap with the following properties

    Args:
      v_model_zoom:

      v_model_center:

      v_model_bounds:

      bounds:
        The bounds of the map
      bounds_sync:
        The bounds of the map with .sync modifier
      center:
        The center of the map
      center_sync:
        The center of the map with .sync modifier
      crs:
        The CRS to use for the map. Can be an object that defines a coordinate
        reference system for projecting geographical points into screen
        coordinates and back (see https://leafletjs.com/reference-1.7.1.html#crs-l-crs-base),
        or a string name identifying one of Leaflet's defined CRSs, such
        as "EPSG4326".
      ease_linearity:

      fade_animation:

      inertia:

      inertia_deceleration:

      inertia_max_speed:

      marker_zoom_animation:

      max_bounds:
        The max bounds of the map
      max_bounds_viscosity:

      max_zoom:
        The maxZoom of the map
      min_zoom:
        The minZoom of the map
      no_blocking_animations:

      options:

      padding:
        The padding of the map
      padding_bottom_right:
        The paddingBottomRight of the map
      padding_top_left:
        The paddingTopLeft of the map
      use_global_leaflet:

      world_copy_jump:
        The worldCopyJump option for the map
      zoom:
        The zoom of the map
      zoom_sync:
        The zoom of the map with .sync modifier
      zoom_animation:

      zoom_animation_threshold:

      v_model_zoom (event):

      v_model_center (event):

      v_model_bounds (event):

      bounds (event):
        The bounds of the map
      bounds_sync (event):
        The bounds of the map with .sync modifier
      center (event):
        The center of the map
      center_sync (event):
        The center of the map with .sync modifier
      crs (event):
        The CRS to use for the map. Can be an object that defines a coordinate
        reference system for projecting geographical points into screen
        coordinates and back (see https://leafletjs.com/reference-1.7.1.html#crs-l-crs-base),
        or a string name identifying one of Leaflet's defined CRSs, such
        as "EPSG4326".
      ease_linearity (event):

      fade_animation (event):

      inertia (event):

      inertia_deceleration (event):

      inertia_max_speed (event):

      marker_zoom_animation (event):

      max_bounds (event):
        The max bounds of the map
      max_bounds_viscosity (event):

      max_zoom (event):
        The maxZoom of the map
      min_zoom (event):
        The minZoom of the map
      no_blocking_animations (event):

      options (event):

      padding (event):
        The padding of the map
      padding_bottom_right (event):
        The paddingBottomRight of the map
      padding_top_left (event):
        The paddingTopLeft of the map
      use_global_leaflet (event):

      world_copy_jump (event):
        The worldCopyJump option for the map
      zoom (event):
        The zoom of the map
      zoom_sync (event):
        The zoom of the map with .sync modifier
      zoom_animation (event):

      zoom_animation_threshold (event):


    """

    def __init__(self, children=None, **kwargs):
        super().__init__("l-map", children, **kwargs)
        self._attr_names += [
            ("v_model_zoom", "v-model:zoom"),
            ("v_model_center", "v-model:center"),
            ("v_model_bounds", "v-model:bounds"),
            "bounds",
            ("bounds_sync", "bounds.sync"),
            "center",
            ("center_sync", "center.sync"),
            "crs",
            ("ease_linearity", "easeLinearity"),
            ("fade_animation", "fadeAnimation"),
            "inertia",
            ("inertia_deceleration", "inertiaDeceleration"),
            ("inertia_max_speed", "inertiaMaxSpeed"),
            ("marker_zoom_animation", "markerZoomAnimation"),
            ("max_bounds", "maxBounds"),
            ("max_bounds_viscosity", "maxBoundsViscosity"),
            ("max_zoom", "maxZoom"),
            ("min_zoom", "minZoom"),
            ("no_blocking_animations", "noBlockingAnimations"),
            "options",
            "padding",
            ("padding_bottom_right", "paddingBottomRight"),
            ("padding_top_left", "paddingTopLeft"),
            ("use_global_leaflet", "useGlobalLeaflet"),
            ("world_copy_jump", "worldCopyJump"),
            "zoom",
            ("zoom_sync", "zoom.sync"),
            ("zoom_animation", "zoomAnimation"),
            ("zoom_animation_threshold", "zoomAnimationThreshold"),
        ]
        self._event_names += [
            "ready",
            ("update_zoom", "update:zoom"),
            ("update_bounds", "update:bounds"),
            ("update_center", "update:center"),
        ]


class LMarker(HtmlElement):
    """
    Component LMarker with the following properties

    Args:
      attribution:

      draggable:

      icon:

      lat_lng:

      layer_type:

      name:

      options:

      pane:

      visible:

      zindex_offset:

      attribution (event):

      draggable (event):

      icon (event):

      lat_lng (event):

      layer_type (event):

      name (event):

      options (event):

      pane (event):

      visible (event):

      zindex_offset (event):


    """

    def __init__(self, children=None, **kwargs):
        super().__init__("l-marker", children, **kwargs)
        self._attr_names += [
            "attribution",
            "draggable",
            "icon",
            ("lat_lng", "latLng"),
            ("layer_type", "layerType"),
            "name",
            "options",
            "pane",
            "visible",
            ("zindex_offset", "zIndexOffset"),
        ]
        self._event_names += [
            "ready",
            ("move_end", "moveend"),
        ]


class LPolygon(HtmlElement):
    """
    Component LPolygon with the following properties

    Args:
      attribution:

      bubbling_mouse_events:

      class_name:

      color:

      dash_array:

      dash_offset:

      fill:

      fill_color:

      fill_opacity:

      fill_rule:

      interactive:

      lat_lngs:

      layer_type:

      line_cap:

      line_join:

      name:

      no_clip:

      opacity:

      options:

      pane:

      smooth_factor:

      stroke:

      visible:

      weight:

      attribution (event):

      bubbling_mouse_events (event):

      class_name (event):

      color (event):

      dash_array (event):

      dash_offset (event):

      fill (event):

      fill_color (event):

      fill_opacity (event):

      fill_rule (event):

      interactive (event):

      lat_lngs (event):

      layer_type (event):

      line_cap (event):

      line_join (event):

      name (event):

      no_clip (event):

      opacity (event):

      options (event):

      pane (event):

      smooth_factor (event):

      stroke (event):

      visible (event):

      weight (event):


    """

    def __init__(self, children=None, **kwargs):
        super().__init__("l-polygon", children, **kwargs)
        self._attr_names += [
            "attribution",
            ("bubbling_mouse_events", "bubblingMouseEvents"),
            ("class_name", "className"),
            "color",
            ("dash_array", "dashArray"),
            ("dash_offset", "dashOffset"),
            "fill",
            ("fill_color", "fillColor"),
            ("fill_opacity", "fillOpacity"),
            ("fill_rule", "fillRule"),
            "interactive",
            ("lat_lngs", "latLngs"),
            ("layer_type", "layerType"),
            ("line_cap", "lineCap"),
            ("line_join", "lineJoin"),
            "name",
            ("no_clip", "noClip"),
            "opacity",
            "options",
            "pane",
            ("smooth_factor", "smoothFactor"),
            "stroke",
            "visible",
            "weight",
        ]
        self._event_names += [
            "ready",
        ]


class LPolyline(HtmlElement):
    """
    Component LPolyline with the following properties

    Args:
      attribution:

      bubbling_mouse_events:

      class_name:

      color:

      dash_array:

      dash_offset:

      fill:

      fill_color:

      fill_opacity:

      fill_rule:

      interactive:

      lat_lngs:

      layer_type:

      line_cap:

      line_join:

      name:

      no_clip:

      opacity:

      options:

      pane:

      smooth_factor:

      stroke:

      visible:

      weight:

      attribution (event):

      bubbling_mouse_events (event):

      class_name (event):

      color (event):

      dash_array (event):

      dash_offset (event):

      fill (event):

      fill_color (event):

      fill_opacity (event):

      fill_rule (event):

      interactive (event):

      lat_lngs (event):

      layer_type (event):

      line_cap (event):

      line_join (event):

      name (event):

      no_clip (event):

      opacity (event):

      options (event):

      pane (event):

      smooth_factor (event):

      stroke (event):

      visible (event):

      weight (event):


    """

    def __init__(self, children=None, **kwargs):
        super().__init__("l-polyline", children, **kwargs)
        self._attr_names += [
            "attribution",
            ("bubbling_mouse_events", "bubblingMouseEvents"),
            ("class_name", "className"),
            "color",
            ("dash_array", "dashArray"),
            ("dash_offset", "dashOffset"),
            "fill",
            ("fill_color", "fillColor"),
            ("fill_opacity", "fillOpacity"),
            ("fill_rule", "fillRule"),
            "interactive",
            ("lat_lngs", "latLngs"),
            ("layer_type", "layerType"),
            ("line_cap", "lineCap"),
            ("line_join", "lineJoin"),
            "name",
            ("no_clip", "noClip"),
            "opacity",
            "options",
            "pane",
            ("smooth_factor", "smoothFactor"),
            "stroke",
            "visible",
            "weight",
        ]
        self._event_names += [
            "ready",
        ]


class LPopup(HtmlElement):
    """
    Component LPopup with the following properties

    Args:
      content:

      lat_lng:

      options:

      content (event):

      lat_lng (event):

      options (event):


    """

    def __init__(self, children=None, **kwargs):
        super().__init__("l-popup", children, **kwargs)
        self._attr_names += [
            "content",
            ("lat_lng", "latLng"),
            "options",
        ]
        self._event_names += [
            "ready",
        ]


class LRectangle(HtmlElement):
    """
    Component LRectangle with the following properties

    Args:
      attribution:

      bounds:

      bubbling_mouse_events:

      class_name:

      color:

      dash_array:

      dash_offset:

      fill:

      fill_color:

      fill_opacity:

      fill_rule:

      interactive:

      lat_lngs:

      layer_type:

      line_cap:

      line_join:

      name:

      no_clip:

      opacity:

      options:

      pane:

      smooth_factor:

      stroke:

      visible:

      weight:

      attribution (event):

      bounds (event):

      bubbling_mouse_events (event):

      class_name (event):

      color (event):

      dash_array (event):

      dash_offset (event):

      fill (event):

      fill_color (event):

      fill_opacity (event):

      fill_rule (event):

      interactive (event):

      lat_lngs (event):

      layer_type (event):

      line_cap (event):

      line_join (event):

      name (event):

      no_clip (event):

      opacity (event):

      options (event):

      pane (event):

      smooth_factor (event):

      stroke (event):

      visible (event):

      weight (event):


    """

    def __init__(self, children=None, **kwargs):
        super().__init__("l-rectangle", children, **kwargs)
        self._attr_names += [
            "attribution",
            "bounds",
            ("bubbling_mouse_events", "bubblingMouseEvents"),
            ("class_name", "className"),
            "color",
            ("dash_array", "dashArray"),
            ("dash_offset", "dashOffset"),
            "fill",
            ("fill_color", "fillColor"),
            ("fill_opacity", "fillOpacity"),
            ("fill_rule", "fillRule"),
            "interactive",
            ("lat_lngs", "latLngs"),
            ("layer_type", "layerType"),
            ("line_cap", "lineCap"),
            ("line_join", "lineJoin"),
            "name",
            ("no_clip", "noClip"),
            "opacity",
            "options",
            "pane",
            ("smooth_factor", "smoothFactor"),
            "stroke",
            "visible",
            "weight",
        ]
        self._event_names += [
            "ready",
        ]


class LTileLayer(HtmlElement):
    """
    Component LTileLayer with the following properties

    Args:
      attribution:

      class_name:

      detect_retina:

      layer_type:

      max_zoom:

      min_zoom:

      name:

      no_wrap:

      opacity:

      options:

      pane:

      subdomains:

      tile_size:

      tms:

      url:

      visible:

      zindex:

      attribution (event):

      class_name (event):

      detect_retina (event):

      layer_type (event):

      max_zoom (event):

      min_zoom (event):

      name (event):

      no_wrap (event):

      opacity (event):

      options (event):

      pane (event):

      subdomains (event):

      tile_size (event):

      tms (event):

      url (event):

      visible (event):

      zindex (event):


    """

    def __init__(self, children=None, **kwargs):
        super().__init__("l-tile-layer", children, **kwargs)
        self._attr_names += [
            "attribution",
            ("class_name", "className"),
            ("detect_retina", "detectRetina"),
            ("layer_type", "layerType"),
            ("max_zoom", "maxZoom"),
            ("min_zoom", "minZoom"),
            "name",
            ("no_wrap", "noWrap"),
            "opacity",
            "options",
            "pane",
            "subdomains",
            ("tile_size", "tileSize"),
            "tms",
            "url",
            "visible",
            ("zindex", "zIndex"),
        ]
        self._event_names += [
            "ready",
        ]


class LTooltip(HtmlElement):
    """
    Component LTooltip with the following properties

    Args:
      content:

      options:

      content (event):

      options (event):


    """

    def __init__(self, children=None, **kwargs):
        super().__init__("l-tooltip", children, **kwargs)
        self._attr_names += [
            "content",
            "options",
        ]
        self._event_names += [
            "ready",
        ]


class LWmsTileLayer(HtmlElement):
    """
    Component LWmsTileLayer with the following properties

    Args:
      attribution:

      class_name:

      crs:

      detect_retina:

      format:

      layer_type:

      layers:

      max_zoom:

      min_zoom:

      name:

      no_wrap:

      opacity:

      options:

      pane:

      styles:

      subdomains:

      tile_size:

      tms:

      transparent:

      uppercase:

      url:

      version:

      visible:

      zindex:

      attribution (event):

      class_name (event):

      crs (event):

      detect_retina (event):

      format (event):

      layer_type (event):

      layers (event):

      max_zoom (event):

      min_zoom (event):

      name (event):

      no_wrap (event):

      opacity (event):

      options (event):

      pane (event):

      styles (event):

      subdomains (event):

      tile_size (event):

      tms (event):

      transparent (event):

      uppercase (event):

      url (event):

      version (event):

      visible (event):

      zindex (event):


    """

    def __init__(self, children=None, **kwargs):
        super().__init__("l-wms-title-layers", children, **kwargs)
        self._attr_names += [
            "attribution",
            ("class_name", "className"),
            "crs",
            ("detect_retina", "detectRetina"),
            "format",
            ("layer_type", "layerType"),
            "layers",
            ("max_zoom", "maxZoom"),
            ("min_zoom", "minZoom"),
            "name",
            ("no_wrap", "noWrap"),
            "opacity",
            "options",
            "pane",
            "styles",
            "subdomains",
            ("tile_size", "tileSize"),
            "tms",
            "transparent",
            "uppercase",
            "url",
            "version",
            "visible",
            ("zindex", "zIndex"),
        ]
        self._event_names += [
            "ready",
        ]


__all__ = [
    "LCircle",
    "LCircleMarker",
    "LControl",
    "LControlAttribution",
    "LControlLayers",
    "LControlScale",
    "LControlZoom",
    "LFeatureGroup",
    "LGeoJson",
    "LGridLayer",
    "LIcon",
    "LImageOverlay",
    "LLayerGroup",
    "LMap",
    "LMarker",
    "LPolygon",
    "LPolyline",
    "LPopup",
    "LRectangle",
    "LTileLayer",
    "LTooltip",
    "LWmsTileLayer",
]
