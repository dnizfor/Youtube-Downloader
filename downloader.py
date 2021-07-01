from pytube import YouTube


print("""

Youtube Dowloader Free

!!!! Write Exit for Exit !!!!

""")

while True :

    try:
        url = input("Give Me Video URL:  ")
        if url.lower() =="exit" :
            exit()

   
    finally : 
        print("False URL or Command , Tyr Again")        
        url = input("Give Me Video URL:  ")
    
    video = YouTube(url)

    print(video.title)

    right = input("is this your video ? Yes or No ?")
    
    if right.lower() == "yes" :

        stream = video.streams.filter(progressive=True).first()
        stream.download()       
        
        print("""We download video in this document

        !!!! Write Exit for Exit !!!!

        or ...      
        
        
        
        
        """)


    elif right.lower() == "no" :
        
        continue
    elif right.lower() =="exit" :
        exit()
    else :
        print( "FALSE COMMAND PLEASE TRY AGAİN  ")
        continue


    


