from flask import Flask,render_template,request
import pandas as pd
import pickle


app = Flask(__name__, template_folder='.')
data=pd.read_csv("cleaned data.csv")
pipe = pickle.load(open("RidgeModel.pkl","rb"))


@app.route('/')
def index():
    
    locations=sorted(data['location'].unique())
    return render_template('index.html',locations=locations)

# @app.route('/predict',methods=['POST'])
# def predict():
#     location = request.form.get("location")
#     bhk=request.form.get("BHK")
#     bath=request.form.get("bath")
#     sqft=request.form.get("total_sqft")
    
#     print(location,bhk,bath,sqft)
    
#     try:
#         input_df = pd.DataFrame([[location, float(sqft), int(bath), int(bhk)]],
#                                 columns=['location', 'total_sqft', 'bath', 'bhk'])
#         prediction = pipe.predict(input_df)[0]
#         return str(round(prediction, 2))
    
#      except Exception as e:
#         print("Prediction error:", e)
#         return "Prediction failed"
    
@app.route('/predict', methods=['POST'])
def predict():
    location = request.form.get("location")
    bhk = request.form.get("BHK")
    bath = request.form.get("bath")
    sqft = request.form.get("total_sqft")

    print(location, bhk, bath, sqft)

    # Check if any required field is missing
    if not location or not bhk or not bath or not sqft:
        return "Please fill in all fields"

    try:
        input_df = pd.DataFrame([[location, float(sqft), int(bath), int(bhk)]],
                                columns=['location', 'total_sqft', 'bath', 'bhk'])
        
        prediction = pipe.predict(input_df)[0]
        return str(round(prediction, 2))

    except Exception as e:
        print("Prediction error:", e)
        return "Prediction failed"

  
    
    # return str(prediction)


if __name__=='__main__':
    app.run(debug=True,port=5001)

