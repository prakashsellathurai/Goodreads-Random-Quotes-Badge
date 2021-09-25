from flask import Flask,render_template,request


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/getbadge', methods=['GET'])
def getbadge():
    goodReadsUrl = request.args.get('goodReadsUrl')
    return render_template('badge.html',goodReadsUrl=goodReadsUrl)


if __name__ == '__main__':
    app.run(debug=True)