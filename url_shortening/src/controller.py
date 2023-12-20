from flask import Flask, redirect, request,jsonify

from .url_shortener import NotFoundError, URLShortener

app = Flask(__name__)

urlShortener = URLShortener()

@app.route('/shorten',methods=['POST'])
def shorten(): 
    #INFO:how to get the URL from the request body.
    url = request.form.get('url')
    if url not in urlShortener.hash.values():
        short_code=urlShortener.main(url)
    else:
        return "url already exists",200
    #TODO: to tackle the situation when the same URL is sent again
    return jsonify(short_code),200#redirect(f'/long_url/{short_code}', code=302)
    

@app.route('/long_url/<short_code>')
def redirect_to_original(short_code):
    try:
        original_url = urlShortener.get_shortened_url_mapping(short_code)
        return jsonify(original_url),200#redirect(original_url, code=302)
    except NotFoundError as e:
        return jsonify(str(e)),404
    

@app.route('/remove/<short_code>',methods=['DELETE'])
def delete_short_code(short_code):
    # TODO: i don't want to show the b
    if short_code in urlShortener.hash:
        urlShortener.hash.pop(short_code)
        return 204
    else:
        return 404
        
    

#? when to do we use 301 and 302 statuscode?
#? what helps when we have to return key based on the values.
#? how do we better use the redirect function in flask? my code is buggy?

if __name__ == '__main__':
    app.run(debug=True)