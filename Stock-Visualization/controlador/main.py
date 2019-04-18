from modelo.DataRequester import DataRequester
from modelo.TimeRanges import TimeRanges
from vista.vista import *

class Control:
    OPCION_MINIMA = 0
    OPCION_MAXIMA = 2

    def __init__(self):
        self.vista = Vista()
        self.dataRequester = DataRequester()
        self.timeRanges = TimeRanges
        self.menu_principal()

    def menu_principal(self):
        while(True):
            self.vista.mostrar_menu_inicio()
            numero_opcion = input(self.vista.INTRODUCE_OPCION)

            if self.comprobar_opcion(numero_opcion):
                self.iniciar_operaciones(numero_opcion)

    def comprobar_opcion(self, numero_opcion):
        if numero_opcion < self.OPCION_MINIMA or numero_opcion > self.OPCION_MAXIMA:
            return False
        else:
            return True

    def iniciar_operaciones(self, opcion):
        if opcion == 0:
            self.vista.show_text(self.vista.SALIR_DEL_PROGRAMA)
            exit(0)
        elif opcion == 1:
            self.show_symbols()

        elif opcion == 2:
            self.symbol_info()

    def show_symbols(self):
        symbols = self.dataRequester.getSymbols()
        self.vista.mostrar_lista(symbols)

    def symbol_info(self):
        symbol = raw_input(self.vista.INTRODUZCA_SIMBOLO)

        if self.dataRequester.check_if_exists_symbol(symbol):
            time_ranges = self.timeRanges.return_time_ranges()

            self.vista.show_text(self.vista.RANGOS_DISPONIBLES)
            self.vista.mostrar_lista(time_ranges)
            selected_range = raw_input(self.vista.INTRODUCE_RANGO)

            if self.timeRanges.check_if_range_exists(selected_range):
                stock_data = self.dataRequester.getSymbolInfo(symbol, selected_range)
                self.vista.show_symbol_info(selected_range, stock_data)
            else:
                self.vista.show_text(self.vista.RANGO_INCORRECTO)
        else:
            self.vista.show_text(self.vista.SIMBOLO_INCORRECTO)

if __name__ == "__main__":
    control = Control()

