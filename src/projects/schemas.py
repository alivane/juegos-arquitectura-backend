from marshmallow import fields
from src.projects import ma
from src.projects.models import Users, Levels, LevelsByUser, Helmets, HelmetsByUser, Avatars, AvatarsByUser


class UserSchema(ma.SQLAlchemyAutoSchema):
    levels = fields.Nested('LevelsByUserSchema', default=[], many=True)
    helmets = fields.Nested('HelmetsByUserSchema', default=[], many=True)

    class Meta:
        include_fk = True
        model = Users
        load_instance = True
        load_only = ('password', )


class LevelsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Levels
        load_instance = True


class LevelsByUserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        include_fk = True 
        model = LevelsByUser
        load_instance = True

class HelmetsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Helmets
        load_instance = True


class HelmetsByUserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        include_fk = True 
        model = HelmetsByUser
        load_instance = True

class AvatarsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Avatars
        load_instance = True


class AvatarsByUserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        include_fk = True 
        model = AvatarsByUser
        load_instance = True


user_schema = UserSchema()
levels_schema = LevelsSchema()
levels_by_user_schema = LevelsByUserSchema()
helmets_schema = HelmetsSchema()
helmets_by_user_schema = HelmetsByUserSchema()
avatars_schema = AvatarsSchema()
avatars_by_user_schema = AvatarsByUserSchema()