from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        myDict = request.form
        BreathingProblem                   = int(myDict['BreathingProblem'])
        Fever                              = int(myDict['Fever'])
        DryCough                           = int(myDict['DryCough'])
        Sorethroat                         = int(myDict['Sorethroat'])
        Runningnose                        = int(myDict['Runningnose'])
        Asthma                             = int(myDict['Asthma'])
        ChronicLungDisease                 = int(myDict['ChronicLungDisease'])
        Headache                           = int(myDict['Headache'])
        HeartDisease                       = int(myDict['HeartDisease'])
        Diabetes                           = int(myDict['Diabetes'])
        HyperTension                       = int(myDict['HyperTension'])
        Fatigue                            = int(myDict['Fatigue'])
        Gastrointestinal                   = int(myDict['Gastrointestinal'])
        Abroadtravel                       = int(myDict['Abroadtravel'])
        ContactwithCOVIDPatient            = int(myDict['ContactwithCOVIDPatient'])
        AttendedLargeGathering             = int(myDict['AttendedLargeGathering'])
        VisitedPublicExposedPlaces         = int(myDict['VisitedPublicExposedPlaces'])
        FamilyworkinginPublicExposedPlaces = int(myDict['FamilyworkinginPublicExposedPlaces'])
        WearingMasks                       = int(myDict['WearingMasks'])
        SanitizationfromMarket             = int(myDict['SanitizationfromMarket'])
        
        # Code of inference
        input_features = [BreathingProblem, Fever, DryCough, Sorethroat, Runningnose, Asthma, ChronicLungDisease, 
                          Headache, HeartDisease, Diabetes, HyperTension, Fatigue, Gastrointestinal, 
                          Abroadtravel, ContactwithCOVIDPatient, AttendedLargeGathering, 
                          VisitedPublicExposedPlaces, FamilyworkinginPublicExposedPlaces, WearingMasks, 
                          SanitizationfromMarket]


        infec = model.predict_proba([input_features])[0][1]
        print(infec)
        return render_template('show.html',prob=infec)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
    

