import matplotlib.pyplot as plt
class Vector3:
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z+other.z)

    def __mul__(self, other):
        return  Vector3(other*self.x, other*self.y, other*self.z)
    __rmul__ = __mul__


class Force:
    def __init__(self, direction):
        self.direction = direction


class Object:
    def __init__(self, pos, velocity,mass, forces):
        self.pos = pos
        self.mass = mass
        self.inverse_mass = 1./mass
        self.velocity = velocity
        self.forces = forces

    def update(self, delta_t):
        self.pos += delta_t*self.velocity
        for f in self.forces:
            self.velocity += f.direction*self.inverse_mass*delta_t


starting_point = Vector3(0, 0, 100)
starting_velocity = Vector3(1, 0, 0)
gravity = Force(Vector3(0, 0, -9.81))  # gravitational force actually depends on mass, but lets ignore that for now....
forces = [gravity]
ball = Object(starting_point, starting_velocity, 1, forces)  #make mass 1 to make acceleration 9.81

dt = 0.001
Nsteps = 5000

ts = [dt*i for i in range(Nsteps)]
poslog = [ball.pos]
vlog   = [ball.velocity]
for _ in ts:
    ball.update(dt)
    poslog.append(ball.pos)
    vlog.append(ball.velocity)
xs = [p.x for p in poslog]
ys = [p.y for p in poslog]
zs = [p.z for p in poslog]

plt.plot(xs,zs)
plt.show()