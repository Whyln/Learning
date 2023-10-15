import pycosat
from copy import deepcopy
from types import *
from tkinter import *
import tkinter.messagebox as messagebox

class sudokuSolve:
    def encode(self,x:int,y:int,z:int)->int:
        """
        返回一个原子命题 : (x,y)的数字为z,同时 -P 表示该命题的否命题
        (x,y) : 数独列表中的点位  
        z   :   该点位填入的数字 
        
        在这里由于数独为9x9,数字为1-9,因此我们一个三位数 xyz 唯一表示 (x,y)上的数字为z 这个命题     
        """
        return x*100+y*10+z
    
    def decode(self,num:int)->tuple[int,int,int]:
        """
        对命题进行解码,返回x,y,z
        """
        return num//100,num//10%10,num%10
    
    def init(self):
        """
        初始化,回到最初条件
        """
        self.clauses=deepcopy(self.KB)
        
    def getKB(self)->list[list[int]]:
        KB=[]
        # 每个位置上的数字只能是1-9之间的一个
        for x in range(9):
            for y in range(9):
                # 保证在 1-9之间
                temp=[]
                for z in range(1,10):
                    temp.append(self.encode(x,y,z))
                KB.append(temp)
                
                # 保证最多只有一个
                for z in range(1,9):
                    for i in range(z+1,10):
                        KB.append([-self.encode(x,y,z),-self.encode(x,y,i)])
        # 每一列都存在1-9
        for y in range(9):
            for z in range(1,10):
                temp=[]
                for x in range(9):
                    temp.append(self.encode(x,y,z))
                KB.append(temp)
        # 每一行都存在1-9
        for x in range(9):
            for z in range(1,10):
                temp=[]
                for y in range(9):
                    temp.append(self.encode(x,y,z))
                KB.append(temp)
        # 每一个九宫格都有1-9
        for i in range(3):
            for j in range(3):
                for z in range(1,10):
                    temp=[]
                    for x in range(3):
                        for y in range(3):
                            temp.append(self.encode(3*i+x,3*j+y,z))
                    KB.append(temp)
        return KB
    
    def __call__(self,grid:list[list])->tuple[bool,list[int]]:
        """
        调用解决 grid这个数独问题,返回一个新的grid
        """
        self.init()
        # 将所有状态加入clauses当中
        for x in range(9):
            for y in range(9):
                if grid[x][y]:
                    self.clauses.append([self.encode(x,y,grid[x][y])])
        solution=pycosat.solve(self.clauses)
        # 初始化为初始状态
        self.init()
        ans=[[0 for i in range(9)] for j in range(9)]
        if type(solution)==list:
            for n in solution:
                if n>0:
                    x,y,z=self.decode(n)
                    ans[x][y]=z
            return True,ans
        return False,ans
        
    def __init__(self) -> None:
        self.KB=self.getKB()   # 数独游戏的基本规则 
        self.clauses=[]        # 加入初始条件后的规则



class SudokuGUI:
    def __init__(self, master):
        self.sudokuSolve=sudokuSolve()
        self.master = master
        self.master.title("数独求解器")
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.create_board()

        self.button_frame = Frame(self.master)
        self.reset_button = Button(self.button_frame, text="重置", command=self.reSet)
        self.solve_button = Button(self.button_frame, text="求解", command=self.solve)
        self.reset_button.pack(side=LEFT, padx=9, pady=5)
        self.solve_button.pack(side=RIGHT, padx=9, pady=5)
        self.button_frame.pack()

    def create_board(self):
        # Create the game board
        self.board_frame = Frame(self.master)
        self.cells = [[0 for _ in range(9)] for _ in range(9)]
        # 验证text为空或在1-9之间
        def validate_entry(text):
            if not text or (text.isdigit() and 1 <= int(text) <= 9):
                return True
            else:
                return False
        validation = self.master.register(validate_entry)
        
        for i in range(9):
            for j in range(9):
                # 输入组件 且输入在 ''和1-9之间
                self.cells[i][j] = Entry(self.board_frame, width=2, font=("Arial", 20, "bold"), justify="center",validate="key", validatecommand=(validation, "%P"))
                self.cells[i][j].grid(row=i, column=j)
        self.board_frame.pack()

    def reSet(self):
        for row in range(9):
            for col in range(9):
                self.cells[row][col].delete(0,END)
                
    def solve(self):
        grid=[[0 for _ in range(9)] for _ in range(9)]
        for row in range(9):
            for col in range(9):
                num_str=self.cells[row][col].get()
                if num_str:
                    grid[row][col]=int(num_str) 
                    
        print("你的输入如下:")
        for row in grid:
                print(row)
                
        flag,solution=self.sudokuSolve(grid)
        if flag:
            messagebox.showinfo("提示","求解成功")
            print("解为:")
            for row in solution:
                print(row)
            for row in range(9):
                for col in range(9):
                    self.cells[row][col].delete(0,END)
                    self.cells[row][col].insert(0,solution[row][col])
        else:
            messagebox.showinfo("提示","求解失败")
            print("无解")
        

if __name__ == "__main__":
    root = Tk()
    game = SudokuGUI(root)
    root.mainloop()
