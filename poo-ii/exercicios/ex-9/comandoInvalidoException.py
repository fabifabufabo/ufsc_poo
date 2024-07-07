class ComandoInvalidoException(Exception):
    def __init__(self):
        super().__init__("comando inválido!")
