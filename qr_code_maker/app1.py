from flask import Flask, render_template, redirect, url_for, session
import pyqrcode
from form import InfoForm
import png
import os
import shutil
from PIL import Image

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/input_address', methods=['GET', 'POST'])
def input_wallet():
    form = InfoForm()
    if form.validate_on_submit():
        session['address'] = form.address.data
        session['chain'] = form.chain.data
        return redirect(url_for('qr_code'))

    return render_template('input.html', form=form)


@app.route('/qr_code', methods=['GET', 'POST'])
def qr_code():

    address = session['address']
    chain = session['chain']

    if chain == 'bsc':
        scanner = 'https://bscscan.com/address/'
    elif chain == 'avax':
        scanner = 'https://snowtrace.io/'
    elif chain == 'eth':
        scanner = 'https://etherscan.io/'
    elif chain == 'ada':
        scanner = 'https://cardanoscan.io/address/'

    link = scanner + address
    qr_code = pyqrcode.create(link)
    qr_code.png("wallet.png", scale=5)
    shutil.move("wallet.png",
                "C:/Users/Luke/Documents/PythonProjects/qr_code_maker/static/wallet.png")
    # os.remove(
    #     r'C:/Users/Luke/Documents/PythonProjects/qr_code_maker/wallet.png')

    return render_template('qr_code.html', chain=chain)


if __name__ == '__main__':
    app.run(debug=True)
