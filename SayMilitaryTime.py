from preferredsoundplayer import soundplay
import sys
from gtts import gTTS

def hour_converter(hours):
    num_words = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve",
        13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 21: "twenty-one",
        22: "twenty-two", 23: "twenty-three"
    }
    if hours < 10:
        return "zero " + num_words[hours]
    return num_words[hours]

def minute_converter(minute):
    num_words = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve",
        13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
        20: "twenty", 30: "thirty", 40: "forty", 50: "fifty"
    }
    
    if minute == 0:
        return "hundred"
    
    elif minute < 20 or minute % 10 == 0:
        return num_words[minute]
    
    else:
        tens = minute // 10 * 10
        ones = minute % 10
        return num_words[tens] + "-" + num_words[ones]

def split_time(mil_time):
    if len(mil_time) != 3 and len(mil_time) != 4:
        print("Invalid 1st command line argument. Must be a 3 or 4 digit military time.") #verify its 3 or 4 digits.
        sys.exit()

    try:
        time_num = int(mil_time) #verify has only digits
        
    except ValueError:
        print("Invalid 1st command line argument. Should contain only digits.") #judging accent has vaild number.
        sys.exit()

    hours = time_num // 100
    minutes = time_num % 100

    if hours > 23:
        print("Invalid 1st command line argument. Hours cannot be more than 23.") #verify hours not exceeding 23.
        sys.exit()

    if minutes > 59:
        print("Invalid 1st command line argument. Minutes cannot be more than 59.") #verify hours not excedding 59.
        sys.exit()

    return hours, minutes


def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3: #judging command line has vaild input
        print("You need to provide command line inputs.") 
        print("Example Input: python3 SayMilitaryTime.py 1535 IND")
        sys.exit()
    
    mil_time = sys.argv[1]
    
    if len(sys.argv) == 3:
        acc = sys.argv[2].upper() 
            
    else:
        acc = 'USA'
        
    acc_lists = ['IND', 'AUS', 'USA']

    if acc not in acc_lists: #judging accent has invaild input
        print("Invalid 2nd argument. Must be one of IND, AUS, USA")
        sys.exit()
        
    elif acc == 'IND':
        top = 'co.in'
        
    elif acc == 'AUS':
        top = 'com.au'
        
    elif acc == 'USA':
        top = 'us'

    hours, minutes = split_time(mil_time)

    final_hours = hour_converter(hours)
    final_minutes = minute_converter(minutes)

    if minutes == 0:
        time_final = f"{final_hours} hundred hours"
        
    else:
        time_final = f"{final_hours} hundred {final_minutes} hours"

    print("Military time:", time_final)

    voice = gTTS(text=time_final, lang='en', tld=top)
    voice.save("SayMilitaryTime.mp3")
    
    soundplay("SayMilitaryTime.mp3", block=True)

if __name__ == "__main__":
    main()
