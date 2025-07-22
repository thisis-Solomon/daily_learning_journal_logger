import datetime


lesson = input("What did you learn today? ")

def daily_learning_logger(msg):
    now = datetime.datetime.now()
    formatted_timestamp = now.strftime("%Y-%m-%d - %I-%M %p")
    rating = int(input("How productive was your day (1-5): "))
    learning = f"{formatted_timestamp}\n\n{msg}\n\nProductivity Rating: {rating}/5 \n\n"
    with open('learning_journal.txt', "a") as f:
        f.write(learning)
        print("save your learning was saved!")
    
daily_learning_logger(lesson)