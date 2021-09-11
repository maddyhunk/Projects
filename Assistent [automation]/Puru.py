import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
from time import sleep


engine = pyttsx3.init('sapi5') #Microsoft provides an API i.e. sapi5
voices = engine.getProperty('voices') #getting all the availabl voices
print(f"Voices are : {voices}")
engine.setProperty('voice', voices[1].id)#setting up the voice property of the engine from the available voices
#print(voices[0].id)


#Speak fucntion having audio as it's parameter , audio stores the string
def speak(audio):  
    engine.say(audio) #system will speakup
    engine.runAndWait()

#Wish me function wish me as per the present time using datetime module
def wishMe():
    hour = int(datetime.datetime.now().hour) #we get the hour , typecasted in int

    #Conditons for Wish as per the times

    if (hour >= 0 and hour < 12):
        speak("Good Morning Sir.")
    elif(hour >= 12 and hour < 18):
        speak("Good Afternoon Sir.")
    else:
        speak("Good Evening Sir.")

    speak("I'm Puru , Your current working AI. What i can do for you ?")

#Takecommand fucntion
def takeCommand():# it takes microphone input from the user and returns string output
    r = sr.Recognizer()  # Recognizer() class helps to recognize the audio(voice speaked by the user)
    mic = sr.Microphone() #Microphone() class helps to record/listen our voice
    with mic as source:
        speak("Listneing...")
        print("Listneing...")
        # r.pause_threshold = 1
        # r.adjust_for_ambient_noise(source)
       
        r.record(source,duration=2)
        # # print("Listneing...")
        # # speak("Listneing...")
        # # r.pause_threshold = 1
        # # speak("Listneing...")
        # # print("Listneing...")
        audio = r.listen(source)
        

    try:
        print("Recognizining...")
        query = r.recognize_google(audio, language='en-in')# Performs speech recognition on ``audio_data`` (an ``AudioData`` instance), using the Google Speech Recognition API.

        print(f"User said :- {query}\n")
        speak(f"User said :- {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again sir!!!")
        speak("Say that again sir!!!")

        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('experiment.dm.05@gmail.com', 'Madhav_sharma05') #i Have given access to Less secure apps
    server.sendmail('experiment.dm.05@gmail.com', to, content)
    server.close()


def step():
    speak("Sir,Do you want to move ahead or Exit from here?")
    print("Sir,Do you want to move ahead or Exit from here?")
    speak("Please write  move ahead , to continue  OR Please write terminate to exit")
    print("Please write  move ahead , to continue  OR Please write terminate to exit")

    n = input("")
    n = n.lower()


    if (n =="move ahead"):
        speak("OK , Sir i'm moving ahead as per your order")
    elif(n =="terminate"):
        speak("OK , Sir i'm Quitting it here as per your order")
        sleep(1)
        exit(0)
    takeCommand()
    
        
  
    
# def calling():
#     print("Sir, Can you tell me your name")
#     speak("Sir, Can you tell me your name")
#     n = input("")
#     speak(f"Your Name is {n}")

