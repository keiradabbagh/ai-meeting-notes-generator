print("main.py running")

from analyzer import analyze_transcript

def main():
    print("Reading transcript...")
    with open("sample_transcript.txt", "r") as f:
        transcript = f.read()

    summary, action_items, decisions = analyze_transcript(transcript)

    print("\nSUMMARY")
    print(summary)

    print("\nACTION ITEMS")
    for item in action_items:
        print("-", item)

    print("\nDECISIONS")
    for decision in decisions:
        print("-", decision)

main()


