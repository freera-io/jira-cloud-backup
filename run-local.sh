sudo find ./data-mongo/ | sudo xargs rm -rf
docker rm -f $(docker ps -a -q)
docker network rm $(docker network ls -q)
export IP_ADDRESS=$(ip addr show | grep "\binet\b.*\bdocker0\b" | awk '{print $2}' | cut -d '/' -f 1)
docker-compose up --build
