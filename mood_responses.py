# Module file for 'Modules and Data Handling.py'

def mood_response(mood):
    if mood == "happy":
        return "It's a good day to be a good day!"
    elif mood == "sad":
        return "The sun will come out tomorrow."
    elif mood == "excited":
        return "Be excited for all the great things to come!"
    elif mood == "angry":
        return "For every minute you are angry you lose sixty seconds of happiness."
    elif mood == "tired":
        return "You can't pour from an empty cup.  Take care of yourself first!"
    else:
        return "Sorry, I don't know that mood."