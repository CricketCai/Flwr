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
      width: 1920px;
      height: 1080px;
      overflow: hidden;
      border: 1px solid #aaa;
      border-radius: 6px;
    }

    iframe {
      width: 800px;
      height: 600px;
      transform: scale(0.25);
      transform-origin: top left;
      border: none;
    }
  </style>
</head>
<body>

<h3></h3>

<div class="mini">
  <iframe src="https://www.google.com"></iframe>
</div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

app.run(host="0.0.0.0", port=3000)