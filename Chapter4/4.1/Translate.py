def translate(sentance):
    """
    Translates a sentence from Spanish to English using generator expressions
    :param sentance: A string containing a sentence in Spanish"""
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    generator_english = (words[word] for word in sentance.split())
    return ' '.join(generator_english)


def main():
    print(translate("el gato esta en la casa"))


if __name__ == "__main__":
    main()