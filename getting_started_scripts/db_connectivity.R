install.packages("pacman")
library(pacman)
p_load(tidyverse,RPostgreSQL,RSQLite,RODBC,
       dbplyr,dplyr,dbplot,odbc)

drv <- dbDriver("PostgreSQL")
# creates a connection to the postgres database
# note that "con" will be used later in each connection to the database
con <- dbConnect(drv, dbname = "postgres",
                 host = "postgres", port = 5432,
                 user = "postgres", password = "postgres")

src_dbi(con)
dbListTables(con)
dbListFields(con,"iris")

dbWriteTable(con,"mtcars",mtcars,overwrite=TRUE)
# copy_to(con,mtcars,"db_mtcars",indexes=list("cyl"))

dbGetQuery(con,"SELECT * FROM iris where species='virginica'")
dbGetQuery(con,"SELECT count(*) FROM iris where species='virginica'") %>% class()
# dbGetQuery(con,"SELECT * FROM sqlite_stat4")

tbl(con,"mtcars")
iris_db <- tbl(con,"iris")
iris_db %>% class()

iris_db %>% filter(species=="virginica") %>% head()
# this results to an error
iris_db %>% filter(species=="virginica") %>% tail()
iris_db %>% filter(species=="virginica") %>% collect() %>% tail()

iris_db %>% select(sepal_length,sepal_width) %>% filter(species=="virginica") %>% 
  show_query()

dbDisconnect(con)
