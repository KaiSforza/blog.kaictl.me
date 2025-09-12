{ pkgs, config, ... }:
{
  name = "devshell";
  motd = "Run {bold}menu{reset} for details";
  packages = with pkgs; [
    zola
  ];
  commands = {
  };
  env = {
  };
  devshell.startup = {
    pre-commit.text = config.pre-commit.installationScript;
  };
}
