import os

from validations import validate_api

from flask import Flask, request, jsonify, render_template, redirect

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

# Стартовая страница входа
@app.route('/', methods=["GET"])
def login():
    try:
        if request.method == "GET":
            apikey = request.cookies.get("apikey")
            if not apikey:
                return render_template("index.html")
            else:
                return redirect(f"/{apikey}/v1/storage")

        return jsonify({
            "message": "method is not allowed"
        }), 400
    except Exception as e:
        pass

@app.route('/<api>/v1/storage')
def storage(api: str):
    if not validate_api(api):
        return jsonify({
            "message": "Access forbidden"
        }, 403)
    return render_template("storage.html")

def main():
    pass

if __name__ == "__main__":
    main()
    app.run(host="0.0.0.0", port=80, debug=True)
