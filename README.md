# Tokenization and Statistical Analysis Using DFA

A Python implementation of a Deterministic Finite Automaton (DFA) for tokenizing Persian text and performing basic statistical analysis of recognized tokens.

## Overview

This project demonstrates how a Deterministic Finite Automaton (DFA) can be used to recognize and classify different types of tokens in Persian text.

The tokenizer uses a state-transition mechanism to identify Persian words, Persian and English numbers, and punctuation marks. After tokenization, the program calculates the frequency of each recognized token type.

The project provides a practical introduction to finite automata, lexical analysis, and text processing.

## Features

* **DFA Implementation:** Implements a deterministic finite automaton using states and transition rules.
* **Persian Word Recognition:** Recognizes sequences of Persian letters.
* **Half-Space Support:** Includes transition rules for the Persian half-space character (`‌`) within words.
* **Number Recognition:** Identifies sequences of Persian and English digits.
* **Punctuation Recognition:** Recognizes supported punctuation marks, including periods, commas, question marks, and parentheses.
* **Token Classification:** Assigns a token type to each recognized token.
* **Statistical Analysis:** Counts the number of recognized tokens in each category.

## Technologies

* Python
* `re` — imported in the current implementation.
* `collections.defaultdict` — used to count token types.

## How It Works

The tokenizer processes the input text character by character.

1. **Define States:** Initialize the DFA with a start state, transition rules, and final states.
2. **Process Characters:** Read each character and check whether a valid transition exists.
3. **Recognize Tokens:** When a transition cannot be followed, check whether the current state is a final state and record the recognized token.
4. **Classify Tokens:** Assign a category to each recognized token, such as `WORD`, `NUMBER`, or `PUNCTUATION`.
5. **Calculate Statistics:** Count the recognized tokens in each category.
6. **Display Results:** Print the extracted tokens and their category counts.

## Token Types

| Token Type    | Description                            | Examples      |
| ------------- | -------------------------------------- | ------------- |
| `WORD`        | Sequences of supported Persian letters | `تهران`       |
| `NUMBER`      | Sequences of Persian or English digits | `۲۱`, `123`   |
| `PUNCTUATION` | Supported punctuation characters       | `.`, `،`, `؟` |

The recognized character set is determined by the transition rules defined in the source code.

## Example Input

```text
تهران ۲۱.۳ میلیون نفر جمعیت دارد و یکی از پرجمعیت‌ترین شهرهای جهان محسوب می‌شود.
```

## Installation and Usage

### Prerequisites

* Python 3.8 or later

No third-party package installation is required by the current implementation.

### Run the Program

Save the Python script and execute it using:

```bash
python "Tokenization and Statistical Analysis Using DFA.py"
```

The program prints the recognized tokens and the number of tokens in each category.

## Project Structure

```text
tokenization-and-statistical-analysis-dfa/
├── Tokenization and Statistical Analysis Using DFA.py
└── README.md
```

## Learning Objectives

* Understand the basic concepts of deterministic finite automata.
* Implement state transitions in Python.
* Apply finite automata to basic lexical analysis.
* Recognize and classify selected Persian text elements.
* Perform simple statistical analysis on tokenized text.

## Limitations

* The tokenizer recognizes only characters explicitly defined in its transition table.
* Whitespace and unsupported characters are not returned as tokens.
* The current implementation focuses on basic token recognition rather than comprehensive Persian language processing.
* Token recognition depends on the configured states and transition rules.
* More advanced tokenization features, such as handling all punctuation variants and normalizing Persian and Arabic character forms, are not implemented.

## Future Improvements

* Expand support for Persian and Arabic character variants.
* Improve handling of punctuation and token boundaries.
* Add support for additional token categories.
* Separate the tokenizer logic from the example corpus and statistical analysis.
* Add unit tests covering different input cases.

## License

This project is distributed under the terms specified in the LICENSE file.
