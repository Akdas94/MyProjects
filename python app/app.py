from taipy.gui import Gui
from tensorflow.keras import models
from PIL import Image
import numpy as np

class_names = {
    0: 'airplane',
    1: 'automobile',
    2: 'bird',
    3: 'cat',
    4: 'deer',
    5: 'dog',
    6: 'frog',
    7: 'horse',
    8: 'ship',
    9: 'truck',
}

model = models.load_model("baseline_mariya.keras")
#index = "# Hello from python!" #OR we can use this <h1>Hello from python!</h1>"

def predict_image(model, path_to_img):
    #print(model.summary())
    #print(path_to_img)
    img = Image.open(path_to_img)
    img = img.convert("RGB")
    img = img.resize((32, 32))
    data = np.asarray(img)
    #print("before", data[0][0])
    data = data / 225
    #print("after", data[0][0])
    probs = model.predict(np.array([data])[:1])
    #print(probs)
    top_prob = probs.max()
    top_pred = class_names[np.argmax(probs)]
    
    return top_prob, top_pred
    
content = ""
img_path = "placeholder_image.png"
#image control component
prob = 0
pred = ""

index = """
<|text-center|
<|{"logo.png"}|image|width=25vw|> 

<|{content}|file_selector|extension=.png|>
Select an image from your file system

<|{pred}|>
<|{img_path}|image|> 

<|{prob}|indicator|value={prob}|min=0|max=100|width=25vw|> 
>                                   
"""
#in above we used file_selector to selecte file from our PC
#by using 'extension=.png' we can selecte just png files & img gets change of placeholder_image
#using 'indicator' we can see 0 to 100 range to see is image is matching


#in taipy we use a function called 'On Change Event'
#Which activated by changes in the state of our software ex- uploading our file
#it change 'content with a file we upload

def on_change(state, var_name, var_val):
    if var_name == "content":
        state.img_path = var_val
        top_prob, top_pred = predict_image(model, var_val)
    #print(var_name, var_val)
        state.prob = round(top_prob * 100)  #here we multpled with 100 to convert no. in %
        state.pred = "This is a " + top_pred
        state.img_path = var_val

app = Gui(page=index)

if __name__ == "__main__":
    app.run(use_reloader=True) #using this use_reloader we can reload our page and changes can observe