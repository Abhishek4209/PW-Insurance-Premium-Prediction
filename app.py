from flask import Flask,request,render_template,jsonify
from src.pipelines.prediction_pipeline import CustomData,PredictPipeline


application=Flask(__name__)

app=application

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])

def predict_datapoint():
    if request.method=='GET':
        return render_template('predict.html')
    
    else:
        data=CustomData(
            age=float(request.form.get('age')),
            sex = request.form.get('sex'),
            bmi = float(request.form.get('bmi')),
            children = float(request.form.get('children')),
            smoker = request.form.get('smoker'),
            region= request.form.get('region')
            
        )
        final_new_data=data.get_data_as_dataframe()
        predict_pipeline=PredictPipeline()
        pred=predict_pipeline.predict(final_new_data)

        results=round(pred[0],2)

        return render_template('predict.html',final_result=results)
    





if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)