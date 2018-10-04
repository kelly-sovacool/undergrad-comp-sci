'''
Author: Kelly Sovacool
Email: kellysovacool@uky.edu
Section: 006
Purpose: Calculate the length of a runway needed for an aircraft based on its take-off velocity and acceleration
Preconditions: Input the take-off velocity of the aircraft in kilometers per hour and the acceleration rate in meters per second squared 
Postconditions: Output the required runway length in meters and feet
Date: 9 Feb. 2015
'''
def main():
    
    #1. Display 'Runway Calculations' and the logo
    print('                            _|_')
    print('Runway Calculations   ---00-(_)-00---')
    print('')
    #2. Prompt the user to enter a velocity (in kilometers per hour)
    velocity_km_hr = float(input('Enter the take-off velocity (km/h): '))
    #3. Prompt the user to enter an acceleration (in meters per second squared)
    acceleration = float(input("Enter the plane's acceleration (m/s^2): "))
    print('')
    
    #4. Create a variable to hold the kilometers to meters conversion factor
    meters_per_kilometer = 1000
    #5. Create a variable to hold the hours to seconds conversion factor
    seconds_per_hour = 3600
    #6. Convert the velocity from kilometers per hour to meters per second
    velocity_m_sec = velocity_km_hr * meters_per_kilometer / seconds_per_hour        
    #7. Calculate the required length of the runway (in meters)
    runway_length_meters = velocity_m_sec**2 / (2 * acceleration)
    #8. Create a variable to hold the meters to feet conversion factor
    feet_per_meter = 3.2808399
    #9. Convert the runway length from meters to feet
    runway_length_feet = runway_length_meters * feet_per_meter
    
    #10. Display the required runway length in both meters and feet
    print("The plane requires a runway at least", round(runway_length_meters, 3), "meters")
    print("or", round(runway_length_feet, 3), "feet long.")

main()

#1. The plane requires a runway at least 1736.111 meters or 5695.903 feet long.
#2. Plane B