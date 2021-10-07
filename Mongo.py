import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://jongee:Gorriceta@cluster1.rfwdq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["istudy"]
collection = db["course"]

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

def statuschk():
    a1 = input("Which class do you want to check on?: ")
    x = collection.find_one({},{"_id":0,"course":0,"credits":0})
    print(x)
    if x == 1:
        print(f"{a1} is in progress.")
    elif x == 0:
        print(f"{a1} is not started.")


a1 = input("What would you like to do?: ")
if a1 == "update":
    updatestat()
elif a1 == "create":
    addclass()
elif a1 == "check":
    statuschk()
else:
    pass