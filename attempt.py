import os
import random
from subprocess import call

countries = [
    ('United States'),
    ('Afghanistan'),
    ('Albania'),
    ('Algeria'),
    ('American Samoa'),
    ('Andorra'),
    ('Angola'),
    ('Anguilla'),
    ('Antarctica'),
    ('Antigua And Barbuda'),
    ('Argentina'),
    ('Armenia'),
    ('Aruba'),
    ('Australia'),
    ('Austria'),
    ('Azerbaijan'),
    ('Bahamas'),
    ('Bahrain'),
    ('Bangladesh'),
    ('Barbados'),
    ('Belarus'),
    ('Belgium'),
    ('Belize'),
    ('Benin'),
    ('Bermuda'),
    ('Bhutan'),
    ('Bolivia'),
    ('Bosnia And Herzegowina'),
    ('Botswana'),
    ('Bouvet Island'),
    ('Brazil'),
    ('Brunei Darussalam'),
    ('Bulgaria'),
    ('Burkina Faso'),
    ('Burundi'),
    ('Cambodia'),
    ('Cameroon'),
    ('Canada'),
    ('Cape Verde'),
    ('Cayman Islands'),
    ('Central African Rep'),
    ('Chad'),
    ('Chile'),
    ('China'),
    ('Christmas Island'),
    ('Cocos Islands'),
    ('Colombia'),
    ('Comoros'),
    ('Congo'),
    ('Cook Islands'),
    ('Costa Rica'),
    ('Cote D`ivoire'),
    ('Croatia'),
    ('Cuba'),
    ('Cyprus'),
    ('Czech Republic'),
    ('Denmark'),
    ('Djibouti'),
    ('Dominica'),
    ('Dominican Republic'),
    ('East Timor'),
    ('Ecuador'),
    ('Egypt'),
    ('El Salvador'),
    ('Equatorial Guinea'),
    ('Eritrea'),
    ('Estonia'),
    ('Ethiopia'),
    ('Falkland Islands (Malvinas)'),
    ('Faroe Islands'),
    ('Fiji'),
    ('Finland'),
    ('France'),
    ('French Guiana'),
    ('French Polynesia'),
    ('French S. Territories'),
    ('Gabon'),
    ('Gambia'),
    ('Georgia'),
    ('Germany'),
    ('Ghana'),
    ('Gibraltar'),
    ('Greece'),
    ('Greenland'),
    ('Grenada'),
    ('Guadeloupe'),
    ('Guam'),
    ('Guatemala'),
    ('Guinea'),
    ('Guinea-bissau'),
    ('Guyana'),
    ('Haiti'),
    ('Honduras'),
    ('Hong Kong'),
    ('Hungary'),
    ('Iceland'),
    ('India'),
    ('Indonesia'),
    ('Iran'),
    ('Iraq'),
    ('Ireland'),
    ('Israel'),
    ('Italy'),
    ('Jamaica'),
    ('Japan'),
    ('Jordan'),
    ('Kazakhstan'),
    ('Kenya'),
    ('Kiribati'),
    ('North Korea'),
    ('South Korea'),
    ('Kuwait'),
    ('Kyrgyzstan'),
    ('Laos'),
    ('Latvia'),
    ('Lebanon'),
    ('Lesotho'),
    ('Liberia'),
    ('Libya'),
    ('Liechtenstein'),
    ('Lithuania'),
    ('Luxembourg'),
    ('Macau'),
    ('Macedonia'),
    ('Madagascar'),
    ('Malawi'),
    ('Malaysia'),
    ('Maldives'),
    ('Mali'),
    ('Malta'),
    ('Marshall Islands'),
    ('Martinique'),
    ('Mauritania'),
    ('Mauritius'),
    ('Mayotte'),
    ('Mexico'),
    ('Micronesia'),
    ('Moldova'),
    ('Monaco'),
    ('Mongolia'),
    ('Montserrat'),
    ('Morocco'),
    ('Mozambique'),
    ('Myanmar'),
    ('Namibia'),
    ('Nauru'),
    ('Nepal'),
    ('Netherlands'),
    ('Netherlands Antilles'),
    ('New Caledonia'),
    ('New Zealand'),
    ('Nicaragua'),
    ('Niger'),
    ('Nigeria'),
    ('Niue'),
    ('Norfolk Island'),
    ('Northern Mariana Islands'),
    ('Norway'),
    ('Oman'),
    ('Pakistan'),
    ('Palau'),
    ('Panama'),
    ('Papua New Guinea'),
    ('Paraguay'),
    ('Peru'),
    ('Philippines'),
    ('Pitcairn'),
    ('Poland'),
    ('Portugal'),
    ('Puerto Rico'),
    ('Qatar'),
    ('Reunion'),
    ('Romania'),
    ('Russian Federation'),
    ('Rwanda'),
    ('Saint Kitts And Nevis'),
    ('Saint Lucia'),
    ('St Vincent/Grenadines'),
    ('Samoa'),
    ('San Marino'),
    ('Sao Tome'),
    ('Saudi Arabia'),
    ('Senegal'),
    ('Seychelles'),
    ('Sierra Leone'),
    ('Singapore'),
    ('Slovakia'),
    ('Slovenia'),
    ('Solomon Islands'),
    ('Somalia'),
    ('South Africa'),
    ('Spain'),
    ('Sri Lanka'),
    ('St. Helena'),
    ('St.Pierre'),
    ('Sudan'),
    ('Suriname'),
    ('Swaziland'),
    ('Sweden'),
    ('Switzerland'),
    ('Syrian Arab Republic'),
    ('Taiwan'),
    ('Tajikistan'),
    ('Tanzania'),
    ('Thailand'),
    ('Togo'),
    ('Tokelau'),
    ('Tonga'),
    ('Trinidad And Tobago'),
    ('Tunisia'),
    ('Turkey'),
    ('Turkmenistan'),
    ('Tuvalu'),
    ('Uganda'),
    ('Ukraine'),
    ('United Arab Emirates'),
    ('United Kingdom'),
    ('Uruguay'),
    ('Uzbekistan'),
    ('Vanuatu'),
    ('Vatican City State'),
    ('Venezuela'),
    ('Vietnam'),
    ('Virgin Islands'),
    ('Yemen'),
    ('Yugoslavia'),
    ('Zaire'),
    ('Zambia'),
    ('Zimbabwe')]

