from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

client = OpenAI()


def get_ai_answer(question):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content":
             f"""You are helpful assistant. Answer question.
             """},
            {"role": "user", "content": question}
        ]
    )

    model_answer = completion.choices[0].message.content
    return model_answer


class Question(BaseModel):
    question: str


app = FastAPI()


@app.post("/questions/")
async def get_question(Question: Question):
    question = Question.question
    answer = get_ai_answer(question=question)
    return answer

    