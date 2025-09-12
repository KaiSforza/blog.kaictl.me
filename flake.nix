{
  description = "devshell";

  # Flake inputs
  inputs = {
    systems.url = "github:nix-systems/default";
    nixpkgs.url = "https://flakehub.com/f/NixOS/nixpkgs/0.1";
    flake-parts.url = "https://flakehub.com/f/hercules-ci/flake-parts/*";
    devshell = {
      url = "github:KaiSforza/devshell/rusty";
      inputs.nixpkgs.follows = "nixpkgs";
    };
    git-hooks = {
      url = "https://flakehub.com/f/cachix/git-hooks.nix/*";
      inputs.nixpkgs.follows = "nixpkgs";
    };
    git-hooks-rs = {
      url = "https://flakehub.com/f/KaiSforza/git-hooks.rs/*";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  # Flake outputs
  outputs =
    inputs:
    inputs.flake-parts.lib.mkFlake { inherit inputs; } {
      systems = import inputs.systems;
      imports = [
        inputs.devshell.flakeModule
        inputs.git-hooks.flakeModule
      ];
      perSystem =
        {
          pkgs,
          config,
          inputs',
          ...
        }:
        let
          p = import ./nix/packages.nix { inherit pkgs inputs; };
        in
        {
          _module.args.pkgs = import ./nix/overlays.nix { inherit inputs inputs'; };
          inherit (p) checks;
          pre-commit = import ./nix/pre-commit.nix { inherit pkgs; };
          devshells = {
            default = import ./nix/devshell.nix { inherit pkgs config; };
          };
        };
    };
}
