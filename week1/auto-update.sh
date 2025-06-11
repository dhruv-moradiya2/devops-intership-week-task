<<comment

this script do daily update on provide crontab time 

comment

#!/bin/bash

sudo apt-get update -y

sudo apt-get upgrade -y

sudo apt autoremove -y

sudo apt autoclean -y

# at 5 am every day update using script
# 0 5 * * * /home/dhruv-moradiya/Devops-intern/devops-intership-week-task/week1/auto-update.sh
