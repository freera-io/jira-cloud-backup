set -e

mongo <<EOF
use $MONGO_INITDB_DATABASE

db.createUser({
  user: '$MONGO_INITDB_USER',
  pwd: '$MONGO_INITDB_PASSWORD',
  roles: [{
    role: 'readWrite',
    db: '$MONGO_INITDB_DATABASE'
  }]
});

db.createCollection('users');
db.createCollection('issues');
db.createCollection('attachments');
db.createCollection('worklogs');
EOF