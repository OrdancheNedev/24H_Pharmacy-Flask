from flask import Flask, render_template, request
import json

app = Flask(__name__)


def load_data():

    with open('info.txt','r') as file:
        return json.load(file)



@app.route('/', methods=['GET','POST'])
def home():

    cities = ["City1","City2","City3"]
   
    weeks = ["week number 1", "week number 2","week number 3","week number 4"]

    search = request.args.get('search', '').lower()
    
    
    week = request.form.get('week')

    city = request.form.get('city')

    data = load_data()

    if city and week:
        data_s = [item for item in data if item['City'] == city and item['Date'] == week]

    elif city:
        data_s = [item for item in data if item['City']==city]  

    elif week:
         data_s = [item for item in data if item['Date']==week]  

    elif search:
        data_s = [item for item in data if search in item['Name'].lower()] 
    
    else:
        data_s = data 

    return render_template('home.html', data=data_s, cities=cities, weeks=weeks)

if __name__ == "__main__":
    app.run(debug=True)