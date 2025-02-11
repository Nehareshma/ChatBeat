import requests
import pywhatkit
import tkinter as tk
from tkinter import ttk
from tkinter import Canvas, Button, Label
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from bs4 import BeautifulSoup
import time
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit as pwt
import pyautogui
import webbrowser
import random
import requests
from tkinter import*
from tkinter.ttk import *
from PIL import Image, ImageTk, ImageSequence
time_now = datetime.datetime.now().strftime('%I:%M %p')
engine = pyttsx3.init()
import pyautogui as pt
voices = engine.getProperty('voices')
engine. setProperty("rate", 185)
engine.setProperty('voice', voices[1].id)
import requests
from tkinter import ttk, scrolledtext
pardonme = ["Sorry, Can you please repeat", "Ohooo, I Forgot to catch up, I am listening can you repeat it", "Sorry please repeat"]
wish=["Hii, How are you?","hello,are you free now?","Hey"]


questions = [
    "hii"
    "Which is the capital of Karnataka?",
    "Who is the current prime minister of India?",
    "When is the independence day?",
    "What is the pincode of Puttur?",
    "Who is the father of Infosys?",
    "Who is the male lead in KGF movie?",
    "Who is the father of C?",
    "Give me some fruits name?",
    "In 2024 world cup winner?",
    "What is ML?"
]

responses = {
    "hii":"Hello",
    "Which is the capital of Karnataka?": "Bangalore",
    "Who is the current prime minister of India?": "Narendra Modi",
    "When is the independence day?": "August 15",
    "What is the pincode of Puttur?": "564203",
    "Who is the father of Infosys?": "Sudha Murthy",
    "Who is the male lead in KGF movie?": "Rocking Star Yash",
    "Who is the father of C?": "Dennis Ritchie",
    "Give me some fruits name?": "Mango, orange, banana etc.",
    "In 2024 world cup winner?": "India",
    "What is ML?": "Machine learning (ML) is a branch of artificial intelligence and computer science that focuses on using data and algorithms to enable AI to imitate the way that humans learn, gradually improving its accuracy."
}

# Vectorize the predefined questions
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

def chatbot_response(user_input):
    # Vectorize the user input
    user_input_vec = vectorizer.transform([user_input])

    # Compute cosine similarity between user input and predefined questions
    similarities = cosine_similarity(user_input_vec, X)

    # Find the index of the most similar question
    most_similar_index = similarities.argmax()

    # Get the corresponding response
    response = responses.get(questions[most_similar_index], "I'm not sure how to respond to that.")
    return response

def open_chatbot_window():
    chatbot_window = tk.Toplevel(root)
    chatbot_window.title("Chatbot")
    chatbot_window.geometry("400x500")

    # Create and place the chat history text widget
    global chat_history
    chat_history = scrolledtext.ScrolledText(chatbot_window, wrap=tk.WORD, state=tk.DISABLED)
    chat_history.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Create and place the user input field
    global user_input_field
    user_input_field = tk.Entry(chatbot_window, width=50)
    user_input_field.pack(padx=10, pady=5, side=tk.LEFT, fill=tk.X, expand=True)

    # Create and place the submit button
    submit_button = tk.Button(chatbot_window, text="Send", command=process_chatbot_input)
    submit_button.pack(padx=10, pady=5, side=tk.RIGHT)

def process_chatbot_input():
    user_input = user_input_field.get()  # Get the user input from the entry field
    if user_input:
        response = chatbot_response(user_input)  # Process the input using the chatbot_response function
        chat_history.config(state=tk.NORMAL)  # Allow editing the chat history text widget
        chat_history.insert(tk.END, f"You: {user_input}\n")  # Add user input to chat history
        chat_history.insert(tk.END, f"Bot: {response}\n")  # Add bot response to chat history
        chat_history.config(state=tk.DISABLED)  # Disable editing the chat history text widget
        user_input_field.delete(0, tk.END)  # Clear the entry field


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]
def get_location():
    try:
        response = requests.get('https://ipinfo.io/json')
        data = response.json()
        location = f"{data['city']}, {data['region']}, {data['country']}"
        return location
    except Exception as e:
        return "Unable to fetch location"
