class Force:
    def __init__(self, source, target):
        self.source = source
        self.target = target
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

    def update(self, delta_t):
        self.pos += delta_t*self.velocity
        for f in self.forces:
            print(f.evaluate())
            self.velocity += f.evaluate()*self.inverse_mass*delta_t
