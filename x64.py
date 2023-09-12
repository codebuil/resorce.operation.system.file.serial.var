class SimuladorX64:
    def __init__(self):
        self.registradores = {
            'rax': 0,
            'rbx': 0,
            'rcx': 0,
            'rdx': 0,
            'rbp': 0,
            'rsi': 0,
            'rdi': 0
        }

    def run(self, codigo):
        linhas = codigo.split('\n')
	
        for linha in linhas:
            print(linha)
            if not linha:
                continue  # Ignora linhas em branco

            partes = linha.split(',')
            operacao = partes[0].strip()
            if len(partes) >= 2:
                 arg1 = partes[1].strip()
                 arg2 = partes[2].strip()

                 if operacao == 'add':
                      self.registradores[arg1] += self._get_valor(arg2)
                 elif operacao == 'sub':
                      self.registradores[arg1] -= self._get_valor(arg2)
                 elif operacao == 'mul':
                      self.registradores[arg1] *= self._get_valor(arg2)
                 elif operacao == 'div':
                      self.registradores[arg1] //= self._get_valor(arg2)
                 elif operacao == 'mov':
                      self.registradores[arg1] = self._get_valor(arg2)
                 elif operacao == 'and':
                      self.registradores[arg1] &= self._get_valor(arg2)
                 elif operacao == 'or':
                      self.registradores[arg1] |= self._get_valor(arg2)

            self._mostrar_estado()
           
              
    def _get_valor(self, valor):
        if valor.isdigit():
            return int(valor)
        else:
            return self.registradores[valor]

    def _mostrar_estado(self):
        print("Estado dos registradores:")
        for registro, valor in self.registradores.items():
            print(f'{registro}: {valor}')

def main():
    print("\x1bc\x1b[44;37m")
    codigo = """
        mov, rax, 10
        mov, rbx, 20
        add, rax, rbx
        sub, rax, 5
        mul, rax, 3
        div, rax, 4

    """

    simulador = SimuladorX64()
    simulador.run(codigo)

main()
