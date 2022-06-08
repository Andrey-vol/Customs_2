from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Basegame'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 10
    ENDOWMENT = 750
    TAX = 10
    P1_ROLE='Импортёр'
    P2_ROLE='Инспектор'
    WEALTH = 200
    MULTIPLIER = 2



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    p1_legal = models.CurrencyField(min=0,
                                 max = C.ENDOWMENT,
                                 label = "Сколько вы хотите провезти через таможню легально, заплатив пошлину?"
                                 )
    p1_bribe = models.CurrencyField(min=0,
                                    max=250,
                                    label="Cколько вы готовы запллатить за нелегальный провоз?")
    p1_unlegal = models.CurrencyField(min=0,
                                      max=C.ENDOWMENT,
                                      label="Сколько вы готовы провезти нелегально?"
                                      )
    def p1_unlegal_1 (group):
        C.ENDOWMENT-group.p1_legal


    def tax_1 (group):
        return group.p1_legal*(C.TAX/100)

    def set_payoffs(group):
        p1 = group.get_player_by_role(1)
        p2 = group.get_player_by_role(2)
        p1.payoff = group.p1_legal-group.tax_1-group.p1_bribe+group.p1_unlegal
        p2.payoff = C.WEALTH+group.p1_bribe*C.MULTIPLIER

    p2_acception = models.BooleanField (
        choices= [[True, "Да, принимаю"],
                  [False, "Нет, не принимаю"],
                  ], label= 'Принимаете ли вы оплату или проведёте досмотр '
                            'с целью удостовериться в правильности указанной суммы?'
    )

    p2_dos = models.BooleanField(
        choices=[[True, "Досмотреть"],
                 [False, "Не досматривать"],
                 ], label='Досмотреть партию товара?'
    )


