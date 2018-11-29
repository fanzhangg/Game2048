import random

def two_or_four():
    a = random.randint(0,10)
    if a == 0:
        return 4
    else:
        return 2

def left_combine_list(li):
    new_li = []
    index = 0
    while index < len(li):
        if li[index] != ' ':
            i = index + 1
            while i < len(li) and li[i] == ' ':
                i += 1
            if i == len(li) or li[i] != li[index]:
                new_li.append(li[index])
                index = i
            else:
                new_li.append(li[index] * 2)
                index = i + 1
        else:
            index += 1
    while len(new_li) < len(li):
        new_li.append(' ')
    return new_li

def right_combine_list(li):
    li.reverse()
    new_li = left_combine_list(li)
    new_li.reverse()
    li.reverse()
    return new_li


class Game2048:

    def __init__(self, n):
        self.n = n
        self.square = sum([[sum([[' '] for a in range(n)], [])] for b in range(n)], [])


    def __str__(self):
        string = ''
        for x in self.square:
            for y in x:
                string += '[' + str(y) + '] '
            string += '\n'
        return string


    def left_move(self):
        new_square = []
        for row in self.square:
            new_square.append(left_combine_list(row))
        return new_square

    def right_move(self):
        new_square = []
        for row in self.square:
            new_square.append(right_combine_list(row))
        return new_square

    def up_move(self):
        new_square = sum([[[]] for i in range(self.n)], [])
        column = sum([[[]] for i in range(self.n)], [])
        for i in range(0, self.n):
            for row in self.square:
                column[i].append(row[i])
            column[i] = left_combine_list(column[i])
        for j in range(0, self.n):
            for col in column:
                new_square[j].append(col[j])
        return new_square

    def down_move(self):
        new_square = sum([[[]] for i in range(self.n)], [])
        column =sum([[[]] for i in range(self.n)], [])
        for i in range(0, self.n):
            for row in self.square:
                column[i].append(row[i])
            column[i] = right_combine_list(column[i])
        for j in range(0, self.n):
            for col in column:
                new_square[j].append(col[j])
        return new_square

    def transmove(self, move):
        if move in 'Aa':
            return self.left_move()
        elif move in 'Dd':
            return self.right_move()
        elif move in 'Ww':
            return self.up_move()
        elif move in 'Ss':
            return self.down_move()


    def valid_move(self, move):
        return True if self.transmove(move) != self.square else False


    def lose(self):
        return False if any([self.valid_move(x) for x in 'wsad']) else True


if __name__ == "__main__":
    restart = 'R'
    while restart in 'Rr':
        n = '0'
        while not n.isnumeric() or int(n) <= 1:
            n = input("Please Choose the n*n board you like (input an integer greater than 1 as n) : ")
        game = Game2048(int(n))
        a1 = random.randint(0, game.n - 1)
        b1 = random.randint(0, game.n - 1)
        a2 = a1
        b2 = b1
        while a2 == a1 or b2 == b1:
            a2 = random.randint(0, game.n - 1)
            b2 = random.randint(0, game.n - 1)
        game.square[a1][b1] = two_or_four()
        game.square[a2][b2] = two_or_four()
        print(game)
        while not game.lose():
            move = 'q'
            while move not in ['W','S','A','D','w','s','a','d'] or not game.valid_move(move):
                move = input("Please input 'W''S''A''D' to move : ")
            if move in 'Aa':
                game.square = game.left_move()
            elif move in 'Dd':
                game.square = game.right_move()
            elif move in 'Ww':
                game.square = game.up_move()
            elif move in 'Ss':
                game.square = game.down_move()
            a3 = random.randint(0, game.n - 1)
            b3 = random.randint(0, game.n - 1)
            while game.square[a3][b3] != ' ':
                a3 = random.randint(0, game.n - 1)
                b3 = random.randint(0, game.n - 1)
            game.square[a3][b3] = two_or_four()
            print(game)
        print("Game Over!")
        restart = 'q'
        restart = input("If you wanna play again, Please input 'R' or else quit : ")

    exit(code=0)





