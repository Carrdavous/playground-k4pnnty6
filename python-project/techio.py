def send_msg(channel, msg):
    print(f'TECHIO> message --channel "{channel}" "{msg}"')


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")


def felicitations():
    send_msg("Félicitations 🎉 !", "Vous avez répondu correctement à l'énoncé.")
