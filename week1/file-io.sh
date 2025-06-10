#!/bin/bash

# simple take output and input from user 
name="Dhruv Moradiya"

echo "hi i am ${name} what is your name?"

read name2

echo "hi there, my name is ${name2}"

echo "Today is " `date`.

# read from file

read -p "enter the file name:" filename

while read line
do 

echo ${line}

done < ${filename}

<<comment
output:
./file-io.sh 
hi i am Dhruv Moradiya what is your name?
raju
hi there, my name is raju
Today is  Tue 10 Jun 2025 05:35:42 PM IST.
enter the file name:week1.txt
Web app deployment basics (Week - 1)

sh/bash/python/node scripting todo file io operations
- Task done as per understanding check file-io.sh

​systemctl basics
-​ Create new service
-​ Add service to auto restart
- Task Done check service-script.sh and install.service

comment