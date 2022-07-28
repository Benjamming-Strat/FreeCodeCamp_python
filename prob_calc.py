import random
from collections import defaultdict
from copy import deepcopy, copy

class Hat:
    def __init__(self, **kwargs) -> None:
        self.args_dict = kwargs
        self.contents = [[k] * v for k,v in kwargs.items()]
        self.contents = [ele for sublist in self.contents for ele in sublist ]
           
    

    def draw(self, draw_amount):
        self.removed_balls = []
        if draw_amount > len(self.contents):
            return self.contents
        
        reps = 1
        while reps <= draw_amount:
            reps += 1
            appender = self.contents.pop(random.randrange(len(self.contents)))         
            self.removed_balls.append(appender)

        
        return self.removed_balls
    
    def __copy__(self):
        hat = Hat(**self.__dict__['args_dict'])
        return hat

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    probs_counter = 0 
    for i in range(num_experiments):
        hat = copy(hat)
        removed_balls = hat.draw(num_balls_drawn)
        # Dictionary declaration
        removed_balls_dic = defaultdict(int)
        # Input list initialisation
        Input = removed_balls
        # Dictionary populate
        for i in Input:
            removed_balls_dic[i]+= 1

        removed_balls_dic = dict(removed_balls_dic)
        
        counter=0
        for k,v in expected_balls.items():
            if k in removed_balls_dic.keys():
                if removed_balls_dic[k] >= v:
                    counter += 1
        
        if counter == len(expected_balls):
            probs_counter +=1

        
    return probs_counter / num_experiments
    

if __name__ == "__main__":

    hat_1 = Hat(blue=3,red=2,green=6)
    probability = experiment(hat_1, {"blue":2,"green":1}, 4, 1000)
    print(probability)
    print(hat_1)
    
    
         

    
        