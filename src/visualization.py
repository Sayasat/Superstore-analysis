import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def connect_to_db(db_file):
    """Подключение к базе данных SQLite."""
    return sqlite3.connect(db_file)


def get_sales_by_category(conn):
    """Получение данных по продажам по категориям из базы данных."""
    query = """
    SELECT Category, SUM(Sales) as Total_Sales
    FROM sales
    GROUP BY Category
    """
    return pd.read_sql(query, conn)


def plot_sales_by_category(df):
    """Построение графика продаж по категориям."""
    plt.figure(figsize=(10, 6))  # Увеличиваем размер графика для лучшего восприятия
    sns.barplot(x="Total_Sales", y="Category", data=df, hue="Category", palette="viridis", legend=False)  # Указываем hue для исправления предупреждения
    plt.title("Продажи по категориям", fontsize=16)
    plt.xlabel("Сумма продаж", fontsize=12)
    plt.ylabel("Категория", fontsize=12)
    plt.tight_layout()  # Подгонка графика, чтобы элементы не перекрывались
    plt.show()


def main():
    """Основная логика программы."""
    db_file = "../db/superstore.db"  # Путь к базе данных
    conn = connect_to_db(db_file)  # Подключение к базе данных

    # Получение данных по продажам по категориям
    df = get_sales_by_category(conn)

    # Построение графика
    plot_sales_by_category(df)

    # Закрытие соединения с базой данных
    conn.close()


# Запуск основного процесса
if __name__ == "__main__":
    main()
