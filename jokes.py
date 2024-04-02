import random

#GLOBAL 
jokes = [
    {
        "joke": "Why don't scientists trust atoms?",
        "response": "Because they make up everything!"
    },

]

def get_random_question():
    """Returns a random joke pair, from the global list of jokes

    Returns:
        dict(str): joke and response pair, with keys 'joke' and 'response'
    """
    return random.choice(jokes)