def cls():
    _ = call('clear' if os.name == 'posix' else 'cls')

def correct_letters(guess, correct_answer):
    if len(guess) != len(correct_answer):
        print("Wow! That's not even the right number of letters!")
    correct_letters = ""
    for letter in correct_answer.lower():
        if letter.isalpha() == False:
            correct_letters += letter
        elif letter in guess.lower():
            correct_letters += letter
        else:
            correct_letters += "-"
    return correct_letters

def game_menu():
    cls()
    correct_answer = random.choice(countries)
    attempt_num = 1
    while attempt_num <= 6:
        print("Guess the random country!")
        print("Today's country has " + str(len(correct_answer)) + " letters.")
        print("Your guess cannot be longer than the country length.")
        print("Lower or uppercase letters do not matter.")
        print(('Attempt ') + str(attempt_num) + (' out of 6'))
        guess = input('Type your guess: ')
            
        if len(guess) > len(correct_answer):
            cls()
            print("Your guess was too long. You have been punished.\n \n")
            attempt_num += 1
            
        elif guess.lower() == correct_answer.lower():
            cls()
            print("Your guess, " + guess + ", was correct.")
            print("You got it!")
            keepplaying()
            break
                  
        else:
            cls()
            attempt_num += 1
            print("Your guess, " + guess + ", was wrong.")
            print("Correct letters: " + str(correct_letters(guess, correct_answer)))
            if attempt_num <= 6:
                print("Try again! \n \n")
                
    if attempt_num > 6:
        print("\n \nGame over!!!")
        print("The correct answer was " + correct_answer)
        keepplaying()
    
def keepplaying():
    print("\n\nPlay again?")
    play_again = input("Type yes to continue: ")
    if play_again.lower() == "yes":
        game_menu()
        
def running():
    running = True
    while running == True:
        game_menu()
        break
    
running()
cls()
print("Thank you for guessing the country of the day!")