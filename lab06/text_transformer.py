import argparse

def transform_upper(text):
    return text.upper()

def transform_lower(text):
    return text.lower()

def get_word_count(text):
    return len(text.split())

def filter_short(text, min_length):
    if len(text) > min_length:
        return text
    return None 

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--action", required=True, choices=["upper", "lower", "count", "filter"])
    parser.add_argument("--data", required=True)
    parser.add_argument("--min_length", type=int, default=0)
    args = parser.parse_args() 
    texts = args.data.split(",")

    for text in texts: 
        if args.action == "upper":
            print(transform_upper(text))
        elif args.action == "lower":
            print(transform_lower(text))
        elif args.action == "count":
            print(get_word_count(text))
        elif args.action == "filter":
            result = filter_short(text, args.min_length)
            if result is not None:
                print(result)