with open('C:/Users/User/Downloads/Telegram Desktop/results.txt') as f:
    lines = f.readlines()
results = {}
for line in lines:
    name, score = line.strip().split(' - ')
    results[name] = int(score)
sorted_results = dict(sorted(results.items(), key=lambda item: item[1], reverse=True))

print("Топ-3 студентов:")
for name, score in list(sorted_results.items())[:3]:
    print(f"{name}: {score}")

with open('sorted_results.txt', 'w') as f:
    for name, score in sorted_results.items():
        f.write(f"{name}: {score}\n")

