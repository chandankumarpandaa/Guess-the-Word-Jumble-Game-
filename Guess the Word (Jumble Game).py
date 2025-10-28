import random

words = ["python", "game", "simple", "fun", "program"]
word = random.choice(words)
jumble = ''.join(random.sample(word, len(word)))

print("Jumbled word:", jumble)
guess = input("Your guess: ")

if guess == word:
    print("🎉 Correct!")
else:
    print("😢 Wrong! The word was:", word)
