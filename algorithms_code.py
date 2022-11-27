# -*- coding: utf-8 -*-
"""ALGORITHMS CODE

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1a8aV7JCb6X6COG4j8w4ImBNoHUCY6vyW

PART 1: UNIVERSITY AND INFO DIRECTORY AND FILTERS
"""

# DIRECTORIO UNI :

class University():
  def __init__(self, name, location, annualbudget, studytype, fields, puborpriv, languages, academicrequirements):
    self.name = name
    self.location = location 
    self.annualbudget = annualbudget 
    self.studytype = studytype
    self.fields = fields
    self.puborpriv = puborpriv
    self.languages = languages
    self.academicrequirements = academicrequirements
    self.photo = None
    self.contact = None

IEUniversityMadrid = University("IEUniversityMadrid","Madrid","20k-30k","Project based","Business","Private","English","Great")
IEUniversitySegovia = University("IEUnivesitySegovia","CastillaLeon","20k-30k","Project based","Business","Private","English","Great")
ICADE = University("ICADE","Madrid", "10k-15k","Study based","Business","Private","Spanish","Excellent")
ICAI = University("ICAI","Madrid","10k-15k","Study based","Engineering","Private","Spanish","Excellent")
CIHS = University("CIHS","Madrid","10k-15k","Study based","Social Sciences","Private","Spanish","Great")
UC3M = University("UC3M","Madrid","1k-2k","Study based","General","Public","Spanish","Excellent")
Complutense = University("Complutense","Madrid","1k-2k","Study based","General","Public","Spanish","Good")
Autonoma = University("Autonoma","Madrid","1k-2k","Study based","General","Public","Spanish","Good")
ESICValencia = University("ESICValencia", "Madrid","10k-15k","Project based","Business","Private","Spanish","Medium")
UNAV = University("UNAV","Pamplona","10k-15k","Study based","Health sciences","Private","Spanish","Great")
#PompeuFabra = University("Barcelona","1k-2k","Study based", "General","Public","Catalan","Excelent")
#ESADE = University("Barcelona", "15k-20k","Project based","Business","Private","Spanish","Great")
#UniversidadSalamanca = University("CastillaLeon","<1k","Study based","General","Public","Spanish","Good")
#ReyJuanCarlos = University("Madrid","1k-2k","Study based","General","Public","Spanish","Good")
#PolitecnicaValencia = University("Valencia","<1k","Study based","Engineering","Public","Spanish","Great")

Universities = [IEUniversityMadrid, IEUniversitySegovia, ICADE, ICAI, 
                CIHS, UC3M, Complutense, Autonoma, ESICValencia, UNAV, ]

#PART 1 IN PYCHARM (photos included)

from graphics import*

class University():
    def __init__(self, name, location, annualbudget, studytype, fields, puborpriv, languages, academicrequirements, photo, contact):
        self.name = name
        self.location = location
        self.annualbudget = annualbudget
        self.studytype = studytype
        self.fields = fields
        self.puborpriv = puborpriv
        self.languages = languages
        self.academicrequirements = academicrequirements
        self.photo = photo
        self.contact = contact

    def show_image(self):
        win = GraphWin("University image", 1000, 1000)
        b = Image(Point(500, 500), self.photo)
        Image.draw(b, win)
        input()
        win.close()

