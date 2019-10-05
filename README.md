
# COMMANDS 
docker-compose up -d
docker ps -a
docker-compose stop  
docker-compose rm -f  
docker-compose stop && docker-compose rm -f  

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

# TODO
* workout volumes logic  
* Configure Shiny server in R image  
* APISTAR ; support for API calls  
* Airflow ; DAG for scheduling tasks; cron on steroids  
* Neo4j image  
* Alternative data exploration toos : Metabase, rawgraphs  
* DBeaver image
