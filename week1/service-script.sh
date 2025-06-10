<<comment
systemctl nginx service install
it enable means it automatically start when our server is on or restart.
comment

#!/bin/bash
# to check user give output or not
if [ $# -eq 0 ]
then
    echo "Please add service: ./service-script.sh service_name"
    exit
fi    

service_name=$1

sudo apt install ${service_name} -y

sudo systemctl start ${service_name}

sudo systemctl enable ${service_name}

sudo systemctl status ${service_name}

<<comment
Output:
witout add service:

./service-script.sh 

Please add service: ./service-script.sh service_name

with add service:

./service-script.sh nginx

Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
nginx is already the newest version (1.24.0-2ubuntu7.3).
Synchronizing state of nginx.service with SysV service script with /usr/lib/systemd/systemd-sysv-install.
Executing: /usr/lib/systemd/systemd-sysv-install enable nginx
● nginx.service - A high performance web server and a reverse proxy server
     Loaded: loaded (/usr/lib/systemd/system/nginx.service; enabled; preset: enabled)
     Active: active (running) since Tue 2025-06-10 15:30:47 IST; 24min ago
comment