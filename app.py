@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to the Events API"
    })