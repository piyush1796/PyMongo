import pymongo as pm

fh = open("Vocabulary_set.csv","r")
wd_list = fh.readlines()

wd_list.pop(0)

vocab_list = []

for raw_data in wd_list:
    word, definition = raw_data.split(',', 1)
    definition = definition.rstrip()
    vocab_list.append({'word': word, 'definition': definition})

#print(vocab_list)

client = pm.MongoClient("mongodb://localhost:27017/")
db = client["vocab"]

dbs = client.list_database_names()

vocab_col = db["vocab_list"]
vocab_col.drop()

vocab_dict = {'word': 'cryptic', 'definition': 'secret with hidden meaning'}
res = vocab_col.insert_one(vocab_dict)
print("inserted_id", res.inserted_id)

if "vocab" in dbs:
    print("Database exists")

res = vocab_col.insert_many(vocab_list)

data = vocab_col.find_one()
print(data)

for document in vocab_col.find({}, {"_id":0}):
    print(document)

upd = vocab_col.update_one({'word': 'boisterous'}, {"$set": { "definition": "rowdy; noisy"}})
print("modified count: ", upd.modified_count)

data = vocab_col.find_one({'word': 'boisterous'})
print(data)