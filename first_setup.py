#from olx_software import installAWSOKTA
from configs import configureSSH
import os
import logging


software = (
    #Install homebrew
    "/bin/bash -c '$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)'",

    #Install Git
    "brew install git",

    #Install Virtualenv
    "sudo chown -R $(whoami) /usr/local/share/zsh /usr/local/share/zsh/site-functions",
    "chmod u+w /usr/local/share/zsh /usr/local/share/zsh/site-functions",

    #Install PIP3
    "curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py",
    "python3 get-pip.py",

    #Install Zsh
    "brew install zsh",

    #Install Zsh Framework
    "sh -c '$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)'",
    
    #Install AWS CLI
    "curl 'https://awscli.amazonaws.com/AWSCLIV2.pkg' -o 'AWSCLIV2.pkg'",
    "sudo installer -pkg AWSCLIV2.pkg -target /",

    #Install JAVA
    "brew install java11",

    #Install K8s Tools
    "brew install k9s",
    "brew install kubectx",
    "brew install kubectl"
)

def installSoftware():
    print('Start software installation......')
    
    try:
       for i, x in enumerate(software):
           logging.info("{}. RUNNING: [{}]".format(i,x))
           os.system(x)
    except ValueError:
        installSoftwareError = 'Install_Software'
        logging.error("An error occurred at %s", installSoftwareError )   

def main ():
    logging.basicConfig(filename='first_setup.log', level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
    logging.info('Start Software Installation')
    installSoftware()
    logging.info('Start SSH Configuration')
    configureSSH()
    logging.info('Cloning SSH Olx Repo')

if __name__ == "__main__":
    main()