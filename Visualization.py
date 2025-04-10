import pandas as pd
import matplotlib.pyplot as plt


def line_chart(file, ax):
    year = 2023
    data = pd.read_csv(file)
    books_read = data.query(f"Год == {year}")
    ax.plot(
        books_read["Месяц"],
        books_read["Книги"],
        marker="o",
        color="g",
        label="Прочитано книг",
    )
    ax.set_title(f"Прочитанные книги {year} год")
    ax.set_xlabel("Месяцы")
    ax.set_ylabel("Количество книг")
    ax.grid(True)
    ax.legend()
    ax.set_facecolor("0.2")


def bar_chart(file, ax):
    year = 2024
    data = pd.read_csv(file)
    pages_read = data.query(f"Год == {year}")
    ax.bar(
        pages_read["Месяц"],
        pages_read["Страницы"],
        color="purple",
        label="Прочитано страниц",
    )
    ax.set_title(f"Прочитанные страницы {year} год")
    ax.set_xlabel("Месяцы")
    ax.set_ylabel("Количество страниц")
    ax.grid(True)
    ax.legend()
    ax.set_facecolor("0.2")


def both():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    line_chart("books.csv", ax1)
    bar_chart("books.csv", ax2)
    plt.tight_layout()
    plt.show()


both()
