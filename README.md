# Web Stack config scripts

## load_balancer
This script does the following:
- Creates a temp folder in which we upload some needed files
- Copies the holberton key (from 0x0B-SSH Task 3) to the authorized_keys file
- Installs HAProxy and makes the basic configuration with our two servers
- For the SSL certificate follow the instructions in this [link](https://www.digitalocean.com/community/tutorials/how-to-secure-haproxy-with-let-s-encrypt-on-ubuntu-14-04)

* For more information go to the README from the load_balancer folder
* DO THE FIREWALL CONFIGURATION MANUALLY. CHECK THE PORTS BEFORE LEAVING THE SERVERS!

## web_server
This script does the following:
- Creates a temp folder in which we upload some needed files
- Copies the holberton key (from 0x0B-SSH Task 3) to the authorized_keys file
- Installs NginX and makes the basic configuration within our two servers
* For more information go to the README from the web_server folder
* DO THE FIREWALL CONFIGURATION MANUALLY. CHECK THE PORTS BEFORE LEAVING THE SERVER
