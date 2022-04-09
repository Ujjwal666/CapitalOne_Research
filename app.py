from flask import Flask
from flask import render_template
from flask import request, redirect, session, url_for
from phase import phases

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/submitt',methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Option 1':
            return_val = phases()
            return render_template('index.html',imgSrc="https://wcs.smartdraw.com/chart/img/basic-bar-graph.png?bn=15100111816",returnVal = return_val)
        elif request.form['submit_button'] == 'Option 2':
            return render_template('index.html',imgSrc="https://www.howtogeek.com/wp-content/uploads/2021/11/GoogleSheetsLineChart.png?width=1198&trim=1,1&bg-color=000&pad=1,1")
        elif request.form['submit_button'] == 'Option 3':
            return render_template('index.html',imgSrc="https://www.jmp.com/en_gb/statistics-knowledge-portal/exploratory-data-analysis/line-graph/_jcr_content/par/styledcontainer_2069/par/image.img.png/1597773227632.png")
        elif request.form['submit_button'] == 'Option 4':
            return render_template('index.html', imgSrc="https://cdn1.byjus.com/wp-content/uploads/2019/11/Line-Graph.png")