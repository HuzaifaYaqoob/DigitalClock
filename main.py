import tkinter as tk
import time
import calendar
import random




colors_list = ['#F3B63A' , '#E44236' , '#74B9FF' , '#D63031' , '#E84342' , '#FF3031' , '#3498DB' , '#2475B0' , '#74B9FF' , '#0A79DF', '#4834DF',
    '#BA2F16' , '#EC4849' , '#FF3E4D' , '#192A56' , '#67E6DC' , '#25CCF7' , '#6A89CC' , '#0ABDE3' , '#0A3D62' , '#10A881' , '#7CEC9F' , '#45CE30' , 
    '#A3CB37' , '#019031' , '#F4C724' , '#FAC42F' , '#FBD28B' , '#FFF222' , '#F3CC79' , '#FBD28B' , '#F3B431' , '#E5B143' , '#DFAF2B' , '#99AAAB' ,
    '#333945' , '#2C3335' , '#DAE0E2' , '#8395A7' , '#4C4B4B' , '#7B8788' , '#758AA2' , '#A4B0BD' , '#777E8B' , '#99AAAB' , '#EAF0F1' , '#E74292' ,
    '#01CBC6' , '#01CBC6' , '#BB2CD9' , '#BB2CD9' , '#BB2CD9' , '#8B78E6' , '#00CCCD' , '#1287A5' , '#EA7773' , '#2B2B52' , '#F5BCBA'
]



# ========================== MAIN WINDOW 
root = tk.Tk()
root.title('Digital Calendar/Clock')
root.geometry("1100x500+200+100")
root.resizable(width=0 , height=0)
root.config(bg='#758AA2')
root.iconphoto() # here you can add your software icon.. yet i have no icon in my folder
# using iconphoto you can also add png formate image

# ========================================= FUNCTIONALITY HERE 


def current_time():
    shuffling_color_lit = random.shuffle(colors_list)
    # Time now
    hour_now = time.strftime('%H')
    minute_now = time.strftime('%M')
    second_now = time.strftime('%S')
    
    # TODAY DATE 
    date_day = time.strftime('%d')
    date_month = time.strftime('%m')
    date_year = time.strftime('%y')

    month_name = calendar.month_name[int(date_month)]


    time_status_ = 'AM'

    if int(hour_now) >= 12:
        hour_box.config(text=(int(hour_now)-12))
        status_box.config(text='PM')
    

    if 17 > int(hour_now) >= 12:
        status_lable.config(text='NOON')
    elif 21 > int(hour_now) >= 17:
        status_lable.config(text='Evening')
    elif 24 > int(hour_now) >= 21:
        status_lable.config(text='NGHT')
    else:
        status_lable.config(text='MORNING')





    # ADD TIME IN TO OUR DESIGN 
    mint_box.config(text=minute_now)
    second_box.config(text=second_now , bg=colors_list[0])
    second_lable.config(bg=colors_list[0])

    # ADDING DATES IN DESIGN ? CALENDAR 

    today_date_day.config(text=date_day)
    today_date_month.config(text=month_name)
    today_date_year.config(text=f"20{date_year}")






    second_box.after(1000 , current_time) # This line will run this function after every 1 second ,,, 1000 mili ssecond = 1 second



# ============================================= END 



# ====================================== DESIGNING PART  

# height of each box = 150
# width of each box = 150
# width of small boxes = 150 
# height is approximatly 
# horizontal margin = 20
# vertical margin = 10

X_Axis = 260  # START POINT 
Y_Axis = 100 # VERTICAL START POINT  


#/////////////////////////////// FIRST COLUMN
hour_box = tk.Label(root , font=("Calibri" , 40 , 'bold') , bg='#74B9FF' , fg="black")
hour_box.place(x=X_Axis , y=Y_Axis , width=150 , height=150)

hour_lable = tk.Label(root , text='Hour' ,  font=("Calibri" , 20 , 'bold') , bg='#74B9FF' , fg="black")
hour_lable.place(x=X_Axis , y=(Y_Axis+150+10) , width=150 , height=30)


today_date_day = tk.Label(root ,  font=("Calibri" , 20 , 'bold') , bg='#74B9FF' , fg="black")
today_date_day.place(x=X_Axis , y=(Y_Axis+30+10+150+10) , width=150 , height=30)





# ////////////////////////////SECOND COLUMN 

mint_box = tk.Label(root , font=("Calibri" , 40 , 'bold') , bg='#1BCA9B' , fg="black")
mint_box.place(x=(X_Axis+150+20), y=Y_Axis , width=150 , height=150)

mint_lable = tk.Label(root , text='Minutes' ,  font=("Calibri" , 20 , 'bold') , bg='#1BCA9B' , fg="black")
mint_lable.place(x=(X_Axis+150+20) , y=(Y_Axis+150+10) , width=150 , height=30)


today_date_month = tk.Label(root ,  font=("Calibri" , 20 , 'bold') , bg='#1BCA9B' , fg="black")
today_date_month.place(x=(X_Axis+150+20) , y=(Y_Axis+30+10+150+10) , width=150 , height=30)



# /////////////////////////////////////// THIRD COLUMN


second_box = tk.Label(root , font=("Calibri" , 40 , 'bold') , bg='#FBD28B' , fg="black")
second_box.place(x=(X_Axis+2*150+2*20), y=Y_Axis , width=150 , height=150)

second_lable = tk.Label(root , text='Seconds' ,  font=("Calibri" , 20 , 'bold') , bg='#FBD28B' , fg="black")
second_lable.place(x=(X_Axis+2*150+2*20), y=(Y_Axis+150+10) , width=150 , height=30)


today_date_year = tk.Label(root ,  font=("Calibri" , 20 , 'bold') , bg='#FBD28B' , fg="black")
today_date_year.place(x=(X_Axis+2*150+2*20) , y=(Y_Axis+30+10+150+10) , width=150 , height=30)



# ////////////////////// FORTH COLUMN


status_box = tk.Label(root , font=("Calibri" , 40 , 'bold') , bg='#E74292' , fg="black")
status_box.place(x=(X_Axis+3*150+3*20), y=Y_Axis , width=150 , height=150)

status_lable = tk.Label(root ,  font=("Calibri" , 20 , 'bold') , bg='#E74292' , fg="black")
status_lable.place(x=(X_Axis+3*150+3*20), y=(Y_Axis+150+10) , width=150 , height=30)


today_date_ = tk.Label(root , text='DATE' ,  font=("Calibri" , 20 , 'bold') , bg='#E74292' , fg="black")
today_date_.place(x=(X_Axis+3*150+3*20) , y=(Y_Axis+30+10+150+10) , width=150 , height=30)





current_time()

root.mainloop()