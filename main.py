from flask import Flask
from routes.main import main_bp
from routes.cats import cats_bp
from routes.dogs import dogs_bp

app = Flask(__name__)

app.register_blueprint(main_bp)
app.register_blueprint(cats_bp)
app.register_blueprint(dogs_bp)

if __name__ == '__main__':
    app.run(debug=True)
