warning_alert = True

while warning_alert:
    user_input = input("What is the speed of the wind(in mph)? ")
    
    if user_input == 'off':
        print("Exiting the program. Goodbye.")
        warning_alert = False
        
    else:
        try:
            wind_speed = int(user_input)
        
            def hurricane_warning():
                
                if wind_speed >= 157:
                    print(f"Tropical storms with winds at {wind_speed}mph are Category 5 hurricanes")
                elif wind_speed >= 130:
                    print(f"Tropical storms with winds at {wind_speed}mph are Category 4 hurricanes")
                elif wind_speed >= 111:
                    print(f"Tropical storms with winds at {wind_speed}mph are Category 3 hurricanes")
                elif wind_speed >= 96:
                    print(f"Tropical storms with winds at {wind_speed}mph are Category 2 hurricanes")
                elif wind_speed >= 74:
                    print(f"Tropical storms with winds at {wind_speed}mph are Category 1 hurricanes")
                elif wind_speed >=39:
                    print("This storm is a Tropical Storm")
                else:
                    print("Tropical depression or less")
            
       
            hurricane_warning()
        except ValueError:
            print("Invalid input. Please enter a valid number or 'off'.")


