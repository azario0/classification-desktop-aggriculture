import webview
import pickle
import numpy as np
import os
with open('classifier.pkl', 'rb') as f:
    classifier = pickle.load(f)
import pandas as pd
class Api:
    def predict_crop(self,*args):
       
        N, P, k, temperature, humidity, ph, rainfall = args
    
        features = pd.DataFrame([[float(N), float(P), float(k), float(temperature), float(humidity), float(ph), float(rainfall)]], 
                            columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'])
        

        prediction = classifier.predict(features).reshape(1, -1)
        
        prediction = prediction[0]
        crop_dict = {1: "التوصية هي زراعة الأرز", 2: "التوصية هي زراعة الذرة", 3: "التوصية هي زراعة الجوت", 4: "التوصية هي زراعة القطن", 5: "التوصية هي زراعة جوز الهند", 6: "التوصية هي زراعة البابايا", 7: "التوصية هي زراعة البرتقال",
                    8: "التوصية هي زراعة التفاح", 9: "التوصية هي زراعة الشمام", 10: "التوصية هي زراعة البطيخ", 11: "التوصية هي زراعة العنب", 12: "التوصية هي زراعة المانجو", 13: "التوصية هي زراعة الموز",
                    14: "التوصية هي زراعة الرمان", 15: "التوصية هي زراعة العدس", 16: "التوصية هي زراعة بلاكجرام", 17: "التوصية هي زراعة فول المونج", 18: "التوصية هي زراعة فول العثة",
                    19: "التوصية هي زراعة البازلاء", 20: "التوصية هي زراعة الفاصوليا", 21: "التوصية هي زراعة الحمص", 22: "التوصية هي زراعة القهوة"}
        if prediction[0] in crop_dict:
            
            return crop_dict[prediction[0]]
        else:
            return "غير قادر على التوصية بالمحصول المناسب لهذه البيئة"

# Create a simple webview window
def create_window():
    api = Api()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    html_file = os.path.join(current_dir, 'index.html')
    webview.create_window("توصية المحاصيل", html_file, js_api=api, width=800, height=600)

if __name__ == '__main__':
    create_window()
    webview.start()
