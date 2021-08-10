#!/bin/sh

source venv/bin/activate

if [ ! -d /data/images/ ]; then
  mkdir /data/images/
  echo Making images folder
else
  echo Ok. Images folder found
fi

if [ ! -f /data/app.db ]; then
  cp ./app.db /data/
  echo Empty database. Copying basic app.db
else
  echo Ok. Database file found
fi

if [ -f ./app.db ]; then
  rm ./app.db
  echo Removing app.db file from current directory.
fi

if [ ! -d /data/migrations ]; then
  echo No migrations folder.
  rm -rf ./migrations
  flask db init
  DATABASE_URL=sqlite:/// flask db migrate -m "First setup"
  flask db stamp head
  #flask db upgrade
  
else
  rm -rf ./migrations
  cp -r /data/migrations/ .
  echo Ok. Migrations folder found
fi

echo Getting ready...
sleep 1
flask db migrate -m "Some Tables have changed"
sleep 1
flask db upgrade
sleep 1

rm -rf /data/migrations
cp -r ./migrations /data/

cp -r /data/images/ ./app/static/

export START_FLAG="True"

echo Starting server...

exec gunicorn -b :3000 --access-logfile - --error-logfile - project:app


