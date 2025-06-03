import random
if __name__ == '__main__':



    class Difficulty:

        def choosing_difficulty(self):
            choose = ''
            while choose not in ('easy','medium','hard','impossible'):
                choose = input('Choose your difficulty:\nEasy - 8 chances\nMedium - 6 chances\nHard - 4 chances\nImpossible - 3 chances\n').lower()
            
            chances = {
                'easy' : 8,
                'medium' : 6,
                'hard' : 4,
                'impossible' : 3
            }
            return print(chances[choose])
        
    class UserNumber:

        def picking_number(self):
            user_number = int(input('Choose a number: '))
            return user_number


    class Game:

        def random_number(self):
            number = random.randint(1,100)
            return number
        
        def main(self):
            print('Welcome to number guessing game. Good Luck!')
            magic_number = self.random_number()

            difficulty = Difficulty()
            user_difficulty = difficulty.choosing_difficulty()

            chances = 1
            user_number = UserNumber()
            
            while chances <= user_difficulty:
                number_picked = user_number.picking_number()
                if number_picked > magic_number:
                    print(f'The number {number_picked} is higher than Magic Number')
                    continue
                elif number_picked < magic_number:
                    print(f'The number {number_picked} is higher than Magic Number')
                    continue

                

    a = Difficulty()
    a.choosing_difficulty()
            