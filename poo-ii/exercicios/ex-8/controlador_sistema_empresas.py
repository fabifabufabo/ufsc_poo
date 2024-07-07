from empresa import Empresa


class ControladorSistemaEmpresas:

    def __init__(self):
        self.__empresas = []

    '''
    Permite incluir uma empresa.
    Valida pelo CNPJ se a empresa ja esta cadastrada
    @param empresa objeto Empresa que sera incluido
    Não permite a inclusão de empresas já cadastradas ou
    outros tipos de objetos
    '''

    def inclui_empresa(self, empresa: Empresa):
        if isinstance(empresa, Empresa) and not self.busca_empresa_pelo_cnpj(
                empresa.cnpj):
            self.__empresas.append(empresa)

    '''
    Permite excluir uma empresa cadastrada.
    @param empresa empresa que sera excluida
    '''

    def exclui_empresa(self, empresa: Empresa):
        if empresa in self.__empresas:
            self.__empresas.remove(empresa)

    '''
    Permite buscar uma empresa na lista de empresas pelo CNPJ.
    @param cnpj numero do CNPJ da empresa desejada
    @return retorna a empresa ou None se a empresa nao for encontrada
    '''

    def busca_empresa_pelo_cnpj(self, cnpj: int) -> Empresa:
        for empresa in self.empresas:
            if empresa.cnpj == cnpj:
                return empresa

    '''
    Retorna a lista de empresas cadastradas
    @return lista de empresas cadastradas
    '''

    @property
    def empresas(self) -> list:
        return self.__empresas

    '''
    Calcula o total de impostos de todas as empresas.
    Invoca a operacao total_impostos() de cada uma das empresas,
        somando os resultados
    @return somatorio dos impostos calculados de todas as empresas
    '''

    def calcula_total_impostos(self) -> float:
        somatoria_controlador_total_impostos = 0.0
        for empresa in self.empresas:
            somatoria_controlador_total_impostos += empresa.total_impostos()
        return somatoria_controlador_total_impostos
