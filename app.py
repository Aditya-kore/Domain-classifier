from flask import Flask, render_template, request
import joblib
app = Flask('url_predicturl')
loaded_model = joblib.load('donebyme.pkl')

@app.route('/')
def opening():
    return render_template('predictor.html')
@app.route('/results', methods=['POST'])
def results():
    form = request.form
    if request.method == 'POST':
      #write your function that loads the model
      #model = get_model() #you can use pickle to load the trained model
       url = request.form['url']
       predicted_category = loaded_model.predict(url)
       return render_template('resultsform.html', url=url,   predicted_url=predicted_category)

#if __name__ == '__main__':
#app.run("localhost", "9999", debug=True)
app.run()