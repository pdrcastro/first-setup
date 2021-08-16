import logging
import getpass
import os


def configureSSH():
    print ('Configure SSH')
    username = getpass.getuser()
    path = ("/Users/{}/.ssh/".format(username))

    file_name = "config"
    fullPathName = os.path.join(path,file_name)
    
    ## user sysadmin default username on ssh connection will be sysadmin
    try:
        file = open(fullPathName, "a")
        file.write("Host *\n"
  	               '  '"AddKeysToAgent yes\n"
  	               '  '"UseKeychain yes\n"
                   '  '"StrictHostKeyChecking no\n"
                   '  '"user sysadmin\n"
  	               '  '"IdentityFile ~/.ssh/{}\n".format(username))
        file.close()
    except ValueError:
        sshError = 'Configure_SSH'
        logging.error("An error occurred at %s", sshError )
