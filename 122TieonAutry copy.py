# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random
import leaderboard as lb

#-----game configuration----
turtleshape = "square"
turtlesize =  3
turtlecolor = "red"

score = 0

timer = 35
counter_interval = 1000
timer_up = False

#scoreboard variables
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input("please enter your name.")


#-----initialize turtle-----
clifford = trtl.Turtle(shape=turtleshape)
clifford.color(turtlecolor)
clifford.shapesize(turtlesize)
clifford.speed(300)

john = trtl.Turtle()
john.ht()
john.penup()
john.goto(-370, 270)

font_setup = ("Arial" , 30, "bold")
john.write(score , font=font_setup)

josh = trtl.Turtle()
josh.ht()
josh.penup()
josh.goto(270, 270 )

#-----game functions--------
def clifford_clicked(x,y):
    print("clifford got clicked")
    change_position()
    update_score()


def change_position():
    clifford.penup()
    clifford.ht()
    if not timer_up:
        cliffordx = random.randint(-400,400)
        cliffordy = random.randint(-300,300)
        clifford.goto(cliffordx,cliffordy)
        clifford.st()
    

def update_score():
    global score
    score += 1
    print(score)
    john.clear()
    john.write(score , font=font_setup)

def countdown():
  global timer, timer_up
  josh.clear()
  if timer <= 0:
    josh.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    josh.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    josh.getscreen().ontimer(countdown, counter_interval) 
    
# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global clifford

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, clifford, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, clifford, score)

#-----events----------------

wn = trtl.Screen()
wn.bgcolor("yellow")
clifford.onclick(clifford_clicked)
wn.ontimer(countdown, counter_interval) 
wn.mainloop()