class Robot:
    
    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.x = 0
        self.y = 0
        self.dir = 0 
        
        self.directions = ["East", "North", "West", "South"]
        self.moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        self.perimeter = 2 * (width + height) - 4

    def step(self, num: int) -> None:
        if self.perimeter == 0:
            return
        
        num = num % self.perimeter
        
        # Special case: if num == 0, robot should face South at (0,0)
        if num == 0 and self.x == 0 and self.y == 0:
            self.dir = 3
            return
        
        while num > 0:
            dx, dy = self.moves[self.dir]
            nx, ny = self.x + dx, self.y + dy
            
            # If next step is out of bounds → turn left
            if not (0 <= nx < self.w and 0 <= ny < self.h):
                self.dir = (self.dir + 1) % 4
            else:
                self.x, self.y = nx, ny
                num -= 1

    def getPos(self):
        return [self.x, self.y]

    def getDir(self):
        return self.directions[self.dir]
    

robot = Robot(6, 3)

robot.step(2)
robot.step(2)
print(robot.getPos())  
print(robot.getDir())  

robot.step(2)
robot.step(1)
robot.step(4)
print(robot.getPos()) 
print(robot.getDir()) 

