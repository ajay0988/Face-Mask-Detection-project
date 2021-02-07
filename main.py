from Air_convas import convas
from speak_method import speak
import pywhatkit as kit
import time
from pygame import mixer

#from detect_mask_video import detect_and_predict_mask
time = time.time()
air_canvas = ['air convas', 'air', 'canvas',]
mask_detect = ['mask detection', 'mask detect', 'mask', 'detect']
MSG = ['message', 'msg', 'mess' ]
ytb = ['youtube', 'watch', 'u tube', 'tube', 'utube', 'ytb']
search = ['search', 'find']
def whatsapp():
    u_info = input("Write phone number, message, time hour, time minute\t: ")
    u_info = u_info.split(', ')      
    if '+91' in u_info[0]:           
        kit.sendwhatmsg(u_info[0], u_info[1], int(u_info[2]), int(u_info[3]))
        print("ok")
    else:
        kit.sendwhatmsg_to_group(u_info[0], u_info[1],  int(u_info[2]), int(u_info[3]))
        print("done")

def sendMail(my_mail, my_pass, mail_to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(my_mail, my_pass) # eneter your email and password but you have to enable <less secure app> in your email privacy setting
        server.sendmail(my_mail, mail_to, content) # eneter your email, reciver email, content to send
        server.close()

def play_music(songName):
    mixer.init()
    mixer.music.load(songName)
    mixer.music.play()
                                 
def welcome():
    print (20*'*'+ ' W E L C O M E '+40*'*')
    print("\n\n")
    print("\tplease, select valid feature.."+ "To enable microphone feature press M")
    print("\n\t 1.\t Air convas\t:")    
    print("\n\t 2.\t Mask Detection\t:")
    print("\n\t 3.\t Message\t:")
    print("\n\t 4.\t Search\t:")
    print("\n\t 5.\t watch on youtube\t:")
    
    
         
    print("\n\t press q to Quit")
    
    choice = input()
    #number = [1,2,3,4,5,6,7,8,9,0]
    
    
    #if choice in number:
    u_choice = int(choice)
                           
    if u_choice == 1:
        convas()
  
    elif u_choice == 2:
        from detect_mask_video import detect_mask
        #detect_mask()
        #print("ok")
        
    elif u_choice == 3:        
        whatsapp()       
            
    elif u_choice == 4:
                                     
        user_search = input("what would like to search\t: ")
        kit.search(user_search)
                   
    elif u_choice == 5:
        user_search = input("What would like to watch\t: ")
        kit.playonyt(user_search)
    elif u_choice == 0:
        exit()
     
        
    else:
        print("SORRY!!!, you have selected invalid service.. ")
        print("\n please, select valid service")
        #time.sleep(5)
            
            
    
                                 
welcome()




