from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# Sample movie watchlist data
watchlist = [
    {"id": 1, "title": "Inception", "genre": "Sci-Fi", "year": 2010, "rating": "8.8/10"},
    {"id": 2, "title": "The Dark Knight", "genre": "Action", "year": 2008, "rating": "9.0/10"},
    {"id": 3, "title": "Interstellar", "genre": "Sci-Fi", "year": 2014, "rating": "8.7/10"},
    {"id": 4, "title": "Spirited Away", "genre": "Animation", "year": 2001, "rating": "8.6/10"}
]

BASE_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ page_title }} - Movie Watchlist</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
        body { background: #0f172a; color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; }
        header { background: #1e293b; border-bottom: 1px solid #334155; padding: 1.2rem 2.5rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; }
        header h1 { font-size: 1.4rem; color: #38bdf8; display: flex; align-items: center; gap: 10px; }
        nav { display: flex; align-items: center; gap: 1.5rem; }
        nav a { color: #94a3b8; text-decoration: none; font-weight: 500; font-size: 0.95rem; transition: color 0.2s; }
        nav a:hover { color: #38bdf8; }
        .badge-live { background: #10b981; color: white; font-size: 0.75rem; padding: 3px 8px; border-radius: 999px; font-weight: 600; }
        main { flex: 1; max-width: 960px; width: 100%; margin: 2rem auto; padding: 0 1.5rem; }
        .hero { text-align: center; padding: 3.5rem 1.5rem; background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%); border-radius: 16px; border: 1px solid #334155; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.3); }
        .hero h2 { font-size: 2.4rem; margin-bottom: 1rem; color: #f8fafc; }
        .hero p { color: #94a3b8; font-size: 1.15rem; max-width: 620px; margin: 0 auto 1.8rem; line-height: 1.6; }
        .btn-group { display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; }
        .btn { display: inline-flex; align-items: center; gap: 8px; background: #2563eb; color: white; padding: 0.75rem 1.4rem; border-radius: 8px; text-decoration: none; font-weight: 600; font-size: 0.95rem; transition: background 0.2s, transform 0.1s; }
        .btn:hover { background: #1d4ed8; transform: translateY(-1px); }
        .btn-secondary { background: #334155; color: #e2e8f0; }
        .btn-secondary:hover { background: #475569; }
        .pipeline-bar { display: flex; justify-content: center; align-items: center; gap: 0.8rem; margin-top: 2rem; flex-wrap: wrap; font-size: 0.85rem; color: #94a3b8; }
        .pipeline-pill { background: #1e293b; border: 1px solid #334155; padding: 4px 12px; border-radius: 999px; color: #38bdf8; font-weight: 500; }
        .card-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1.5rem; margin-top: 1.5rem; }
        .movie-card { background: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 1.5rem; transition: transform 0.2s, border-color 0.2s; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); }
        .movie-card:hover { transform: translateY(-4px); border-color: #38bdf8; }
        .movie-title { font-size: 1.3rem; font-weight: 700; color: #f1f5f9; margin-bottom: 0.5rem; }
        .tag { display: inline-block; background: #0f172a; color: #93c5fd; font-size: 0.8rem; padding: 4px 10px; border-radius: 6px; margin-right: 6px; font-weight: 500; }
        .rating { color: #facc15; font-size: 0.85rem; font-weight: 600; margin-top: 0.8rem; }
        .featured-banner { background: #f59e0b; color: #78350f; font-size: 0.75rem; font-weight: 800; text-transform: uppercase; padding: 4px 10px; border-radius: 4px; display: inline-block; margin-bottom: 0.8rem; }
        footer { text-align: center; padding: 1.5rem; color: #64748b; font-size: 0.85rem; border-top: 1px solid #1e293b; margin-top: 2rem; }
    </style>
</head>
<body>
    <header>
        <h1>🎬 Personal Movie Watchlist Tracker</h1>
        <nav>
            <a href="/">Home</a>
            <a href="/watchlist">Watchlist</a>
            <a href="/top-pick">Tonight's Pick</a>
            <a href="/health">Health Check <span class="badge-live">Live</span></a>
        </nav>
    </header>
    <main>
        {{ content | safe }}
    </main>
    <footer>
        DevOps Lab Mini-Project &bull; GitHub &bull; Jenkins &bull; Docker &bull; AWS EC2 &bull; Pytest
    </footer>
</body>
</html>
"""

@app.route("/")
def home():
    content = """
    <div class="hero">
        <h2>Organize, Discover & Track Movies</h2>
        <p>A lightweight, cloud-deployed movie watchlist application running on AWS EC2, automated with Jenkins and Docker.</p>
        <div class="btn-group">
            <a href="/watchlist" class="btn">📋 View Watchlist</a>
            <a href="/top-pick" class="btn btn-secondary">⭐ Tonight's Top Pick</a>
            <a href="/health" class="btn btn-secondary">🩺 Health Check</a>
        </div>
        <div class="pipeline-bar">
            <span>DevOps Pipeline:</span>
            <span class="pipeline-pill">GitHub</span> ➔
            <span class="pipeline-pill">Jenkins</span> ➔
            <span class="pipeline-pill">Pytest</span> ➔
            <span class="pipeline-pill">Docker</span> ➔
            <span class="pipeline-pill">AWS EC2</span>
        </div>
    </div>
    """
    return render_template_string(BASE_HTML, page_title="Home", content=content)

@app.route("/watchlist")
def get_watchlist():
    cards_html = "".join([
        f"""
        <div class="movie-card">
            <div class="movie-title">{m['title']}</div>
            <div>
                <span class="tag">{m['genre']}</span>
                <span class="tag">Year: {m['year']}</span>
            </div>
            <div class="rating">⭐ Rating: {m['rating']}</div>
        </div>
        """ for m in watchlist
    ])
    content = f"""
    <div>
        <h2 style="font-size: 1.8rem; margin-bottom: 0.5rem;">📋 My Planned Watchlist</h2>
        <p style="color: #94a3b8; margin-bottom: 1rem;">Total Movies Planned: <strong style="color: #38bdf8;">{len(watchlist)}</strong></p>
        <div class="card-grid">
            {cards_html}
        </div>
    </div>
    """
    return render_template_string(BASE_HTML, page_title="Watchlist", content=content)

@app.route("/top-pick")
def top_pick():
    featured = watchlist[0]
    content = f"""
    <div style="max-width: 600px; margin: 0 auto;">
        <h2 style="font-size: 1.8rem; margin-bottom: 1rem; text-align: center;">⭐ Tonight's Top Pick</h2>
        <div class="movie-card" style="border-color: #f59e0b; padding: 2rem;">
            <span class="featured-banner">Featured Recommendation</span>
            <div class="movie-title" style="font-size: 1.8rem; margin-bottom: 0.8rem;">{featured['title']}</div>
            <p style="color: #cbd5e1; margin-bottom: 1rem; line-height: 1.5;">
                A mind-bending psychological thriller where dream thieves pull off the ultimate heist inside the subconscious mind. Must-watch cinematic masterpiece!
            </p>
            <div style="margin-bottom: 1rem;">
                <span class="tag">{featured['genre']}</span>
                <span class="tag">Release: {featured['year']}</span>
            </div>
            <div class="rating" style="font-size: 1rem;">⭐ IMDb Rating: {featured['rating']}</div>
            <a href="/watchlist" class="btn" style="margin-top: 1.5rem;">⬅ Back to Watchlist</a>
        </div>
    </div>
    """
    return render_template_string(BASE_HTML, page_title="Tonight's Top Pick", content=content)

@app.route("/health")
def health_check():
    # Keep as pure JSON for automated DevOps health checks & curl
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
