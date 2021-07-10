# djntra

# Install

```
python3 -m venv djntra-env
cd djntra-env/
. bin/activate
pip install -U pip wheel
pip install -e git+ssh://git@github.com/guettli/djntra.git#egg=djntra
cp src/djntra/.env.example src/djntra/.env
echo '. $VIRTUAL_ENV/src/djntra/.env' >> bin/activate
echo 'export $(cut -d= -f1 $VIRTUAL_ENV/src/djntra/.env)' >> bin/activate

. bin/activate

# You need to have PostgreSQL installed
# Create user "djntra" with password "djntra":
sudo runuser -u postgres -- createuser -s -P djntra

createdb $PGDATABASE
manage.py migrate
```

The migration create a user "anonymous" (for not authorized users) and "admin" (with password "admin").

# Naming convention

See: https://github.com/guettli/django-htmx-fun

# Guidelines

See: https://github.com/guettli/programming-guidelines

