from vector3 import Vector3
class Force:
    def __init__(self, source, target):
        self.source = source
        self.target = target
        self.delta_v = Vector3(0, 0, 0)
        self.delta_pos = Vector3(0, 0, 0)
    def evaluate(self):
        raise NotImplementedError


class Gravity(Force):
    def evaluate(self):
        G = 6.67430e-11
        diff_vector =self.source.pos-self.target.pos
        amplitude =  G*self.source.mass*self.target.mass/diff_vector.squared_norm()
        return amplitude/diff_vector.norm()*diff_vector


class Entity:
    def __init__(self, pos, velocity,mass, forces):
        self.pos = pos
        self.mass = mass
        self.inverse_mass = 1./mass
        self.velocity = velocity
        self.forces = forces

    def compute_update(self, delta_t):
        self.delta_pos =delta_t*self.velocity
        deltas = [f.evaluate() for f in self.forces]
        self.delta_v  = Vector3(0, 0, 0)
        for d in deltas:
            self.delta_v += d * self.inverse_mass * delta_t

    def apply_update(self):
        self.pos += self.delta_pos
        self.velocity+=self.delta_v
