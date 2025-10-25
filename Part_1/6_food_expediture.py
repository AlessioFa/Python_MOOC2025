"""
Scrivi un programma che stimi la spesa alimentare tipica di un utente.

Il programma chiede all'utente quante volte a settimana mangia alla mensa universitaria. Poi chiede il prezzo di un pranzo tipico alla mensa e quanti soldi spende per la spesa durante la settimana.

Sulla base di queste informazioni, il programma calcola la spesa alimentare tipica dell’utente sia settimanale che giornaliera.

Il programma dovrebbe funzionare come segue:
Esempio di output

Quante volte a settimana mangi alla mensa universitaria? 4
Qual è il prezzo di un pranzo tipico alla mensa? 2.5
Quanto spendi per la spesa in una settimana? 28.5

Spesa alimentare media:
Giornaliera: 5.5 euro
Settimanale: 38.5 euro
"""

student_cafeteria_weekly: int = int(input("How many times do you eat at the cafeteria? "))

price_typical_lunch: float = float(input("The price of a typical student lunch? "))

grocery_weekly: float = float(input("How much money do you spend on groceries in a week? "))

weekly_total: float = (price_typical_lunch * student_cafeteria_weekly) + grocery_weekly
daily_average: float = weekly_total / 7

print("\nAverage food expenditure:")
print(f"Daily: {daily_average:.2f} euros")
print(f"Weekly: {weekly_total:.1f} euros")


# 