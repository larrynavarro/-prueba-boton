class restaurante(object):
  def __init__(self, name):
     self.name = name

  def set_num_trabajadores(self, numero):
      self.num_trabajadores = numero 

  def print_num_trabajadores(self):
      print self.name + " tiene " + str(self.num_trabajadores)+ "trabajadores"

rincon = restaurante("restaurante de mariscos de Nicaragua")

print rincon.name

rincon.set_num_trabajadores(15)
rincon.print_num_trabajadores()

rivas = restaurante("retaurante rincon")
rivas.set_num_trabajadores(12)
rivas.print_numt_trabajadore()