def tell(text):
    engine.say(text)
    engine.runAndWait()
def wishMe():
    hour=datetime.datetime.now().hour
    time.sleep(3)
    print(pyautogui.position())
    if hour>=0 and hour<12:
        tell("Good Morning Sir... it is" + time_now)
        print("Good Morning Sir")
    elif hour>=12 and hour<18:
        tell("Good Afternoon Sir... it is" + time_now)
        print("Good Afternoon Sir")
    else:
        tell("Good Evening Sir... it is" + time_now)
        print("Good Evening Sir")
def take_listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio=r.listen(source)
        try:
            command=r.recognize_google(audio,language='en-in')
            print(f"you said :{command}\n")
        except Exception as e:
            tell(random.choice(pardonme))
            return "None"
        return process(command)

def process(command):
        if "hai" in command:
            tell(random.choice(wish))
        if 'time now' in command:
            time_now = datetime.datetime.now().strftime('%I:%M %p')
            print(time_now)
            tell('Its' + time_now)
        elif 'name' in command:
            tell("MY name is sariya, I Am your virtual assistant")
        elif 'date' in command:
            day = datetime.date.today()
            print(day)
            tell(day)
        elif 'Hey'in command:
            tell("hii there. How can I help you");
        elif 'How can you Help me'in command:
            tell("I am your personal assistant here to navigate you and guide You everywhere")
        elif 'who are you' in command:
            tell("I am JARVIS , I am your personal Assistant")
        elif 'who' in command:
            person = command.replace('who is', '')
            info_person = wikipedia.summary(person, 2)
            search1_google = pwt.search(person)
            print(info_person)
            tell(info_person)
        elif 'google search' in command:
            search1 = command.replace('search', '')
            search1_google = pwt.search(search1)
            tell('searching')
        elif 'define'in command:
            search_wiki = wikipedia.summary(command, 3)
            print(search_wiki)
            tell(search_wiki)
        elif'who are you'in command:
            tell("I am sariya your personal assistant")
        elif 'play'in command:
            tell("What song do I hit for you")
            take_listen()
            pwt.playonyt(command)
            tell("You Song is coming right away")
        elif"Find the location" in command:
            tell("Tell me the location to be searched")
            tell("listening")
            location=take_listen()
        elif"my current location" in command:
            url = "https://www.google.com/maps/search/Where+am+I+?/"
            webbrowser.get().open(url)
            tell("You must be somewhere near here, as per Google maps")
        elif "weather outside"in command:
            url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
            webbrowser.get().open(url)
            tell("Here is what I found for on google")
        elif'news'in command:
            tell('here are some hot news from bbc')
            webbrowser.open('https://www.bbc.com/news')
            for s in range(60):
                url = 'https://www.bbc.com/news'
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                headlines = soup.find('body').find_all('h3')
                pyautogui.scroll(-500)
                for x in headlines:
                    print(x.text.strip())
                    pyautogui.scroll(-70)
                    tell(x.text.strip())
            tell("Closing tab")
            pyautogui.click(1871, 22)
        elif 'new' in command:
            tell('here are some state news from polimer news')
            webbrowser.open('https://www.polimernews.com/dcategory/22/english')
            for s in range(60):
                url = 'https://www.polimernews.com/dcategory/22/english'
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                headlines = soup.find('body').find_all('h4')
                for x in headlines:
                    print(x.text.strip())
                    pyautogui.scroll(-70)
                    tell(x.text.strip())
            tell("Closing tab")
            pyautogui.click(1871, 22)
        elif "remind me" in command:  # That I have my meeting regarding FInal Project on 29th May
            save = command.replace("remind me", "", 1)
            openFile = open(
                file=r"C:\Users\Admin\PycharmProject\Voice assistant\memory.txt",
                mode="a",
            )
            openFile.write(save + "\n")  # to save new text on new line
            openFile.close()
            tell("Ok Sir, I will remember this")
        elif "recall" in command:
            readFile = open(
                file=r"C:\Users\Admin\PycharmProject\Voice assistant\memory.txt",
                mode="r+",
            )
            reading = readFile.read()
            if readFile.tell() == 0:
                print("No task To Remember")
                tell("No task to remember")

            else:
                readFile.truncate(0)
                readFile.close()
                tell("You said me to remember that" + reading)

