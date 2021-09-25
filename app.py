from flask import Flask,render_template,request, abort, jsonify,Markup
from io import StringIO

app = Flask(__name__)



@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


    
@app.route('/getbadge', methods=['GET'])
def getbadge():
    try:
        goodReadsProfileUrl = request.args.get('goodReadsUrl')  
        goodReadsprofileId = goodReadsProfileUrl.split('/')[-1]
        goodReadsQuotesUrl = "https://www.goodreads.com/quotes/widget/" +goodReadsProfileUrl.split('/')[-1]+ "?v=2"
         
        return render_template('badge.svg',goodReadsProfileUrl=goodReadsProfileUrl,goodReadsQuotesUrl=goodReadsQuotesUrl)


    except Exception as e:
        print(e)
        abort(404, description="Resource not found")



if __name__ == '__main__':
    app.run(debug=True)