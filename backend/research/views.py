import asyncio
from rest_framework.decorators import api_view
from rest_framework.response import Response
from agents.graph import graph
from .models import Conversation
from .cache import redis_client


@api_view(["POST"])
def ask_question(request):

    question = request.data.get("question")

    # ---------- REDIS CACHE ----------
    cached = redis_client.get(question)

    if cached:
        print("The answer is there in cache")
        return Response({
            "cached": True,
            "answer": cached
        })

    # ---------- RUN AGENTS ----------
    result = asyncio.run(
        graph.ainvoke({"question": question})
    )
    print("In views,ans bt graph is ", result,"Done")

    plan = result.get("plan")
    search_result = result.get("search_result")
    answer = result.get("answer")

    # ---------- SAVE POSTGRESQL ----------
    Conversation.objects.create(
        question=question,
        plan=plan,
        search_result=search_result,
        answer=answer
    )

    # ---------- SAVE REDIS ----------
    redis_client.set(question, answer)

    return Response(result)