# display variable
working_dir= path/to/app-dir
branch= main
App_name= node-app

# change dir for out app dir 
cd ${working_dir} || exit
echo "change directory to ${working_dir}"

# to pull new code from github repo on main branch
git pull origin ${branch}
echo "pull code from ${branch}"

# install new dependency for related node js app
npm install 
echo "install npm dependency"

# using pm2 reload our app 
pm2 reload ${App_name}
echo "reload node js app name: ${App_name}"

# use to see status of pm2 node app
pm2 status ${App_name}
echo "Display of app status: ${App_name}"

echo "deployment is successful our ${App_name}"
