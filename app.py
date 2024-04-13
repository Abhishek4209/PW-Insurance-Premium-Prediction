from flask import Flask,render_template
from src.exception import CustomException
from src.logger import logging
import sys,os
from src.components.data_ingestion import DataIngestion


app=Flask(__name__)



try:
    @app.route('/')
    def index():
        return render_template("index.html")


    @app.route('/get-prediction',methods=['POST'])
    def get_prediction():
        return render_template("predict.html")
        



except Exception as e:
    raise CustomException(sys,e)
    # logging.info("Some error Occured")








if __name__ == "__main__":
    app.run(debug=True)
    logging.info()