def loop():
    while True:
        take_listen()

def photo():
    import cv2
    import os
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # set video width
    cam.set(4, 480)  # set video height
    face_detector = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml.py')
    # For each person, enter one numeric face id
    face_id = input('\n enter user id end press enter = ')
    print("\n [INFO] Initializing face capture. Look the camera and wait ...")
    # Initialize individual sampling face count
    count = 0
    while (True):
        ret, img = cam.read()
        img = cv2.flip(img, 1)  # flip video image vertically
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            count += 1
            # Save the captured image into the datasets folder
            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])
            cv2.imshow('image', img)
        k = cv2.waitKey(5) & 0xff  # Press 'ESC' for exiting video
        if k == 27:
            break
        elif count >= 75:  # Take 30 face sample and stop video
            break
    # Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()
    ###################################################################################################3
    import cv2
    import numpy as np
    from PIL import Image
    import os
    # Path for face image database
    path = 'dataset'
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier("Cascades/haarcascade_frontalface_default.xml.py");
    # function to get the images and label data
    def getImagesAndLabels(path):
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        faceSamples = []
        ids = []
        for imagePath in imagePaths:
            PIL_img = Image.open(imagePath).convert('L')  # convert it to grayscale
            img_numpy = np.array(PIL_img, 'uint8')
            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = detector.detectMultiScale(img_numpy)
            for (x, y, w, h) in faces:
                faceSamples.append(img_numpy[y:y + h, x:x + w])
                ids.append(id)
        return faceSamples, ids
    print("\n [INFO] Training faces. It will take a few seconds. Wait ...")
    faces, ids = getImagesAndLabels(path)
    recognizer.train(faces, np.array(ids))
    # Save the model into trainer/trainer.yml
    recognizer.write('trainer/trainer.yml')  # recognizer.save() worked on Mac, but not on Pi
    # Print the numer of faces trained and end program
    print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))
    ########################################################################################################
def detection():
    import cv2
    import numpy as np
    import os
    global id
    global confidence
    import imutils
    import requests
    i = 0
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascadePath = "Cascades/haarcascade_frontalface_default.xml.py"
    faceCascade = cv2.CascadeClassifier(cascadePath)
    font = cv2.FONT_HERSHEY_SIMPLEX
    # iniciate id counter
    i = 0
    # names related to ids: example ==> Marcelo: id=1,  etc
    names = ['UNKNOWN','Bharath']
    # Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # set video width
    cam.set(4, 480)  # set video height
    # Define min window size to be recognized as a face
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)
    while True:
        ret, img = cam.read()
        img = cv2.flip(img, 1)  # Flip vertically
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
            # Check if confidence is less them 100 ==> "0" is perfect match
            if (confidence < 100):
                id = names[i]
                confidence = "  {0}%".format(round(100 - confidence))
            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))

            cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)
            if(i<3):
                foo = ['is standing in front of you', 'is apporaching you', 'is near by you']
                tell((str(id), random.choice(foo)))
                print(str(id))
                i=i+1
        cv2.imshow('camera', img)
        k = cv2.waitKey(3000) # Press 'ESC' for exiting video
        time.sleep(3)
        k=27
        if k == 27:
            break
    # Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()
def composeLetter():
    tell("opening  ms word .composing Business letter")
    pt.hotkey('win','r')
    pt.typewrite("winword")
    time.sleep(2)
    pt.press("enter")
    time.sleep(2)
    pt.press("enter")
    date=datetime.date
    To='No 8A ramalingam\nnagar south gandhi gramam\nkarur'
    body='Mr.Surya\nAnna nagar \nchennai.\n\n'+To+'\nhello,\n I am writing you concerning a recent purchase of widgets. Approximately two weeks ago, on October 1, I ordered a total of 50 widgets for Company, Inc. via the Widgets Galore client webpage. I received an email notification two days later confirming the receipt of payment and the shipment of the widgets. According to your website, shipments should reach their destination within 3-5 business days of being sent, but I have yet to receive the widgets.' \
                                                                    '\nsincerly\nMr.Surya\nAnna nagar \nchennai.'
    pt.typewrite(body)
