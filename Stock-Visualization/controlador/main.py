from modelo.DataRequester import DataRequester
from modelo.TimeRanges import TimeRanges
from vista.vista import *
import json

class Control:

    def __init__(self):
        self.vista = Vista()
        self.dataRequester = DataRequester()
        self.timeRanges = TimeRanges
        self.menu_principal()



    def menu_principal(self):
        while(True):
            print("---- MENU ---- \n"
                + "0. Salir \n"
                + "1. Simbolos disponibles \n"
                + "2. Stock info \n")

            numero_opcion = input("Introduce la opcion: ")

            if (self.comprobar_opcion(numero_opcion)):
                self.iniciar_operaciones(numero_opcion)

    def comprobar_opcion(self, numero_opcion):
        if numero_opcion < 0 or numero_opcion > 2:
            return False
        else:
            return True

    def iniciar_operaciones(self, opcion):
        if opcion == 0:
            print("Saliendo del programa...")
            exit(0)
        elif opcion == 1:
            self.show_symbols()

        elif opcion == 2:
            self.symbol_info()

    def show_symbols(self):
        symbols = self.dataRequester.getSymbols()
        self.vista.mostrar_lista(symbols)

    def symbol_info(self):
        symbol = raw_input("Introduzca el simbolo a consultar: ")

        if self.dataRequester.check_if_exists_symbol(symbol):
            self.vista.show_text("Rangos disponibles: ")
            time_ranges = self.timeRanges.return_time_ranges()

            self.vista.mostrar_lista(time_ranges)
            selected_range = raw_input("Introduce un rango: ")

            if self.timeRanges.check_if_range_exists(selected_range):
                stock_data = self.dataRequester.getSymbolInfo(symbol, selected_range)
                self.vista.show_text((stock_data[0])['volume'])
            else:
                self.vista.show_text("No existe ese rango de tiempo")
        else:
            self.vista.show_text("No existe ese simbolo")

if __name__ == "__main__":
    control = Control()