IEUniversityMadrid = University("IE University Madrid","Madrid","20k-25k","Project based","Business","Private","English","Great","IE_Business_School_Logo.png","university@ie.edu")
IEUnivesitySegovia = University("IE University Segovia","CastillaLeon","20k-25k","Project based","Business","Private","English","Great","IE_Business_School_Logo.png","university@ie.edu")
ICADE = University("ICADE Comillas","Madrid", "10k-15k","Study based","Business","Private","Spanish","Excellent","logo_icade.png","admisiones@comillas.edu")
ICAI = University("ICAI Comillas","Madrid","10k-15k","Study based","Engineering","Private","Spanish","Excellent","logo-icai-site.png","admisiones@comillas.edu")
CIHS = University("CIHS Comillas","Madrid","10k-15k","Study based","Social Sciences","Private","Spanish","Great","logo_CIHS.png","admisiones@comillas.edu")
UC3M = University("Uiversidad Carlos III de Madrid","Madrid","0k-5k","Study based","General","Public","Spanish","Excellent","Logo_UC3M.png","dpd@uc3m.es")
Complutense = University("Universidad Complutense de Madrid","Madrid","0k-5k","Study based","General","Public","Spanish","Good","complu_logo.png","oipd@ucm.es")
Autonoma = University("Universidad Autonoma de Madrid","Madrid","0k-5k","Study based","General","Public","Spanish","Good","Autonoma-Logo.png","informacion.general@uam.es")
ESICValencia = University("ESIC Valencia","Madrid","10k-15k","Project based","Business","Private","Spanish","Medium","ESIC.png","info.valencia@esic.edu")
UNAV = University("Universidad de Navarra","Pamplona","10k-15k","Study based","Health sciences","Private","Spanish","Great","Universidad de Navarra_LOGO.png","info@unav.es")
PompeuFabra = University("Universitat Pompeu Fabra","Barcelona","0k-5k","Study based", "General","Public","Catalan","Excelent","Pompeu Fabra_Logo.png","carreres.professionals@upf.edu")
ESADE = University("ESADE University","Barcelona", "15k-20k","Project based","Business","Private","Spanish","Great","ESADE_logo.png","shop@2000publimark.com")
UniversidadSalamanca = University("Universidad de Salamanca","CastillaLeon","0k-5k","Study based","General","Public","Spanish","Good","Salamanca_Logo.png","protocolo@usal.es")
ReyJuanCarlos = University("Universidad Rey Juan Carlos","Madrid","0k-5k","Study based","General","Public","Spanish","Good","REY JUAN CARLOS_LOGO.png","fuenlabrada.secretariadealumnos@urjc.es")
PolitecnicaValencia = ("Universidad Politecnica de Valencia","Valencia","0k-5k","Study based","Engineering","Public","Spanish","Great","Politecnica_Valencia_LOGO.png","informacion@upv.es")

Universities = [IEUniversityMadrid, IEUnivesitySegovia, ICADE, ICAI,
                CIHS, UC3M, Complutense, Autonoma, ESICValencia, UNAV,
                PompeuFabra, ESADE, UniversidadSalamanca, ReyJuanCarlos,
                PolitecnicaValencia]

# FILTERED SEARCH :
  #Location 
  #Price
  #Name of university

"""PART 2: PERSONAL FORM; "DONT KNOW WHERE TO STUDY? FILL OUT THIS FORM"
"""

#Spacialties
#Sort of study
#Types of grades 

# PARA 5 PREGUNTAS

pregunta1 = input("Do you feel confortable working in groups (a) or would you rather work by yourself (b)? Type a or b: ")
pregunta2 = input("Are you capable of studying for long time periods (b) or do you prefer shorter ones (a)? Type a or b: ")
pregunta3 = input("Do you prefer studying in a quiet library (b) or studying outdoors with more people (a)? Type a or b: ")
pregunta4 = input("Are you spontaneous and ingenious (a) or analytical and detailed (b)? Type a or b:  ")
pregunta5 = input("Are you used to studying everything by heart (b) or do you understand what you study and then put it in your own words (a)? Type a or b: ")
listarespuestas = [pregunta1, pregunta2,pregunta3, pregunta4, pregunta5]

def studytype(listarespuestas):

  counter = 0
  for pregunta in listarespuestas:
    if pregunta.lower() == 'a':
      counter = counter + 1
    if pregunta.lower() == 'b':
      counter = counter - 1
  if counter > 0 :
    return "Project based"
  else:
    return "Study based"

def filterbystudytype(studytype, Universities):
  selected = []
  for university in Universities:
    if university.studytype == studytype:
      selected.append(university.name)
  return(selected)

studytype(listarespuestas)

studytype = studytype(listarespuestas)
filterbystudytype(studytype,Universities)

#SET INTERSECTIONS, TOPIC 11, SESSION 21, AT THE END
#MAX HEAP TOPIC 7, SESSION 13, AT THE END

"""El numero de intersections entre lo que dice el user y los atributos de las universidades va a ser el priority value de la max heap, donde cada valor sera una tupla --> (priority value, university name)

para ello Universities tiene que ser un diccionario donde cada university es una key y sus values un set de atributos, por ejemplo (solo con una universidad) --> 
Universities =  {"IEUniversityMadrid":{"IEUniversityMadrid","Madrid","20k-30k","Project based","Business","Private","English","Great"}, "UNIVERSIDAD2" : {....,....,...},....}


Respuestas del user al cuestionario se guardan en otro set y, mediante un loop, se comparan con todos y cada uno de los sets de atributo cada universidad. Obteniendo asi el numero de intersecciones entre ambos len(respuestas & setatributosuniversidad).

se asignan el numero de intersecciones de cada set de atributos con el nombre de la universidad y se meten en una heap.

heapq_max


Se hara pop de la heap y se le mostrara al user la universidad con mas coincidencias. Si el user quiere ver la segunda universidad con mas coincidencias, se le pregunta y si dice que si, se activa otra vez el heappop
"""