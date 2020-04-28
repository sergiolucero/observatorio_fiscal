from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
app.df = pd.read_csv('DATA/review_0427.csv')

@app.route('/top')
def top():
    df = app.df.sort_values('ratio', ascending=False)
    df['url'] = df.id_OC.apply(lambda oc: f'<A HREF="http://localhost:5000/review/{oc}">link</A>')
    data = df.to_html(index=False, escape=False)
    
    return render_template('review.html', data=data)

@app.route('/review/<id_oc>')
def helloIndex(id_oc):
    oc_df = app.df[app.df.id_OC == int(id_oc)].T
    data_oc = oc_df.to_html()

    return render_template('review.html', data=data_oc)

app.run(host='0.0.0.0', port=5000)