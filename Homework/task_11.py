print('Is it raining outside?')
answer1 = input().lower()
if answer1 == 'yes':
    print('Is it windy as well?')
    answer2 = input().lower()
    if answer2 == 'yes':
        print('It is too windy for an umbrella')
    elif answer2 == 'no':
        print('Take an umbrella')
    else:
        print('Please, answer "Yes" or "No". Try again')
elif answer1 == 'no':
    print('Enjoy your day')
else:
    print('Please, answer "Yes" or "No". Try again')
