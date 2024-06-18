# Documentación de la API de Dragon Ball

### Introducción
La API de Dragon Ball proporciona información detallada sobre personajes, sagas, episodios y otros aspectos del universo de Dragon Ball. Esta API es ideal para desarrolladores que deseen integrar información de Dragon Ball en sus aplicaciones, sitios web o proyectos.

### Información General
- Base URL: https://apidragonball.vercel.app/
- Formato de Respuesta: JSON
- Autenticación: Algunos endpoints requieren una clave de API. Puedes obtener tu clave de API registrándote en nuestro sitio web.

### Endpoints Disponibles
#### 1. Personajes
Obtener todos los personajes

- **URL**: /dragonball, /dragonballz y proximamente mas
- **Método**: GET
**Descripción**: Recupera una lista de todos los personajes de Dragon Ball.
- **Parámetros de Consulta:**
id (opcional): Filtra personajes por nombre.

### Ejemplo de Solicitud
`GET /characters`

#### Ejemplo de Respuesta
    [
        {
            "id": "6666cc9b1a4827579e4b4657",
            "name": "Anuciador",
            "genre": "Masculino",
            "race": "Humano",
            "image": "https://apidragonball.vercel.app/static/images/Anunciador_Dokkan.png",
            "planet": "Tierra",
            "description": "El Anunciador (アナウンサー Anaunsā¿?, Announcer) es quien presenta cada edición del Torneo Mundial de las Artes Marciales en Isla Papaya como locutor desde el comienzo del manga y anime de Dragon Ball hasta Dragon Ball GT, siendo principalmente el comentarista en todas las peleas de la competición. Aunque no lo aparente con su traje negro, sus gafas de sol y su cabello rubio peinado hacia atrás, el Anunciador también es uno de los monjes que resguarda el templo sagrado que alberga el torneo.",
            "biography": "El Anunciador presentando la batalla entre Krilin y Bacterian. En cada torneo, aparte de el 21, se produce un suceso desafortunado que realiza su papel, como en la saga del Rey Piccolo cuando fue testigo del asesinato de Krilin a manos de Tambourine. Más tarde, se vuelve muy importante como testigo de Goku en la lucha contra Piccolo desde la barrera, junto con los amigos de Goku. El Anunciador Mundial de Artes Marciales es el único que no es de los Guerreros Z en no abandonar el torneo cuando Piccolo dice que masacrará a todos. Finalmente, cuando Goku es declarado el Ganador del Torneo porque Piccolo se cae fuera de la arena, haciendo de él uno de los pocos civiles en acordarse de esto (este suceso se hace referencia más adelante en la saga de Majin Buu cuando Piccolo compite en el torneo, en el que en tono de broma le pide no destruir el Tatami otra vez, a lo que Piccolo respondió de forma amistosa que lo intentará)."
        },
    ...
    ]

### Obtener un personaje por ID
- **URL**: /characters/{id}
- **Método**: GET
- **Descripción**: Recupera la información de un personaje específico por su ID.

### Ejemplo de Solicitud
    GET /characters/6666cc9b1a4827579e4b4657

#### Ejemplo de Respuesta


    {
        "id": "6666dc6ee29e9670e0613d11",
        "name": "Capitan Dock",
        "genre": "Masculino",
        "race": "Humano",
        "image": "https://apidragonball.vercel.app/static/images/Captain_Dock.png",
        "planet": "Tierra",
        "description": "Dock (ドック Dokku[1]¿?) es un soldado del Ejército del Listón Rojo que trabaja en la Brigada Azul bajo el cargo de capitán para el General Blue en el manga y anime de Dragon Ball.",
        "biography": "Dock es enviado por el General Blue a la Casa Kame para robar el Radar del Dragón y secuestrar a Muten Roshi ya que piensan que es un científico y que él creó el radar. Cuándo llega a Kame House inmediatamente le pide a Muten Roshi el radar del dragón, luego lo amenaza con que si no le entrega también las Esferas del Dragón matará a Lunch. Pero Muten Roshi se niega y golpea fuertemente en el estómago a Dock, derrotando de paso a todos sus soldados, a excepción de dos, uno el cual fue asesinado por Lunch y otro que intenta escapar pero es visto y le ordena limpiar la isla que esta llena de todos los soldados derrotados, incluido Dock. Dock vuelve a aparecer en Dragon Ball GT escapando del Infierno, pero volvería al lugar luego de que Androide Número 17 del Infierno fuese derrotado por Son Goku."
    }

![Captura de pantalla 2024-06-18 092548](https://github.com/juanppdev/DragonBallApi/assets/81490579/d292faa1-5dbc-4722-a731-88f7a17ea028)
![Captura de pantalla 2024-06-18 092527](https://github.com/juanppdev/DragonBallApi/assets/81490579/acc266ff-7b55-4330-b133-c456c8ac5429)

