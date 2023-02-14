# import the required modules
import rbm
import math
import numpy as np

if __name__ == '__main__':
	# define test values
	psi = math.pi/2
	theta = math.pi/2
	phi = math.pi/2
	# rotation about x through pi/2
	x = rbm.rot_x(psi)
	# rotation about y through pi/2
	y = rbm.rot_y(theta)
	# rotation about z through pi/2
	z = rbm.rot_z(phi)
	# calculate a total rotation via FIXED FRAME
	R = np.matmul(z, y)
	R1 = np.matmul(R, x)
