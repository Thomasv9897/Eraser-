def self_destruct():
    count = 1
    with open(__file__, 'r') as f:
        lines = f.readlines()