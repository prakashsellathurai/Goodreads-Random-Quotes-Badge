from flask import Flask,render_template,request, abort, jsonify,Markup,make_response
import requests


app = Flask(__name__)

@app.errorhandler(404)
def resource_not_found(e):
    return render_template("404.html"),404

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html'),200

def parse_content(content):
    content = content.decode()
    content = content.replace(r"\n", "")
    content = content[16:].replace('\\','').replace("&ldquo;","").replace("&rdquo;","")
    content = content[:-2].replace("&mdash;"," -  ")
    content = content[:-6]
    content = content.split("</h3>    <br/>")[1]
    content = content[:-8]
    content = content.split(" <br/>  <br/>  ")[0]
    content = content.replace(" -  ","  <br/> <style> #author { text-align: right; }</style>  <div id='author'> -   ")
    content = content + "</div>"
    return content

@app.route('/getbadge', methods=['GET'])
def getbadge():
    try:
        goodReadsProfileUrl = request.args.get('goodReadsUrl')  
        goodReadsprofileId = goodReadsProfileUrl.split('/')[-1]
        goodReadsQuotesUrl = "https://www.goodreads.com/quotes/widget/" +goodReadsProfileUrl.split('/')[-1]
        
        
        content = requests.get(goodReadsQuotesUrl).content
        content = parse_content(content=content)
        
        template =  render_template('badge.svg',content=content,goodReadsQuotesUrl=goodReadsQuotesUrl,goodReadsProfileUrl=goodReadsProfileUrl)

        response = make_response(template)
        response.headers["Content-Type"] = "image/svg+xml"
        response.headers["charset"] = "utf-8"
        response._status_code = 200

        return response

    except Exception as e:
        abort(404, description="Resource not found")


