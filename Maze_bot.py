"""This is part of original code for solving minibot assignment of intro to python course """
#pip install --upgrade --force-reinstall minobot
class common_robot():
    
    def __init__(self,global_direction:int,corrdination:list):
        self.global_direction=global_direction
        self.corrdination=corrdination
        self.corrdination=corrdination
         
            
    def compass_turn(self,target):
        action = target- self.global_direction
        if action < -180:
            action+=360
        elif action > 180:
            action -= 360
        elif abs(action) == 180: 
            turn_left()
            turn_left()
            self.global_direction=target 
        elif action==0: 
            return target
    
        if action == 90:
            turn_left()
            self.global_direction=target 
        elif action == -90:
            turn_right()
            self.global_direction=target   
                       
    def common_move_recorder(self):
        if self.global_direction==90:
            move()
            self.corrdination[1]+=1
        if self.global_direction==270:
            move()
            self.corrdination[1]-=1
        if self.global_direction==180:
            move()
            self.corrdination[0]-=1
        if self.global_direction==0:
            move()
            self.corrdination[0]+=1   
        
    def op(self,temp):
        op_direction=temp+180
        if op_direction >=360:
            return op_direction-360
        else:
            return op_direction
            
    def robot_image_move(self,memory,robot_state,temp_direction):
        score={0:0,90:0,180:0,270:0}
        image_coordination={0:[self.corrdination[0]+1,self.corrdination[1]],
                            90:[self.corrdination[0],self.corrdination[1]+1],
                            180:[self.corrdination[0]-1,self.corrdination[1]],
                            270:[self.corrdination[0],self.corrdination[1]-1]}
        
        if temp_direction !=360:
            robot_state[self.op(temp_direction)]=1
        for key in robot_state:
            if robot_state[key]==1:
                continue
            elif key==self.op(temp_direction):
                continue
            elif tuple(image_coordination[key]) in memory:
                score[key]=2
            else:
                score[key]=3
        return score
             
    def common_move_system(self):
        robot_memory=[tuple(self.corrdination)]
        temp_md=360
        while not has_reached_end():
            robot_state1={0:1,90:1,180:1,270:1}
            for key in robot_state1:
                self.compass_turn(key)
                if can_move():
                    robot_state1[key]=0
            score=self.robot_image_move(memory=robot_memory,robot_state=robot_state1,temp_direction=temp_md)
            optimal_direction=max(score,key=score.get)
            self.compass_turn(optimal_direction)
            temp_md=optimal_direction
            self.common_move_recorder()
            if tuple(self.corrdination) not in robot_memory:
                robot_memory.append(tuple(self.corrdination))
##instance                            
def solution_random():
    robot=common_robot(0,[0,0])
    robot.common_move_system()            

