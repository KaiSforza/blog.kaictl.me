{ inputs', inputs, ... }:
inputs'.nixpkgs.legacyPackages.extend (
  inputs.nixpkgs.lib.composeManyExtensions [
    inputs.git-hooks-rs.overlays.default
  ]
)
