import pymongo

#Establish connection
client = pymongo.MongoClient("mongodb://localhost:27017/")
#Switching to university database
mydb = client["university"]
#Switching to Studentdetailscollection
collection = mydb["Studentdetails"]
y = []
def getemail():
    '''Retrieve the emails of the students'''
    for x in collection.find({},{"_id":0,"Name":0,"phno":0}):
        y.append(x["email"])
    return y
def getphonenumber():
    '''Retrieve the Phone numbers of the students'''
    for x in collection.find({},{"_id":0,"Name":0,"email":0}):
        y.append(x["phno"])
    return y
