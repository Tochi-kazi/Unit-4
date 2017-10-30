# Created by: Tochukwu Iroakazi
# Created on: Oct 2016
# Created for: ICS3U
# This program displays fahrenhiet


def calculate_fahrenhiet(celcius):
    fahrenhiet = (1.8) * celcius + 32
    print(fahrenhiet)

celcius = input('Enter the tempurature in degrees celcius: ')
calculate_fahrenhiet(celcius)
