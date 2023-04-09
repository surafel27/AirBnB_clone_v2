#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment

if ! hash nginx;
then
    sudo apt-get update -y
    sudo apt-get install nginx -y
fi
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared/
$fake_html="<html><heade></heade><body><h1> Test My Nginx configuration</h1></body></html>"
echo "$fake_html" >> /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "/^\tlocation \/ {$/ i\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}" /etc/nginx/sites-available/default
sudo service nginx restart
