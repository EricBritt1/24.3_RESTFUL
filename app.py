"""Flask app for Cupcakes"""
from flask import Flask, request, render_template, flash, session, jsonify
from models import db, connect_db, Cupcake


app = Flask(__name__)
app.app_context().push()

app.config ['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcake'
app.config ['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config ['SECRET_KEY'] = "chickenzarecool21837"
11



connect_db(app)

@app.route('/')
def home_page():
    return render_template('base.html')

@app.route('/api/cupcakes', methods = ['GET'])
def all_cupcakes():
    all_cupcakes = [cupcake.serialization() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=all_cupcakes)

@app.route('/api/cupcakes/<int:cupcake_id>', methods = ['GET'])
def one_cupcake(cupcake_id):
    one_cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=one_cupcake.serialization())

@app.route('/api/cupcakes', methods = ['POST'])
def create_cupcake():
    new_cupcake = Cupcake(flavor=request.json['flavor'], size=request.json['size'], rating=request.json['rating'], image=request.json['image'])
    db.session.add(new_cupcake)
    db.session.commit()
    response = jsonify(cupcake=new_cupcake.serialization())

    return(response, 201)

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['PATCH'])
def edit_cupcake(cupcake_id):
    cupcake_to_edit = Cupcake.query.get_or_404(cupcake_id)

    cupcake_to_edit.flavor = request.json.get('flavor', cupcake_to_edit.flavor)
    cupcake_to_edit.size = request.json.get('size', cupcake_to_edit.size)
    cupcake_to_edit.rating = request.json.get('rating', cupcake_to_edit.rating)
    cupcake_to_edit.image = request.json.get('image', cupcake_to_edit.image)

    db.session.add(cupcake_to_edit)
    db.session.commit()

    return jsonify(cupcake=cupcake_to_edit.serialization())

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['DELETE'])
def delete_cupcake(cupcake_id):
    cupcake_to_delete = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake_to_delete)
    db.session.commit()

    return jsonify(message="Deleted")