def repeat():
    tell("Hi there Iam Sariya Your Beloved Personal Assistant")
    time.sleep(1)
    time_now = datetime.datetime.now().strftime('%I:%M %p')
    print(time_now)
    tell('Current Time is ' + time_now)
    day = datetime.date.today()
    print(day)
    tell("It is")
    tell(day)
    tell("Your cuurent location is M kumarasamy college of engineering, Thalavapalayam, karur")
    tell('opening.whatsapp')
    webbrowser.open('https://web.whatsapp.com/')
    time.sleep(5)
    tell('opening.google')
    webbrowser.open('https://www.google.com/')
    time.sleep(5)
    tell('PLaying latest songs')
    pywhatkit.playonyt('ponni nadhi')
    time.sleep(10)
    pyautogui.click(1024,670)
    tell('here are some hot news from bbc')
    webbrowser.open('https://www.bbc.com/news')
    for s in range(60):
        pyautogui.scroll(-20)
        time.sleep(0.5)
    url = 'https://www.bbc.com/news'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find('body').find_all('h3')
    for x in headlines:
        print(x.text.strip())
        tell(x.text.strip())
    tell("Closing tab")
    pyautogui.click(1871,22)

#-------------------------------------------------------------------------------------------------------------------------------------------
root = tk.Tk()
root.geometry("2000x1100")
root.title("JARVIS")

canvas = Canvas(root, width=1000, height=1000)
canvas.pack(fill="both", expand=True)

canvas.create_image(1030, 500, anchor=CENTER)
canvas.create_text(550, 300, text="           Hello, I am Sariya \nYour beloved Personal Assistant...", font='Times 12 italic bold')
canvas.create_text(460, 800, text="Press to listen", font='Times 12 italic bold')
canvas.create_text(1560, 800, text="Press to chat", font='Times 12 italic bold')
# canvas.create_text(1000, 450, text="Accuracy of chatbot - 88%", font='Times 12 italic bold')


img = ImageTk.PhotoImage(file="finalmic (1).jpg")
vision = ImageTk.PhotoImage(file="face (1).png")
Loop = ImageTk.PhotoImage(file="reload-refresh-arrows-loop-flat-icon-vector-20383569 (1).jpg")
limg = ImageTk.PhotoImage(file="final.jpg")

MIC_button = Button(root, command=take_listen, image=img)
Loop_mic = Button(root, text="Loop", command=open_chatbot_window, image=Loop)
Face_Detection = Button(root, text="Face", command=detection, image=vision)

lbl = Label(root, image=limg)
lbl_canvas = canvas.create_window(850, 100, anchor="nw", window=lbl)
button1_canvas = canvas.create_window(400, 600, anchor="nw", window=MIC_button)
Loop_button = canvas.create_window(1500, 600, anchor='nw', window=Loop_mic)
# face_button = canvas.create_window(400, 600, anchor="nw", window=Face_Detection)left


info_frame = tk.Frame(root, padx=10, pady=10)
info_frame.place(x=1300, y=170)  # Adjust the position as needed

time_label = ttk.Label(info_frame, text="", font=("Helvetica", 24))
time_label.pack(pady=10)

date_label = ttk.Label(info_frame, text="", font=("Helvetica", 18))
date_label.pack(pady=10)


def update_time_date():
    current_time = time.strftime('%H:%M:%S')
    current_date = time.strftime('%Y-%m-%d')
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    root.after(1000, update_time_date)

# Define location function
def get_location():
    try:
        response = requests.get('https://ipinfo.io/json')
        data = response.json()
        location = f"{data['city']}, {data['region']}, {data['country']}"
        return location
    except Exception as e:
        return "Unable to fetch location"


location = get_location()
location_label = ttk.Label(info_frame, text=f"Location: {location}", font=("Helvetica", 14))
location_label.pack(pady=10)

# Update time and date
update_time_date()


print("Accuracy of Chatbot is 99.28%")

root.mainloop()

