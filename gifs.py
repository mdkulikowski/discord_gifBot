class Gif:
    def __init__(self, command, link):
        self.command = command
        self.link = link


commands = ['!herewegoagain', '!addict']


here_we_go_again = Gif(
    commands[0], 'https://media.tenor.com/cJRcMyUAiMcAAAAC/ah-shit-here-we-go-again-ah-shit.gif')

addict = Gif(
    commands[1], 'https://tenor.com/view/itch-crack-head-drugs-drug-addict-addict-gif-5783847')
