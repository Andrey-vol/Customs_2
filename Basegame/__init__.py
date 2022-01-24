from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Basegame'
    players_per_group = 2
    num_rounds = 10
    endowment = 750
    tax = 10
    p1_role='Импортёр'
    p2_role='Инспектор'
    wealth = 200



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    p1_legal = models.CurrencyField(min=0,
                                 max = Constants.endowment,
                                 label = "Сколько вы хотите провезти через таможню легально, заплатив пошлину?"
                                 )
    p1_bribe = models.CurrencyField(min=0,
                                    max=250,
                                    label="Cколько вы готовы запллатить за нелегальный провоз?")
    p1_unlegal = models.CurrencyField(min=0,
                                      max=Constants.endowment,
                                      label="Сколько вы готовы провезти нелегально?"
                                      )
    def p1_unlegal_1 (self):
        Constants.endowment-self.p1_legal


    def tax_1 (self):
        self.p1_legal*(Constants.tax/100),

    def set_payoffs(self):
        p1 = self.get_player_by_role (role=Constants.p1_role)
        p2 = self.get_player_by_role (role=Constants.p2_role)
        p1.payoff = self.p1_legal-self.tax_1()-self.p1_bribe+self.p1_unlegal_1()
        p2.payoff = Constants.wealth+self.p1_bribe

    p2_acception = models.BooleanField (
        choices= [[True, "Да, принимаю"],
                  [False, "Нет, не принимаю"],
                  ], label= 'Принимаете ли вы оплату или проведёте досмотр '
                            'с целью удостовериться в правильности указанной суммы?'
    )


class Player(BasePlayer):

    age = models.IntegerField(min=0,
                              label= 'Для того, чтобы начать введите Ваш возраст:')
    sex = models.IntegerField(
    choices=[
        [1, 'Мужской'],
        [2, 'Женский'],
    ],
    widget=widgets.RadioSelect,
    label="Укажите Ваш пол"
)
# PAGES
class Game1(Page):
    form_model = 'group'
    form_fields = ['p1_legal','p1_unlegal',"p1_bribe"]

    def is_displayed(self):
        return self.role == Constants.p1_role

class Game2(Page):
        form_model = 'group'
        form_fields = ['p2_acception']

        def is_displayed(self):
            return self.role == Constants.p2_role

class Results(Page):

    def vars_for_template (player:role):
        group = player.


class ResultsWaitPage(WaitPage):
    pass



class Introduction(Page):
    form_model = 'player'
    form_fields = ['age','sex']



class Results(Page):
    pass


page_sequence = [Introduction, Game1,  ResultsWaitPage, Game2, ResultsWaitPage, Results]
