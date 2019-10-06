
# PYMONGO
# https://www.mongodb.com/blog/post/getting-started-with-python-and-mongodb
from pymongo import MongoClient
client = MongoClient('mongodb://%s:%s@127.0.0.1' % ('root', 'example'))
client.list_database_names()

# Issue the serverStatus command and print the results
db = client.business
serverStatusResult=db.command("serverStatus")
print(serverStatusResult)

# CREATE DATA AND INSERT TO DATABASE
from random import randint
#Step 1: Connect to MongoDB - Note: Change connection string as needed
db = client['business']
#Step 2: Create sample data
names = ['Kitchen','Animal','State', 'Tastey', 'Big','City','Fish', 'Pizza','Goat', 'Salty','Sandwich','Lazy', 'Fun']
company_type = ['LLC','Inc','Company','Corporation']
company_cuisine = ['Pizza', 'Bar Food', 'Fast Food', 'Italian', 'Mexican', 'American', 'Sushi Bar', 'Vegetarian']
for x in range(1, 501):#501
    business = {
        'name' : names[randint(0, (len(names)-1))] + ' ' + names[randint(0, (len(names)-1))]  + ' ' + company_type[randint(0, (len(company_type)-1))],
        'rating' : randint(1, 5),
        'cuisine' : company_cuisine[randint(0, (len(company_cuisine)-1))] 
    }
    #
    # print(business)
    #Step 3: Insert business object directly into MongoDB via isnert_one
    result=db.reviews.insert_one(business)
    #Step 4: Print to the console the ObjectID of the new document
    # print('Created {0} of 500 as {1}'.format(x,result.inserted_id))
#Step 5: Tell us that you are done
print('finished creating 500 business reviews')

# Queries
client.list_database_names()
db = client['business']
db.list_collection_names()

# FIND_ONE
db.reviews.find_one({'rating': 5})
a_result = db.reviews.find_one({'rating': 5})
type(a_result)
a_result['name']

# FIND
db.reviews.find({'rating': 2}).count()
for x in db.reviews.find({'rating': 2}):
    print(x)

# FIND ALL {} AND SELECT FIELDS TO RETURN
db = client["business"]
mycol = db["reviews"]
# You are not allowed to specify both 0 and 1 values in the same object
# (except if one of the fields is the _id field). If you specify a field with the value 0, all other fields get the value 1, and vice versa:
# for x in mycol.find({'rating': 2},{ "_id": 0, "name": 1 , "cuisine": 1}):
for x in mycol.find({},{ "_id": 0, "name": 1 , "cuisine": 1}):
  print(x)

# INSERT ONE
new_observation = { "name": "Vlaxos", "rating": "5", "cuisine" : 'Greek' }
x = db.reviews.insert_one(new_observation)
print(x.inserted_id)

# INSERT MULTIPLE
mycol = db['reviews']
mylist = [
  { "name": "Acropolis"      , "rating": 5 , "cuisine": "Greek"  },
  { "name": "Papiri Poopiri" , "rating": 5 , "cuisine": "Italian"},
  { "name": "La Pizzarela"   , "rating": 5 , "cuisine": "Italian"},
  { "name": "Lecabetus"      , "rating": 5 , "cuisine": "Greek"  },
]

x = mycol.insert_many(mylist)
print(x.inserted_ids)

# QUERY
db = client["business"]
mycol = db["reviews"]

# example queries
myquery = { "name": { "$lt": "K" } }
myquery = { "name": { "$eq": "Acropolis" } }
myquery = { "name": { "$regex": "^V" } }

myquery = { "name": { "$lt": "K" } ,
            "name": { "$gt": "D" }
           }

# execute query
mydoc = mycol.find(myquery)
for x in mydoc:
  print(x)


# SELECT FILTER SORT QUERY
myfilter = { "name": { "$lt": "K" } ,
             "name": { "$gt": "D" }
           }
myselection = { "_id": 0, "name": 1 , "cuisine": 1}

mycol.find(myfilter,myselection).count()

for x in mycol.find(myfilter,myselection).sort("name",-1):
  print(x)


# AGGREGATION
stargroup=db.reviews.aggregate(
# The Aggregation Pipeline is defined as an array of different operations
[
# The first stage in this pipe is to group data
{ '$group':
    { '_id': "$rating",
     "count" : 
                 { '$sum' :1 }
    }
},
# The second stage in this pipe is to sort the data
{"$sort":  { "_id":1}
}
# Close the array with the ] tag             
] )
# Print the result
for group in stargroup:
    print(group)



# MONGO ENGINE
# https://www.youtube.com/watch?v=PO-z4nwdMUs&t=62s
from mongoengine import connect, Document, fields, disconnect
# connect('testdb')
connect(
    'testdb',
    host = '127.0.0.1',
    port = 27017,
    username = 'root',
    password = 'example'
    )

# Display an image
my_image = open('./images/dog.jpg','rb')
from IPython.display import Image
Image(my_image.read())

class User(Document):
    meta = {'collection':'my_users'}
    username = fields.StringField(required=True)
    profile_image = fields.ImageField(thumbnail_size=(150,150,False))

conny = User(username = 'conny')
conny.profile_image.replace(my_image, filename='conny.jpg')

disconnect()
