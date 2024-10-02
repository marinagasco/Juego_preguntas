bienvenida = """"Bienvenide al 🔎 “Algoritmo de la verdad” 👩🏼‍💻 : un juego en el que tendrás que demostrar tus dotes
de data analyst(o detective)🕵🏽‍♀️ y discernir entre la realidad ✅ y la mentira 🤥"""
presentación = """Verás 10 preguntas con 4 opciones con UNA sola respuesta que es *VERDAD*.¡Pero ojo cuidao!👀
No todo es lo que parece y en este juego… ¡Mucho menos!🤯 """
start = "PressEnter"

print(bienvenida)
print("-------------------------------------------------------------------------------------------------------")
print(presentación)
print("-------------------------------------------------------------------------------------------------------")
print(start)
print("-------------------------------------------------------------------------------------------------------")

start_game = input("PressEnter")

nombre_usuario = input("¿Quién se va a poner a poner a prueba? 🧐 Dinos tu nombre🫵🏼:")
                        
print(f"Ahora sí que sí...🥁🥁🥁 {nombre_usuario} ¡Estamos ready para empezar el “Algoritmo de la verdad”!🚀🚀🚀")
print("-------------------------------------------------------------------------------------------------------")

# Diccionario que almacena las preguntas, respuestas y respuesta_correcta.
preguntas = {
    1:  {
        "pregunta": "1. ¿Cuál de estas historias sobre inteligencia artificial es VERDAD?",
        "respuestas": {"a)": "Una IA escribió una novela que ganó un premio literario en Japón.", 
                       "b)": "Una IA fue nombrada CEO de una empresa tecnológica en Silicon Valley.", 
                       "c)": "Un programa de IA creó una obra de arte vendida por millones de dólares en una subasta.",
                       "d)": "Un robot con IA ganó una competición de ajedrez contra el campeón mundial sin entrenamiento previo."},
        "respuesta_correcta": "c"
    },
    2:  {
        "pregunta": "2. ¿Cuál de estas noticias sobre avances médicos es MENTIRA?",
        "respuestas": {"a)": "Un científico chino modificó genéticamente a dos bebés para que sean inmunes al VIH.", 
                       "b)": "En 2025, se espera que los órganos impresos en 3D estén disponibles para trasplantes humanos.", 
                       "c)": "Un hospital en Alemania curó una enfermedad genética rara mediante terapia de genes.",
                       "d)": "Un equipo en Islandia logró clonar un mamut utilizando ADN prehistórico."},
        "respuesta_correcta": "d"
    },
    3:  {
        "pregunta": "3. ¿Cuál de estas noticias sobre animales es VERDAD?",
        "respuestas": {"a)": "Un perro salvó a su dueño de un incendio en su casa en Londres.", 
                       "b)": "Un gato fue premiado por guiar a un turista perdido en los Alpes hasta un refugio.",
                       "c)": "Un delfín rescató a un grupo de buceadores en una cueva subterránea en Australia.",
                       "d)": "Un elefante se unió a una protesta en defensa de los derechos animales en Tailandia."},
       "respuesta_correcta": "b"
    },
    4:  {
        "pregunta": "4. ¿Cuál de estos hechos son MENTIRA?",
        "respuestas": {"a)": "Un niño en Canadá creó un dispositivo que limpia los océanos y fue premiado por la ONU.", 
                       "b)": "Un proyecto en Países Bajos convierte casas abandonadas en refugios para abejas.", 
                       "c)": "Un grupo de jubilados en España plantó 10.000 árboles en un solo día",
                       "d)": "Un programa en Suecia permite a las personas donar su energía sobrante de paneles solares a hospitales."},
        "respuesta_correcta": "a"
    },
    5:  {
        "pregunta": "5. ¿Cuál de estos logros es VERDAD?",
        "respuestas": {"a)": "Una científica desarrolló una vacuna contra el cáncer de piel.", 
                       "b)": "Una ingeniera mexicana inventó una prótesis que puede ser controlada por la mente.", 
                       "c)": "Una activista de 16 años creó una fundación para enseñar a niñas a codificar.",
                       "d)": "Una deportista de 55 años ganó una medalla de oro en natación en los Juegos Olímpicos."},
        "respuesta_correcta": "c"
    },
    6:  {
        "pregunta": "6. ¿Cuál de estas noticias es MENTIRA?",
        "respuestas": {"a)": "Una mujer fue elegida primera ministra de su país a los 25 años.", 
                       "b)": "Una activista ganó el Nobel de la Paz por sus esfuerzos en promover la educación de las niñas en África.", 
                       "c)": "Una astronauta pasó 1 año en el espacio sin regresar a la Tierra.",
                       "d)": "Una escritora se convirtió en la mujer más joven en ganar el premio Pulitzer por una novela."},
        "respuesta_correcta": "a"
    },
    7:  {
        "pregunta": "7. ¿Cuál de las siguientes historias, aunque parezca inverosímil, son VERDAD?",
        "respuestas": {"a)": "Un hombre logró sobrevivir cayendo desde un avión sin paracaídas gracias a una pila de heno que amortiguó su caída.", 
                       "b)": "Un grupo de científicos descubrió un tiburón de más de 500 años nadando en el Ártico.", 
                       "c)": "Se reportó que un gato callejero atravesó medio país para volver con su dueño después de que lo dieron en adopción.",
                       "d)": "Una mujer fue rescatada en el Himalaya por un Yeti después de quedar atrapada en una avalancha."},
        "respuesta_correcta": "b"
    },
    8:  {
        "pregunta": "8. ¿Cuál de estas historias por muy creíble que parezca, son MENTIRA??",
        "respuestas": {"a)": "Un millonario japonés compró una isla desierta para construir un parque temático inspirado en películas de terror.", 
                       "b)": "Un grupo de arqueólogos en América del Sur descubrió una ciudad perdida con tecnología avanzada desconocida para la época.", 
                       "c)": "Un magnate de Silicon Valley declaró que se está preparando para congelar su cuerpo y revivirlo en el futuro.",
                       "d)": "Una tribu aislada en el Amazonas fue contactada por primera vez en 2023 tras décadas de permanecer desconocida para la humanidad."},
        "respuesta_correcta": "b"
    },
    9:  {
        "pregunta": "9. ¿Cuál de las siguientes noticias, a pesar de ser surrealistas, son VERDAD?",
        "respuestas": {"a)": "David Bustamente anunció su retiro de la música para abrir una granja en Cantabria.", 
                       "b)": "Anabel Pantoja fue sorprendida organizando una quedada de fans en un karaoke en la playa, con disfraces de tiburones incluidos.", 
                       "c)": "Isabel Pantoja lanzará una línea de perfumes inspirados en las noches de Cantora",
                       "d)": "Kiko Rivera se ha propuesto hacer una gira nacional de DJ... ¡pero solo en bodas y bautizos!"},
        "respuesta_correcta": "c"
    },
    10: {
        "pregunta": "10. ¿Cuál de las siguientes historias sobre Belén Esteban son MENTIRA?",
        "respuestas": {"a)": "Rompió un plato en directo durante una discusión acalorada en televisión.", 
                       "b)": "Participó en una campaña para defender el uso de protectores solares.", 
                       "c)": "Hizo un directo accidental en Instagram mientras dormía.",
                       "d)": "Fue acusada de tener problemas con la seguridad del aeropuerto por llevar un perfume en la maleta."},
        "respuesta_correcta": "b"
    }
}


