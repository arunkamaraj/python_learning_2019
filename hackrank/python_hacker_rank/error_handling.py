try:
    print(1 / 0)
except Exception as e:
    print("Error Code:", e.args[0])

