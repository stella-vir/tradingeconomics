import pandas as pd
import tradingeconomics as te
import urllib.request as u
import json
import os
from flask import Flask, render_template


te.login('5b47a77efd37439:5kzkij2hyxd98d4')


# /*----------------------------------*/
# webpage1:
# generate tesla stock symbols table from database and display it on web page
# mydata = te.getFinancialsData(country=['mexico', 'china', 'finland', 'united states'], symbol='TSLA:US', output_type='df')
data = te.getFinancialsData(symbol='tsla:us', output_type='df')
# df = pd.DataFrame(data)

path_csv = r'data.csv'
path_html = r'data.html'
data.to_csv(path_csv, index=False, header=True, sep='|')
# convert all values into str to avoid scientific notations displayed on the web page
data = data.astype(str)
data.round(5)
data.to_html(path_html)
# /*----------------------------------*/



# /*----------------------------------*/
# webpage2:
# fetch finland import/export data json file from url, store it into csv file and display as a table back to the web page
url = 'https://brains.tradingeconomics.com/v2/search/wb,fred,comtrade?q=finland&pp=50&p=0&_=1557934352427&stance=1'
with u.urlopen(url) as url:
    # dict
    js = json.load(url)
    # str
    json_object = json.dumps(js, indent=4)

    with open("data.json", "w+") as j:
         j.write(json_object)

data = json.load(open('data.json'))
df = pd.DataFrame(data["hits"])

path_csv1 = r'data1.csv'
path_html1 = r'data1.html'
df.to_csv(path_csv1, index=False, header=True, sep='|')
df.to_html(path_html1)
# /*----------------------------------*/


# /*----------------------------------*/
# flask app3:
# app = Flask(__name__, template_folder='template')
app = Flask (__name__)

@app.route("/")
def index():
    return render_template('data.html')

if __name__ == "__main__":
    app.run(debug=True)
# /*----------------------------------*/










# end
