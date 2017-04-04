from classProjectile import Projectile
	
def getInputs():
	a = input("Enter the launch angle (in degrees): ")
	v = input("Enter the initial velocity (in meters/sec): ")
	h = input("Enter the initial height (in meters): ")
	t = input("Enter the time initerval between position calculations: ")
	return a, v, h, t

def main():
	angle, vel, h0, time = getInputs()
	cball = Projectile(angle, vel, h0)
	maxheight = 0
	while cball.getY() >= 0:
		cball.update(time)
		if cball.getY() > maxheight:
			maxheight = cball.getY()
		
	print "\nDistance traveled: %0.1f meters." % (cball.getX())
	print "\nMaximum height: %0.1f meters." % (maxheight)

main()
