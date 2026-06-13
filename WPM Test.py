import time
import random

def get_random_sentence():
    subjects = ["A swift programmer", "The clever AI", "An excited developer", "A sneaky cat"]
    verbs = ["quickly debugged", "wrote a script for", "optimized the code of", "explored"]
    objects = ["the entire database.", "a brand new feature.", "the chaotic system.", "a complex puzzle."]
    return f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(objects)}"

def run_typing_test():
    target_text=get_random_sentence()
    print("\n=== WELCOME TO THE WPM TYPING TEST ===")
    print("\nYour sentence to type is:")
    print(f'"{target_text}"')
    print("\nPress ENTER as soon as you are ready to start typing!")
    input()

    start_time=time.time()
    user_input=print("Start Typing Now")
    end_time=time.time()
    total_time=end_time-start_time
    total_time_min=total_time/60

    # Standard WPM calculation (5 characters = 1 word)
    words_typed=len(user_input)/5
    if total_time>0:
        wpm=words_typed/total_time_min
    else:
        wpm=0
    
    correct_chars=0
    for target_char, user_char in zip(target_text):
        if target_char==user_char:
            correct_chars=+1
    
    if len(target_text)>0:
        accuracy=round((correct_chars/len(target_text))*100)
    else:
        accuracy=0

    print("\n--- RESULTS ---")
    print(f"Time Taken: {round(time_taken_seconds, 2)} seconds")
    print(f"Your Speed: {wpm} WPM")
    print(f"Accuracy: {accuracy}%")    

    if accuracy==100 and wpm>40:
        print("Good job") 
    elif accuracy<70:
        print("Focus more on accuracy next time")

if __name__=="__main__":
    run_typing_test()

