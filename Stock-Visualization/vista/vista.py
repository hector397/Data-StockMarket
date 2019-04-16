class Vista:
    MENU_INICIO = "---- MENU ---- \n" \
                  "0. Salir \n" \
                  "1. Simbolos disponibles \n" \
                  "2. Stock info \n"
    INTRODUZCA_SIMBOLO = "Introduzca simbolo a consultar: "
    INTRODUCE_OPCION = "Introduzca una opcion: "
    SALIR_DEL_PROGRAMA = "Saliendo del programa..."
    INTRODUCE_RANGO = "Introduce un rango: "
    RANGOS_DISPONIBLES = "Rangos disponibles: "
    RANGO_INCORRECTO = "No existe ese rango"
    SIMBOLO_INCORRECTO = "No existe ese simbolo"

    def __init__(self):
        pass

    def mostrar_menu_inicio(self):
        print(self.MENU_INICIO)

    def mostrar_lista(self, lista):
        for elemento in lista:
            print(elemento)

        print("\n")

    def show_text(self, text):
        print(text)

    def show_symbol_info(self, range, stock_data):
        if range == "1d":
            self.show_stock_average_by_minute(stock_data)
        else:
            self.show_stock_data_by_date(stock_data)



    def show_stock_data_by_date(self, stock_data):
        print("             High  ----  Low")
        for data in stock_data:
            print(str(data['date']) + ":  " + str(data['high']) + " ---- " + str(data['low']))

        print("\n")

    def show_stock_average_by_minute(self, stock_data):
        print("        High ---- Low")
        for data in stock_data:
            print(str(data['minute']) + ":  " + str(data['high']) + " ---- " + str(data['low']))

        print("\n")