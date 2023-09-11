import pandas as pd 
import numpy as np 
import streamlit as st
import joblib
from forex_python.converter import CurrencyRates


c = CurrencyRates()
currency = c.get_rate('INR','USD') ** -1

def main():
    html_temp = """
    <div style = "background-colour:liteblue;padding:16px">
    <h3 style = "colour:black;text-align:center;"> Car Price Prediction </h3> 
    </div>
"""
    st.markdown(html_temp, unsafe_allow_html= True)

    st.write('')
    st.write('')

    st.markdown("##### Predict the Price of your dream car below #####")

    p1 = st.number_input("Give points to the risk factor (high value means high risk) :",-3,3,step = 1)

    p2 = st.selectbox("What is the prefered Aspiration (i.e., Initial combustion of engine):", ('std' ,'turbo'))

    p3 = st.number_input("Number of doors : ", 2, 4, step=2)

    p4 = st.selectbox("What prefered car body :",('convertible', 'hatchback', 'sedan', 'wagon', 'hardtop'))

    p5 = st.selectbox("What is the prefered Drive Wheel ? ", ('rwd', 'fwd', '4wd'))

    p6 = st.selectbox("Prefered Engine Location ? :", ('front', 'rear'))

    p7 = st.number_input("Prefered height of the car (Inches):",50.0,60.0,step = 0.5)

    p8 = st.selectbox("Prefered engine type ? : ",('dohc' ,'ohcv', 'ohc', 'l', 'rotor', 'ohcf', 'dohcv'))

    p9 = st.selectbox("Number of Cylinder prefered in car : ", ('four', 'six', 'five', 'three', 'twelve', 'two', 'eight'))

    p10 = st.selectbox("Prefered Fuel system ? : ", ('mpfi', '2bbl', 'mfi', '1bbl', 'spfi', '4bbl', 'idi', 'spdi'))

    p11 = st.number_input("Set the Bore ratio of the car :",1.0, 1.5,step = 0.05)

    p12 = st.number_input("What is the prefer value of stroke :", 1.0, 4.0, step= 0.1)

    p13 = st.number_input("Prefered Compression ratio :", 7.0,25.0,step=1.0)

    p14 = st.number_input("Value of Horse power :", 100, 200, step = 1)

    p15 = st.selectbox("Peak Value of Rpm :",(5000 ,5500, 5800, 4250, 5400, 5100, 4800, 6000, 4750, 4650, 4200, 4350, 4500, 5200,
 4150, 5600, 5900, 5750, 5250, 4900, 4400, 6600, 5300))
    
    p16 = st.number_input("Average MPG of the car",17,55, step = 1)

    p17 = st.selectbox("Name of the company ",('alfa-romero', 'audi', 'bmw', 'chevrolet', 'dodge', 'honda', 'isuzu', 'jaguar',
 'maxda', 'mazda', 'buick', 'mercury', 'mitsubishi', 'Nissan', 'nissan',
 'peugeot', 'plymouth', 'porsche', 'porcshce', 'renault', 'saab', 'subaru',
 'toyota', 'toyouta', 'vokswagen', 'volkswagen', 'vw', 'volvo'))
    
    ####### Encoding ##########
    p17 = code_p17(p17)
    p15 = code_p15(p15)
    p10 = code_p10(p10)
    p9 = code_p9(p9)
    p8 = code_p8(p8)
    p6 = code_p6(p6)
    p5 = code_p5(p5)
    p4 = code_p4(p4)
    p2 = code_p2(p2)

    ### Converting into data Frame ###

    df = pd.DataFrame(
        {'symboling' : p1,
        'aspiration': p2, 
        'doornumber' : p3,
        'carbody': p4,
        'drivewheel': p5,
       'enginelocation' : p6,
       'carheight' : p7,
       'enginetype': p8,
        'cylindernumber': p9,
       'fuelsystem' : p10,
       'boreratio' : p11,
       'stroke': p12,
        'compressionratio': p13,
        'horsepower': p14,
       'peakrpm' : p15,
       'highwaympg' : p16,
       'carcompany': p17}, index = [0]
    )

    #### Prediction ####

    data = joblib.load("finalmodel1.pkl")
    try:
        if st.button("Predict"):
            y_pred = data.predict(df)

            st.success("Estimated price of your car will be Rs {}".format(round(y_pred[0]*currency,2)))
    
    except:
        st.warning("Something wrong ! Please Try Again !")


    
def get_key_by_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None
    
def code_p17(p17):
    d = {0: 'Nissan', 1: 'alfa-romero', 2: 'audi', 3: 'bmw', 4: 'buick', 5: 'chevrolet', 6: 'dodge', 
        7: 'honda', 8: 'isuzu', 9: 'jaguar', 10: 'maxda', 11: 'mazda', 12: 'mercury', 13: 'mitsubishi', 14: 'nissan', 
        15: 'peugeot', 16: 'plymouth', 17: 'porcshce', 18: 'porsche', 19: 'renault', 20: 'saab', 21: 'subaru', 22: 'toyota', 
        23: 'toyouta', 24: 'vokswagen', 25: 'volkswagen', 26: 'volvo', 27: 'vw'} 
    return get_key_by_value(d, p17)

def code_p15(p15):
    d = {0: 4150, 1: 4200, 2: 4250, 3: 4350, 4: 4400, 
         5: 4500, 6: 4650, 7: 4750, 8: 4800, 9: 4900, 10: 5000, 11: 5100, 12: 5200, 
         13: 5250, 14: 5300, 15: 5400, 16: 5500, 17: 5600, 18: 5750, 19: 5800, 20: 5900, 21: 6000, 22: 6600} 
    
    return get_key_by_value(d,p15)

def code_p10(p10):
    d = {0: '1bbl', 1: '2bbl', 2: '4bbl', 3: 'idi', 4: 'mfi', 5: 'mpfi', 6: 'spdi', 7: 'spfi'} 
    return get_key_by_value(d,p10)

def code_p9(p9):
    d = {0: 'eight', 1: 'five', 2: 'four', 3: 'six', 4: 'three', 5: 'twelve', 6: 'two'} 
    return get_key_by_value(d,p9)
def code_p8(p8):
    d = {0: 'dohc', 1: 'dohcv', 2: 'l', 3: 'ohc', 4: 'ohcf', 5: 'ohcv', 6: 'rotor'} 

    return get_key_by_value(d,p8)

def code_p6(p6):
    d = {0: 'front', 1: 'rear'} 
    return get_key_by_value(d,p6)

def code_p5(p5):
    d = {0: '4wd', 1: 'fwd', 2: 'rwd'} 

    return get_key_by_value(d,p5)

def code_p4(p4):
    d = {0: 'convertible', 1: 'hardtop', 2: 'hatchback', 3: 'sedan', 4: 'wagon'} 

    return get_key_by_value(d,p4)

def code_p2(p2):
    d = {0: 'std', 1: 'turbo'} 

    return get_key_by_value(d,p2)






if __name__ == "__main__":
    main()