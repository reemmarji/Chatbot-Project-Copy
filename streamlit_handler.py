import psutil 

def kill_st():
#Find Streamlit processes
    streamlit_processes = [] 
    for proc in psutil.process_iter(['pid', 'name']): 
        if proc.info['name'] == 'streamlit': 
            streamlit_processes.append(proc)
    #Terminate Streamlit processes 
    for proc in streamlit_processes: proc.terminate()