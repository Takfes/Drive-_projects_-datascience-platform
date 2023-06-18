## Resources

* [Youtube Video](https://www.youtube.com/watch?v=bl1XSZy11vQ&list=WL&index=58&t=1295s) PyCon.DE 2018: Building Your Own Data Science Platform With Python & Docker - Joshua Görner
  
### Docker Compose
* docker-compose up -d
* docker ps -a
* docker-compose stop  
* docker-compose rm -f  
* docker logs container_name
* [more docker compose commands](https://www.thegeekstuff.com/2016/04/docker-compose-up-stop-rm/)

### Docker Volumes
* docker volume prune
* docker volume ls --help
* docker volume ls
* docker volume create --name DockerShare
* docker volume inspect DockerShare
* docker volume rm DockerShare

### Docker Exect
* docker exec -it minio /bin/sh
* docker exec -it jupyter /bin/sh  
* jupyter notebook list  
