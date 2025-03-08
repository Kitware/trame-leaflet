from pathlib import Path

serve_path = str(Path(__file__).with_name("vue3").resolve())
serve = {"__trame_leaflet3": serve_path}
scripts = [
    "__trame_leaflet3/trame-leaflet3.umd.js",
]
styles = [
    "__trame_leaflet3/style.css",
]
vue_use = [
    "TrameLeaflet3",
]
