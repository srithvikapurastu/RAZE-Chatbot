import time

print("🔄 Loading AI Engine...")
time.sleep(2)
print("✅ AI Ready!\n")

from colorama import init, Fore, Style

init(autoreset=True)

print(Fore.MAGENTA + "=" * 60)
print(Fore.CYAN + Style.BRIGHT + "✨ VibeMatch AI ✨")
print(Fore.YELLOW + "Find Your Perfect Energy...")
print(Fore.MAGENTA + "=" * 60)

vibes = {
    "sad": [
        "🎧 Lo-fi Night Playlist",
        "☕ Rainy Cafe Journaling",
        "📖 Read a Comfort Book",
        "🌃 Midnight Walk"
    ],
    "happy": [
        "🎉 Dance Playlist",
        "📸 Aesthetic Photo Session",
        "🌈 Explore New Cafes",
        "🎨 Creative Art Challenge"
    ],
    "stressed": [
        "🧘 Meditation Session",
        "🎵 Soft Piano Music",
        "🌿 Nature Walk",
        "☁️ Digital Detox"
    ],
    "motivated": [
        "🚀 Build a Side Project",
        "📚 Learn a New Skill",
        "💪 Workout Session",
        "🎯 Goal Planning"
    ],
    "bored": [
        "🎬 Watch a Mind-Bending Movie",
        "🎮 Try an Indie Game",
        "🗺️ Solo Exploration",
        "📱 Create Content"
    ]
}

print(Fore.GREEN + "\n💭 Select Your Mood:")
print(Fore.CYAN + "sad | happy | stressed | motivated | bored")

mood = input(Fore.YELLOW + "\n✨ Enter mood: ").lower()

if mood in vibes:
    print(Fore.MAGENTA + "\n🔮 Analyzing Your Vibe...")
    print(Fore.BLUE + "━━━━━━━━━━━━━━━━━━━━━━━━━━")

    for i, item in enumerate(vibes[mood], start=1):
        print(Fore.GREEN + f"{i}. {item}")

    print(Fore.BLUE + "━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(Fore.YELLOW + '\n🌟 Quote of the Day:')
    print(Fore.CYAN + Style.BRIGHT +
          '"Your vibe attracts your tribe."')

else:
    print(Fore.RED + "\n⚠️ Mood not recognized!")
    print(Fore.YELLOW + "Try one of these moods:")
    print(Fore.CYAN + "sad, happy, stressed, motivated, bored")

print(Fore.MAGENTA + "\n✨ Thanks for using VibeMatch AI ✨")