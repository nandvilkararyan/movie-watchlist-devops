from flask import Flask, jsonify

app = Flask(__name__)

# Sample movie watchlist data
watchlist = [
    {"id": 1, "title": "Inception", "genre": "Sci-Fi", "year": 2010},
    {"id": 2, "title": "The Dark Knight", "genre": "Action", "year": 2008},
    {"id": 3, "title": "Interstellar", "genre": "Sci-Fi", "year": 2014}
]

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to the Personal Movie Watchlist Tracker API!",
        "routes": {
            "watchlist": "/watchlist",
            "top_pick": "/top-pick",
            "health": "/health"
        }
    })

@app.route("/watchlist")
def get_watchlist():
    return jsonify({
        "total_movies": len(watchlist),
        "movies": watchlist
    })

@app.route("/top-pick")
def top_pick():
    return jsonify({
        "recommendation": watchlist[0],
        "note": "Tonight's featured must-watch movie!"
    })

@app.route("/health")
def health_check():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
