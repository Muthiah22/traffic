import streamlit as st
st.set_page_config(
     page_title="Road Sign Classification App",
     page_icon="🚦",
     
     initial_sidebar_state="expanded"
     
   

 )

hide_menu_style="""
    <style>
    #MainMenu {visibility:hidden;}
    footer {visibility:hidden;}
    </style>
    """
st.markdown(hide_menu_style,unsafe_allow_html=True)

import glob,time
import os
from gtts import gTTS
from googletrans import Translator 
translator = Translator()
import numpy as np
import cv2
from keras.models import load_model
import streamlit as st
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
from keras.applications.resnet import preprocess_input
import pyttsx3
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Road Signs", [ 'German', "Persian"], 
        icons=['list-task', 'list-task'], menu_icon="cast", default_index=1)
    


  
if selected== "German":

    model = load_model("C:/Users/Kotha/Downloads/traficsignrecog.h5")


    new_title = '<p style="font-family:Open Sans; color:##FFFFFF; font-size: 29px;">GERMAN ROAD SIGN CLASSIFICATION</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    st.sidebar.success('Driving in Germany can be a delight: the scenery is beautiful and the roads are well maintained. But there are many rules and regulations to observe')
                   
    st.sidebar.success('                   If you’re going to be driving in Germany, it’s a good idea to get to grips with the different road signs and their meanings, before hitting the road.') 
    #st.sidebar.success('                   There are over 1000 traffic signs in the German traffic code, including warning signs, speed limit signs, and information signs.')
    from PIL import Image
    image = Image.open("C:/Users/Kotha/Downloads/IMGG.jpeg")
    st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    uploaded_file = st.file_uploader("UPLOAD IMAGE HERE", type=["jpg","jpeg","png"])

    classNo = {0:'Speed limit 20km',
            1:'Speed limit 30km/h', 
            2:'Speed limit 50km/h', 
            3:'Speed limit 60km/h', 
            4:'Speed limit 70km/h', 
            5:'Speed limit 80km/h', 
            6:'End of speed limit 80km/h', 
            7:'Speed limit 100km/h', 
            8:'Speed limit 120km/h', 
            9:'No passing', 
            10:'No passing vehicles over 3.5 tons', 
            11:'Right-of-way at intersection', 
            12:'Priority road', 
            13:'Yield', 
            14:'Stop', 
            15:'No vehicles', 
            16:'Vehicles greater than 3.5 tons prohibited', 
            17:'No entry', 
            18:'General caution', 
            19:'Dangerous curve left', 
            20:'Dangerous curve right', 
            21:'Double curve', 
            22:'Bumpy road', 
            23:'Slippery road', 
            24:'Road narrows on the right', 
            25:'Road work', 
            26:'Traffic signals', 
            27:'Pedestrians', 
            28:'Children crossing', 
            29:'Bicycles crossing', 
            30:'Beware of ice/snow',
            31:'Wild animals crossing', 
            32:'End speed + passing limits', 
            33:'Turn right ahead', 
            34:'Turn left ahead', 
            35:'Ahead only', 
            36:'Go straight or right', 
            37:'Go straight or left', 
            38:'Keep right', 
            39:'Keep left', 
            40:'Roundabout mandatory', 
            41:'End of no passing', 
            42:'End no passing vehicle over 3.5 tons'}
     
    if uploaded_file is not None:
     
     file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
     opencv_image = cv2.imdecode(file_bytes, 1)
     
     resized = cv2.resize(opencv_image,(30,30))     
     img = np.reshape(resized,[1,30,30,3])
     
     st.image(opencv_image, channels="RGB")

     resized = preprocess_input(resized)
     img_reshape = resized[np.newaxis]
   
     loaden = st.button("ENGLISH")    
    
     if "loaden_state" not in st.session_state:
         st.session_state.loaden_state= False

    
     if loaden or st.session_state.loaden_state:
         st.session_state.loaden_state= True

         try:
             os.mkdir("temp")
         except:
             pass
         
         translator = Translator()
         prediction = model.predict(img_reshape).argmax()     
         res = classNo[np.argmax(model.predict(img))]
         
         text = res

         in_lang = "en"


         out_lang ="en"


         tld = "com"



         def text_to_speech(in_lang, out_lang, text, tld):
             translation = translator.translate(text, src=in_lang, dest=out_lang)
             trans_text = translation.text
             tts = gTTS(trans_text, lang=out_lang, tld=tld, slow=False)
             try:
                 my_file_name = text[0:20]
             except:
                 my_file_name = "audio"
             tts.save(f"temp/{my_file_name}.mp3")
             return my_file_name, trans_text


         

         if st.checkbox("English Text"):
             result, output_text = text_to_speech(in_lang, out_lang, text, tld)
             audio_file = open(f"temp/{result}.mp3", "rb")  
             audio_bytes = audio_file.read()
             
             st.audio(audio_bytes, format="audio/mp3", start_time=0)
         
             
             st.info(f" {output_text}")  
      
     load = st.button("TAMIL")    
    
     if "load_state" not in st.session_state:
         st.session_state.load_state= False

    
     if load or st.session_state.load_state:
         st.session_state.load_state= True

         try:
             os.mkdir("temp")
         except:
             pass
         
         translator = Translator()
         prediction = model.predict(img_reshape).argmax()     
         res = classNo[np.argmax(model.predict(img))]
         
         text = res

         in_lang = "en"


         out_lang ="ta"


         tld = "com"



         def text_to_speech(in_lang, out_lang, text, tld):
             translation = translator.translate(text, src=in_lang, dest=out_lang)
             trans_text = translation.text
             tts = gTTS(trans_text, lang=out_lang, tld=tld, slow=False)
             try:
                 my_file_name = text[0:20]
             except:
                 my_file_name = "audio"
             tts.save(f"temp/{my_file_name}.mp3")
             return my_file_name, trans_text


         

         if st.checkbox("Tamil Text"):
             result, output_text = text_to_speech(in_lang, out_lang, text, tld)
             audio_file = open(f"temp/{result}.mp3", "rb")  
             audio_bytes = audio_file.read()
             
             st.audio(audio_bytes, format="audio/mp3", start_time=0)
         
             
             st.info(f" {output_text}")


     loade = st.button("GERMAN")    
    
     if "loade_state" not in st.session_state:
         st.session_state.loade_state= False

    
     if loade or st.session_state.loade_state:
         st.session_state.loade_state= True

         try:
             os.mkdir("temp")
         except:
             pass
         
         translator = Translator()
         prediction = model.predict(img_reshape).argmax()     
         res = classNo[np.argmax(model.predict(img))]
         
         text = res

         in_lang = "en"


         out_lang ="de"


         tld = "com"



         def text_to_speech(in_lang, out_lang, text, tld):
             translation = translator.translate(text, src=in_lang, dest=out_lang)
             trans_text = translation.text
             tts = gTTS(trans_text, lang=out_lang, tld=tld, slow=False)
             try:
                 my_file_name = text[0:20]
             except:
                 my_file_name = "audio"
             tts.save(f"temp/{my_file_name}.mp3")
             return my_file_name, trans_text


         

         if st.checkbox("German  Text"):
             result, output_text = text_to_speech(in_lang, out_lang, text, tld)
             audio_file = open(f"temp/{result}.mp3", "rb")  
             audio_bytes = audio_file.read()
             
             st.audio(audio_bytes, format="audio/mp3", start_time=0)
         
             
             st.info(f" {output_text}")    
             
     loadeq = st.button("LATIN")    
     
     if "loadeq_state" not in st.session_state:
          st.session_state.loadeq_state= False

     
     if loadeq or st.session_state.loadeq_state:
          st.session_state.loadeq_state= True

          try:
              os.mkdir("temp")
          except:
              pass
          
          translator = Translator()
          prediction = model.predict(img_reshape).argmax()     
          res = classNo[np.argmax(model.predict(img))]
          
          text = res

          in_lang = "en"


          out_lang ="lv"


          tld = "com"



          def text_to_speech(in_lang, out_lang, text, tld):
              translation = translator.translate(text, src=in_lang, dest=out_lang)
              trans_text = translation.text
              tts = gTTS(trans_text, lang=out_lang, tld=tld, slow=False)
              try:
                  my_file_name = text[0:20]
              except:
                  my_file_name = "audio"
              tts.save(f"temp/{my_file_name}.mp3")
              return my_file_name, trans_text


          

          if st.checkbox("Latin  Text"):
              result, output_text = text_to_speech(in_lang, out_lang, text, tld)
              audio_file = open(f"temp/{result}.mp3", "rb")  
              audio_bytes = audio_file.read()
              
              st.audio(audio_bytes, format="audio/mp3", start_time=0)
          
              
              st.info(f" {output_text}")         
        

        
