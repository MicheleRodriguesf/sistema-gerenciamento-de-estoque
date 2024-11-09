from enum import Enum
from texttable import Texttable

class CorredorEstoque:
    bloco: int
    sessao: int

    def __init__(self, bloco: int, sessao: int):
        self.bloco = bloco
        self.sessao = sessao

class Produto:
    id: int # Codigo identificador do produto
    nome: str
    categoria: str
    quantidade_em_estoque: int
    preco: float
    localizacao: CorredorEstoque

    def __init__(self,nome,categoria,quantidade_em_estoque,preco,localizacao:CorredorEstoque):
        self.nome = nome
        self.categoria = categoria
        self.quantidade_em_estoque = quantidade_em_estoque
        self.preco = preco
        self.localizacao = localizacao

class TipoMovimentacao(Enum):
    ADICAO = 1
    DELECAO = 2

class Movimentacoes:
    produto: Produto
    acao: TipoMovimentacao

    def __init__(self,produto: Produto, acao: TipoMovimentacao):
        self.produto = produto
        self.acao = acao

class Estoque:
    produtos: list[Produto]
    movimentacoes: list[Movimentacoes]

    def __init__(self, produtos: list[Produto]):
        indexes = 0
        for produto in produtos:
            produto.id = indexes
            indexes+=1
        self.produtos = produtos
        self.movimentacoes = list()

    def listarProdutos(self):
        print('LISTA DE PRODUTOS NO ESTOQUE')
        t = Texttable()
        t.add_row(['ID','Nome', 'Categoria','Quantidade', 'Preco', 'Localizacao'])

        for produto in self.produtos:
            t.add_row([produto.id, produto.nome, produto.categoria, produto.quantidade_em_estoque, produto.preco, f'{produto.localizacao.bloco}, {produto.localizacao.sessao}'])

        print(t.draw())

    def adicionarProdutoAoEstoque(self, produto: Produto):
        if len(self.produtos) > 0:
            produto.id = self.produtos[len(self.produtos) - 1].id + 1
        else:
            produto.id = 0
        self.produtos.append(produto)
        self.movimentacoes.append(Movimentacoes(produto,TipoMovimentacao.ADICAO))
        print(f'Produto {produto.nome} foi adicionado ao estoque')

    def removerProdutoDoEstoque(self, id: int):
        produtoParaDeletar: Produto = None
        idx = 0
        for produto in self.produtos:
            if produto.id == id:
                produtoParaDeletar = produto
                idx =  self.produtos.index(produto)
                break
        if produtoParaDeletar == None:
            print(f'Produto com o identificador:" {id} nao encontrado.')
            return

        print(idx)
        del self.produtos[idx]
        self.movimentacoes.append(Movimentacoes(produto,TipoMovimentacao.DELECAO))
        print(f'Produto {produtoParaDeletar.nome} com o identificador {produtoParaDeletar.id} deletado com sucesso')

    def buscarProdutosPorCorredor(self, corredor: CorredorEstoque):
        t = Texttable()
        t.add_row(['ID','Nome', 'Categoria','Quantidade', 'Preco', 'Localizacao'])

        for produto in self.produtos:
            if produto.localizacao == corredor:
                t.add_row([produto.id, produto.nome, produto.categoria, produto.quantidade_em_estoque, produto.preco, f'{produto.localizacao.bloco}, {produto.localizacao.sessao}'])

        print(t.draw())

        def gerarRelatorioEstoqueBaixo(self):
            print('RELATORIO DE PRODUTOS COM BAIXO ESTOQUE')

            t = Texttable()
            t.add_row(['ID','Nome', 'Categoria','Quantidade', 'Preco', 'Localizacao'])
            for produto in self.produtos:
                if produto.quantidade <= 10:
                    t.add_row([produto.id, produto.nome, produto.categoria, produto.quantidade_em_estoque, produto.preco, f'{produto.localizacao.bloco}, {produto.localizacao.sessao}'])

        print(t.draw())

        def gerarRelatorioEstoqueExcesso(self):
            print('RELATORIO DE PRODUTOS COM EXCESSO DE ESTOQUE')

            t = Texttable()
            t.add_row(['ID','Nome', 'Categoria','Quantidade', 'Preco', 'Localizacao'])
            for produto in self.produtos:
                if produto.quantidade >= 100:
                    t.add_row([produto.id, produto.nome, produto.categoria, produto.quantidade_em_estoque, produto.preco, f'{produto.localizacao.bloco}, {produto.localizacao.sessao}'])

        print(t.draw())


    def gerarRelatorioMovimentacoes(self):
        print('RELATORIO DE MOVIMENTACOES NO ESTOQUE')
        t = Texttable()
        t.add_row(['Produto', 'Acao']) 

        for movimentacao in self.movimentacoes:
            t.add_row([f'{movimentacao.produto.id} - {movimentacao.produto.nome}', movimentacao.TipoMovimentacao])

        print(t.draw())



corredores: list[CorredorEstoque] = list()
corredores.append(CorredorEstoque(1,1))

produtos: list[Produto] = list()
produtos.append(Produto("Notebook", "Informatica", 30, 8.300, corredores[0]))

estoque = Estoque(produtos)

estoque.adicionarProdutoAoEstoque(Produto("Monitor", "Informatica", 4, 1.200,corredores[0]))
estoque.listarProdutos()

estoque.removerProdutoDoEstoque(1)

estoque.listarProdutos()

estoque.buscarProdutosPorCorredor(corredores[0])
