# Digital Escape 
# Имя: А. Азиза 
# Группа: 
# Проект: Побег из цифровой лаборатории

lives = 3
game_running = True
game_won = False
inventory = []

commands = (
        'осмотреться',
        'перейти',
        'инвентарь',
        'помощь',
        'выход'
)
visited_rooms = set()
current_room = None 
solved_pazzle = set()                                                                

rooms = {
    'комната управления': {
        'description': 'Вы находитесь в комнате управления. Вокруг полумрак',
        'item': 'карта доступа'
    },
    'серверная': {
        'description': 'Здесь главный сервер лаборотории. Мрачновато конечно',
        'item': 'ключ'
    },
    'лаборотория': { 
        'description': 'в лаборотории стоят компьютеры и страное оборудование',
        'item': 'пароль'
    },
    'главная дверь': {
        'description': 'Перед вами массивная дверь, панель которой запрашивает пароль',
        'item': None
    }
   
}
#показывает комнату + предмет
def enter_room(room_name: str): 
    print()
    print('============================')
    print(room_name.upper())
    print('============================')
    room = rooms[room_name]  
    print(room['description'])
    visited_rooms.add(room_name)      #отмечает посещенные комнаты
    if room['item'] is not None:
        print(f"Здесь находится {room['item']}")
        

#меню
def show_menu(commands: tuple) -> None:
    print()
    print('МЕНЮ:')
    print('----------------------')
    for i, command in enumerate(commands):
        print(f'{i+1}. {command}') 
    print('----------------------')   

    
#инвентарь
def show_inventory(inventory: list):
    if len(inventory) == 0:
        print()
        print('==================')
        print('= инвентарь пуст =')
        print('==================')
    else:
        print()
        print('инвентарь:')
        print('=================================================')
        print(*inventory, sep=' | ')
        print('=================================================')

def show_rooms():
    print('----------------------')
    for i, room in enumerate(rooms.keys()):  
        print(f'{i+1}. {room}')            
    print('----------------------')

#загадка1
def solve_math_pazzle(lives: int) -> tuple[bool, int]:
    print('Чтобы получить ключ реши загадку. Неправельный ответ бьет по жизни -1')
    print('Сколько будет 2+2 = ?')
    try:
        answer = int(input('Ваш ответ: '))

    except ValueError:
        print()
        print('Нужно вести целое число!')
        return False, lives
    
    if answer == 4:
        print()
        print('Правельный ответ!')
        return True, lives
    else:
        print()
        print('Неправельный ответ(')
        lives -= 1
        print(f'Ты потерял жизнь. Осталось: {lives}')
        return False, lives 

#загадка2
def solve_word_pazzle(lives: int):
    print()
    print('отгадай загадку')
    print('Может ли страус назвать себя птицей?')
    print('да/нет')
    answer = input('Ваш ответ: ').lower().strip()
    
    if answer == 'да':
        print()
        print('Нет, он не разговаривает')
        lives -= 1
        print(f'Ты потерял жизнь. Осталось: {lives} ')
        return False, lives
    
    elif answer == 'нет':
            print()
            print('Правильно!')
            return True, lives
    else:
        print()
        print('Напишите да либо нет')
        return False, lives

#предмет добавлен в инвентарь     
def add_to_inventory(room_name: str):
    item = rooms[room_name]['item']

    if item is not None:
        inventory.append(item)
        print(f'Получен новый предмет: {item} =)')
        print('Добавлено в инвентарь-')
        rooms[room_name]['item'] = None


 #итоги/статистика   
def show_result(player_name, game_won, lives, visited_rooms, inventory):
    print()
    print('=======================================')
    print('             ИТОГИ ИГРЫ                ')
    print('=======================================')
    print(f'Игрок: {player_name}')
    if game_won:
        print('Результат: ПОБЕДА!')
    elif lives <= 0:
        print('Результат: ПОРАЖЕНИЕ!')
    else:
        print('Результат: ИГРА ПРЕРВАНА')
    print(f'Осталость жизней: {lives}')
    print(f'Посещено комнат: {len(visited_rooms)} из {len(rooms)}')
    print('Посещенные комнаты: ', end='')
    print(*visited_rooms, sep=', ')
    print(f'Собрано предметов: {len(inventory)}')
    print('Собранные предметы :', end='')
    print(*inventory, sep=', ')

    print('=======================================')


