import random
from textblob import TextBlob
from textblob.np_extractors import ConllExtractor

# import nltk

# nltk.download("punkt")

extractor = ConllExtractor()


def main():
    print("Hello, I am Marvin, the friendly robot.")
    print("You can end this conversation at any time by typing 'bye'")
    print("After typing each answer, press 'enter'")
    print("How are you today?")

    while True:
        user_input = input("> ")
        if user_input.lower() == "bye":
            break
        else:
            user_input_blob = TextBlob(user_input, np_extractor=extractor)
            np = user_input_blob.noun_phrases  # extract noun phrases
            response = ""
            if user_input_blob.polarity <= -0.5:
                response = "Oh dear, that sounds bad."
            elif user_input_blob.polarity <= 0:
                response = "Hmm, that's not great."
            elif user_input_blob.polarity <= 0.5:
                response = "Well, that sounds positive."
            elif user_input_blob.polarity <= 1:
                response = "Wow, that sounds great."

            if len(np) != 0:
                response = (
                    response + "Can you tell me more about " + np[0].pluralize() + "?"
                )
                print(response)

    print("It was nice talking to you, goodbye!")


main()
