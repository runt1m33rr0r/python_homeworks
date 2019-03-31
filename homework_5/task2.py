import wx
import string
from random import randint


class Game:
    def __init__(self):
        self.padding = 10
        self.words = self.load_words()
        self.selected_word = self.select_word()
        self.guessed = [self.selected_word[0], self.selected_word[len(self.selected_word) - 1]]
        self.intial_tries = 6
        self.tries = self.intial_tries

        self.app = wx.App()
        self.frame = wx.Frame(None, title='game', size=(600, 700))
        self.panel = wx.Panel(self.frame)

        self.font = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        self.player_message = wx.StaticText(self.panel, label='')
        self.player_message.SetFont(self.font)
        self.word = wx.StaticText(self.panel, label=self.construct_word())
        self.word.SetFont(self.font)
        self.letters_grid = wx.GridSizer(rows=3, cols=11, hgap=0, vgap=0)

        self.content = wx.BoxSizer(wx.VERTICAL)
        self.content.AddSpacer(self.padding)
        self.content.Add(self.word, flag=wx.ALIGN_CENTER)
        self.content.AddSpacer(self.padding)
        self.content.Add(self.player_message)
        self.content.AddSpacer(self.padding)
        self.content.Add(self.letters_grid, flag=wx.ALIGN_CENTER)
        self.content.AddSpacer(self.padding)
        self.letter_buttons = []

        for let in string.ascii_uppercase:
            button = wx.ToggleButton(self.panel, label=let, size=(50, 50))
            button.Bind(wx.EVT_TOGGLEBUTTON, self.select_letter(button.GetLabel()))
            self.letters_grid.Add(button)
            self.letter_buttons.append(button)

        self.images = self.load_images()
        self.image = wx.StaticBitmap(self.panel, bitmap=self.images[0])
        self.content.Add(self.image, flag=wx.ALIGN_CENTER)
        self.content.AddSpacer(self.padding)

        self.guess_button = wx.Button(self.panel, label='Guess')
        self.guess_button.Bind(wx.EVT_BUTTON, self.reset_game)
        self.content.Add(self.guess_button, flag=wx.ALIGN_CENTER)

        self.panel.SetSizer(self.content)
        self.panel.Layout()

        self.frame.Show()
        self.app.MainLoop()

    
    def reset_game(self, ev):
        for button in self.letter_buttons:
            button.SetValue(False)

        self.player_message.SetLabel('')
        self.tries = self.intial_tries
        self.selected_word = self.select_word()
        self.guessed = [self.selected_word[0], self.selected_word[len(self.selected_word) - 1]]
        self.word.SetLabel(self.construct_word())
        self.image.SetBitmap(self.images[0])


    def load_images(self):
        result = []
        for i in range(7):
            result.append(wx.Bitmap('./images/%d.jpg' % i, wx.BITMAP_TYPE_JPEG))
        return result


    def load_words(self):
        with open('./words.txt') as f:
            return f.read().splitlines()


    def select_word(self):
        return self.words[randint(0, len(self.words) - 1)].upper()


    def construct_word(self):
        result = []
        
        for let in self.selected_word:
            if let in self.guessed:
                result.append(let)
            else:
                result.append('_')

        return ''.join(result)


    def control_game_state(self):
        for let in self.guessed:
            if let not in self.selected_word:
                self.tries -= 1
                self.guessed.remove(let)
                self.image.SetBitmap(self.images[self.intial_tries - self.tries])

        if '_' not in self.word.GetLabel():
            self.player_message.SetLabel('You win!')
        elif self.tries == self.intial_tries:
            self.player_message.SetLabel('')
        elif self.tries <= 0:
            self.player_message.SetLabel('You lose!')
        else:
            self.player_message.SetLabel('You have %d tries left!' % self.tries)


    def select_letter(self, letter):
        def on_select(ev):
            self.guessed.append(letter)
            self.word.SetLabel(self.construct_word())
            self.control_game_state()

        return on_select


game = Game()
