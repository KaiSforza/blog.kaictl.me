{ pkgs, ... }:
{
  check.enable = false;
  settings = {
    default_stages = [ "pre-push" ];
    hooks = {
      nixfmt-rfc-style.enable = true;
    };
  };
}
