# Object Oriented Programming OOP
'''
class NameOfClass():
	def __init__(self, param1, param2):
		"""
  	This is the constructior of trhe class
    Allows to create instances of the class
		self.param is equal to the parameter passed to the constructor self.param1 = param1
   	"""
		self.param = param1
  	self.param2 = param2
   
  def some_method(self):
  """
  A function inside a class is called method
  Passing the self as argument let python know the method belongs to the class
  """
		# DO Something
		print ( self.param1)
'''
print ('Simple: '.upper())
class Dog():
  # Class object attributes are like global variables
  # They are placed above the constructor and are the same in any instance of the class
  species = 'mammal'
  
  def __init__(self, mybreed, name, spots):
    # Attribute
    # We take in the argument
    # Assign it using self.attribute_name = argument
    # Attributes are calles without () cause they are not executed
    self.breed = mybreed
    self.name = name
    self.spots = spots
  
  def bark(self):
    """
    OPERATIONS/actions -----> methods
    Functions defined inside the class body are called methods
    Used to perform operations that some times uses the attributes of the object defined in __init__ (the constructor)
    Functions acting on a object through its attributes by the use of the self keyword.
    As methods perform actions, they have to be called with () to call them
    """
    print ('  WOOF! my name is {}'.format(self.name))

my_dog = Dog(mybreed='Lab', name='Sammy', spots=False)
print (f'- Instance of the class Dog: {my_dog} with breed: {my_dog.breed}, name: {my_dog.name} and spots: {my_dog.spots}')
print (f'- The Dog is a {my_dog.species}.')
print ('Methods: '.upper())
print (f'- Call method without initialization (my_dog.bark): {my_dog.bark}')
print ('- Call and initialize method (my_dog.bark()):')
my_dog.bark()

print ('Circle'.upper())
class Circle():
  # CLASS OBJECT ATTRIBUTE
  pi = 3.14
  
  def __inint__(self, radius=1):
    """
    Some attribute can just be created
    When calling class object attr one can use self (self.pi), as instantiating the attrib or using the class name (Circle.pi)
    The className.attrib calling just work with class object attributes
    """
    self.radius = radius
    self.area = radius*radius*Circle.pi
  
  def get_circumference(self):
    return self.radius * self.pi * 2

my_circle = Circle()
my_circle
print ('- Circle: {}'.format(my_circle))
    


