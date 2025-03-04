import {
  LCircle,
  LCircleMarker,
  LControl,
  LControlAttribution,
  LControlLayers,
  LControlScale,
  LControlZoom,
  LFeatureGroup,
  LGeoJson,
  LGridLayer,
  LIcon,
  LIconDefault,
  LImageOverlay,
  LLayerGroup,
  LMap,
  LMarker,
  LPolygon,
  LPolyline,
  LPopup,
  LRectangle,
  LTileLayer,
  LTooltip,
  LWMSTileLayer,
} from 'vue2-leaflet';
import 'leaflet/dist/leaflet.css';

export default {
  install(Vue) {
    Vue.component('l-circle', LCircle);
    Vue.component('l-circle-marker', LCircleMarker);
    Vue.component('l-control', LControl);
    Vue.component('l-control-attribution', LControlAttribution);
    Vue.component('l-control-layers', LControlLayers);
    Vue.component('l-control-scale', LControlScale);
    Vue.component('l-control-zoom', LControlZoom);
    Vue.component('l-feature-group', LFeatureGroup);
    Vue.component('l-geo-json', LGeoJson);
    Vue.component('l-grid-layer', LGridLayer);
    Vue.component('l-icon', LIcon);
    Vue.component('l-icon-default', LIconDefault);
    Vue.component('l-image-overlay', LImageOverlay);
    Vue.component('l-layer-group', LLayerGroup);
    Vue.component('l-map', LMap);
    Vue.component('l-marker', LMarker);
    Vue.component('l-polygon', LPolygon);
    Vue.component('l-polyline', LPolyline);
    Vue.component('l-popup', LPopup);
    Vue.component('l-rectangle', LRectangle);
    Vue.component('l-tile-layer', LTileLayer);
    Vue.component('l-tooltip', LTooltip);
    Vue.component('l-wms-tile-layer', LWMSTileLayer);
  },
};
