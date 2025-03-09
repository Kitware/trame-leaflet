# CHANGELOG


## v1.2.4 (2025-03-09)

### Bug Fixes

- **api**: Add missing v-model
  ([`c77289e`](https://github.com/Kitware/trame-leaflet/commit/c77289e447c70cfb0ba26c3056698d14873eb8a8))


## v1.2.3 (2025-03-09)

### Bug Fixes

- **release**: Trigger a release
  ([`6ccfbb6`](https://github.com/Kitware/trame-leaflet/commit/6ccfbb686b5dfdf6bdf7f6a6f1be809de7aec85b))


## v1.2.2 (2025-03-09)

### Bug Fixes

- **ci**: Add missing dep
  ([`2578827`](https://github.com/Kitware/trame-leaflet/commit/25788271b86af1ccc20ba251c3d74ceeb3831f0d))

- **release**: Update build tech
  ([`9751931`](https://github.com/Kitware/trame-leaflet/commit/9751931bf97a0000a0c2cea618b6a351c969cd85))


## v1.2.1 (2025-03-09)

### Bug Fixes

- **release**: Update ci to publish vue3
  ([`f5b7d59`](https://github.com/Kitware/trame-leaflet/commit/f5b7d596d560219ee4e373671875d0b95e965358))


## v1.2.0 (2025-03-09)

### Bug Fixes

- **vue2**: Rename old components to enable vue3
  ([`eff4a7f`](https://github.com/Kitware/trame-leaflet/commit/eff4a7fe06c6e3395504f6121119be6c52050efa))

### Continuous Integration

- Add build for vue3
  ([`345b3e6`](https://github.com/Kitware/trame-leaflet/commit/345b3e67aecd7b62fb5fc91643f7208b2d8b26af))

- Fix semantic-release version v7.34.6
  ([`6154b61`](https://github.com/Kitware/trame-leaflet/commit/6154b61fe86c3767440b816c13767634b8bad020))

### Documentation

- Update README.rst
  ([`e7e8e2a`](https://github.com/Kitware/trame-leaflet/commit/e7e8e2a4300054c8773d205cdb84f06c9ac0612f))

- **js**: List JS dependency
  ([`dd3d018`](https://github.com/Kitware/trame-leaflet/commit/dd3d018a730e3a1dee06515ed1c09e95df09cb43))

### Features

- **vue3**: Add vue3 support
  ([`fed6e01`](https://github.com/Kitware/trame-leaflet/commit/fed6e01911517d5dd19a6393b8824f622eda0f42))


## v1.1.1 (2023-04-25)

### Bug Fixes

- **api**: Expose only meaningful classes
  ([`0b2a82e`](https://github.com/Kitware/trame-leaflet/commit/0b2a82eb831755eb8cf61d3eac875ff543f580f7))


## v1.1.0 (2023-02-23)

### Features

- **snake_case**: Expose attribute following Python snake_case
  ([`e8f7273`](https://github.com/Kitware/trame-leaflet/commit/e8f7273dc41a2a4e45ce4a955daa9dac33d81f41))

* Map JS name to python name for min/max zoom params in LMap * Add back missing paddingBottomRight
  param to LMap * map JS to python for object attributes * Remove duplicate `update:latLng` from
  `LMarker` * reformatting


## v1.0.3 (2023-02-23)

### Bug Fixes

- **version**: Add __version__
  ([`90cf51a`](https://github.com/Kitware/trame-leaflet/commit/90cf51ab2c59b1ed7b0a7c90c6a789a8b2d3a7be))

Signed-off-by: Patrick Avery <patrick.avery@kitware.com>


## v1.0.2 (2022-09-02)

### Bug Fixes

- **ci**: Fix failing tests
  ([`1d5367a`](https://github.com/Kitware/trame-leaflet/commit/1d5367a465e74edfaf51491e4950f633b646bb43))

### Chores

- **ci**: Update python-semantic-release to master
  ([`2ce4d44`](https://github.com/Kitware/trame-leaflet/commit/2ce4d44968e29d59575fe928e416ac0814374e7b))

This is necessary for semantic-release to upload successfully.

Signed-off-by: Patrick Avery <patrick.avery@kitware.com>


## v1.0.1 (2022-08-31)

### Bug Fixes

- **config**: Fix missing .png files of markers and layers
  ([`329807c`](https://github.com/Kitware/trame-leaflet/commit/329807c66a6c8aec4039af6662eb9bf040a2a8f3))

### Chores

- **ci**: Setup CI
  ([`c67303c`](https://github.com/Kitware/trame-leaflet/commit/c67303c48d281a9849e76ecf9d88a1fc4c8e8dcd))

- **lint**: Run linter and remove serve folder
  ([`3c85cfb`](https://github.com/Kitware/trame-leaflet/commit/3c85cfb65a0a55a317fe950ff030effea23a37fc))
