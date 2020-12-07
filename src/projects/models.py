from src.projects import db, bcrypt


class Levels(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    path = db.Column(db.String, nullable=False)

    def __init__(self, **kwargs):
        super(Levels, self).__init__(**kwargs)


class Helmets(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    path_image = db.Column(db.String, nullable=False)
    coins = db.Column(db.Integer, nullable=True)

    def __init__(self, **kwargs):
        super(Helmets, self).__init__(**kwargs)

class Avatars(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    path_image = db.Column(db.String, nullable=False)
    gender = db.Column(db.Integer, nullable=False) ## 0 => masculino, 1 => femenino

    def __init__(self, **kwargs):
        super(Avatars, self).__init__(**kwargs)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=True)
    mail = db.Column(db.String, nullable=False)
    gender = db.Column(db.Integer, nullable=False) ## 0 => masculino, 1 => femenino
    coins = db.Column(db.Integer, nullable=False)
    id_avatar = db.Column(db.Integer, db.ForeignKey(Avatars.id), nullable=True)
    id_helmet = db.Column(db.Integer, db.ForeignKey(Helmets.id), nullable=True)
    helmets = db.relationship('HelmetsByUser', backref='users')
    levels = db.relationship('LevelsByUser', backref='users')

    def __init__(self, **kwargs):
        super(Users, self).__init__(**kwargs)
        self.password = self.generate_password_hash(**kwargs)
    
    def generate_password_hash(self, **kwargs):
        if 'password' in kwargs:
            return bcrypt.generate_password_hash(kwargs['password']).decode()

        return None


class LevelsByUser(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer, db.ForeignKey(Users.id), nullable=False)
    id_level = db.Column(db.Integer, db.ForeignKey(Levels.id), nullable=False)
    
    def __init__(self, **kwargs):
        super(LevelsByUser, self).__init__(**kwargs)

##### helmets

class HelmetsByUser(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer, db.ForeignKey(Users.id), nullable=False)
    id_helmet = db.Column(db.Integer, db.ForeignKey(Helmets.id), nullable=False)
    
    def __init__(self, **kwargs):
        super(HelmetsByUser, self).__init__(**kwargs)


##### avatar
class AvatarsByUser(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer, db.ForeignKey(Users.id), nullable=False)
    id_avatar = db.Column(db.Integer, db.ForeignKey(Avatars.id), nullable=False)
    
    def __init__(self, **kwargs):
        super(AvatarsByUser, self).__init__(**kwargs)
