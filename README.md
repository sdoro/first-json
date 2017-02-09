
# First project using JSON

### 01. init

    # make/edit README.md
    echo "*.py[cod]" > .gitignore
    echo "Django==1.10.5" > requirements.txt

### 02. build a virtual environment with django 1.10.5 (and verify it)

    sudo pip install virtualenv
    virtualenv $HOME/.env
    source $HOME/.env/bin/activate
    pip install -r requirements.txt
    pip freeze

### 03. create a project named firstJson (and verify it)

    django-admin.py startproject firstJson
    cd firstJson
    # edit firstJson/settings.py and change ALLOWED_HOSTS
    ./manage.py runserver $IP:$PORT
    firefox https://first-json-sdoro.c9users.io/
