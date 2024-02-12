import uuid


# we need a callable to generate a default value that isn't repeated
# https://github.com/marshmallow-code/marshmallow/issues/2156
def uuid4_str():
    return str(uuid.uuid4())
