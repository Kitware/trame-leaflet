from pathlib import Path

# Compute local path to serve
serve_path = str(Path(__file__).with_name("serve").resolve())

# Serve directory for JS/CSS files
serve = {"__trame_leaflet": serve_path}

# List of JS files to load (usually from the serve path above)
scripts = [
    "__trame_leaflet/trame-leaflet.umd.min.js",
]
styles = ["__trame_leaflet/trame-leaflet.css"]

# List of Vue plugins to install/load
vue_use = ["TrameLeaflet"]
