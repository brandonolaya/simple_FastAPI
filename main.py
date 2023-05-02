from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

app= FastAPI() #crear la instancia de FastAPI
app.title = "Mi app con FastAPI"
app.version = '0.0.1'


#Lista de manhwas que por dentro tiene un diccionario
manhwas = [
    {
        "id":1,
        "title": "The Beginning After the End",
        "genres": "Drama, Acción, Aventura, Comedia, Reencarnación,Magia, Superpoderes",
        "overview": "King Grey has unrivaled strength, wealth, and prestige in a world governed by martial ability. However, solitude lingers closely behind those with great power. Beneath the glamorous exterior of a powerful king lurks the shell of man, devoid of purpose and will. Reincarnated into a new world filled with magic and monsters, the king has a second chance to relive his life. Correcting the mistakes of his past will not be his only challenge, however. Underneath the peace and prosperity of the new world is an undercurrent threatening to destroy everything he has worked for, questioning his role and reason for being born again",
        "year": 2018
    },
    {
        "id":2,
        "title": "Lout of Count’s Family",
        "genres": "Action, Adventure, Comedy, Fantasy, Isekai, Magic, Pilitical",
        "overview": "Kim Roksu has one life motto: “Let’s not get beat up.” But after dozing off somewhere midway through the novel “Birth of a Hero,” he wakes up as Cale Henituse - one of the minor villains in the novel who gets the beating of a lifetime from soon-to-be hero Choi Han. Only time will tell how much longer he has before that dreadful encounter. Can Kim Roksu change the course of this story so he can enjoy a long and lavish life free of the soon-to-be hero?",
        "year": 2020
    },
    {
        "id":3,
        "title": "A Returner's Magic Should Be Special",
        "genres": "Action, Adventure, Comedy, Fantasy, Age Transformation, Magic School",
        "overview": "For 10 years, magical prodigy Desir and his party have been battling inside the mysterious Shadow Labyrinth—and against the end of the world. Much of humanity has already perished and just as Desir is about to be killed, he's sent back 13 years into the past. Despite knowing the cursed future that lies ahead, Desir steels his resolve as he sees an opportunity to train his friends and better prepare to face Armageddon together, without losing the ones they love!",
        "year": 2018
    },
    {
        "id":4,
        "title": "So I'm a Spider, So What? ",
        "genres": "Action, Adventure, Comedy, Drama, Dungeon, Isekai, RPG",
        "overview": "I used to be a normal high school girl but in the blink of an eye, I woke up in a place I've never seen before and-and I was reborn as a spider?! How could something that's nothing more than a tiny spider (that's me) possibly survive in literally the worst dungeon ever? Are there no rules? There should be some rules! Who the hell is responsible for this? SHOW YOUR FACE!",
        "year": 2015
    },
    {
        "id":5,
        "title": "The Eminence in Shadow",
        "genres": "Action, Adventure, Comedy, School life, Parody, Reincarnation, Shounen",
        "overview": "Shadowbrokers are those who go unnoticed, posing as unremarkable people, when in truth, they control everything from behind the scenes. Cid wants to be someone just like that more than anything, and something as insignificant as boring reality isn't going to get in his way! He trains in secret every single night, preparing for his eventual rise to power—only to denied his destiny by a run-of-the-mill (yet deadly) traffic accident. But when he wakes up in another world and suddenly finds himself at the head of an actual secret organization doing battle with evil in the shadows, he'll finally get a chance to act out all of his delusional fantasies! ",
        "year": 2018
    }
]


@app.get('/', tags=['home'])
def message():
    """Solo es para ver que tambien se puede retorna
    una etiqueta gtml
    """
    return HTMLResponse('<h1>Hellos putos</h1>')

@app.get('/manhwas', tags=['manhwas'])
def get_manhwas():
    """retorna una lista completa
    """
    return manhwas


@app.get('/manhwas/{id}', tags=['manhwas'])
def get_manhwas(id: int):
    """Se realiza un manejo de paremetros de ruta en donde busca
    por id las lista entre los diccionarios y retorna todo su contenido
    """
    for item in manhwas:
        if item["id"] == id:
            return item
    return []


@app.get('/manhwas/', tags=['manhwas'])
def get_manhwas_by_title(title: str, year: int):
    """En esta funcion se piden dos parametros y se hace una listconhvergetion
    para la busqueda y retornar todo el contenido donde se cumplan esas dos condiciones
    """
    return [item for item in manhwas
            if item["title"] == title and item["year"]==year]

@app.post('/manhwas', tags=['manhwas'])
def create_manhwa(id: int = Body(), title: str = Body(),
                genres: str = Body(), overview: str = Body(), year: int = Body()):
    """Pertime añadir algo al diccionario, es mas facil de leer
    y reemplazr los valores
    """
    manhwas.append({
        "id":id,
        "title":title,
        "genres":genres,
        "overview":overview,
        "year":year
    })
    return manhwas

@app.put('/manhwas{id}', tags=['manhwas'])
def update_manhwa(id: int, title: str = Body(),
                genres: str = Body(), overview: str = Body(), year: int = Body()):
    for item in manhwas:
        if item["id"] == id:
            item['title'] = title,
            item['genres'] = genres,
            item['overview'] = overview,
            item['year']=year
            return item

@app.delete('/manhwas{id}', tags=['manhwas'])
def delete_manhwa(id: int):
    for item in manhwas:
        if item['id'] == id:
            manhwas.remove(item)
            return manhwas