def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError("Неверное количество полей")
    
    city, temp_str, date = parts
    if not city.strip() or not date.strip():
        raise ValueError("Город или дата пустые")
    
    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError(f"Температура не число: {temp_str}")
        
    return {"city": city.strip(), "temperature": temp, "date": date.strip()}

def read_valid(lines: list[str]) -> list[dict]:
    valid_records = []
    for line in lines:
        if not line.strip():
            continue
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            continue
    return valid_records

def average_by_city(records: list[dict]) -> dict:
    totals = {}
    counts = {}
    for r in records:
        city = r["city"]
        totals[city] = totals.get(city, 0.0) + r["temperature"]
        counts[city] = counts.get(city, 0) + 1
        
    return {city: round(totals[city] / counts[city], 1) for city in totals}

def warmest_city(records: list[dict]) -> str:
    averages = average_by_city(records)
    if not averages:
        return ""
    return sorted(averages.keys(), key=lambda c: (-averages[c], c))[0]
