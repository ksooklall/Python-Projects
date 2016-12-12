"""
Drone Flight Planner

You are planning the amount of fuel need to complete a drone flight.
To fly higher, the drone burns 1 liter of fuel per feet. However, flying lower
charges the drone with the amount of energy equivalent to 1 liter of fuel for
every feet. Flying sideways takes no energy (only flying up and down
takes/charges energy).

Given an array of 3D coordinates named route, find the minimal amount of fuel the drone would need to fly through this route.
Explain and code the most efficient solution possible, with the minimal number of actions and variables.

Example:
Completing the route [{x:0, y:2, z:10}, {x:3, y:5, z:0}, {x:9, y:20, z:6}, {x:10, y:12, z:15}, {x:10, y:10, z:8}] requires a minimum of 5 liters of fuel.
"""

# Linear search, have two counters. One for current fuel and the other for excess fuel
# As the drone flies adjust current fuel accordingly, once current fuel < 0
# add to excess fuel and return excess furl
# T: O(n)
# S: O(1)   current_fuel and excess_fuel are stored in memory and updated

def droneFlightPlan(p):
   current_fuel=0
   excess_fuel=0
   for i in range(len(p)-1):
      if p[i+1]['z']<p[i]['z']:  # add fuel is the drone goes up
         current_fuel+= abs(p[i+1]['z']-p[i]['z']) 
      else:                      # remove fuel is the drone goes up
         current_fuel-=abs(p[i+1]['z']-p[i]['z']) 

      if current_fuel<0:                    # add excess
         excess_fuel+=abs(current_fuel)
   return excess_fuel

# A more elegant solution is noting the fact that it take the drone consumes the
# same amount of fuel going up or down. Therefore excess fuel will only be needed
# for height > the starting height. So find the max height and take the difference
# from the starting
# T: O(n) To find the max height
# S: O(1) Only maxHeight

def calcFuelElegant(path):
   maxHeight = path[0]['z']
   for i in range(len(path)-1):
      if (path[i]['z'] > maxHeight):
         maxHeight = path[i]['z']
   return maxHeight - path[0]['z']

# Testing it
if __name__ == '__main__':
    path = [{'x':0, 'y':2, 'z':10}, {'x':3, 'y':5, 'z':0},
            {'x':9, 'y':20, 'z':6}, {'x':10, 'y':12, 'z':15}, {'x':10, 'y':10, 'z':8}]
    print(calcFuelElegant(path)) # Ans = 5
