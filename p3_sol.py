# import the required modules
import p2_sol
import math
import numpy as np
# Transformation 1 (name it H_1):
	# A translation of 2.5 units along the current x-axis,
	# followed by a translation of 0.5 units along the current z-axis,
	# followed by a translation of -1.5 units along the current y-axis.
	
def H_1():
	Tx = p2_sol.trans_x(2.5)
	Tz = p2_sol.trans_z(0.5)
	Ty = p2_sol.trans_y(-1.5)
	# calculate a total rotation via CURRENT FRAMES
	R = np.matmul(Tx, Tz, Ty)

# Transformation 2 (name it H_2):
	# A translation of 0.5 units along the current z-axis,
	# followed by a translation of 2.5 units along the current x-axis 
	# followed by a translation of -1.5 units along the current y-axis.
	
def H_2():
	Tz = p2_sol.trans_z(0.5)
	Tx = p2_sol.trans_x(2.5)
	Ty = p2_sol.trans_y(-1.5)
	# calculate a total rotation via CURRENT FRAMES
	R = np.matmul(Tz, Tx, Ty)
	
# Transformation 3 (name it H_3):
	# A transformation with the same steps and order as in Transformation 1 but in the fixed frame
	
def H_3():
	Tx = p2_sol.trans_x(2.5)
	Tz = p2_sol.trans_z(0.5)
	Ty = p2_sol.trans_y(-1.5)
	# calculate a total rotation via FIXED FRAME
	R = np.matmul(Ty, Tz, Tx)
	
# Transformation 4 (name it H_4):
	# A transformation with the same steps and order as in Transformation 2 but in the fixed frame
	
def H_4():
	Tz = p2_sol.trans_z(0.5)
	Tx = p2_sol.trans_x(2.5)
	Ty = p2_sol.trans_y(-1.5)
	# calculate a total rotation via FIXED FRAME
	R = np.matmul(Ty, Tx, Tz)
	
#Transformation 5 (name it H_5):
	# A rotation by angle 𝜋/2 about the current x-axis
	# followed by a translation of 3 units along the current x-axis, 
	# followed by a translation of -3 units along the current z-axis,
	# followed by a rotation by angle  ―𝜋/2 about the current z-axis
	
def H_5():
	Tx = p2_sol.trans_x(math.pi/2)
	Tx = p2_sol.trans_x(3)
	Tz = p2_sol.trans_z(-3)
	Tz = p2_sol.trans_z(-math.pi/2)
	# calculate a total rotation via CURRENT FRAMES
	R = np.matmul(Tx, Tz)

