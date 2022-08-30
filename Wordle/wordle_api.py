from fastapi import FastAPI
from pydantic import BaseModel, Field
from wordle_classbased import Wordle, create_word_list

app = FastAPI()


class Response(BaseModel):
    word_played: str = Field(regex=r'^[a-z]{5}$')
    answer: str = Field(regex=r'^[gmy]{5}$')

wordle = Wordle(create_word_list())
game = {1: wordle}

@app.get("/newgame")
def newgame():
    game[1] = Wordle(create_word_list())
    return {"Suggestions": game[1].wordle_words[:10], "Turn": game[1].turn}


@app.post("/play-round")
def play_round(response: Response):
    game[1].play_round(response.word_played, response.answer)
    return {"Suggestions": game[1].wordle_words[:10], "Turn": game[1].turn}
