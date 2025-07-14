from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    color = os.getenv('BG_COLOR', 'lightgreen')  # Default color if not set
    return f"""
    <html>
      <body style="background-color: {color};">
        <h1>Welcome to the Color App!</h1>
        <p>Current background color: <strong>{color}</strong></p>
        <p>To change the color, update the ConfigMap and restart the pod.</p>
      </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)