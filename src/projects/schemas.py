from src.projects import ma
from src.projects.models import Users


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Users
        load_instance = True
        load_only = ('password', )


user_schema = UserSchema()