if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()

        # logic for executong tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak("Accoding to Wikipedia")
            print(results)
            speak(results)

        # elif 'name' in query:
        #     calling()

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
            query = query.replace('open youtube', "")
            step()

        elif 'open google' in query:
            webbrowser.open('google.com')
            query = query.replace('open youtube', "")

        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')
            query = query.replace('open stackoverflow', "")

        elif 'open whatsapp' in query:
            programs_dir = 'C:\\Users\\hunkm\\AppData\\Local\\WhatsApp\\WhatsApp.exe'
            os.startfile(os.path.join(programs_dir))
            query = query.replace('open whatsapp', "")

        elif 'open visual studio code' in query:
            programs_dir = "C:\\Users\\hunkm\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(os.path.join(programs_dir))
            query = query.replace('open visual studio code', "")


        # elif 'open fifa 19' in query: 
        #     programs_dir = "D:\\Games\\FIFA 19\\FIFA19.exe"
        #     os.startfile(os.path.join(programs_dir))
        #     query = query.replace('open fifa 19' , "")



        elif 'play movies' in query:
            movies_dir = 'D:\\hunkm\\MOVIES' #my movies folder's path
            movie = os.listdir(movies_dir) #listing my all movies/movies folders
            print(movie) #printing  all the movies/moives folder
            speak(movie) #speaking  all the movies/moives folder
            speak("Which one you want to select Sir?")
            print("Which one you want to select Sir?")
            a = input("") #Taking movie name from the user
            i = 0
            
            while(i < 3): 
                if(a == movie[i]):
                    os.startfile(os.path.join(movies_dir, movie[i])) #starting/playing our desried movie/movie folder
                    # os.startfile(os.path.join(word_dir, word[i]))
                    speak("I have played your wished movie sir. What can i do now?")
                    break
                else:
                    i = i + 1
            query = query.replace('play movies', "")
            

        elif 'word cloud' in query:
            word_dir = 'D:\\hunkm\\CODING\\SHORT-PROJECTS\\Project no 1 (Wordcloud)'
            word = os.listdir(word_dir)
            print(word)
            speak(word)
            speak("Which one you want to select Sir?")
            print("Which one you want to select Sir?")
            a = input("")
            i = 0
            while(i < 4):
                if(a == word[i]):
                    os.startfile(os.path.join(word_dir, word[i]))
                    speak("Sir i have done your task , what i can do now?")
                    break
                else:
                    i = i + 1
            query = query.replace('wordcloud', "")

        elif 'automation' in query:
            auto_dir = 'D:\\hunkm\\CODING\\SHORT-PROJECTS\\Project no 3(Auto-Mation)'
            auto = os.listdir(auto_dir)
            print(auto)
            speak(auto)
            speak("Which one you want to select Sir?")
            print("Which one you want to select Sir?")
            a = input("")
            i = 0
            while(i < 7):
                if(a == auto[i]):
                    os.startfile(os.path.join(auto_dir, auto[i]))
                    speak("Sir i have done your task , what i can do now?")
                    break
                else:
                    i = i + 1

            query = query.replace('automation', "")

        
        
        
        
        elif 'the time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(str_time)
            speak(f"Sir,The time is :- {str_time}")
            query = query.replace('the time', "")

        elif 'the date' in query:
            str_date = datetime.datetime.now().date()
            print(str_date)
            speak(f"Sir,The date is :- {str_date}")
            query = query.replace('the date', "")

        
        
        
        elif 'email' in query:
            try:
                speak("What should i say? Please note me down.")
                content = takeCommand()
                print("Sir , To whom you want to send E-mail ?")
                speak("Sir , To whom you want to send E-mail ?")
                speak("Please write the E-Mail of the USer :- ")
                email = input("")
                to = email
                sendEmail(to, content)
                print("Congrats.....Sir,Email has been sent")
                speak("Congrats.... Sir,Email has been sent")

            except Exception as e:
                print(e)
                speak("Sorry Sir , I can't able to send the mail.....")

        
        
        
        elif 'exit' in query:
            query = query.replace('exit', "")
            speak("User wants to exit")
            speak(" Call me again for your help.")
            exit(0)

        elif 'bye' in query:
            query = query.replace('bye', "")
            speak("Bye Sir have a good time ahead!!")
            speak(" Call me again for your help.")
            exit(0)

        elif 'thankyou' in query:
            query = query.replace('thankyou', "")
            print("Sir, It's my duty to help you out in any possible way.")
            speak("Sir, It's my duty to help you out in any possible way.")
            sleep(5)
            print("I encourage you Sir to improve me with your further positive efforts")
            speak("I encourage you Sir to improve me with your further positive efforts")
            exit(0)
        elif 'thank you' in query:
            query = query.replace('thank you', "")
            print("Sir, It's my duty to help you out in any possible way.")
            speak("Sir, It's my duty to help you out in any possible way.")
            sleep(2)
            print("I encourage you Sir to improve me with your further positive efforts.")
            speak("I encourage you Sir to improve me with your further positive efforts.")
            exit(0)