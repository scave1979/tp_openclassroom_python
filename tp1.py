#https://openclassrooms.com/courses/apprenez-a-programmer-en-python/tp-un-dictionnaire-ordonne


class dictord :
	

	
	def __init__(self, base= {}, **kwargs):
		
		self._valeurs = []
		self._cles = []
		
		
			
			
	def __repr__(self):
		
		str = "{"
		
		for elt in len(self_valeurs):
			 str += self_valeurs[elt] + ":" + self._cles[i] + ","
			 
		str += "}"
		
		
	def __str__(self):
		
		str = "{"
		
		for elt in len(self_valeurs):
			 str += self_valeurs[elt] + ":" + self._cles[i] + ","
			 
		str += "}"
		
		
	def __del__(self):
		del self._values
		del self._cles
			
			
	def __setattr__(self, nom_attr, val_attr):
			 
		if nom_attr not in self._cles:
			self._cles.append(nom_attr)
		i = self._cles.find(nom_attr)
		self._values[i] = val_attr
			
	def __getattr__(self, nom_attr) :
		
		if nom_attr not in self._cles:
			raise KeyError ("key not found")
			
		i = self._cles.find(nom_attr)
		return self._values[i]

	 
	def __hasattr__(self, nom_attr):

		if nom_attr not in self._cles:
			return False
		else :
			return True


	def __delattr__(self, nom_attr):
		
		if nom_attr not in self._cles:
			raise KeyError ("key not found")
			
		i = self._cles.find(nom_attr)
		del self._cles[i]
		del self._values[i]

	   
	def __contains__(self, item):
		return item in self._values
		
	 
	def __len__(self):
		return len(self._values)
	   

if __name__ == '__main__':	
	d = dictord()
	#print d
	
	
	
	
	
