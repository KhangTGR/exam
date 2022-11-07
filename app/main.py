from flask import Flask
from flask import render_template

# Import missing libraries here
# ...

import os
hostname = os.uname()[1]

app = Flask(__name__)

# Suggestion:
# Upload file: https://www.youtube.com/watch?v=GeiUTkSAJPs


# Write code for class/functions if need
# ...


@app.route('/', methods=['GET'])
def home():
    # Your code is here #
    # ...
    # Your code is here #
    return render_template('index.html', hostname=hostname)


@app.route('/upload', methods=['POST'])
def upload():
    # Your code is here #
    # ...
    # Your code is here #
    return ""


@app.route('/result', methods=['GET'])
def result():
    uploaded_file = "uploaded-file"
    content = ""

    # Your code is here #
    # ...
    # Your code is here #

    return render_template('result.html', hostname=hostname, uploaded_file=uploaded_file, content=content)


if __name__ == '__main__':
  app.run(debug=True)
