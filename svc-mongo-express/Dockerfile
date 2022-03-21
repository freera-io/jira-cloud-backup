FROM mongo-express:1.0.0-alpha.4

# nc command from netcat-openbsd is used in entrypoint.sh to wait for mongodb
RUN apk add netcat-openbsd

COPY ./entrypoint.sh /entrypoint.sh

# Config.js used to disable logging (too much logs) - comment the following line if you need logging
COPY ./config.js /node_modules/mongo-express/config.js

# MongoDB creates too much logs: change the bottom line to CMD ["mongo-express"] if you want standard behavior
CMD ["sh","-c", "/entrypoint.sh && node --no-warnings --no-deprecation app.js "]