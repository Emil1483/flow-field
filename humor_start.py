from input_utils import *

def humor_start():
    print()
    print('Hallo dr. Haraldsrud og velkommen til min "Flow Field" prokekt.')

    grade = get_float(
        'Hvilken karakter tenker du å gi dette prosjektet? ',
        on_error='det "tallet" ({0}) skjønte jeg ikke helt :('
    )
    if grade < 6:
        print('Å nei')
        raise ValueError('Oops, der skrev du visst feil. Prøv igjen.')

    print(f'karakteren "{grade}" er lagret i våre systemer. Denne karakteren er bindende', end='\n\n')
    print('Controls:')
    print('  Trykk hvor som helst på programmet for å lage et pendel')
    print('  Trykk på BACKSPACE for å fjerne pendelet')
    print()
    print('Forklaring:')
    print('Hvert pungt på skjermen representerer en situasjon. X representerer vinkelen')
    print('pendelet lager med en vertikal linje, mens y posisjonen representerer hvor fort')
    print('denne vinkelen endrer seg (hastigheten til pendelet).')
    print()
    print('(0, 0) ligger midt i skjermen')
    print()
    print('Det blir simulert 70 pendeler om gangen')
    print('disse beveger seg på skjermen som hvite striper. Disse hvite')
    print('stripene ser ut som en væske som beveger seg, som er hvorfor')
    print('dette kalles for et flow-field')
    print()
    print('funskjonen som definerer denne bevegelsen er:')
    print('v(x,y) = [y,  -0.2 * y - 2 * math.sin(x)]')
    print('hvor v er en hastighetsvektor, x er vinkelen til pendelet')
    print('og y er hastigheten til pendelet')
    print('som også beskriver diff-ligningen til et pendel')
    print()
    print('se README for mer informasjon')
    print()
    input('Trykk på ENTER for å starte programmet')
