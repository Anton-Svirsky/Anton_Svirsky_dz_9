from telegram import Update
from telegram.ext import callbackcontext
import datetime
import re


def hello(update: Update, context: callbackcontext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


def help_command(update: Update, context: callbackcontext):
    update.message.reply_text(f'/hello\n/time\n/help\n/calculation')


def time_command(update: Update, context: callbackcontext):
    update.message.reply_text(f'{datetime.datetime.now().time()}')


def calculation_command(update: Update, context: callbackcontext):
    operations = {
        "*": lambda x, y: str(float(x) * float(y)),
        "/": lambda x, y: str(float(x) / float(y)),
        "+": lambda x, y: str(float(x) + float(y)),
        "-": lambda x, y: str(float(x) - float(y))
    }
    prior_reg_exp = r"\((.+?)\)"
    operations_reg_exp = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"

    def eval_function(exp: str) -> str:
        while match := re.search(prior_reg_exp, exp):
            exp: str = exp.replace(match.group(0), eval_function(match.group(1)))

        for symbol, action in operations.items():
            while match := re.search(operations_reg_exp.format(symbol), exp):
                exp: str = exp.replace(match.group(0), action(*match.groups()))
        return exp

    task = update.message.text
    result = eval_function(task)
    update.message.reply_text(f'{result}')
