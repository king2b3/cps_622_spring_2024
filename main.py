import time
from jokes import get_random_question

def main():
    joke = get_random_question()

    print(f"{joke['joke']}")

    #basic counter to delay the response
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')

    print(f"{joke['response']}")

if __name__ == "__main__":
    main()
