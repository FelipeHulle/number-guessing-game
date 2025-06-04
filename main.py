import random


class Difficulty:
    def choosing_difficulty(self):

        choose = -1

        chances = {
            1 : 8,
            2 : 6,
            3 : 4,
            4 : 3
        }
        while choose not in chances:
        
            try:
                choose = int(input('Choose your difficulty (Write the name):\n1. Easy (8 chances)\n2. Medium (6 chances)\n3. Hard (4 chances)\n4. Impossible (3 chances)\n\n'))
            except:
                print('Choose a valid number')
        
        return chances[choose]
    
class UserNumber:
    def picking_number(self):
        user_number = int(input('\nChoose a number: '))
        return user_number
    
class Game:

    def random_number(self):
        number = random.randint(1,100)
        return number
    
    def main(self):
        print('\nWelcome to the Number Guessing Game. I\'m thinking of a number between 1 and 100.\nTry guess the number! Good Luck!\n')

        magic_number = self.random_number()
        difficulty = Difficulty()
        user_difficulty = difficulty.choosing_difficulty()
        chances = 1
        user_number = UserNumber()

        while chances <= user_difficulty:
            number_picked = user_number.picking_number()

            if number_picked > magic_number:
                chances += 1
                print(f'The number is greater than Magic Number')
                continue
            elif number_picked < magic_number:
                chances += 1
                print(f'The number is less than Magic Number')
                continue
            elif number_picked == magic_number:
                return print('\n********YOU WONNNNNN!!!!!!********\nTHE NUMBER IS CORRECT')
            
        return print(f'\nYou lose, try again :(\nThe Magic Number was: {magic_number}')
            

game_instance = Game()
game_instance.main()