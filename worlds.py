from random import randint
worlds = ["mecanografia", "estetoscopio", "operacion", "colectivo", "artista", "aplanadora", "mensajero", "negocios", "papelera", "informatica", "delincuenta","escoba", "resonante", "mercurio", "portero","tempestad","advertencia","trasbordar","hamacas","guardaspaldas","kamikaze","mantequilla","proteger","fotocopia","galletitas","eternidad","amenazar","decapitar","espaguetis","veredicto","estudios","reclinar","aspero","calculadora","sombrilla","chimenea","camioneta","microondas","caballete"]

def get_world():
  random = randint(0,len(worlds) - 1)
  world = worlds[random]
  return world