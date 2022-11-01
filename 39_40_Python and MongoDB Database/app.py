from flask import Flask, render_template
import os

MONGODB_URI = 'mongodb+srv://himanshu:him12345@python-june.m1kdy6d.mongodb.net/?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)

# creating database
db = client.june_python
# creating student collection and document
# db.students.insert_one({
#     'name':'Anuj',
#     'country': 'India',
#     'city':'Indore',
#     'age': '21'
# })

#  CRUD - Create Read Update Delete

# inserting multiple values

students = [
    {'name': 'Dev', 'country': 'India', 'city': 'Indore', 'age': 34},
    {'name': 'Rohit', 'country': 'India', 'city': 'Indore', 'age': 24},
    {'name': 'Ravi', 'country': 'USA', 'city': 'Boston', 'age': 41},
]

for student in students:
    db.students.insert_one(student)


# Read - Find

student = db.students.find_one()
print(student)  #  { '_id': ObjectId('4545y43jb4892y3324y932') 'name': 'Dev', 'country': 'India', 'city': 'Indore', 'age': 34}       

db = client['june_python']

student = db.students.find_one({'_id': ObjectId('4545y43jb4892y3324y932')})
print(student)


# find

db = client['june_python']

students = db.students.find()
for student in students:
    print(student)

# find with query/condition


db = client['june_python']

# query = {
#     'country': 'USA',
#     'city':'Boston'
# }
query = {
    'age': {'$gt': 25}
}

students = db.students.find(query)
for student in students:
    print(student)

#  limits

db.students.find().limit(3) # 3 documents/rows

# sort
db.student.find().sort('name')



# update

query = {'age': 250}
new_value = {'$set': {'age':30}}

db.students.update_one(query, new_value)

for student in db.students.find():
    print(student)




# delete

query = {
    'name': 'Dev'
}

db.students.delete_one(query)

for student in db.students.find():
    print(student)


#  drop the collection

db.students.drop()








print(client.list_database_names())

app = Flask(__name__)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)