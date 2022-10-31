#!/bin/bash
# installer for TOOLBAR
# DO NOT EDIT THIS SCRIPT

# color variables
red="\e[0;91m"
green="\e[0;92m"
blue="\e[0;94m"
bold="\e[1m"
reset="\e[0m"

function staging {
    # continue prompt
    while true
    do
    read -r -p "This will copy TOOLBAR to your home directory. If you already had TOOLBAR installed, this will reinstall it. Would you like to continue? [Y/n]" input
    case $input in
        [yY][eE][sS]|[yY])
        echo -e "${green}Continuing...${reset}"
        sleep 2
        install=true
        break
        ;;

        [nN][oO]|[nN])
        echo -e "${red}Operation canceled.${reset}"
        break
        exit 0
        ;;

        *)
        echo -e "${red}Invalid input...${reset}"
        ;;

    esac
    done

    # staging
    echo -e "${blue}[*] Staging process...${reset}"
    rm -rf ~/.TOOLBAR
    cd ..
    cp -r TOOLBAR ~/.TOOLBAR
    echo -e "${green}[+] Complete${reset}"
}

function alias_workflow {
    # set up alias workflow
    echo -e "${blue}[*] Setting up alias...${reset}"

    # check if it already exists in bashrc
        # Do it in one command instead of repeating yourself.
        echo "
        export TOOLBAR_PATH=\"~/.TOOLBAR\"
        alias toolbar=\"python3 ~/.TOOLBAR/main.py\"
        " >> ~/.bashrc
    fi

    #check if it already exists in zshrc
    if ! cat ~/.zshrc | grep "TOOLBAR_PATH" > /dev/null; then
        # Do it in one command instead of repeating yourself.
        echo "
        export TOOLBAR_PATH=\"~/.TOOLBAR\"
        alias toolbar=\"python3 ~/.TOOLBAR/main.py\"
        " >> ~/.zshrc
    fi

    echo -e "${green}[+] Completed${reset}"

    # call staging
    staging

    # clean up
    echo -e "${green}[+] Installation Successful"
    echo -e "[+] Please Restart your terminal"
    echo -e "[+] type 'toolbar' launch ToolBar${reset}"
    bash
}

# check if run with sudo
if [ "$EUID" -ne 0 ]; then
    continue
else
    echo -e "${red}Do not run as root. The script will prompt you for root access.${reset}"
    exit 0
fi

# arguments
while [ -n "$1" ]
do
case "$1" in
--help) 
  echo "
        SUPPORTED DISTROS:
        - Debian
            - Parrot
            - Ubuntu
            - Kali
            - Mint
        - Arch
        - Void
        Please see the TOOLBAR README for more infomation:
        https://github.com/SaintsConnor/ToolBar
  "
  exit 0
;;
--unsupported-distro)
    # call alias workflow function
    alias_workflow
    exit 0
;;
esac
shift
done

# check for valid distro (Parrot, Ubuntu, Void, Debian, Arch)
distro=`sudo cat /etc/issue | awk '{print $1;}'`

if [[ "$distro" == "Debian" ]] || [[ "$distro" == "Parrot" ]] || [[ "$distro" == "Ubuntu" ]] || [[ "$distro" == "Linux" ]] || [[ "$distro" == "Kali" ]]; then
    # installing tools for debian
    echo -e "${red}Debian${reset} system detected."
    echo -e "${blue}[*] Installing tools...${reset}"
    sudo apt update
    sudo apt-get install -y python3 python3-pip python-dev
    pip install qrcode
    pip install Cryptography
    pip install googletrans==3.1.0a0
    pip install colorama
    pip install pillow
    pip install numpy
    apt-get install python3-pyftpdlib
    echo -e "${green}[+] Completed${reset}"

elif [[ "$distro" == "Void" ]]; then
    # installing tools for void
    echo -e "${green}Void${reset} system detected."
    echo -e "${blue}[*] Installing tools...${reset}"
    sudo xbps-install -S python3
    pip install qrcode
    pip install Cryptography
    pip install googletrans==3.1.0a0
    pip install colorama
    apt-get install python3-pyftpdlib
    echo -e "${green}[+] Completed${reset}"

elif [[ "$distro" = "Arch" ]]; then
    # installing tools for arch
    echo -e "${blue}Arch${reset} system detected."
    echo -e "${blue}[*] Installing tools...${reset}"
    sudo pacman -Syu
    sudo pacman -S python python-pip
    python3 -m pip install qrcode
    python3 -m pip install Cryptography
    python3 -m pip install googletrans==3.1.0a0
    python3 -m pip install colorama
    apt-get install python3-pyftpdlib

    echo -e "${green}[+] Completed${reset}"

else
    echo -e "${red}[!] Unknown distro, please see documentation for unknown distros.${reset}"
    exit 0
fi

# call alias workflow
alias_workflow
