def parse_event(line: str) -> dict:
    line = line.strip()
    if not line:
        raise ValueError("Пустая строка")
    
    # Делим не более чем на 3 части
    parts = line.split(" ", 2)
    if len(parts) != 3:
        raise ValueError("Неверный формат строки")
    
    time, level, message = parts
    valid_levels = {"DEBUG", "INFO", "WARNING", "ERROR"}
    
    if level not in valid_levels:
        raise ValueError(f"Неизвестный уровень: {level}")
        
    return {"time": time, "level": level, "message": message.strip()}

def count_levels(lines) -> dict:
    counts = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
            level = event["level"]
        except ValueError:
            level = "BROKEN"
            
        counts[level] = counts.get(level, 0) + 1
    return counts

def top_errors(lines, n: int) -> list[list]:
    errors = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
            if event["level"] == "ERROR":
                msg = event["message"]
                errors[msg] = errors.get(msg, 0) + 1
        except ValueError:
            pass # Пропускаем некорректные строки
            
    # Сортируем: сначала по частоте (убывание), потом по алфавиту (возрастание)
    sorted_errors = sorted(errors.items(), key=lambda item: (-item[1], item[0]))
    # Берем первые n и превращаем в списки
    return [[msg, count] for msg, count in sorted_errors[:n]]

def format_report(counts: dict, errors: list[list]) -> str:
    lines = ["Отчёт по журналу", ""]
    
    # Сортируем уровни по алфавиту
    for level in sorted(counts.keys()):
        lines.append(f"{level}: {counts[level]}")
        
    lines.append("")
    lines.append("Частые ошибки:")
    
    for err in errors:
        lines.append(f"- {err[0]} — {err[1]}")
        
    # В конце текста обязательно должен быть перевод строки
    return "\n".join(lines) + "\n"
