from interface import Interface
from modele import load_model

model, params, infos = load_model()

inta = Interface(params, model, infos)

inta.mainloop()