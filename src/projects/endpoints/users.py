from datetime import datetime
import jwt
import operator
from functools import wraps
from flask import request, jsonify, Blueprint, current_app
from src.projects import db, bcrypt
from src.projects.models import (
    Users, Levels, LevelsByUser, Avatars, Helmets,
    HelmetsByUser
)
from src.projects.schemas import (
    user_schema, levels_schema, levels_by_user_schema, 
    helmets_schema, avatars_schema, helmets_by_user_schema
)
import marshmallow


blueprint = Blueprint('users', __name__)


def check_token():
    authorization = request.headers.get('Authorization')

    if authorization is None:
        return False

    split_auth = authorization.split(' ')

    if len(split_auth) != 2:
        return False

    if split_auth[0] != 'Bearer':
        return False

    token = split_auth[1]

    try:
        token = jwt.decode(token, current_app.config['SECRET'])
        return token
    except:
        return False

def authentificater(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        check_response = check_token()

        if check_response is False:
            return 'Unauthorized', 401

        return f(check_response, *args, **kwargs)

    return wrapper


@blueprint.route('/register', methods=['POST'])
@blueprint.route('/users', methods=['POST'])
def register():
    user = user_schema.load(request.json)

    db.session.add(user)
    db.session.commit()

    return user_schema.dump(user), 201


@blueprint.route('/users', methods=['GET'])
@authentificater
def list_users(payload):
    users = Users.query.all()

    return jsonify(user_schema.dump(users, many=True)), 200


@blueprint.route('/users/<id>', methods=['GET'])
@authentificater
def view_user(payload, id):
    if str(payload['sub']) != str(id):
        return 'Forbidden', 403

    user = Users.query.get_or_404(id)
    return user_schema.dump(user), 200


@blueprint.route('/update_user/<id>', methods=['PUT'])
@authentificater
def update_user(payload, id):
    user = Users.query.get_or_404(id)
    user = user_schema.load(
        data=request.json,
        instance=user,
        partial=False
    )
    db.session.add(user)
    db.session.commit()

    return user_schema.dump(user), 200


@blueprint.route('/users/<id>', methods=['PATCH'])
@authentificater
def patch_user(payload, id):
    user = Users.query.get_or_404(id)
    user = user_schema.load(
        data=request.json,
        instance=user,
        partial=True
    )

    db.session.add(user)
    db.session.commit()

    return user_schema.dump(user), 200


@blueprint.route('/users/<id>', methods=['DELETE'])
@authentificater
def delete_user(payload, id):
    user = user.query.get_or_404(id)

    db.session.delete(user)
    db.session.commit()

    return '', 204


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    data = request.get_json()
    mail = data.get('mail')
    password = data.get('password')

    user = Users.query.filter_by(mail=mail).first()

    if user is None:
        return 'Not found', 404


    if bcrypt.check_password_hash(user.password, password) is False:
        return 'Not Found', 404

    payload = {
        'sub': user.id,
        'name': user.name,
        'iat': datetime.now()
    }

    return jwt.encode(
        payload,
        current_app.config['SECRET'],
        algorithm='HS256'
    )

@blueprint.route('/token', methods=['GET'])
@authentificater
def user(payload):
    user = Users.query.get_or_404(payload['sub'])
    
    return user_schema.dump(user), 200


@blueprint.route('/levels', methods=['GET'])
@authentificater

def list_levels(payload):
    levels = Levels.query.all()

    return jsonify(levels_schema.dump(levels, many=True)), 200


@blueprint.route('/levels_register', methods=['POST'])
def levels_register():
    levels = levels_schema.load(request.json)

    db.session.add(levels)
    db.session.commit()

    return levels_schema.dump(levels), 201


@blueprint.route('/levels_by_user/<id>', methods=['GET'])
@authentificater
def list_levels_by_user(payload, id):
    if str(payload['sub']) != str(id):
        return 'Forbidden', 403

    levelsbyuser = LevelsByUser.query.filter_by(id_user=id)

    return jsonify(levels_by_user_schema.dump(levelsbyuser, many=True)), 200


@blueprint.route('/avatars/<gender>', methods=['GET'])
@authentificater
def list_avatars_by_gender(payload, gender):
    avatars = Avatars.query.filter_by(gender=gender)

    return jsonify(avatars_schema.dump(avatars, many=True)), 200


@blueprint.route('/avatar/<id>', methods=['GET'])
@authentificater
def get_avatars(payload, id):
    avatars = Avatars.query.filter_by(id)

    return jsonify(avatars_schema.dump(avatars, many=True)), 200


@blueprint.route('/avatars_register', methods=['POST'])
def avatars_register():
    avatars = avatars_schema.load(request.json)

    db.session.add(avatars)
    db.session.commit()

    return avatars_schema.dump(avatars), 201

@blueprint.route('/helmets', methods=['GET'])
@authentificater
def list_helmets(payload):
    helments_response = Helmets.query.all()

    return jsonify(helmets_schema.dump(helments_response, many=True)), 200


@blueprint.route('/helmets_register', methods=['POST'])
def helmets_register():
    helmets = helmets_schema.load(request.json)

    db.session.add(helmets)
    db.session.commit()

    return helmets_schema.dump(helmets), 201


@blueprint.route('/helmets_by_user_register', methods=['POST'])
def helmets_by_user_register():
    helmets = helmets_by_user_schema.load(request.json)

    db.session.add(helmets)
    db.session.commit()

    return helmets_by_user_schema.dump(helmets), 201


@blueprint.route('/helmets_by_user/<id>', methods=['GET'])
@authentificater
def helmets_by_user(payload, id):
    if str(payload['sub']) != str(id):
        return 'Forbidden', 403

    data = HelmetsByUser.query.filter_by(id_user=id)

    return jsonify(helmets_by_user_schema.dump(data, many=True)), 200


@blueprint.route('/levels_by_user_register', methods=['POST'])
def levels_by_user_register():
    data = levels_by_user_schema.load(request.json)

    db.session.add(data)
    db.session.commit()

    return levels_by_user_schema.dump(data), 201

