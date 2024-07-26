from app import app
from flask_static_digest import FlaskStaticDigest

flask_static_digest = FlaskStaticDigest(app)

if __name__ == '__main__':
    flask_static_digest.digest()
