from flask import Flask, render_template
import pandas as pd
import subprocess

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    # Run the Python script to retrieve data
    subprocess.run(["python", "retrieve_data.py"])

    # Read the retrieved data into a Pandas DataFrame
    df = pd.read_csv("data.csv")  # Assuming data is saved in a CSV file

    # Render the template with DataFrame data
    return render_template('index.html', data=df.to_html())

if __name__ == '__main__':
    app.run(debug=True)
