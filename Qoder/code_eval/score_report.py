import csv

def load_scores(path):
    records = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                score = int(row["score"])
                records.append({
                    "name": row["name"],
                    "score": score
                })
            except (ValueError, TypeError):
                continue
    return records

def average_score(records):
    total = sum(r["score"] for r in records)
    return total / len(records)

def passed_students(records):
    return [r for r in records if r["score"] >= 60]

def top_student(records):
    records = sorted(records, key=lambda x: x["score"], reverse=True)
    return records[0]

def main():
    records = load_scores("scores.csv")
    print("total:", len(records))
    print("average:", average_score(records))
    print("passed:", len(passed_students(records)))
    top = top_student(records)
    print("top:", top["name"], top["score"])

if __name__ == "__main__":
    main()
