import sys
from logstats import count_levels, top_errors, format_report

def main():
    # Читаем имя файла из первой строки ввода
    filename = sys.stdin.readline().strip()
    if not filename:
        return

    # Первый проход по файлу: сбор статистики
    with open(filename, encoding="utf-8") as log:
        counts = count_levels(log)

    # Второй проход по файлу: поиск ошибок
    with open(filename, encoding="utf-8") as log:
        errors = top_errors(log, 3) # n=3 судя по примеру

    total_lines = sum(counts.values())
    error_count = counts.get("ERROR", 0)
    broken_count = counts.get("BROKEN", 0)

    # Печатаем три числа
    print(total_lines)
    print(error_count)
    print(broken_count)

    # Формируем и записываем отчет
    report_text = format_report(counts, errors)
    with open("report.txt", "w", encoding="utf-8") as report_file:
        report_file.write(report_text)

if __name__ == "__main__":
    main()
