from flask import Flask
from routes.prediction_routes import prediction_bp

app = Flask(__name__)

# REGISTER ROUTES
app.register_blueprint(prediction_bp)

# HOME ROUTE
@app.route('/')
def home():
    from flask import render_template
    return render_template('index.html')

# RUN APP
if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )