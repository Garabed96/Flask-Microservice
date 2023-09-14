from flask import Flask, jsonify, render_template, request
from random import choice
from flask import jsonify
from flask_cors import CORS
from models import db, User, Cafe
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

with app.app_context():
    db.init_app(app)
    db.create_all()

@app.route("/")
def home():
    print()
    return render_template("index.html")

@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    updated_cafe = db.session.query(Cafe).filter_by(id=cafe_id) .first()
    if updated_cafe:
        new_price = request.args.get("new_price")
        updated_cafe.coffee_price = new_price
        return jsonify(response={"success": "Successfully updated the price."})
    else:
        return jsonify(error={"Not Found": "Sorry, a cafe with that id was not found."})



# Get user by id Number
@app.route("/users/<int:id>", methods=["GET"])
def get_user_by_id(id):
    user = db.session.query(User).filter_by(id=id).first()
    if user:
        new_user = request.args.get("new_user")
        return jsonify(user=user.to_dict())
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a user with that id."})

# GET data from the form and Update user information by id Number
@app.route("/update/<int:id>", methods=["GET", "PATCH"])
def update_user(id):
    user = db.session.query(User).filter_by(id=id).first()
    if user:
        new_name = request.get_json().get("name")
        if new_name:
            user.name = new_name
            db.session.commit()
            return jsonify(response={"success": "Successfully updated the name."})
        else:
            return jsonify(error={"Bad Request": "No name provided."})
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a user with that id."})

# DELETE a user based of their id number
@app.route("/delete/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = db.session.query(User).filter_by(id=id).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify(response={"success": "Successfully deleted the user."})
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a user with that id."})

@app.route("/all")
def all_users():
    users = db.session.query(User).all()
    return jsonify(users=[user.to_dict() for user in users])

# Route for all the users
@app.route("/adduser", methods=["GET", "POST"])
def create_new_user():
    data = request.get_json()
    if data:
        new_user = User(
            email=data.get("email"),
            name=data.get("name"),
            password=data.get("password"),
            membership_status=data.get("membership_status"),
            weight_value=data.get("weight_value"),
            weight_unit=data.get("weight_unit"),
            height_value=data.get("height_value"),
            height_unit=data.get("height_unit"),
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully"}), 201
    else:
        return jsonify({"error": "Invalid JSON data"}), 400
@app.route("/add", methods=["GET", "POST"])
def post_new_cafe():
    cafes = db.session.query(Cafe).all()
    cafe_length = len(cafes)
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        has_sockets=bool(request.form.get("sockets")),
        can_take_calls=bool(request.form.get("calls")),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# Random user
@app.route("/random_user")
def random():
    user = choice(User.query.all())
    return jsonify(user.to_dict())


@app.route("/search")
def location():
    query_location = request.args.get("loc")
    cafe = db.session.query(Cafe).filter_by(location=query_location).first()
    if cafe:
        return jsonify(cafes=cafe.to_dict())
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
