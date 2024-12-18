import calendar
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

def calculate_sales_forecast():
    try:
        # Получаем значения из полей ввода
        plan = float(plan_entry.get())
        fact_to_date = float(fact_entry.get())
        year = int(year_entry.get())
        month = int(month_entry.get())

        # Определяем количество дней в месяце
        days_in_month = calendar.monthrange(year, month)[1]

        # Текущая дата
        today = datetime.now().day

        # Среднесуточный план продаж
        daily_plan = plan / days_in_month

        # Прогнозируемый объем продаж на конец месяца
        forecasted_sales = (fact_to_date / today) * days_in_month if today > 0 else 0

        # Выполнение плана в % на текущую дату
        completed_percentage = (fact_to_date / plan) * 100 if plan > 0 else 0

        # Прогноз выполнения плана в % на конец месяца
        forecast_percentage = (forecasted_sales / plan) * 100 if plan > 0 else 0

        # Выводим результаты в всплывающем окне
        messagebox.showinfo("Результаты", 
                            f"Выполнено плана на текущую дату: {completed_percentage:.2f}%\n"
                            f"Прогноз выполнения плана на конец месяца: {forecast_percentage:.2f}%")
    except ValueError:
        messagebox.showerror("Ошибка", "Убедитесь, что все поля заполнены правильно.")

# Создание окна
app = tk.Tk()
app.title("Прогноз продаж")

# Настройка окна
tk.Label(app, text="План продаж (всего):").grid(row=0, column=0, padx=10, pady=5)
plan_entry = tk.Entry(app)
plan_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(app, text="Факт продаж на текущую дату:").grid(row=1, column=0, padx=10, pady=5)
fact_entry = tk.Entry(app)
fact_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(app, text="Год:").grid(row=2, column=0, padx=10, pady=5)
year_entry = tk.Entry(app)
year_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(app, text="Месяц (число 1-12):").grid(row=3, column=0, padx=10, pady=5)
month_entry = tk.Entry(app)
month_entry.grid(row=3, column=1, padx=10, pady=5)

# Кнопка расчета
calculate_button = tk.Button(app, text="Рассчитать", command=calculate_sales_forecast)
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

# Запуск приложения
app.mainloop()