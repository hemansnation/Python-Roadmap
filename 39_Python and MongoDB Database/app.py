from flask import Flask, render_template
import os

MONGODB_URI = 'mongodb+srv://himanshu:@python-june.m1kdy6d.mongodb.net/?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)

# creating database
db = client.june_python
# creating student collection and document
db.students.insert_one({
    'name':'Anuj',
    'country': 'India',
    'city':'Indore',
    'age': '21'
})

print(client.list_database_names())

app = Flask(__name__)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)