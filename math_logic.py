from random import randint, choice

def zero_division(first, second):
    if second == 0:
        return 0
    else:
        return first / second


def generate_new_math():
    num1 = randint(0, 10)
    num2 = randint(0, 10)
    problem_type = 5
    problem = None
    solution = None

    if problem_type == 0:  # Compare
        problem = 'Салыстыр:\n'
        problem += str(num1) + '  ' + str(num2)
        if num1 > num2:
            solution = '>'
        elif num1 < num2:
            solution = '<'
        else:
            solution = '='
    else:
        big = (num1 + num2) / 2 + abs(num1 - num2) / 2
        small = (num1 + num2) / 2 - abs(num1 - num2) / 2

        if problem_type == 1:
            char = choice([ "-", "+"])
            problem = 'Теңдеуді шеш:\n'
            position = randint(0, 1)
            if char == '+':
                if position == 0:
                    problem += 'X' + char + str(int(small)) + '=' + str(int(big))
                elif position == 1:
                    problem += str(int(small)) + char + 'X' + '=' + str(int(big))
                solution = int(big - small)
            else:
                if position == 0:
                    n1 = choice([num1, num2])
                    n2 = num1 + num2 - n1
                    problem += 'X' + char + str(int(n1)) + '=' + str(int(n2))
                    solution = int(n1 + n2)
                elif position == 1:
                    problem += str(int(big)) + char + 'X' + '=' + str(int(small))
                    solution = int(big - small)    

        elif problem_type == 2:
            problem = 'Есепті шығар:\n'
            problem += str(int(num1)) + '+' + str(int(num2)) + '='
            solution = int(num1 + num2)

        elif problem_type == 3:
            problem = 'Есепті шығар:\n'
            problem += str(int(big)) + '-' + str(int(small)) + '='
            solution = int(big - small)

        elif problem_type == 4:
            boys = [['Бекасыл', 'Бекасылдың', 'Бекасылға', 'Бекасылда'],
                    ['Айтөре', 'Айтөренің', 'Айтөреге', 'Айтөреде'],
                    ['Айсұлтан', 'Айсұлтанның', 'Айсұлтанға', 'Айсұлтанда'],
                    ['Жақсылық', 'Жақсылықтың', 'Жақсылыққа', 'Жақсылықта'],
                    ['Азамат', 'Азаматтың', 'Азаматқа', 'Азаматта'],
                    ['Арнат', 'Арнаттың', 'Арнатқа', 'Арнатта'],
                    ['Рустем', 'Рустемнің', 'Рустемге', 'Рустемде']]


            girls= [['Адия', 'Адияның', 'Адияға', 'Адияда'],
                    ['Жансая', 'Жансаяның', 'Жансаяға', 'Жансаяда'],
                    ['Раяна', 'Раянаның', 'Раянаға', 'Раянада'],
                    ['Айым', 'Айымның', 'Айымға', 'Айымда'],
                    ['Айша', 'Айшаның', 'Айшаға', 'Айшада'],
                    ['Фариза', 'Фаризаның', 'Фаризаға', 'Фаризада'],
                    ['Аяна', 'Аянаның', 'Аянаға', 'Аянада'],
                    ['Айсәуле', 'Айсәуленің', 'Айсәулеге', 'Айсәуледе']]

            school_items = [['қарындаш', 'қарындаштарына', 'қарындашқа', 'қарындаштардан', 'қарындаштың'],
                            ['қалам', 'қаламдарына', 'қаламға', 'қаламдардан', 'қаламның'],
                            ['кітап', 'кітаптарына', 'кітапқа', 'кітаптардан', 'кітаптың'],
                            ['дәптер', 'дәптерлеріне', 'дәптерге', 'дәптерлерден', 'дәптердің']]
            
            position = randint(0, 1)
            gender = randint(0, 1)
            item = school_items[randint(0, 3)]
            girl = girls[randint(0, 7)]
            boy = boys[randint(0, 6)]
            char = choice([ "-", "+"])
            
            if char == '+':
                if position == 0:
                    if gender == 0:
                        problem = girl[1]+' '+item[1]+' '+str(int(small))+' '+item[0]+' қосса '+str(int(big))+' '+item[0]+' болады.\n'+girl[3]+' бастапқыда неше '+item[0]+' болды?'
                    else:
                        problem = boy[1]+' '+item[1]+' '+str(int(small))+' '+item[0]+' қосса '+str(int(big))+' '+item[0]+' болады.\n'+boy[3]+' бастапқыда неше '+item[0]+' болды?'
                elif position == 1:
                    if gender == 0:
                        problem = 'Үстелдегі '+str(int(small))+' '+item[2]+' '+girl[1]+' сөресіндегі '+str(item[1])[:-1]+' қоссқанда '+str(int(big))+' '+item[0]+' болады.\n'+girl[1]+' сөресінде неше '+item[0]+' болған екен?'
                    else:
                        problem = 'Үстелдегі '+str(int(small))+' '+item[2]+' '+boy[1]+' сөресіндегі '+str(item[1])[:-1]+' қоссқанда '+str(int(big))+' '+item[0]+' болады.\n'+boy[1]+' сөресінде неше '+item[0]+' болған екен?'
                solution = int(big - small)
            else:
                if position == 0:
                    n1 = choice([num1, num2])
                    n2 = num1 + num2 - n1
                    if gender == 0:
                        problem = 'Сөредегі '+item[3]+' '+girl[0]+' '+str(int(n1))+' '+item[0]+' алып еді, сөреде '+str(int(n2))+' '+item[0]+' қалды.\nБастапқыда сөреде неше '+item[0]+' болды?'
                    else:
                        problem = 'Сөредегі '+item[3]+' '+boy[0]+' '+str(int(n1))+' '+item[0]+' алып еді, сөреде '+str(int(n2))+' '+item[0]+' қалды.\nБастапқыда сөреде неше '+item[0]+' болды?'
                    solution = int(n1 + n2)
                elif position == 1:
                    if gender == 0:
                        problem = 'Сөредегі '+str(int(big))+' '+item[4]+' бірнешеуін '+girl[0]+' алып кетіп еді, сөреде '+str(int(small))+' '+item[0]+' қалды.\n'+girl[0]+' неше '+item[0]+' алып кетті?'
                    else:
                        problem = 'Сөредегі '+str(int(big))+' '+item[4]+' бірнешеуін '+boy[0]+' алып кетіп еді, сөреде '+str(int(small))+' '+item[0]+' қалды.\n'+boy[0]+' неше '+item[0]+' алып кетті?'
                    solution = int(big - small)

        else:
            num1 = randint(0, 4)
            num2 = randint(0, 10)
            arr = [num1, num2]

            if problem_type == 5:
                problem = 'Есепті шығар:\n'
                problem += str(int(num1)) + '*' + str(int(num2)) + '='
                solution = int(num1 * num2)
            
            elif problem_type == 6:
                problem = 'Есепті шығар:\n'
                b = int(choice(arr))
                problem += str(int(num1*num2)) + '/' + str(b) + '='
                solution = int(int(num1 * num2) / b)

    return problem, problem_type, solution
