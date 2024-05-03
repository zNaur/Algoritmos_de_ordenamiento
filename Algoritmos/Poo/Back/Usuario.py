class Usuario:
    @staticmethod
    def get_method(chosen_method):
        if chosen_method < 1 or chosen_method > 9:
            print("Número de método de ordenamiento inválido. Debe estar entre 1 y 9.")
            return None
        return chosen_method
