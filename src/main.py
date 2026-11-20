from interface import Interface
from modele import Modele

model, params, infos = Modele.load_model()

inta = Interface(params, model, infos)

inta.mainloop()