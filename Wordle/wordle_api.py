from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel, Field
from wordle_classbased import Wordle

app = FastAPI()


class Response(BaseModel):
    word_played: str = Field(regex=r'^[a-z]{5}$')
    answer: str = Field(regex=r'^[gmy]{5}$')

wordle = Wordle()
game = {1: wordle}

@app.get("/newgame")
def newgame():
    game[1] = Wordle()
    return {"Suggestions": game[1].wordle_words[:10], "listLength": len(game[1].wordle_words)}


@app.post("/play-round")
def play_round(response: Response):
    game[1].play_round(response.word_played, response.answer)
    return {"Suggestions": game[1].wordle_words[:10], "listLength": len(game[1].wordle_words)}
