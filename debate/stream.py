import time

def stream_print(title, text, delay=0.01):
    print(f"\n--- {title} ---\n")
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print("\n")
