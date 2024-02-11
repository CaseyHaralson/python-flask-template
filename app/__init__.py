from flask import Flask
app = Flask(__name__)

from app.api import api
app.register_blueprint(api)

if __name__ == '__main__':
    import os
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
