from abc import ABC,abstractmethod

class Piece(ABC):
    def __init__(self,color):
        self.color = color;
#    @abstractmethod
    def PossibleMoves(self,X,Y,board):
        pass

class Rook(Piece):
    def PossibleMoves(self,X,Y,board):
        arr = board.array
        color = arr[X][Y].piece.color
        moves = []
        def moves_list(row=X,col=Y):
            if(row==None):
                j = Y + col
                while(j in range(0, 8) and arr[X][j].piece == None and (arr[X][j].piece==None or color != arr[X][j].piece.color)):
                    moves.append([X, j])
                    if (arr[X][j].piece!=None and arr[X][j].piece.color != color):
                        break
                    j = j + col
            else:
                i = X + row
                while (i in range(0, 8) and arr[i][Y].piece == None and (arr[i][Y].piece==None or color != arr[i][Y].piece.color)):
                    moves.append([i, Y])
                    if (arr[i][Y].piece!=None and arr[i][Y].piece.color != color):
                        break
                    i = i + row
        moves_list(None,1)
        moves_list(None,-1)
        moves_list(1,None)
        moves_list(-1,None)
        return moves

class Knight(Piece):
    def PossibleMoves(self,X,Y,board):
        arr = board.array
        color = arr[X][Y].piece.color
        moves=[]
        def moves_list():
            L = [X+2,Y-1,X-2,Y-1,X+2,Y+1,X-2,Y+1,X+1,Y-2,X+1,Y+2,X-1,Y-2,X-1,Y+2];
            for i in range(0,len(L),2):
                if(L[i] in range(0,8) and L[i+1] in range(0,8) and (arr[L[i]][L[i+1]].piece==None or color!=arr[L[i]][L[i+1]].piece.color)):
                    moves.append([L[i],L[i+1]])
        moves_list()
        return moves


class Bishop(Piece):
    def PossibleMoves(self,X,Y,board):
        arr = board.array
        color = arr[X][Y].piece.color
        moves = []
        def moves_list(row,col):
            i,j = X+row,Y+col
            while(i in range(0,8) and j in range(0,8) and (arr[i][j].piece==None or color!=arr[i][j].piece.color)):
                moves.append([i,j])
                if(arr[i][j].piece!=None and arr[i][j].piece.color!=color):
                    break
                i=i+row
                j=j+col
        moves_list(-1,-1)
        moves_list(1,1)
        moves_list(1,-1)
        moves_list(-1,1)
        return moves

class Queen(Piece):
    def PossibleMoves(self,X,Y,board):
        moves = Bishop(self.color).PossibleMoves(X,Y,board) + Rook(self.color).PossibleMoves(X,Y,board)
        return moves
        pass

class King(Piece):
    def PossibleMoves(self, X, Y, board):
        arr = board.array
        moves = []
        for i in range(Y-1,Y+2):
            for j in range(X-1,X+2):
                if((i in range(0,8) and j in range(0,8)) and arr[i][j].piece != None and arr[X][Y].piece.color != arr[i][j].piece.color):
                    moves.append([i,j])
        return moves


class Pawn(Piece):
    def PossibleMoves(self,X,Y,board):
        arr = board.array
        moves = []
        if(arr[X][Y].piece.color=="White"):
            sign = 1
        else:
            sign = -1
        def moves_list():
            if(arr[X+sign][Y].piece == None):
                moves.append([X+sign,Y])
            if(arr[X+(sign*2)][Y].piece == None):
                moves.append([X+(sign*2),Y])
            if(Y not in [0] and (arr[X + 1][Y - 1].piece != None and arr[X + 1][Y -1 ].piece.color == "White")):
                moves.append([X+1,Y-1])
            if(Y not in [7] and (arr[X + 1][Y + 1].piece != None and arr[X + 1][Y + 1].piece.color == "White")):
                moves.append([X + 1,Y + 1])
            if(Y not in [0] and (arr[X - 1][Y - 1].piece != None and arr[X - 1][Y - 1].piece.color == "Black")):
                moves.append([X - 1,Y - 1])
            if(Y not in [7] and (arr[X - 1][Y + 1].piece != None and arr[X - 1][Y + 1].piece.color == "Black")):
                moves.append([X - 1,Y + 1])
            return moves;
        return(moves_list())

class Square:
    def __init__(self,piece,X,Y):
        self.piece = piece
        self.X = X
        self.Y = Y
    def set_X(self,X:int):
        self.X = X
    def get_X(self):
        return self.X
    def set_Y(self,Y:int):
        self.Y = Y
    def get_Y(self):
        return self.Y
    def set_piece(self,piece:Piece):
        self.piece = piece
    def get_piece(self):
        return self.piece


class Board:
    def __init__(self,array):
        self.array = array
    def start(self):
#        pieces = [Rook(),Knight(),Bishop(),King(),Queen()]
        for i in range(8):
            for j in range(8):
                #Square contains pieces
                if(i in [0,1,6,7]):
                    if(i==1):
                        self.array[i][j] = Square(Pawn("White"),i,j)
                    elif(i==6):
                        self.array[i][j] = Square(Pawn("Black"), i, j)
                    elif(i==0 or i==7):
                        if(i==0):
                            color = "White"
                        else:
                            color = "Black"
                        if(j==0 or j==7):
                            self.array[i][j] = Square(Rook(color),i,j)
                        elif(j==1 or j==6):
                            self.array[i][j] = Square(Knight(color), i, j)
                        elif (j == 2 or j == 5):
                            self.array[i][j] = Square(Bishop(color), i, j)
                        elif (j == 1):
                            self.array[i][j] = Square(Knight(color), i, j)
                        elif(j==3):
                            self.array[i][j] = Square(Queen(color),i,j)
                        else:
                            self.array[i][j] = Square(King(color),i,j)
                else:
                    self.array[i][j] = Square(None,i,j)
        self.array[3][4] = Square(Queen("White"),3,4)

class Players:
    def __init__(self,side):
        self.side = side
        pass

class Move:
    def makemove(self,arr,oldX,oldY,newX,newY,board):
        possible_moves = arr[oldX][oldY].piece.PossibleMoves(oldX,oldY,board)
        if([newX,newY] in possible_moves):
            arr[newX][newY].piece = arr[oldX][oldY].piece
            arr[oldX][oldY].piece = None
        else:
            print("Invalid move, Make a new move")


def start():
    array = [[i for i in range(8)] for j in range(8)]
    board = Board(array)
    board.start()
    arr = board.array
    m = Move()
    colr = "White"
    while(True):
        oldX = int(input("Enter oldX: "))
        oldY = int(input("Enter oldY: "))
        newX = int(input("Enter newX: "))
        newY = int(input("Enter newY: "))
        print("The color of the piece: ",arr[oldX][oldY].piece.color)
        if(arr[oldX][oldY].piece.color==colr):
            if(colr=="White"):
                colr = "Black"
            else:
                colr = "White"
        else:
            print("You have touched the opponent's piece, touch your piece")
            continue
        print("Old Position", arr[oldX][oldY].piece)
        print("New Position", arr[newX][newY].piece)
        m.makemove(arr, oldX, oldY, newX, newY, board)
        print("Old Position", arr[oldX][oldY].piece)
        print("New Position", arr[newX][newY].piece)
        res = str(input("Game Continue: Y/N"))
        if(res=="N"):
            break

if __name__=="__main__":
    start()

