from fastapi import APIRouter
from app.models import ChatRequest, ChatResponse
from app.services.memory import save_message, get_history
from app.services.embeddings import get_embeddings
from app.services.retriever import retrieve_context
from app.services.llm import generate_response

router = APIRouter(prefix="/chat", tags=["Conversational RAG"])

@router.post("/", response_model=ChatResponse)
async def chat_endpoint(req: ChatRequest):
    user_message = req.message
    session_id = req.session_id


    history = get_history(session_id)

    query_vector = get_embeddings([user_message])[0]
    context = retrieve_context(query_vector)

    response_text, booking_info = generate_response(user_message, session_id, context)


    save_message(session_id, "user", user_message)
    save_message(session_id, "assistant", response_text)

    return ChatResponse(
        response=response_text,
        context_used=context,
        booking_confirmation=booking_info.json() if booking_info else None
    )
