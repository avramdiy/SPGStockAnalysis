from flask import Flask, render_template_string, Response
import pandas as pd
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

@app.route('/')
def display_dataframe():
    # File path
    file_path = r"C:\Users\avram\OneDrive\Desktop\TRG Week 23\spg.us.txt"

    try:
        # Read the file, treating the first row as headers
        df = pd.read_csv(file_path, delimiter=",", header=0)

        # Drop the "OpenInt" column if it exists
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
                <p><a href="/plot" class="btn btn-primary mt-3">View Plot of Average Prices (2005-2017)</a></p>
            </div>
        </body>
        </html>
        """
        return render_template_string(html_template, table=html_table)
    except Exception as e:
        return f"Error reading the file: {str(e)}"


@app.route('/plot')
def plot_average_prices():
    # File path
    file_path = r"C:\Users\avram\OneDrive\Desktop\TRG Week 23\spg.us.txt"

    try:
        # Read the file
        df = pd.read_csv(file_path, delimiter=",", header=0)

        # Convert "Date" to datetime and extract year
        df["Date"] = pd.to_datetime(df["Date"])
        df["Year"] = df["Date"].dt.year

        # Filter for years 2005 to 2017
        df_filtered = df[(df["Year"] >= 2005) & (df["Year"] <= 2017)]

        # Calculate average "Open" and "Close" prices by year
        avg_open_by_year = df_filtered.groupby("Year")["Open"].mean()
        avg_close_by_year = df_filtered.groupby("Year")["Close"].mean()

        # Calculate the median of the yearly average Open and Close prices
        yearly_median_price = (avg_open_by_year + avg_close_by_year) / 2

        # Plot the data
        plt.figure(figsize=(10, 6))

        # Plot "Yearly Median Average Price" as a blue line
        plt.plot(yearly_median_price.index, yearly_median_price.values, color="blue", linewidth=2, label="Median Avg Price", marker='o')

        # Add titles and labels
        plt.title("Yearly Median Prices (2005-2017)", fontsize=16)
        plt.xlabel("Year", fontsize=14)
        plt.ylabel("Price", fontsize=14)
        plt.xticks(rotation=45, fontsize=12)
        plt.legend()
        plt.grid(axis="y", linestyle="--", alpha=0.7)

        # Save plot to a BytesIO buffer
        buf = io.BytesIO()
        plt.tight_layout()
        plt.savefig(buf, format="png")
        buf.seek(0)
        plt.close()

        # Return the plot as a response
        return Response(buf, mimetype="image/png")
    except Exception as e:
        return f"Error generating plot: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
