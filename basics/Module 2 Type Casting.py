# Bad because input returns string and you can't divide string by float
# height_cm = input('Height converter: Enter your height in cm: ')
# print('Your height in feet is:', height_cm / 30.48)


height_cm = input('Height converter: Enter your height in cm: ')
float_height_cm = float(height_cm)
print('Your height in feet is:', float_height_cm / 30.48)

height_cm = float(input('Height converter: Enter your height in cm: '))
print('Your height in feet is:', height_cm / 30.48)

year_born = int(input('What year were you born? '))
print('You will be', 2100 - year_born, 'in the year 2100.')

temp_c = input('Enter the temperature in Celsius: ')
temp_f = float(temp_c) * 1.8 + 32
temp_statement = str(temp_c) + ' in Celsius equals ' + str(temp_f) + ' in Farenheit. '
print(temp_statement)
