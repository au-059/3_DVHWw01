def main():
        time = str(input("What time is it? "))
        new_time = convert(time)

        if new_time >= 7 and new_time <=8:
                print("Breakfast time")
        if new_time >= 12 and new_time <=13:
                print("Lunch time")
        if new_time >= 18 and new_time <=19:
                print("Dinner time")

def convert(time):
        hrs, mins = time.split(":")
        float_mins = float(mins) / 60
        return float(hrs) + float_mins

main()
