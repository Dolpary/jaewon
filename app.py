from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:test@cluster0.wgehy8y.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name' : name_receive,
        'comment' : comment_receive
    }

    db.orders.insert_one(doc)

    return jsonify({'msg':'팬명록 저장완료!!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    orders_list = list(db.orders.find({}, {'_id': False}))

    return jsonify({'orders':orders_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)

@app.route("/homework", methods=["GET"])
def homework_get():
    pans_list = list(db.pans.find({}, {'_id': False}))
    return jsonify({'pans':pans_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)