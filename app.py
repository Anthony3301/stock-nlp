from flask import Flask, render_template
from io import BytesIO
import base64

app = Flask(__name__)

def load_existing_plot():
    # Load the pre-existing plot from file
    with open('existing_plot.png', 'rb') as file:
        img_base64 = base64.b64encode(file.read()).decode('utf-8')

    return img_base64

@app.route('/')
def index():
    # Load the existing plot and pass it to the template
    plot_data = load_existing_plot()
    return render_template('index.html', plot_data=plot_data)

if __name__ == '__main__':
    app.run(debug=True)
