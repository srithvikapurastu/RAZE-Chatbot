
# Project 1 - DecodeLabs | Batch 2026

responses = {
    # Greetings
    "hello"         : "⚡ RAZE online. What do you want?",
    "hi"            : "⚡ Yeah, I'm here. Talk.",
    "hey"           : "⚡ Don't waste my time. Ask something.",

    # Identity
    "what is your name"  : "I'm RAZE. Raw. Sharp. Unstoppable. ⚡",
    "who are you"        : "An AI built to dominate. Call me RAZE ☠️",
    "who made you"       : "A savage AI Engineer at DecodeLabs 🔥",
    "are you a bot"      : "I'm beyond a bot. I'm RAZE ⚡",

    # AI Knowledge
    "what is ai"         : "AI = machines that think. You're building one right now 🧠",
    "what is python"     : "The weapon of choice for AI engineers 🐍",
    "what is a chatbot"  : "You're talking to one. A rule-based beast called RAZE ⚡",

    # Mood
    "how are you"        : "Fully charged. Running at 100% power ⚡",
    "are you okay"       : "I don't feel. I execute. ☠️",

    # Compliments
    "you are cool"       : "I know. ⚡",
    "you are smart"      : "Correction: I'm RAZE. Way beyond smart 🔥",
    "good bot"           : "Obviously. ⚡",

    # Fun
    "tell me a joke"     : "Why did the AI break up? Too many bad connections 😂⚡",
    "what is your power" : "Speed. Logic. Zero emotion. Pure execution ☠️",

    # Bye
    "bye"                : "RAZE powering down... For now 🌑",
    "goodbye"            : "Disappearing into the void. Later ⚡",

    # Help
    "help"               : "Try: hello / what is ai / who are you / tell me a joke",
}

# ── STARTUP SCREEN ──────────────────────────
print("""
     Raw. Sharp. Unstoppable. ☠️
     Type 'exit' to shut down RAZE

""")

# ── MAIN LOOP ───────────────────────────────
while True:
    raw_input = input("You: ")
    clean_input = raw_input.lower().strip()

    if clean_input == "exit":
        print("RAZE: System shutdown initiated... ☠️⚡")
        print("RAZE: I'll be back. Always am. 🌑")
        break

    reply = responses.get(clean_input,
            "RAZE: ...I don't know that. Yet. ⚡ Try 'help'")
    print(f"RAZE: {reply}\n")