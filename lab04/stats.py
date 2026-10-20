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
        
    return {"city": city.strip(), "temp": temp, "date": date.strip()}