@echo off

SET red=\e[0;91m
SET green=\e[0;92m
SET blue=\e[0;94m
SET bold=\e[1m
SET reset=\e[0m
function "staging" "{"
REM UNKNOWN: {"type":"While","clause":{"type":"CompoundList","commands":[{"type":"Command","name":{"text":"true","type":"Word"}}]},"do":{"type":"CompoundList","commands":[{"type":"Command","name":{"text":"read","type":"Word"},"suffix":[{"text":"-r","type":"Word"},{"text":"-p","type":"Word"},{"text":"This will copy TOOLBAR to your home directory. If you already had TOOLBAR installed, this will reinstall it. Would you like to continue? [Y/n]","type":"Word"},{"text":"input","type":"Word"}]},{"type":"Case","clause":{"text":"$input","expansion":[{"loc":{"start":0,"end":5},"parameter":"input","type":"ParameterExpansion"}],"type":"Word"},"cases":[{"type":"CaseItem","pattern":[{"text":"[yY][eE][sS]","type":"Word"},{"text":"[yY]","type":"Word"}],"body":{"type":"CompoundList","commands":[{"type":"Command","name":{"text":"echo","type":"Word"},"suffix":[{"text":"-e","type":"Word"},{"text":"\"${green}Continuing...${reset}\"","expansion":[{"loc":{"start":1,"end":8},"parameter":"green","type":"ParameterExpansion"},{"loc":{"start":22,"end":29},"parameter":"reset","type":"ParameterExpansion"}],"type":"Word"}]},{"type":"Command","name":{"text":"sleep","type":"Word"},"suffix":[{"text":"2","type":"Word"}]},{"type":"Command","prefix":[{"text":"install=true","type":"AssignmentWord"}]},{"type":"Command","name":{"text":"break","type":"Word"}}]}},{"type":"CaseItem","pattern":[{"text":"[nN][oO]","type":"Word"},{"text":"[nN]","type":"Word"}],"body":{"type":"CompoundList","commands":[{"type":"Command","name":{"text":"echo","type":"Word"},"suffix":[{"text":"-e","type":"Word"},{"text":"\"${red}Operation canceled.${reset}\"","expansion":[{"loc":{"start":1,"end":6},"parameter":"red","type":"ParameterExpansion"},{"loc":{"start":26,"end":33},"parameter":"reset","type":"ParameterExpansion"}],"type":"Word"}]},{"type":"Command","name":{"text":"break","type":"Word"}},{"type":"Command","name":{"text":"exit","type":"Word"},"suffix":[{"text":"0","type":"Word"}]}]}},{"type":"CaseItem","pattern":[{"text":"*","type":"Word"}],"body":{"type":"CompoundList","commands":[{"type":"Command","name":{"text":"echo","type":"Word"},"suffix":[{"text":"-e","type":"Word"},{"text":"\"${red}Invalid input...${reset}\"","expansion":[{"loc":{"start":1,"end":6},"parameter":"red","type":"ParameterExpansion"},{"loc":{"start":23,"end":30},"parameter":"reset","type":"ParameterExpansion"}],"type":"Word"}]}]}}]}]}}
echo "-e" "%blue%[*] Staging process...%reset%"
DEL /S "~\.TOOLBAR"
cd ".."
COPY  "TOOLBAR" "~\.TOOLBAR"
echo "-e" "%green%[+] Complete%reset%"
function "alias_workflow" "{"
echo "-e" "%blue%[*] Setting up alias...%reset%"
echo "
        export TOOLBAR_PATH="~/.TOOLBAR"
        alias toolbar="python3 ~/.TOOLBAR/main.py"
        " REM UNKNOWN: {"type":"Redirect","op":{"text":">>","type":"dgreat"},"file":{"text":"~/.bashrc","type":"Word"}}
IF REM UNKNOWN: {"type":"Pipeline","commands":[{"type":"Command","name":{"text":"!","type":"Word"},"suffix":[{"text":"cat","type":"Word"},{"text":"~/.zshrc","type":"Word"}]},{"type":"Command","name":{"text":"grep","type":"Word"},"suffix":[{"text":"TOOLBAR_PATH","type":"Word"},{"type":"Redirect","op":{"text":">","type":"great"},"file":{"text":"/dev/null","type":"Word"}}]}]} (
  echo "
          export TOOLBAR_PATH="~/.TOOLBAR"
          alias toolbar="python3 ~/.TOOLBAR/main.py"
          " REM UNKNOWN: {"type":"Redirect","op":{"text":">>","type":"dgreat"},"file":{"text":"~/.zshrc","type":"Word"}}
)
echo "-e" "%green%[+] Completed%reset%"
staging
echo "-e" "%green%[+] Installation Successful"
echo "-e" "[+] Please Restart your terminal"
echo "-e" "[+] type 'toolbar' launch ToolBar%reset%"
bash
IF "%EUID%" "-ne" "0" (
  continue
) ELSE (
  echo "-e" "%red%Do not run as root. The script will prompt you for root access.%reset%"
  exit "0"
)
REM UNKNOWN: {"type":"While","clause":{"type":"CompoundList","commands":[{"type":"Command","name":{"text":"[","type":"Word"},"suffix":[{"text":"-n","type":"Word"},{"text":"\"$1\"","expansion":[{"loc":{"start":1,"end":2},"parameter":1,"type":"ParameterExpansion","kind":"positional"}],"type":"Word"},{"text":"]","type":"Word"}]}]},"do":{"type":"CompoundList","commands":[{"type":"Case","clause":{"text":"\"$1\"","expansion":[{"loc":{"start":1,"end":2},"parameter":1,"type":"ParameterExpansion","kind":"positional"}],"type":"Word"},"cases":[{"type":"CaseItem","pattern":[{"text":"--help","type":"Word"}],"body":{"type":"CompoundList","commands":[{"type":"Command","name":{"text":"echo","type":"Word"},"suffix":[{"text":"\n        SUPPORTED DISTROS:\n        - Debian\n            - Parrot\n            - Ubuntu\n            - Kali\n            - Mint\n        - Arch\n        - Void\n        Please see the TOOLBAR README for more infomation:\n        https://github.com/SaintsConnor/ToolBar\n  ","type":"Word"}]},{"type":"Command","name":{"text":"exit","type":"Word"},"suffix":[{"text":"0","type":"Word"}]}]}},{"type":"CaseItem","pattern":[{"text":"--unsupported-distro","type":"Word"}],"body":{"type":"CompoundList","commands":[{"type":"Command","name":{"text":"alias_workflow","type":"Word"}},{"type":"Command","name":{"text":"exit","type":"Word"},"suffix":[{"text":"0","type":"Word"}]}]}}]},{"type":"Command","name":{"text":"shift","type":"Word"}}]}}
SET distro=%undefined%
IF [[ "%distro%" == "Debian" "]]" || [[ "%distro%" == "Parrot" "]]" || [[ "%distro%" == "Ubuntu" "]]" || [[ "%distro%" == "Linux" "]]" || [[ "%distro%" == "Kali" "]]" (
  echo "-e" "%red%Debian%reset% system detected."
  echo "-e" "%blue%[*] Installing tools...%reset%"
  sudo "apt" "update"
  sudo "apt-get" "install" "-y" "python3" "python3-pip" "python-dev"
  pip "install" "qrcode"
  pip "install" "Cryptography"
  pip "install" "googletrans==3.1.0a0"
  pip "install" "colorama"
  pip "install" "pillow"
  pip "install" "numpy"
  echo "-e" "%green%[+] Completed%reset%"
) ELSE (
  IF [[ "%distro%" == "Void" "]]" (
    echo "-e" "%green%Void%reset% system detected."
    echo "-e" "%blue%[*] Installing tools...%reset%"
    sudo "xbps-install" "-S" "python3"
    pip "install" "qrcode"
    pip "install" "Cryptography"
    pip "install" "googletrans==3.1.0a0"
    pip "install" "colorama"
    echo "-e" "%green%[+] Completed%reset%"
  ) ELSE (
    IF [[ "%distro%" "=" "Arch" "]]" (
      echo "-e" "%blue%Arch%reset% system detected."
      echo "-e" "%blue%[*] Installing tools...%reset%"
      sudo "pacman" "-Syu"
      sudo "pacman" "-S" "python" "python-pip"
      python3 "-m" "pip" "install" "qrcode"
      python3 "-m" "pip" "install" "Cryptography"
      python3 "-m" "pip" "install" "googletrans==3.1.0a0"
      python3 "-m" "pip" "install" "colorama"
      echo "-e" "%green%[+] Completed%reset%"
    ) ELSE (
      echo "-e" "%red%[!] Unknown distro, please see documentation for unknown distros.%reset%"
      exit "0"
    )
  )
)
alias_workflow
