from actions import *


def menu(driver):
    level = 'root'
    while True:
        if level == 'root':
            print('1-change term')
            print('2-program')
            print('3-unit selection')
            print('4-transcript')
            print('5-payment')
            print('0-exit\n')
            command = int(input('Choose a Number: '))
            if command == 1:
                level = 'changeTerm'
            elif command == 2:
                level = 'program'
            elif command == 3:
                level = 'unitSelect'
            elif command == 4:
                level = 'transcript'
            elif command == 5:
                level = 'payment'
            elif command == 0:
                break
        elif level == 'changeTerm':
            driver = changeTerm(driver)
            print("\nDone, Please Open Your Chrome Tab.\n")
            level = 'root'
        elif level == 'program':
            program(driver)
            print("\nDone, Please Open Your Chrome Tab.\n")
            print('0-back\n')
            command = int(input('Choose a Number: '))
            if command == 0:
                driver.back()
                level = 'root'
        elif level == 'unitSelect':
            selectUnit(driver)
            print("\nDone, Please Open Your Chrome Tab.\n")
            level = 'root'
        elif level == 'transcript':
            transcript(driver)
            print("\nDone, Please Open Your Chrome Tab.\n")
            level = 'root'
        elif level == 'payment':
            payment(driver)
            print("\nDone, Please Open Your Chrome Tab.\n")
            level = 'root'
