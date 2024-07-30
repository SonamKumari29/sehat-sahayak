from flask import Flask, render_template
from heart_disease import heart_bp
from diabetes import diabetes_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(heart_bp, url_prefix='/heart')
app.register_blueprint(diabetes_bp, url_prefix='/diabetes')

@app.route('/')
def main():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
