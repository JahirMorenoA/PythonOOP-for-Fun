class GameObject(object):
	class_name= ""
	desc=""
	objects={}

	def __init__(self, name):
		self.name=name
		GameObject.objects[self.class_name] = self

	def get_desc(self):
		return self.class_name + "\n" + self.desc

class Ninja(GameObject):
	def __init__(self,name):
		self.class_name="ninja"
		self._desc="A dark fighter"
		self.health= 20
		super(Ninja,self).__init__(name)

	@property
	def desc(self):
		if 15 < self.health <= 20:
			return self._desc
		elif 10 < self.health <= 15:
			health_line = "is getting tired"
		elif 2 < self.health <= 10:
			health_line = "is hurt"
		elif self.health == 2:
			health_line = "barely he can keep stand"
		elif self.health == 1:
			health_line = "He's almost dead"
		elif self.health <= 0:
			health_line = "is dead!"
		return self._desc + "\n" + health_line

	@desc.setter
	def desc(self, valor):
		self._desc = valor

ninja = Ninja("ninja")

def hit(noun):
	if noun in GameObject.objects:
		thing = GameObject.objects[noun]
		if type(thing) == Ninja:
			thing.health -= 1
			if thing.health <= 0:
				mensaje = "You have killed the {}!".format(thing.class_name)
			else:
				mensaje= "You hit the {}!!".format(thing.class_name)
	else:
		mensaje= "There is no {}".format(noun)

	return mensaje


def examine(noun):
	if noun in GameObject.objects:
		return GameObject.objects[noun].get_desc()
	else:
		return "There is no {} in the crews.".format(noun)


def get_input():
	command = entry.split()
	word = command[0]

	if word in GameObject.objects:
		print(GameObject.objects[word].desc)
		return
	if word in verb_dict:
		verb = verb_dict[word]
	else:
		print("Verb {} unknown".format(word))
		return
	if len(command) >= 2:
		noun_word = command[1]
		print(verb(noun_word))
	else:
		print(verb())



def say(noun):
	return 'You have said "{}"'.format(noun)


verb_dict={"say":say,"examine":examine, "hit":hit}

while True:

	inputuser = input(": ")
	entry = inputuser.lower()
	if entry == "quit":
		break
	else:
		try:
			get_input()
		except TypeError:
			if entry == "examine":
				print("You didn't say what examine")
			if entry == "say":
				print("You have not said what I have to say")



