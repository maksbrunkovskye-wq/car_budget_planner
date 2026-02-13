def read_float(prompt: str) -> float:
    while True:
        value = input(prompt).replace(",", ".").strip()
        try:
            return float(value)
        except ValueError:
            print("Bitte eine Zahl eingeben (z.B. 2000 oder 2000,50).")


def berechne_restbetrag(gehalt: float, miete: float, essen: float, sonstiges: float) -> float:
    return gehalt - (miete + essen + sonstiges)


def zeige_ergebnis(restbetrag: float) -> None:
    print("\n============================")
    print(f"Verfügbarer Restbetrag: {restbetrag:.2f} €")

    if restbetrag < 0:
        print("Achtung: Ausgaben sind höher als das Gehalt!")
    elif restbetrag < 100:
        print("Sehr knapp. Budget ist riskant.")
    else:
        print("Budget sieht stabil aus.")
    print("============================\n")


def budget_rechner() -> None:
    print("\n--- Budget-Rechner ---")
    gehalt = read_float("Monatsgehalt (€): ")
    miete = read_float("Miete/Wohnkosten (€): ")
    essen = read_float("Essen (€): ")
    sonstiges = read_float("Sonstiges (€): ")

    restbetrag = berechne_restbetrag(gehalt, miete, essen, sonstiges)
    zeige_ergebnis(restbetrag)

def main() -> None:
    while True:
        print("=== Car Budget Planner ===")
        print("1) Budget berechnen")
        print("0) Beenden")

        choice = input("Auswahl: ").strip()

        if choice == "1":
            budget_rechner()
        elif choice == "0":
            print("Tschüss!")
            break
        else:
            print("Ungültige Auswahl. Bitte 1 oder 0.\n")


if __name__ == "__main__":
    main()
