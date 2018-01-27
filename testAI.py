from env4 import TicTacToeEnv as env
from AI import AI
import numpy as np
import pandas as pd
def csv_to_arr(file):
 df=pd.read_csv(file,sep=',',header=None)
 return(df.values)
env=env()
player1=AI(env,2)
player2=AI(env,1)
player1.q=csv_to_arr('data1.csv')
player2.q=csv_to_arr('data2.csv')
p1=0 
p2=0
for i in range(1000000):
 env.reset()
 player1.reset()
 player2.reset()
 while (env.done==False):
  player1.nextState()
  #env.show_board()
  if (env.done):
   p1=p1+1
   break
  player2.nextState()
  if (env.done):
   p2=p2+1
print(p1,p2)