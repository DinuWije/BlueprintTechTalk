from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    user = request.args.get('user')
    term = request.args.get('term')
    if not term and not user:
        return 'This is a simple API!'
    return (f'{user} is in term {term}')

if __name__ == "__main__":
    app.run(debug=True)