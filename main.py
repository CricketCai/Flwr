from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
  <title>Website Embedder</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      padding: 20px;
    }

    .mini {
      width: 1000px;
      height: 1000px;
      overflow: hidden;
      border: 1px solid #aaa;
      border-radius: 6px;
    }

    iframe {
      width: 1000px;
      height: 1000px;
      transform: scale(1);
      transform-origin: top left;
      border: none;
    }
  </style>
</head>
<body>

<h3></h3>

<div class="mini">
  <iframe src="https://dashboard.uptimerobot.com/login?rt=true"></iframe>
</div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

app.run(host="0.0.0.0", port=3000)