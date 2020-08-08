zyczenia = ['Nam-Myoho-Renge-Kyo', 'Kocham Cię! <3', 'Jesteś moją Wieżą Skarbów',
            'Jesteś Buddą od samego początku', 'Masz potencjał stanu Buddy',
            'Jesteś moim życiem', 'Razem damy radę!', 'Jeszcze troszkę', 
            'Za niedługo się widzimy', 'Zleci szybko', 'Mój kwiatuszku',
            'Moje słoneczko', 'Skarbie <3']

import datetime
import random as rand
rand.seed(datetime.date.today())

powrot = datetime.date(2020,8,31)
dzis = datetime.date.today()

if powrot > dzis:
    print(rand.choice(zyczenia))
    print(f'Do mojego powrotu zostało: {powrot-dzis}')
else:
    print('Jestem już w domu! :D')
    
odpowiedz = input('Wciąż mnie kochasz? ')
odpowiedz = odpowiedz.casefold()
if odpowiedz == 't' or odpowiedz == 'tak':
    print('Ja ciebie też. Bardzo mocno <3')
elif odpowiedz == 'n' or odpowiedz == 'nie':
    print('A ja ciebie tak!')
else:
    print('Nie rozumiem')
    
koniec = input('Nacisnij enter aby zakończyć')
