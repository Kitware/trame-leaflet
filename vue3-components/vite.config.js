export default {
  base: "./",
  build: {
    lib: {
      entry: "./src/main.js",
      name: "TrameLeaflet3",
      formats: ["umd"],
      fileName: "trame-leaflet3",
    },
    rollupOptions: {
      external: ["vue"],
      output: {
        globals: {
          vue: "Vue",
        },
      },
    },
    assetsDir: ".",
  },
};
