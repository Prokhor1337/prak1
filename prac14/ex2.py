import json
import os

FILENAME = "player_stats.json"

def load_stats():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"games_played": 0, "wins": 0, "losses": 0}

def save_stats(stats):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=4)

def update_stats(win):
    stats = load_stats()
    stats["games_played"] += 1
    if win:
        stats["wins"] += 1
    else:
        stats["losses"] += 1
    save_stats(stats)
    print("Оновлена статистика:", stats)

if __name__ == "__main__":
    result = input("Чи виграв гравець? (так/ні): ").lower()
    update_stats(result == "так")
