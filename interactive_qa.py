import openai

# Set up the necessary API key for the LLM service (masking the value for security)
openai.api_key = 'YOUR_API_KEY_HERE'

def chat_with_student(query, previous_context=None):
    """
    Handles interaction with the LLM to provide Q&A functionality.

    Args:
    - query (str): The question or input from the student.
    - previous_context (list): Optional. Maintains state and context for ongoing dialogues.

    Returns:
    - response (str): The LLM-generated response and additional resources.
    """
    # Set the initial context if not provided
    if previous_context is None:
        previous_context = []

    # Add the new query to the context
    previous_context.append({'role': 'user', 'content': query})

    # Generate response using the LLM
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=previous_context
    )

    # Extract the message from the response
    answer = response['choices'][0]['message']['content'].strip()

    # Update the context with the assistant's response
    previous_context.append({'role': 'assistant', 'content': answer})

    return answer, previous_context

# Example Usage
if __name__ == "__main__":
    context = []  # Context can keep track of conversation history
    question = "What is Newton's second law?"
    answer, updated_context = chat_with_student(question, context)
    print(answer)