solve_maze("simple_random", solution_random)
##
class common_robot_colour():
    
    def __init__(self,global_direction:int,coordination:list):
        self.global_direction=global_direction          #initialize global_direction 0 degree to spawn direction
        self.coordination=coordination                  #initialize coordination (0,0) to spawn tile
            
    def compass_turn(self,target):
        """compass system can give 0 90 180 270 global navigation, +90 mean turn lefr -90 mean turn right"""
        action = target- self.global_direction
        if action < -180:
            action+=360
        elif action > 180:
            action -= 360
        elif abs(action) == 180: 
            turn_left()
            turn_left()
            self.global_direction=target 
        elif action==0: 
            return target
    
        if action == 90:
            turn_left()
            self.global_direction=target 
        elif action == -90:
            turn_right()
            self.global_direction=target 
              
    def compass_turn_right(self):
        """use compass turn can make sure whole moving system work well"""
        target_r=self.global_direction-90
        if target_r<0:
            target_r+=360
        self.compass_turn(target_r)
        
    def common_move_recorder(self):
        """coordination recorder can record every steps with coordination (x,y) """
        if self.global_direction==90:
            move()
            self.coordination[1]+=1
        if self.global_direction==270:
            move()
            self.coordination[1]-=1
        if self.global_direction==180:
            move()
            self.coordination[0]-=1
        if self.global_direction==0:
            move()
            self.coordination[0]+=1   
                
    def robot_image_move_x(self,parent_colour:str,step_trace:list):
        """robot detect the environment by 360 degree can give a score for 4 direction, 
        tile grade :Unexplored>current colour(most current tile)>parent colour> current opponent direction>wall  """
        score={0:0,90:0,180:0,270:0}
        image_coordination={0:[self.coordination[0]+1,self.coordination[1]],
                            90:[self.coordination[0],self.coordination[1]+1],
                            180:[self.coordination[0]-1,self.coordination[1]],
                            270:[self.coordination[0],self.coordination[1]-1]}
        #score[self.op(temp_direction)]=1
        if parent_colour=="initial" and tuple(self.coordination)==(0,0):
            return False
        index_cd=step_trace.index(tuple(self.coordination))
        for key in score:
            self.compass_turn(key)
            if not can_move():
                score[key]=0

            elif can_move() and get_forward_color()=='none':
                score[key]=4
            elif index_cd==0:
                if can_move() and get_forward_color()==parent_colour:
                    score[key]=2
            elif tuple(image_coordination[key]) == step_trace[index_cd-1]:
                score[key]=3
        if get_current_color()=='yellow':
            print(score, self.coordination,step_trace)                      
        return score
    
                
    def advanced_common_move_system(self):              
        branch_colour=("red", "blue","green","yellow","purple","cyan", "pink")
        n=0
        branch_colour_memory={"red":"initial"}    #colour: [parent colour, total explored steps, total checked steps                  
        step_trace:list[str,list[tuple]]={branch_colour[n]:[tuple(self.coordination)]}

        while not has_reached_end()
            base_counter=0
            while True and not has_reached_end():
                """self explore stage"""
                if can_move() and get_forward_color() =='none':
                    base_counter=0
                    if get_current_color() =='none':
                        paint_current(branch_colour[n])
                        #branch_colour_memory[branch_colour[n]][1]+=1
                    self.common_move_recorder() 
                    step_trace[branch_colour[n]].append(tuple(self.coordination))
                    #steps_counter+=1 
                    #step_trace[tuple(self.coordination)]=tuple([[branch_colour[n],steps_counter]])
                else:
                    if base_counter ==4:
                        if get_current_color() =='none':
                            paint_current(branch_colour[n])
                            #branch_colour_memory[branch_colour[n]][1]+=1
                        #branch_colour_memory[branch_colour[n]][2]+=1
                        break
                    base_counter+=1    
                    self.compass_turn_right()


            while True and not has_reached_end():
                """trace-detect stage"""
                decision_score=self.robot_image_move_x(branch_colour_memory[branch_colour[n]],step_trace[branch_colour[n]])
                if decision_score== False :
                    return False
                direction=max(decision_score,key=decision_score.get)
                if decision_score[direction]==4:
                    self.compass_turn(direction)
                    self.common_move_recorder()     #edit
                    if get_current_color()=='none':
                        parent_colour=branch_colour[n]
                        if branch_colour[n+1] not in branch_colour_memory:
                                n+=1
                        else:
                            for colour in branch_colour:
                                if colour not in branch_colour_memory:
                                    n=branch_colour.index(colour)  
                                    break 
                    branch_colour_memory[branch_colour[n]]=parent_colour
                    step_trace[branch_colour[n]]=[tuple(self.coordination)]
                    print(branch_colour_memory)
                    break
                else:
                    self.compass_turn(direction)
                    self.common_move_recorder()
                    if get_current_color() != branch_colour[n]:
                        print(branch_colour[n])
                        n=branch_colour.index(get_current_color())
                        print(branch_colour[n],print(branch_colour_memory[branch_colour[n]]))
                        break
                    
          
        if has_reached_end():
            return True
##instance
def solution_complex():
    common_robot=common_robot_colour(0,[0,0])

    common_robot.advanced_common_move_system()
    
competition_maze1 = [[0,0,0,0,0,0],
                    [0,0,0,1,1,1],
                    [0,1,0,1,0,0],
                    [0,1,0,0,0,0],
                    [2,0,0,1,0,0]] 
solve_maze("complex", solution_complex)
show_maze(competition_maze1)
solve_maze(competition_maze1,solution_complex)
