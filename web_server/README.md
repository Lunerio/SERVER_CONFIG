# Web-01 Server config

### Before running the script make sure you have Fabric installed on your machine
- Use this commands:
```
* pip3 uninstall Fabric
* sudo apt-get install libffi-dev
* sudo apt-get install libssl-dev
* sudo apt-get install build-essential
* sudo apt-get install python3.4-dev
* sudo apt-get install libpython3-dev
* pip3 install pyparsing
* pip3 install appdirs
* pip3 install setuptools==40.1.0
* pip3 install cryptography==2.8
* pip3 install bcrypt==3.1.7
* pip3 install PyNaCl==1.3.0
* pip3 install Fabric3==1.14.post1
```

## Usage:
```
Usage: ./main_script <web-01 ip> <web-02 ip> <path_to_pub_key>
```

- Don't run any other script from here because they will run locally.
- This creates a folder in the home directory with some files, but after running it will be deleted.

* This script won't break a working server
* You need to install and configure the mysql server manually
* DO THE FIREWALL CONFIGURATION MANUALLY. CHECK THE PORTS BEFORE LEAVING THE SERVERS!
