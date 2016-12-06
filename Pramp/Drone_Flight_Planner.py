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

def droneFlightPlanner(p):
   f=0
   e=0
   for i in range(len(p)-1):
      if p[i+1]['z']<p[i]['z']:
         f+= abs(p[i+1]['z']-p[i]['z'])
      else: f-=abs(p[i+1]['z']-p[i]['z'])

      if f<0: e+=abs(f)
   return e

# Elegant solution
def calcFuelSimple(zRoute):
   maxHeight = zRoute[0]['z']
   for i in range(len(zRoute)-1):
      if (zRoute[i]['z'] > maxHeight):
         maxHeight = zRoute[i]['z']
   return maxHeight - zRoute[0]['z']

if __name__ == '__main__':
    path = [{'x':0, 'y':2, 'z':10}, {'x':3, 'y':5, 'z':0},
            {'x':9, 'y':20, 'z':6}, {'x':10, 'y':12, 'z':15}, {'x':10, 'y':10, 'z':8}]
    print(calcFuelSimple(path))