class Player(BasePlayer):

    name = models.StringField (min=0,
                              label='Укажите Ваше имя')

    surname = models.StringField (min=0,
                              label='Укажите Вашу фамилию')

    age = models.IntegerField (min=0,
                              label= 'Для того, чтобы начать введите Ваш возраст:')
    sex = models.IntegerField(
    choices=[
        [1, 'Мужской'],
        [2, 'Женский'],
    ],
    widget=widgets.RadioSelect,
    label="Укажите Ваш пол"
)
    risk = models.IntegerField(
    choices=[
        [-3, 'Высоко рискую'],
        [-2, 'Склонен к риску'],
        [-1, 'Мало рискую'],
        [0, 'Нейтрален к риску'],
        [1, 'Не склонен к риску'],
        [2, 'Осторожен'],
        [3, 'Максимально осторожен'],
    ],
    widget = widgets.RadioSelectHorizontal,
        label="Насколько по Вашему мнению вы склонны к риску?"
    )
    #Тест на 5-ти факторный опросник личности

    ex1 = models.IntegerField(
    choices=[
        [-3, '-3'],
        [-2, '-2'],
        [-1, '-1'],
        [0, '0'],
        [1, '1'],
        [2, '2'],
        [3, '3'],
    ],
    widget = widgets.RadioSelectHorizontal,
        label="Я воспринимаю себя как открытого, полного энтузиазма"

    )

    fre1 = models.IntegerField(
        choices=[
            [-3, '-3'],
            [-2, '-2'],
            [-1, '-1'],
            [0, '0'],
            [1, '1'],
            [2, '2'],
            [3, '3'],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="Я воспринимаю себя как критичного, склонного спорить"

    )
    con1 = models.IntegerField(
        choices=[
            [-3, '-3'],
            [-2, '-2'],
            [-1, '-1'],
            [0, '0'],
            [1, '1'],
            [2, '2'],
            [3, '3'],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="Я воспринимаю себя как надежного и дисциплинированного"

    )
    emo1 = models.IntegerField(
        choices=[
            [-3, '-3'],
            [-2, '-2'],
            [-1, '-1'],
            [0, '0'],
            [1, '1'],
            [2, '2'],
            [3, '3'],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="Я воспринимаю себя как тревожного, меня легко расстроить"

    )
    open1 = models.IntegerField(
        choices=[
            [-3, '-3'],
            [-2, '-2'],
            [-1, '-1'],
            [0, '0'],
            [1, '1'],
            [2, '2'],
            [3, '3'],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="Я воспринимаю себя как открытого для нового опыта, сложного"

    )
    ex2 = models.IntegerField(
        choices=[
            [-3, '-3'],
            [-2, '-2'],
            [-1, '-1'],
            [0, '0'],
            [1, '1'],
            [2, '2'],
            [3, '3'],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="Я воспринимаю себя как замкнутого, тихого"

    )
    fre2 = models.IntegerField(
        choices=[
            [-3, '-3'],
            [-2, '-2'],
            [-1, '-1'],
            [0, '0'],
            [1, '1'],
            [2, '2'],
            [3, '3'],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="Я воспринимаю себя как сочувствующего, сердечного"

    )
    con2 = models.IntegerField(
        choices=[
            [-3, '-3'],
            [-2, '-2'],
            [-1, '-1'],
            [0, '0'],
            [1, '1'],
            [2, '2'],
            [3, '3'],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="Я воспринимаю себя как неорганизованного, беспечного"

    )
    emo2 = models.IntegerField(
        choices=[
            [-3, '-3'],
            [-2, '-2'],
            [-1, '-1'],
            [0, '0'],
            [1, '1'],
            [2, '2'],
            [3, '3'],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="Я воспринимаю себя как спокойного, эмоционально устойчивого"

    )
    open2 = models.IntegerField(
        choices=[
            [-3, '-3'],
            [-2, '-2'],
            [-1, '-1'],
            [0, '0'],
            [1, '1'],
            [2, '2'],
            [3, '3'],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="Я воспринимаю себя как обыкновенного, не творческого"

    )


    WF = models.IntegerField(
        choices=[
            [-2, 'Низкий'],
            [-1, 'Ниже среднего'],
            [0, 'Средний'],
            [1, 'Выше среднего'],
            [2, 'Высокий'],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="Каков по Вашему мнению Ваш ежемесячный доход?"
    )
# PAGES
class Game1(Page):
    form_model = 'group'
    form_fields = ['p1_legal','p1_unlegal',"p1_bribe"]

    def is_displayed(self):
        return self.role == C.P1_ROLE

class Game2(Page):
        form_model = 'group'
        form_fields = ['p2_acception']

        def is_displayed(self):
            return self.role == C.P2_ROLE


class Game3(Page):
    form_model = 'group'
    form_fields = ['p2_dos']

    def is_displayed(self):
        return self.role == C.P2_ROLE

class Results(Page):
    pass


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(group: Group):
        print('in after_all_players_arrive')
        print(group.p1_legal)
        print(group.p1_bribe)
        print(group.p1_unlegal)
        p1 = group.get_player_by_role(C.P1_ROLE)
        p2 = group.get_player_by_role(C.P2_ROLE)
        tax = group.tax_1()
        p1.payoff = group.p1_legal - tax - group.p1_bribe + group.p1_unlegal
        p2.payoff = 1.0 * C.WEALTH + group.p1_bribe * C.MULTIPLIER

class Introduction(Page):
    form_model = 'player'
    form_fields = ['name','surname','age','sex','risk','WF']

    def is_displayed(player):
        return player.round_number == 1

class Test(Page):
    form_model = 'player'
    form_fields = ['ex1','fre1','con1','emo1','open1','ex2','fre2','con2','emo2','open2']

    def is_displayed(player):
        return player.round_number == 1


page_sequence = [Introduction, Test, Game1,  ResultsWaitPage, Game3, ResultsWaitPage, Game2, ResultsWaitPage, Results]

