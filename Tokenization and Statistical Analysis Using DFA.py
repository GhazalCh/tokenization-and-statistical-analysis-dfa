import re
from collections import defaultdict

# تعریف DFA به‌عنوان یک کلاس
class DFA:
    def __init__(self, transitions, start_state, final_states):
        self.transitions = transitions
        self.start_state = start_state
        self.final_states = final_states

    def tokenize(self, text):
        tokens = []
        state = self.start_state
        token = ""

        for char in text:
            # بررسی انتقال‌های موجود
            if (state, char) in self.transitions:
                state = self.transitions[(state, char)]
                token += char
            else:
                # اگر به حالت نهایی برسیم
                if state in self.final_states:
                    tokens.append((token, self.final_states[state]))
                state = self.start_state
                token = ""
                if (state, char) in self.transitions:
                    state = self.transitions[(state, char)]
                    token += char

        # بررسی توکن باقی‌مانده
        if state in self.final_states:
            tokens.append((token, self.final_states[state]))
        return tokens


# تعریف DFA برای متن فارسی
# مثال: DFA برای شناسایی کلمات فارسی، اعداد و علائم
transitions = {}

# حروف فارسی
for char in "اآبپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی":
    transitions[(0, char)] = 1
    transitions[(1, char)] = 1
    transitions[(1, '‌')] = 1  # پشتیبانی از نیم‌فاصله

# اعداد فارسی
for char in "۰۱۲۳۴۵۶۷۸۹":
    transitions[(0, char)] = 2
    transitions[(2, char)] = 2

# اعداد انگلیسی
for char in "0123456789":
    transitions[(0, char)] = 2
    transitions[(2, char)] = 2

# علائم نگارشی
for char in ".,!?؟؛:()«»":
    transitions[(0, char)] = 3

start_state = 0
final_states = {1: 'WORD', 2: 'NUMBER', 3: 'PUNCTUATION'}

dfa = DFA(transitions, start_state, final_states)

# بخش نمونه‌ای از کورپوس همشهری
corpus = """
تهران ۲۱.۳ میلیون نفر جمعیت دارد و یکی از پرجمعیت‌ترین شهرهای جهان محسوب می‌شود.
"""

# Tokenize
tokens = dfa.tokenize(corpus)

# آمارگیری
statistics = defaultdict(int)
for token, token_type in tokens:
    statistics[token_type] += 1

# چاپ نتایج
print("Tokens:", tokens)
print("Statistics:")
for token_type, count in statistics.items():
    print(f"{token_type}: {count}")
