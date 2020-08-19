
# coding: utf-8

# In[ ]:


from pygame import mixer

mixer.init()
mixer.music.load("Nmae of the song.mp3")
mixer.music.set_volume(0.7)
mixer.music.play()
while True:
    print("Press 'p' to Pause, 'r' to Resume")
    print("\nPress 'e' to exit the player")
    
    query = input(" ")
    
    if query == 'p':
        mixer.music.pause()
    elif query == 'r':
        mixer.music.unpause()
    elif query == 'e':
        mixer.music.stop()
        break

