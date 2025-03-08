import "leaflet/dist/leaflet.css";

import * as VueLeaflet from "@vue-leaflet/vue-leaflet";

export function install(Vue) {
  console.log("VueLeaflet", VueLeaflet);
  Object.keys(VueLeaflet).forEach((name) => {
    Vue.component(name, VueLeaflet[name]);
  });
}
