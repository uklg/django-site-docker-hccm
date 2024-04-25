you can set up a Django environment in Docker using ./build 

To use whitenoise (Production handling of static files and caching as such in code)  /admin with css works with debug but not with debug off the css files are missing

To get the admin css  for the staticfiles/admin you can:

./build 

attach to latest container

cp -pr /usr/local/lib/python3.8/site-packages/django/contrib/admin/static/admin /app/staticfiles/

Now these files can be added to the admin and added to git locally as they are in the repo now

aws.env is needed  in root is needed for emails
