#!/bin/bash
echo "Waiting for MongoDB..."
while ! nc -z $MONGO_SERVER $MONGO_PORT; do
  sleep 0.1
done
echo "Mongodb is alive. Ready to use it."




