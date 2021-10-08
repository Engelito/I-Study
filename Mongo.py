import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://jongee:Gorriceta@cluster1.rfwdq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["istudy"]
collection = db["course"]
# Angel if you could take this function block and link it to the 'add course' button on the page that would be great
# I just need you to fix the variables so that they take the input from the entry boxes on the front of the page
# *** Delete course function coming soon
def addclass():
    a1 = input("what course are you taking?: ")
    a2 = int(input("How many credits is it?: "))

    entry = {"course": a1, "credits": a2,"status":0 }
    collection.insert_one(entry)
    print("Database Updated")

    for x in collection.find({},{"_id":0}):
        print(x)
def updatestat():
    a1 = input("What course would you like to update?: ")
    targ = { "course": a1 }
    newvalues = { "$set": { "status":1 } }
    collection.update_one(targ,newvalues)
    for x in collection.find({},{"_id":0}):
        print(x)
# 'statuschk' shows you the order the data is presented in a dict and it's the same when you convert it to a list
def statuschk():
    x = collection.find({},{"_id":0})
    for row in x:
        print(row)

# Luis, this looptest function returns a looped list of the courses and their status.
# The code below takes the MongoDB cursor object, converts it to a list, and then indexes the list to return the 'status' value.
# You can add this to your page and I need you to make it so that it loops through all the classes and shows the courses you're taking on the boxes
# to access a specific value you just need to index the list, 'vallist[0]' should return the course code from the dataset.
def looptest():
    for x in collection.find({},{"_id":0}):
        y = x.values()
        vallist = list(y)
        if vallist[2] == 0:
            print(f"Course: {vallist[0]} | Progress: Not Started")
        elif vallist[2] == 1:
            print(f"Course: {vallist[0]} | Progress: In Progress")
        else:
            pass

a1 = input("What would you like to do?: ")
if a1 == "update":
    updatestat()
elif a1 == "create":
    addclass()
elif a1 == "check":
    statuschk()
elif "loop" in a1:
    looptest()
else:
    pass