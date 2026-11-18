def count_by_extension(paths: list[str]) -> dict[str, int]:
    # Создаем пустой словарь для подсчета
    counts = {}
    
    for path in paths:
        # Берем имя файла (отсекаем всё, что до последнего слэша)
        filename = path.split("/")[-1]
        
        # Ищем последнюю точку в имени файла
        if "." in filename:
            # Если точка есть, берем всё, что после нее, и переводим в нижний регистр
            ext = filename.split(".")[-1].lower()
        else:
            # Если точки нет (например, "Makefile"), расширение пустое
            ext = ""
            
        # Увеличиваем счетчик для этого расширения
        counts[ext] = counts.get(ext, 0) + 1
        
    return counts


def deepest_path(paths: list[str]) -> str:
    # Если список пустой, возвращаем пустую строку
    if not paths:
        return ""
        
    best_path = paths[0]
    # Считаем вложенность первого пути (количество слэшей)
    max_depth = best_path.count("/")
    
    for path in paths[1:]:
        depth = path.count("/")
        
        # Если нашли путь глубже
        if depth > max_depth:
            max_depth = depth
            best_path = path
        # Если глубина такая же, но путь по алфавиту идет раньше (меньше)
        elif depth == max_depth and path < best_path:
            best_path = path
            
    return best_path


def human_size(n_bytes: int) -> str:
    # Если размер меньше 1024 байт, выводим просто байты
    if n_bytes < 1024:
        return f"{n_bytes} Б"
        
    # Список единиц измерения (начиная с КБ, так как Б мы уже проверили)
    units = ["КБ", "МБ", "ГБ", "ТБ"]
    
    # Переводим байты в float, чтобы делить с остатком
    size = float(n_bytes)
    
    # Делим на 1024, пока размер не станет меньше 1024
    for unit in units:
        size /= 1024.0
        if size < 1024.0:
            # Как только размер меньше 1024, форматируем с одним знаком после запятой
            return f"{size:.1f} {unit}"
            
    # На случай очень больших чисел (если пройдем весь цикл)
    return f"{size:.1f} ТБ"