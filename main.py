from application import calculate_salary, get_employees
from datetime import datetime


def main():
    calculate_salary()
    get_employees()
    print(f"Сегодня {datetime.now().date()}")


if __name__ == "__main__":
    main()

## Задание 4.
from time import sleep
from progress.bar import IncrementalBar

bar = IncrementalBar('Random', max=8)

for item in range(8):
    bar.next()
    sleep(0.5)

bar.finish()
