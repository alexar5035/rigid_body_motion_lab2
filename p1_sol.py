# import the required modules
import math
import numpy as np

def rot_2d(theta):
	"""
	Receives an input in radians and
	returns a 2D rotation matrix
	R = [cos(theta) -sin(theta)
	     sin(theta)  cos(theta)]
	"""
	rot = np.array([[math.cos(theta), -math.sin(theta)],
					[math.sin(theta), math.cos(theta)]])
	return rot

# use lecture slides for the mathematical equations 
def rot_x(psi):
	rot = np.array([[1.0,  0.0, 0.0],
				    [0.0, math.cos(pi/2), -math.sin(pi/2)],
					[0.0, math.sin(pi/2), math.cos(pi/2)]])
	return rot
	
def rot_y(theta):
	rot = np.array([[math.cos(pi/2),  0.0, math.sin(pi/2)],
				    [0.0, 1.0, 0.0],
					[-math.sin(pi/2), 0.0, math.cos(pi/2)]])
	return rot
	
def rot_z(phi):
	rot = np.array([[math.cos(pi/2),  -math.sin(pi/2), 0.0],
					[math.sin(pi/2),   math.cos(pi/2), 0.0],
				    [0.0, 0.0, 1.0]])
	return rot