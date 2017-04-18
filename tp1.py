#https://openclassrooms.com/courses/apprenez-a-programmer-en-python/tp-un-dictionnaire-ordonne


class dictord :
	

	
	def __init__(self, base= {}, **kwargs):
		
		self._valeurs = []
		self._cles = []
		
		for i in base :
			self[i] = base[i]
			
		for i in kwargs:
			self[i] = kwargs[i]
			
			
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
        """Méthode appelée quand l'objet est supprimé"""
        del self._values
        del self._cles
        
        
def __setattr__(self, nom_attr, val_attr):
        """Méthode appelée quand on fait objet.nom_attr = val_attr.
        On se charge d'enregistrer l'objet"""
     
    if nom_attr not in self._cles:
		self._cles.append(nom_attr)
	i = self._cles.find(nom_attr)
	self.values[i] = val_attr
		
def __getattr__(self, nom_attr) :
	
	if nom_attr not in self._cles:
		raise KeyError ("key not found")
		
	i = self._cles.find(nom_attr)
	return self.values[i]

 
def __hasattr__(self, nom_attr):

		if nom_attr not in self._cles:
			return False
		else :
			return True


def __delattr__(self, nom_attr):
	if nom_attr not in self._cles:
		raise KeyError ("key not found")
		
	i = self._cles.find(nom_attr)
	return self.values[i]
	
delattr(objet, "nom") # = del objet.nom ou objet.__delattr__("nom")
   
	
