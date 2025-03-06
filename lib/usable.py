def double(x):
  return x*2
class Player:
  def __init__(self):
    self.health = 100
    self.attackv = 5
  def attack(self, target: "Player"):
    target.update(health=target.health-self.attack)
  def regen(self):
    self.update(health=self.health+10)
  def update(self, **kwargs):
    self.health = kwargs.get("health", self.health)
    self.attackv = kwargs.get("attack", self.attack)
