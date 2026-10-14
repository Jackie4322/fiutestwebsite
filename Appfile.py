from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Bank Statement Parser App</h1><p>Ready to upload files!</p>"

if __name__ == '__main__':
    app.run()
