from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        myDict = request.form
        Avg_Area_Income = float(myDict['Avg_Area Income'])
        Avg_Area_House_Age = float(myDict['Avg_Area House Age'])
        Avg_Area_Number_of_Rooms = float(myDict['Avg_Area_Number_of_Rooms'])
        Avg_Area_Number_of_Bedrooms = float(myDict['Avg_Area_Number_of_Bedrooms'])
        Area_Population = float(myDict['Area_Population'])
        # Code of inference
        input_features = [Avg_Area_Income, Avg_Area_House_Age, Avg_Area_Number_of_Rooms, Avg_Area_Number_of_Bedrooms, Area_Population]
        prediction_price = model.predict([input_features])
        print(prediction_price)
        return render_template('show.html',prob=prediction_price)
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)
    