# начало + краткое обьеснение игры
print('----------------------------')
print('      Digital Escape   ')
print('Побег из цифровой лаборатории')
print('----------------------------')
print('вы просыпаетесь в закрытой цифровой лаборатории.')
print('Чтобы выбраться, вам нужно пройти несколько помещений и собрать необходимые предметы,') 
print('чтобы восстановить код финальной двери')
print()
player_name = input('Введите ваше имя: ')
print() 
print( f'Приветствуем тебя {player_name}! Твой следущий шаг...?')

while game_running == True:                         
    
    if lives <= 0:
        print(f'Вы проиграли! жизнь: {lives}')
        game_running = False
        break

    show_menu(commands)
    command = input('Введите команду > ').lower().strip()

    if command == '1':
        command = 'осмотреться'
    elif command == '2':
        command = 'перейти'
    elif command == '3':
        command = 'инвентарь'
    elif command == '4':
        command = 'помощь'
    elif command == '5':
        command = 'выход'
    if command == 'exit':
        command = 'выход'

    if command not in commands: 
        print('Неизвестная команда!')
        continue
    
    if command == 'инвентарь':
        show_inventory(inventory)

    if command == 'выход':
        print('игра завершена!')
        game_running = False

    if command == 'перейти':
        print()
        print('Выберите комнату:')
        show_rooms()     
        room_name = input('введите комнату > ').lower().strip()
        
        if room_name == '1':
            room_name = 'комната управления'
        elif room_name == '2':
            room_name = 'серверная'
        elif room_name == '3':
            room_name = 'лаборотория'
        elif room_name == '4':
            room_name = 'главная дверь'
        
        if room_name not in rooms.keys():
            print('такой комнаты не существует')
            continue
            
        else: 
            if room_name == 'комната управления':
                current_room = room_name
                enter_room(room_name)
                add_to_inventory(room_name)
                print('Серверная разблокирована!')
            
            if room_name == 'серверная':
                if 'карта доступа' not in inventory:
                    print()
                    print('-Нет карты доступа! Дверь заблокирована-')
                                       
                else:
                    current_room = room_name
                    enter_room(room_name)
                    if 'серверная' in solved_pazzle:
                        print()
                        print('загадка уже решена')
                    else: 
                        success, lives = solve_math_pazzle(lives)
                        if success:
                            add_to_inventory(room_name)                    
                            solved_pazzle.add('серверная')
                    
            
            if room_name == 'лаборотория':
                if 'ключ' not in inventory:
                    print()
                    print('-Нет ключа! Дверь заблокирована-')                                       
                else:
                    current_room = room_name
                    enter_room(room_name)
                    if 'лаборотория' in solved_pazzle:
                        print()
                        print('Загадка уже решена')
                    else:
                        success, lives = solve_word_pazzle(lives)
                        if success:
                            rooms['лаборотория']['item'] = 'пароль: 0102'
                            add_to_inventory(room_name)
                            solved_pazzle.add('лаборотория')
                                        
                      
            
            if room_name == 'главная дверь':
                if ('карта доступа' in inventory and 'ключ' in inventory and 'пароль: 0102' in inventory):
                    current_room = room_name
                    enter_room(room_name)
                    print('Неправельный ввод бьет по жизни -1.')
                    password = input(' Введите пароль > ').strip()
                    if password == '0102':
                        print('Вы победили!!!')
                        game_won = True
                        game_running = False
                    else:
                        print()
                        print('Неправельный пароль!')
                        lives -= 1
                        print(f'Ты потерял жизнь. Осталось: {lives}')
                else:
                    print()
                    print('Недостаточно предметов! найдите карту, ключ и пароль')


    if command == 'осмотреться':
        if len(visited_rooms) == 0:   #игрок пока не заходил не в одну из комнат
            print()
            print('Вы пока не вошли ни в одну комнату')
            print('Перед вами четыре двери.')
        else:
            enter_room(current_room)

    if command == 'помощь':
        print()
        print('========== ПОМОЩЬ ==========')
        print('Команды игры:')
        print('1. Осмотреться — осмотреть текущую комнату')
        print('2. Перейти — выбрать комнату для перехода')
        print('3. Инвентарь — посмотреть собранные предметы')
        print('4. Помощь — показать список команд')
        print('5. Выход — завершить игру')
        print('Также можно написать exit для выхода.')
        print('============================')
               

show_result(player_name,
            game_won,
            lives,
            visited_rooms, 
            inventory)              
