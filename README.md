
# COMMANDS
docker-compose up -d
docker ps -a
docker-compose stop  
docker-compose rm -f  

> https://www.thegeekstuff.com/2016/04/docker-compose-up-stop-rm/

# DEBUGGING
docker logs container_name

# JUPYTER NOTEBOOK CONTAINER
### Access token
docker exec -it jupyter /bin/sh  
jupyter notebook list  
exit  

# MINIO CONTAINER
docker exec -it minio /bin/sh

# VOLUMES
docker volume prune
docker volume ls --help
docker volume ls
docker volume create --name DockerShare
docker volume inspect DockerShare
docker volume rm DockerShare

# TODO
* Airflow ; DAG for scheduling tasks; cron on steroids  
* APISTAR ; support for API calls  
* Alternative data exploration toos : Metabase, rawgraphs  
