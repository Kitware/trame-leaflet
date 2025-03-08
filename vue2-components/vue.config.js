const path = require('path');
const CopyPlugin = require('copy-webpack-plugin');
const DST_PATH = '../trame_leaflet/module/leaflet2/serve';

module.exports = {
  outputDir: path.resolve(__dirname, DST_PATH),
  publicPath: './',
  configureWebpack: {
    plugins: [
      new CopyPlugin({
        patterns: [
          { from: 'node_modules/leaflet/dist/images/marker-icon.png', to: "tramemarker-icon.png" },
          { from: 'node_modules/leaflet/dist/images/marker-icon-2x.png', to: "tramemarker-icon-2x.png" },
          { from: 'node_modules/leaflet/dist/images/marker-shadow.png', to: "tramemarker-shadow.png" },
          { from: 'node_modules/leaflet/dist/images/layers.png', to: "tramelayers.png" },
          { from: 'node_modules/leaflet/dist/images/layers-2x.png', to: "tramelayers-2x.png" },
        ],
      }),
    ],
  },
};
