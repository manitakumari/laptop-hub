This is a django-starter template.

PLEASE DON'T COMMIT TO THIS REPO UNLESS ABSOLUTELY REQUIRED.

Clone this repo and modify according to client requirements.
Setup a new git repo for project and change git remote url in .git/config

```
git clone git@bitbucket.org:sakethtech/django-starter.git <PROJECT>
rm -rf .git
git remote add origin git@bitbucket.org:sakethtech/XXXX.git
```

## Setup project
```
cp env/local .env
vim .env
```
Set PROJECT environment variable

Generate secret key from https://www.miniwebtool.com/django-secret-key-generator/

Configure postgres database. Use hard to guess database username and password.

Copy .env to env/local and commit to repo

```
cp .env env/local
git add -f env
git commit
```

## Project Documentation
```
cp .env env/local
source .env
mkvirtualenv -p $(which python3.6) ${PROJECT}
workon ${PROJECT}
pip install -r requirements.txt
# Install custom python packages
# cd src && python setup.py develop && cd - (Optional)
```

### Install frontend packages using yarn
```
yarn --modules-folder app/static/assets
# Add any other frontend packages
# yarn add font-awesome --modules-folder app/static/assets
git add -f yarn.lock
```

## Create database
```
python scripts/createdb.py | sudo -u postgres psql postgres
python manage.py migrate
python manage.py createsuperuser

python manage.py makemigrations (Optional)
python manage.py collectstatic (Optional)
```
