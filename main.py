import random
import time

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
                print('\nChoose a valid number\n')
        
        return chances[choose]
    
class User:

    def picking_number(self):
        
        while True:
            try:
                user_number = int(input('Choose a number: '))
            except ValueError:
                print("Choose a valid number\n")
                continue
            
            break
        return user_number
    
    def playing_again(self):
        playing_again = input('\nDo you want to play again? (Y/N): ').upper()
        return playing_again
    
class Game:

    def random_number(self):
        number = random.randint(1,100)
        if number % 2 == 0:
            even_or_odd = 'Even'
        else:
            even_or_odd = 'Odd'
        return number, even_or_odd
    

    
    def playing(self):

        print('\nWelcome to the Number Guessing Game. I\'m thinking of a number between 1 and 100.\nTry guess the number! Good Luck!\n')

        magic_number, even_or_odd = self.random_number()

        difficulty = Difficulty()
        user_difficulty = difficulty.choosing_difficulty()
        chances = 1
        user_number = User()

        initial_time = time.time()

        last_number_picked = None
        number_picked = 0

        while chances <= user_difficulty:

            number_picked = user_number.picking_number()

            if last_number_picked == number_picked:
                print(f'\nOh, you are stuck. I will help you, the Magic Number is {even_or_odd}')

            last_number_picked = number_picked

            if number_picked > magic_number:
                chances += 1
                print(f'The Magic number is LESS\n')
                continue
            elif number_picked < magic_number:
                chances += 1
                print(f'The Magic number is GREATER\n')
                continue
            elif number_picked == magic_number:
                final_time = time.time()

                return print(
                            f'\n********YOU WONNNNNN!!!!!!********\n' 
                            f'THE NUMBER IS CORRECT\n'
                            f'You took only {chances} attempts\n' 
                            f'You spend {final_time - initial_time: .2f} seconds to guess the number'
                        )
        
        final_time = time.time()
        return print(
            f'\nYou lose, try again :('
            f'\nThe Magic Number was: {magic_number}'
            f'\nYou spend {final_time - initial_time: .2f} seconds')
    
    def main(self):

        playing_again = 'Y'

        while playing_again == 'Y':
            self.playing()
            user = User()
            playing_again = user.playing_again()
            

game_instance = Game()
game_instance.main()