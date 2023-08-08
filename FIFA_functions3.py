def sofifa_clean_df(df):
    import math
    import numpy as np
    import pandas as pd
       
    def feet_to_cm(height_str):
        feet, inches = map(int, height_str.replace('"', '').split("'"))
        total_inches = (feet * 12) + inches
        cm = total_inches * 2.54
        return cm
   
   
    def value_calc(value_str):
        value = value_str.replace("€","")
        if 'M' in value:
            value = value.replace("M","")
            value = pd.to_numeric(value, errors='coerce')
            value = value * 1000000
        elif 'K' in value:
            value = value.replace("K","")
            value = pd.to_numeric(value, errors='coerce')
            value = value * 1000
        else:
            value = pd.to_numeric(value, errors='coerce')
        return value
    
    
    df2=df[['BP','Age','Height','Weight','foot','Growth','Value','Attacking','Skill','Movement','Power','Mentality','Defending',
              'Goalkeeping','Total Stats','Base Stats', 'W/F', 'SM', 'A/W','D/W', 'IR', 'PAC', 'SHO', 'PAS', 'DRI', 'DEF',
              'PHY','OVA']].copy()
    df2['Height'] = df['Height'].apply(feet_to_cm)
    df2['Weight']=df2['Weight'].str.replace("lbs","")
    df2['Weight']=pd.to_numeric(df2['Weight'], errors='coerce')
    df2['Value'] = df2['Value'].apply(value_calc)
  
    df2['W/F'] = df2['W/F'].str.replace(" ★","")
    df2['W/F']=pd.to_numeric(df2['W/F'], errors='coerce')
   
    df2['SM'] = df2['SM'].str.replace("★","")
    df2['SM']=pd.to_numeric(df2['SM'], errors='coerce')
    df2['IR'] = df2['IR'].str.replace(" ★","")
    df2['IR']=pd.to_numeric(df2['IR'], errors='coerce')
    
    #fill NAN
    df2['A/W'] = df2['A/W'].fillna('Medium')
    df2['D/W'] = df2['D/W'].fillna('Medium')
    return df2
    
