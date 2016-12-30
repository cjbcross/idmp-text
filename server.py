from flask import Flask, render_template, request, send_from_directory, redirect, g, make_response, Markup, flash
import readcsv
import readdrop
import chartout

app = Flask(__name__)
app.debug = True
app.secret_key = '2dyUy8v7d62jDFCEqnUr1X3XLIT31IxL'

gcustomer = None

@app.route('/', methods=['GET', 'POST', 'OPTIONS'])
def home():
    return render_template('index - Copy.html')


@app.route('/sasView.html', methods=['GET', 'POST', 'OPTIONS'])
def sasView():
    global gcustomer
    g.cust_id = gcustomer
    return render_template('sasView.html')


@app.route('/chart.html', methods=['GET', 'POST', 'OPTIONS'])
def chart():
    global gcustomer
    g.cust_id = gcustomer
    return render_template('chart.html')


@app.route('/customers/', methods=['POST'])
def parse_customers():
    global gcustomer
    gcustomer = request.form['customer']
    return redirect('/sasView.html')

@app.route('/js/<path:filename>', methods=['GET', 'POST', 'OPTIONS'])
def send_js(filename):
    return send_from_directory('js', filename)


@app.route('/css/<path:filename>', methods=['GET', 'POST', 'OPTIONS'])
def send_css(filename):
    return send_from_directory('css', filename)


@app.route('/includes/<path:filename>', methods=['GET', 'POST', 'OPTIONS'])
def send_includes(filename):
    return send_from_directory('includes', filename)


@app.route('/fonts/<path:filename>', methods=['GET', 'POST', 'OPTIONS'])
def send_fonts(filename):
    return send_from_directory('fonts', filename)


@app.route('/font-awesome-4.7.0/<path:filename>', methods=['GET', 'POST', 'OPTIONS'])
def send_fa(filename):
    return send_from_directory('font-awesome-4.7.0', filename)


@app.route('/csv/', methods=['GET', 'POST', 'OPTIONS'])
def get_json():
    body = readcsv.return_rest()
    return body


@app.route('/drop/', methods=['GET', 'POST', 'OPTIONS'])
def get_control():
    body = readdrop.return_drop()
    return body


@app.route('/chartout/', methods=['GET', 'POST', 'OPTIONS'])
def get_chart_data():
    body = chartout.return_chart()
    return body


if __name__ == '__main__':
    app.run()
