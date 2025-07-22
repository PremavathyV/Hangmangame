import random
name=input("Enter your name :")

words = ['python', 'hangman', 'developer', 'awesome', 'keyboard', 'project']
word = random.choice(words)
guessed = ['_'] * len(word)
attempts = 6
used_letters = []

print(f"🎉 Welcome {name} to 🌟 H A N G M A N 🌟 Game!")
print("🧠 Word to guess: ", ' '.join(guessed))
print("💡 You have 6 chances. Let's go!\n")

while attempts > 0:
    guess = input("🔤 Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Enter **only one valid alphabet letter!**\n")
        continue

    if guess in used_letters:
        print("🙅‍♀️ You've already guessed that letter!\n")
        continue

    used_letters.append(guess)

    if guess in word:
        print("✅ Nice! Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print(f"❌ Oops! Wrong guess. ❤️ {attempts} chances left.")

    print("\n🧩 Word: ", ' '.join(guessed))
    print("🔁 Letters tried:", ', '.join(used_letters))
    print("-" * 40)

    if '_' not in guessed:
        print(f"\n🏆 YOU WIN, {name} 🎉 Word was: **{word}**")
        break

if '_' in guessed:
    print(f"\n💀 Game Over! The word was: **{word}**. Better luck next time 🌈")
input("Press Enter to exit")