# iniciamos el controlador de preguntas en uno porque en el diccionario empieza por uno si no me da error.
controlador_preguntas = 1
# iniciamos el puntuaje en 0. 
puntuaje = 0

# Utilizo el bucle WHILE para recorrer las preguntas.
while controlador_preguntas < 11 :

    pregunta_actual = preguntas[controlador_preguntas]

    # Para mostrar la pregunta y las opciones busco detro del diccionario, donde le estoy pidiendo que acceda a la pregunta actual (key) y a los valores de 'respuesta' : sub-diccionario.
    print(pregunta_actual["pregunta"]) # Aqui se imprime el texto de la pregunta que se va a mostrar al usuario.
    print("a)", pregunta_actual["respuestas"]['a)']) # Aqui se imprime la opcion respuesta "a" que esta detro del subdiccionario.
    print("b)", pregunta_actual["respuestas"]['b)']) # """" "b"
    print("c)", pregunta_actual["respuestas"]['c)']) # """" "c"
    print("d)", pregunta_actual["respuestas"]['d)']) # """" "d"

    respuesta_usuario = input("Elije una respuesta (a, b, c, d):").lower() # Le pedimos al usuario que nos diga una respuesta.

    # Verificamos si la respuesta es válida (solo aceptamos a, b, c, d)
    if respuesta_usuario not in ["a", "b", "c", "d"] :
        print("te has equivocado : te toca MARINA")
        print("-------------------------------------------------------------------------------")
        continue  # Si la respuesta no es válida, vuelve a pedir la misma pregunta

    # Verificar si la respuesta es correcta
    if respuesta_usuario == pregunta_actual["respuesta_correcta"]:
        print("¡Correcto!: te sigue tocando MARINA JEJEJE 😎")
        print("-------------------------------------------------------------------------------")
        puntuaje += 1  # Suma 1 si la respuesta es correcta y se almacena para luego el resultado.

    else: # Aqui si el usuario se equivoca, se lo hago saber y se suma 1 error. 
        print(f"Incorrecto. La respuesta correcta es: {pregunta_actual['respuesta_correcta']}.")  #MARINAAAAAAAAAAA AYUDAAAAAAA SOY MUY BASICAA
        print("-------------------------------------------------------------------------------")

    controlador_preguntas += 1  # Avanza a la siguiente pregunta 

# Para mostrar el puntuaje final:
print(f"TE TOCO OTRA VEZ MARINA {puntuaje} Y LO QUE MAS SE TE OCURRA")

# Comentarios personalizados segun el puntuaje:
if puntuaje == 10:
    print("¡Excelente! AYUDA MARINA")
elif puntuaje >= 7:
    print("¡Muy bien hecho! AYUDA MARINA")
elif puntuaje >= 4:
    print("No está mal. AYUDA MARINA")
else:
    print("Necesitas estudiar más. AYUDA MARINA")