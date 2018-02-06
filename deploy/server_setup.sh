#!/usr/bin/env bash

# TODO: Set to URL of git repo.
PROJECT_GIT_URL='https://github.com/baherami/web-shop-backend.git'

PROJECT_BASE_PATH='/usr/local/apps'
VIRTUALENV_BASE_PATH='/usr/local/virtualenvs'

# Set Ubuntu Language
locale-gen en_GB.UTF-8

# Install Python, SQLite and pip
apt-get update
apt-get install -y python3-dev sqlite python-pip supervisor nginx git

# Upgrade pip to the latest version.
pip install --upgrade pip
pip install virtualenv

mkdir -p $PROJECT_BASE_PATH
git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH/web-shop-backend

mkdir -p $VIRTUALENV_BASE_PATH
virtualenv --python=python3 $VIRTUALENV_BASE_PATH/web_shop_backend

source $VIRTUALENV_BASE_PATH/profiles_api/bin/activate
pip install -r $PROJECT_BASE_PATH/web-shop-backend/requirements.txt

# Run migrations
cd $PROJECT_BASE_PATH/web-shop-backend/src

# Setup Supervisor to run our uwsgi process.
cp $PROJECT_BASE_PATH/web-shop-backend/deploy/supervisor_profiles_api.conf /etc/supervisor/conf.d/profiles_api.conf
supervisorctl reread
supervisorctl update
supervisorctl restart web_shop_backend

# Setup nginx to make our application accessible.
cp $PROJECT_BASE_PATH/web-shop-backend/deploy/nginx_webshop_app.conf /etc/nginx/sites-available/web_shop_backend.conf
rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/web_shop_backend.conf /etc/nginx/sites-enabled/web_shop_backend.conf
systemctl restart nginx.service

echo "DONE! :)"