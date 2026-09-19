# token_estimator.py
# A tiny beginner-friendly script that estimates how many "tokens" a piece
# of text will use, and roughly what that would cost against a couple of
# made-up example prices. This is a rough estimate, not an exact count —
# real tokenizers are more complicated than "characters divided by 4".


# ---------------------------------------------------------------------
# Section 1: The function that estimates tokens
# ---------------------------------------------------------------------
# A "function" is a reusable block of code that takes an input, does
# something with it, and gives back an output. Here, the input is some
# text, and the output is our estimated token count.
def estimate_tokens(text):
    # len(text) counts the number of characters in the text (including
    # spaces and punctuation).
    character_count = len(text)

    # A common rough rule of thumb is: 1 token is about 4 characters.
    # So we divide the character count by 4 to estimate tokens.
    # We use "-(-a // b)" as a simple trick to divide and round UP
    # (this is called "ceiling division") without needing extra imports.
    estimated = -(-character_count // 4)

    # "return" sends this value back to whoever called the function.
    return estimated


# ---------------------------------------------------------------------
# Section 2: Example prices for two made-up models
# ---------------------------------------------------------------------
# A "dictionary" stores information as key-value pairs, like a mini
# lookup table: {key: value, key: value}.
#
# IMPORTANT: These are ILLUSTRATIVE EXAMPLE RATES ONLY, made up for this
# practice script. They are NOT real, live prices for any actual model.
price_per_1000_tokens = {
    "ExampleModel-Small": 0.002,   # made-up: $0.002 per 1,000 tokens
    "ExampleModel-Large": 0.02,    # made-up: $0.02 per 1,000 tokens
}


# ---------------------------------------------------------------------
# Section 3: A sample paragraph of text to test our function on
# ---------------------------------------------------------------------
# A "variable" is just a named box that holds a value — here it holds
# a string (a piece of text) that we'll estimate the cost for.
sample_paragraph = (
    "Learning to code is a lot like learning a new language. "
    "At first the vocabulary feels strange and the grammar rules "
    "seem arbitrary, but with enough small daily practice, the "
    "patterns start to click. Every expert was once a beginner "
    "who kept showing up and trying one more example."
)


# ---------------------------------------------------------------------
# Section 4: Estimate tokens for the sample paragraph
# ---------------------------------------------------------------------
# We call our function from Section 1 and store its result in a variable.
token_count = estimate_tokens(sample_paragraph)

print("Sample paragraph:")
print(sample_paragraph)
print()
print(f"Estimated token count: {token_count}")
print()


# ---------------------------------------------------------------------
# Section 5: Print the estimated cost for each example model
# ---------------------------------------------------------------------
# A "for loop" lets us repeat an action once for each item in something.
# Here, we loop over each (model_name, price) pair in our dictionary.
print("Estimated cost by example model (illustrative rates, not real prices):")
for model_name, price in price_per_1000_tokens.items():
    # Cost = (tokens / 1000) * price per 1000 tokens.
    estimated_cost = (token_count / 1000) * price

    # f-strings (the f before the quotes) let us drop variables directly
    # into a string using curly braces {}.
    print(f"  {model_name}: ${estimated_cost:.6f}")
