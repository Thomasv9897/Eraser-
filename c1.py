def get_run_count():
    print("hai")
    try:
        with open('run_count.txt', 'r') as f:
            count = int(f.read().strip())
    except FileNotFoundError:
        count = 0
    return count