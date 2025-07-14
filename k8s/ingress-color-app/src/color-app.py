from flask import Flask
import os

app = Flask(__name__)

# Get color from environment variable (default: lightblue)
BG_COLOR = os.getenv('BG_COLOR', 'lightblue')

@app.route('/')
def home():
    return f'''
    <html>
      <body style="background-color: {BG_COLOR};">
        <h1>Docker-Controlled Color App</h1>
        <p>Background color: <strong>{BG_COLOR}</strong></p>
        <p>Set via Dockerfile environment variable</p>
      </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)