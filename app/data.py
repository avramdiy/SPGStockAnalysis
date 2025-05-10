from flask import Flask, render_template_string
import pandas as pd

app = Flask(__name__)

@app.route('/')
def display_dataframe():
    # File path
    file_path = r"C:\Users\avram\OneDrive\Desktop\TRG Week 23\spg.us.txt"

    try:
        # Read the file, treating the first row as headers
        df = pd.read_csv(file_path, delimiter=",", header=0)

        # Drop the "OpenInt" column
        if "OpenInt" in df.columns:
            df = df.drop(columns=["OpenInt"])

        # Convert DataFrame to HTML
        html_table = df.to_html(classes="table table-striped", index=False)

        # HTML Template
        html_template = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>DataFrame Display</title>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css">
        </head>
        <body>
            <div class="container mt-5">
                <h1 class="mb-4">DataFrame from File</h1>
                {{ table | safe }}
            </div>
        </body>
        </html>
        """
        return render_template_string(html_template, table=html_table)
    except Exception as e:
        return f"Error reading the file: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