if selected == "Persian":    
  model = load_model("C:/Users/Kotha/Downloads/cnnpersiantraffic.h5")

  #('When you are driving in Persia you are in control of everything. You can discover many pristine spots and explore every corner of this amazing country.')
  st.sidebar.success('The driving rules are international rules, the same as other countries, so there is nothing unfamiliar about it.')
  st.sidebar.success(' Also, most signs on the roads are written in both English and Persian, so you have no problem understanding them.')
  new_title = '<p style="font-family:Open Sans; color:##FFFFFF; font-size: 29px;">PERSIAN ROAD SIGN CLASSIFICATION</p>'
  st.markdown(new_title, unsafe_allow_html=True)
  from PIL import Image
  image = Image.open("C:/Users/Kotha/Downloads/dataset-cover (1).png")
  st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
  uploaded_file = st.file_uploader("UPLOAD IMAGE HERE", type=["jpg","jpeg","png"])
  class_names={0:'Compulsory Keep BothSide',
         1:'Maximum Speed 30',
         2:'Maximum Speed 40',
         3:'Maximum Speed 50', 
         4:'Maximum Speed 60', 
         5:'Maximum Speed 70',
         6:'Maximum Speed 80',
         7: 'Maximum Speed 90',
         8:'MotorCycle Prohibited',
         9: 'No Entry',
         10:'No Horn',
         11:'Compulsory Keep Left',
         12:'NO Stopping',
         13:'NO Waiting',
         14:'One way Traffic',
         15:'Park', 
         16:'Park Forbidden', 
         17:'Pedestrain',
         18:'Pedestrian crossing',
         19: 'Right Bend', 
         20:'Right Margin',
         21: 'Right Turn Prohibited',
         22: 'Compulsory Keep Right',
         23: 'Road Work',
         24:'Roundabouts',
         25: 'School',
         26: 'School Crossing',
         27: 'Side Road Right',
         28:'Slow',
         29:'Speed Camera',
         30:'STOP',
         31:'Truck Prohibited', 
         32:'Two Way Traffic', 
         33:'Cycle crossing',
         34:'U-Turn',
         35:'U-Turn Allowed',
         36:'U-turn Prohibited',
         37:'Danger', 
         38:'Give Way',
         39:'Hump',
         40:'Left Bend',
         41:'Left Margin',
         42:'Left Turn Prohibited'}  
  if uploaded_file is not None:
   
   file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
   opencv_image = cv2.imdecode(file_bytes, 1)
   
   resized = cv2.resize(opencv_image,(32,32))     
   img = np.reshape(resized,[1,32,32,3])
   
   st.image(opencv_image, channels="RGB")

   resized = preprocess_input(resized)
   img_reshape = resized[np.newaxis]
 
   loadenf = st.button("ENGLISH")    
  
   if "loadenf_state" not in st.session_state:
       st.session_state.loadenf_state= False

  
   if loadenf or st.session_state.loadenf_state:
       st.session_state.loadenf_state= True

       try:
           os.mkdir("temp")
       except:
           pass
       
       translator = Translator()
       prediction = model.predict(img_reshape).argmax()     
       res = class_names[np.argmax(model.predict(img))]
       
       text = res

       in_lang = "en"


       out_lang ="en"


       tld = "com"



       def text_to_speech(in_lang, out_lang, text, tld):
           translation = translator.translate(text, src=in_lang, dest=out_lang)
           trans_text = translation.text
           tts = gTTS(trans_text, lang=out_lang, tld=tld, slow=False)
           try:
               my_file_name = text[0:20]
           except:
               my_file_name = "audio"
           tts.save(f"temp/{my_file_name}.mp3")
           return my_file_name, trans_text


       

       if st.checkbox("English Text"):
           result, output_text = text_to_speech(in_lang, out_lang, text, tld)
           audio_file = open(f"temp/{result}.mp3", "rb")  
           audio_bytes = audio_file.read()
           
           st.audio(audio_bytes, format="audio/mp3", start_time=0)
       
           
           st.info(f" {output_text}")  
    
   load = st.button("TURKISH")    
  
   if "load_state" not in st.session_state:
       st.session_state.load_state= False

  
   if load or st.session_state.load_state:
       st.session_state.load_state= True

       try:
           os.mkdir("temp")
       except:
           pass
       
       translator = Translator()
       prediction = model.predict(img_reshape).argmax()     
       res = class_names[np.argmax(model.predict(img))]
       
       text = res

       in_lang = "en"


       out_lang ="tr"


       tld = "com"



       def text_to_speech(in_lang, out_lang, text, tld):
           translation = translator.translate(text, src=in_lang, dest=out_lang)
           trans_text = translation.text
           tts = gTTS(trans_text, lang=out_lang, tld=tld, slow=False)
           try:
               my_file_name = text[0:20]
           except:
               my_file_name = "audio"
           tts.save(f"temp/{my_file_name}.mp3")
           return my_file_name, trans_text


       

       if st.checkbox("Turkish Text"):
           result, output_text = text_to_speech(in_lang, out_lang, text, tld)
           audio_file = open(f"temp/{result}.mp3", "rb")  
           audio_bytes = audio_file.read()
           
           st.audio(audio_bytes, format="audio/mp3", start_time=0)
       
           
           st.info(f" {output_text}")


   loade = st.button("ARAB")    
  
   if "loade_state" not in st.session_state:
       st.session_state.loade_state= False

  
   if loade or st.session_state.loade_state:
       st.session_state.loade_state= True

       try:
           os.mkdir("temp")
       except:
           pass
       
       translator = Translator()
       prediction = model.predict(img_reshape).argmax()     
       res = class_names[np.argmax(model.predict(img))]
       
       text = res

       in_lang = "en"


       out_lang ="ar"


       tld = "com"



       def text_to_speech(in_lang, out_lang, text, tld):
           translation = translator.translate(text, src=in_lang, dest=out_lang)
           trans_text = translation.text
           tts = gTTS(trans_text, lang=out_lang, tld=tld, slow=False)
           try:
               my_file_name = text[0:20]
           except:
               my_file_name = "audio"
           tts.save(f"temp/{my_file_name}.mp3")
           return my_file_name, trans_text


       

       if st.checkbox("Arab Text"):
           result, output_text = text_to_speech(in_lang, out_lang, text, tld)
           audio_file = open(f"temp/{result}.mp3", "rb")  
           audio_bytes = audio_file.read()
           
           st.audio(audio_bytes, format="audio/mp3", start_time=0)
       
           
           st.info(f" {output_text}")    
           
   loadez = st.button("RUSSIAN")    
   
   if "loadez_state" not in st.session_state:
        st.session_state.loadez_state= False

   
   if loadez or st.session_state.loade_state:
        st.session_state.loadez_state= True

        try:
            os.mkdir("temp")
        except:
            pass
        
        translator = Translator()
        prediction = model.predict(img_reshape).argmax()     
        res = class_names[np.argmax(model.predict(img))]
        
        text = res

        in_lang = "en"


        out_lang ="ru"


        tld = "com"



        def text_to_speech(in_lang, out_lang, text, tld):
            translation = translator.translate(text, src=in_lang, dest=out_lang)
            trans_text = translation.text
            tts = gTTS(trans_text, lang=out_lang, tld=tld, slow=False)
            try:
                my_file_name = text[0:20]
            except:
                my_file_name = "audio"
            tts.save(f"temp/{my_file_name}.mp3")
            return my_file_name, trans_text


        

        if st.checkbox("Russian Text"):
            result, output_text = text_to_speech(in_lang, out_lang, text, tld)
            audio_file = open(f"temp/{result}.mp3", "rb")  
            audio_bytes = audio_file.read()
            
            st.audio(audio_bytes, format="audio/mp3", start_time=0)
        
            
            st.info(f" {output_text}") 
   

  
   
     
     
            
