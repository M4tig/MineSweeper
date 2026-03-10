def cria_gerador(b, s):
    '''
    Função que recebe um inteiro correspondente ao número de bits do gerador e um inteiro positivo 
    correspondente à seed ou estado inicial e devolve o gerador

    int x int -> gerador
    '''
    if not isinstance(b, int) or not isinstance(s, int) or (b != 32 and b != 64) or s <= 0 or s > 2**b:
        raise ValueError('cria_gerador: argumentos invalidos')
    return [b, s]

def cria_copia_gerador(gerador):
    '''
    Função que recebe um gerador e que devolve uma cópia do gerador

    gerador -> gerador
    '''
    return gerador.copy()

def obtem_estado(gerador):
    '''
    Função que recebe um gerador e devolve o estado do gerador sem o alterar

    gerador -> int 
    '''
    return gerador[1]

def define_estado(gerador, news):
    '''
    Função que recebe um gerador e um inteiro e define o estado do gerador como o inteiro recebido e devolve esse inteiro

    gerador x int -> int
    '''
    gerador[1] = news
    return gerador[1]

def atualiza_estado(gerador):
    '''
    Função que recebe um gerador e atualiza o seu estado de acordo com o algoritmo xorshift de geração de números pseudoaleatórios e devolve o estado atualizado do gerador

    gerador -> int
    '''
    seed = obtem_estado(gerador)
    if gerador[0] == 32:
        seed ^= ( seed << 13 ) & 0xFFFFFFFF
        seed ^= ( seed >> 17 ) & 0xFFFFFFFF
        seed ^= ( seed << 5 ) & 0xFFFFFFFF
     
    if gerador[0] == 64:
        seed ^= ( seed << 13 ) & 0xFFFFFFFFFFFFFFFF
        seed ^= ( seed >> 7 ) & 0xFFFFFFFFFFFFFFFF
        seed ^= ( seed << 17 ) & 0xFFFFFFFFFFFFFFFF
    
    define_estado(gerador, seed)
    return seed

def eh_gerador(arg):
    '''
    Função que recebe um argumento e devolve True caso este seja um TAD gerador e False caso contrário

    universal -> booleano
    '''
    return isinstance(arg, list) and len(arg) == 2 and isinstance(arg[0], int) and isinstance(arg[1], int) and (arg[0] == 32 or arg[0] == 64)  \
         and arg[1] > 0 and arg[1] <= 2**arg[0]

def geradores_iguais(g1, g2):
    '''
    Função que recebe dois geradores e devolve True apenas se os geradores forem iguais, em caso contrário devolve False

    gerador x gerador -> booleano
    '''
    return g1[0]==g2[0] and g1[1]==g2[1]

def gerador_para_str(gerador):
    '''
    Função que recebe um gerador e devolve uma cadeia de caracteres que traduz a representação do gerador em caracteres

    gerador -> str
    '''
    bits = gerador[0]
    seed = obtem_estado(gerador)
    return f'xorshift{bits}(s={seed})'

def gera_numero_aleatorio(gerador,n):
    '''
    Função que recebe um gerador e um inteiro e devolve um número aleatório entre 1 e o inteiro recebido obtido a partir do
    novo estado s do gerador recebido como 1 + mod(s, n) onde mod corresponde à operação resto da divisão inteira

    gerador x int -> int
    '''
    return 1 + atualiza_estado(gerador) % n

def gera_carater_aleatorio(gerador, c):
    '''
    Função que recebe um gerador e um caractér maiúsculo, atualiza o estado do gerador recebido e devolve um caráter aleatório
    no intervalo entre 'A' e o caráter maiúsculo recebido sendo este obtido através do novo estado s do gerador recebido como
    o caráter na posição mod(s, l) da cadeia de caracteres de tamanho l formada por todos os caracteres entre 'A' e o caráter
    recebido 

    gerador x str -> str
    '''
    return chr(atualiza_estado(gerador) % ((ord(c)) - ord('A')+ 1) + ord('A'))

def cria_coordenada(col, lin):
    '''
    Função que recebe uma cadeia de caracteres e um inteiro e devolve a coordenada correspondente

    str x int -> coordenada
    '''
    if not isinstance(col, str) or len(col) != 1 or ord(col) < ord('A') or ord(col) > 90 or not isinstance(lin, int) or  lin < 1 or lin > 99:
        raise ValueError ('cria_coordenada: argumentos invalidos')
    return (col, lin)

def obtem_coluna(coord):
    '''
    Função que recebe uma coordenada e devolve a coluna da mesma

    coordenada -> str
    '''
    return coord[0]

def obtem_linha(coord):
    '''
    Função que recebe uma coordenada e devolve a linha da mesma

    coordenada -> int
    '''
    return coord[1]

def eh_coordenada(arg):
    '''
    Função que recebe um argumento e devolve True caso o argumento seja um TAD coordenada e caso contrário devolve False

    universal -> booleano
    '''
    return  isinstance(arg, tuple) and isinstance(obtem_coluna(arg), str) and len(obtem_coluna(arg)) == 1 and ord('A') <= ord(obtem_coluna(arg)) <= 90 \
        and isinstance(obtem_linha(arg), int) and 1 <= obtem_linha(arg) <= 99 

def coordenadas_iguais(c1, c2):
    '''
    Função que recebe duas coordenadas e devolve True apenas se as coordenadas forem iguais, em caso contrário devolve False

    coordenada x coordenada -> booleano
    '''
    return obtem_coluna(c1) == obtem_coluna(c2) and obtem_linha(c1) == obtem_linha(c2)

def coordenada_para_str(coordenada):
    '''
    Função que recebe uma coordenada e devolve uma cadeia de caracteres que traduz a representação da coordenada em caracteres

    coordenada -> str
    '''
    return obtem_coluna(coordenada)+str(obtem_linha(coordenada)).zfill(2)

def str_para_coordenada(strcoord):
    '''
    Função que recebe uma cadeia de caracteres e devolve coordenada que traduz a representação da cadeia de caracteres em coordenada

    str -> coordenada
    '''
    return (strcoord[0],int(strcoord[1:]))

def obtem_coordenadas_vizinhas(coordenada):
    '''
    Função que recebe uma coordenada e devolve um tuplo com as coordenadas vizinhas à coordenada recebida começando pela na diagonal acima
    à esquerda e seguindo pelo sentido horário

    coordenada -> tuplo
    '''
    colunas_coord_viz = [chr(ord(obtem_coluna(coordenada))-1),obtem_coluna(coordenada),chr(ord(obtem_coluna(coordenada))+1), chr(ord(obtem_coluna(coordenada))+1),
    chr(ord(obtem_coluna(coordenada))+1),chr(ord(obtem_coluna(coordenada))),chr(ord(obtem_coluna(coordenada))-1),chr(ord(obtem_coluna(coordenada))-1)]
    linhas_coord_viz = [obtem_linha(coordenada)-1, obtem_linha(coordenada)-1, obtem_linha(coordenada)-1, obtem_linha(coordenada), obtem_linha(coordenada)+1, 
    obtem_linha(coordenada)+1, obtem_linha(coordenada)+1, obtem_linha(coordenada)]
    coord_viz = ()
    for caso in range(len(colunas_coord_viz)):
        try:
            coord_viz += (cria_coordenada(colunas_coord_viz[caso], linhas_coord_viz[caso]),)
        except ValueError:
            pass
    return coord_viz

def obtem_coordenada_aleatoria(c, g):
    '''
    Função que recebe coordenada e um TAD gerador e devolve uma coordenada gerada aleatoriamente onde a coordenada recebida 
    define a maior coluna e maior linha possíveis

    coordenada x gerador -> coordenada
    '''
    return cria_coordenada(gera_carater_aleatorio(g, obtem_coluna(c)), gera_numero_aleatorio(g, obtem_linha(c)))

def cria_parcela():
    '''
    Função que devolve uma parcela tapada sem mina escondida

    {} -> parcela
    '''
    return {'Estado' : 'Tapada', 'Mina' : 'N'}

def cria_copia_parcela(p):
    '''
    Função que recebe uma parcela e que devolve uma cópia da parcela

    parcela -> parcela
    '''
    p_copia = {}
    for key, value in p.items():
        p_copia[key] = value
    return p_copia

def limpa_parcela(p):
    '''
    Função que recebe uma parcela e modifica-a destrutivamente alterando o seu estado para limpa e devolve a parcela alterada

    parcela -> parcela
    '''
    p['Estado'] = 'Limpa'
    return p

def marca_parcela(p):
    '''
    Função que recebe uma parcela e modifica-a destrutivamente alterando o seu estado para marcada e devolve a parcela alterada

    parcela -> parcela
    '''
    p['Estado'] = 'Marcada'
    return p

def desmarca_parcela(p):
    '''
    Função que recebe uma parcela e modifica-a destrutivamente alterando o seu estado para tapada e devolve a parcela alterada

    parcela -> parcela
    '''
    p['Estado'] = 'Tapada'
    return p

def esconde_mina(p):
    '''
    Função que recebe uma parcela e modifica-a destrutivamente escondendo uma mina na parcela e devolve a parcela alterada

    parcela -> parcela
    '''
    p['Mina'] = 'S'
    return p

def eh_parcela(arg):
    '''
    Função que recebe um argumento e devolve True caso o argumento seja um TAD parcela e caso contrário devolve False

    universal -> booleano
    '''
    return isinstance(arg, dict) and len(arg) == 2 \
        and 'Estado' in arg.keys() and 'Mina' in arg.keys() \
        and arg['Estado'] in ['Limpa', 'Tapada', 'Marcada'] \
        and arg['Mina'] in ['S', 'N']  
        
def eh_parcela_tapada(arg):
    '''
    Função que recebe um argumento e devolve True caso a parcela recebida se encontre tapada e caso contrário devolve False

    parcela -> booleano
    '''
    return arg['Estado'] == 'Tapada'

def eh_parcela_marcada(arg):
    '''
    Função que recebe um argumento e devolve True caso a parcela recebida se encontre marcada e caso contrário devolve False

    parcela -> booleano
    '''
    return arg['Estado'] == 'Marcada'

def eh_parcela_limpa(arg):
    '''
    Função que recebe um argumento e devolve True caso a parcela recebida se encontre limpa e caso contrário devolve False

    parcela -> booleano
    '''
    return arg['Estado'] == 'Limpa'

def eh_parcela_minada(arg):
    '''
    Função que recebe um argumento e devolve True caso a parcela tenha uma mina escondida e caso contrário devolve False

    parcela -> booleano
    '''
    return arg['Mina'] == 'S'

def parcelas_iguais(par1, par2):
    '''
    Função que recebe duas parcelas e devolve True apenas se as parcelas forem iguais, em caso contrário devolve False

    parcela x parcela -> booleano
    '''
    return eh_parcela(par1) and eh_parcela(par2) \
        and par1['Estado'] == par2['Estado'] and par1['Mina'] == par2['Mina']

def parcela_para_str(parcela):
    '''
    Função que recebe uma parcela e devolve uma cadeia de caracteres que traduz a representação da parcela em caracteres
    em função do seu estado

    parcela -> str
    '''
    if eh_parcela_tapada(parcela):
        return '#'
    if eh_parcela_marcada(parcela):
        return '@'
    if eh_parcela_limpa(parcela) and not eh_parcela_minada(parcela):
        return '?'
    else: 
        return 'X'

def alterna_bandeira(parcela):
    '''
    Função que recebe uma parcela e modifica a parcela destrutivamente para desmarcada em caso de se encontrar marcada e marcada em
    caso de se encontrar desmarcada nestes casos devolve True em qualquer outro caso não modifica e devolve False

    parcela -> booleano 
    '''
    if eh_parcela_marcada(parcela):
        desmarca_parcela(parcela)
        return True
    if eh_parcela_tapada(parcela):
        marca_parcela(parcela)
        return True
    else:
        return False

def cria_campo(c, l):
    '''
    Função que recebe uma cadeia de caracteres e um inteiro correspondentes à última coluna e à ultima linha de um campo de minas e devolve 
    o campo com o tamanho pretendido formado por parcelas tapadas sem minas 

    str x int -> campo
    '''
    if not isinstance(c, str) or len(c) != 1 or ord(c) < ord('A') or ord(c) > 90 or not isinstance(l, int) or l < 1 or l > 99:
        raise ValueError ('cria_campo: argumentos invalidos')
    campo = []
    for _ in range(l):
        linha = [] 
        for _ in range(ord(c)-ord('A')+1):
            linha.append(cria_parcela())
        campo.append(linha)
          
    return campo

def cria_copia_campo(campo):
    '''
    Função que recebe um campo e que devolve uma cópia do campo

    campo -> campo
    '''
    campo_copy = []
    lista_new = []
    for linha in campo:
        for coluna in linha:
            lista_new += [cria_copia_parcela(coluna)]
        campo_copy += [lista_new]
        lista_new =[]
    return campo_copy

def obtem_ultima_coluna(m):
    '''
    Função que recebe um campo e devolve uma cadeia de caracteres correspondente à última coluna do campo recebido

    campo -> str
    '''
    return chr((ord('A') + len(m[0])-1))

def obtem_ultima_linha(m):
    '''
    Função que recebe um campo e devolve um inteiro correspondente à última linha do campo recebido

    campo -> int
    '''
    return len(m)

def obtem_parcela(m, coord):
    '''
    Função que recebe um campo e uma coordenada e devolve a parcela que se encontra na coordenada recebida do campo recebido

    campo x coordenada -> parcela
    '''
    return m[obtem_linha(coord)-1][ord(obtem_coluna(coord)) - ord('A')]

def obtem_coordenadas(m, s):
    '''
    Função que recebe um campo e uma cadeia de caracteres e devolve um tuplo formado pelas coordenadas ordenadas em ordem
    ascendente de esquerda à direita e de cima a baixo das parcelas dependendo do valor de s

    campo x str -> tuplo
    '''
    conditions = {'limpas': eh_parcela_limpa, 'tapadas': eh_parcela_tapada, 'marcadas': eh_parcela_marcada, 'minadas': eh_parcela_minada}
    coord =()
    for linha in range(len(m)):
        for coluna in range(len(m[linha])):
            if conditions[s](m[linha][coluna]):
                coord += (cria_coordenada(chr(ord('A') + coluna),(linha+1)),)
    return coord

def obtem_numero_minas_vizinhas(m, c):
    '''
    Função que recebe um campo e uma coordenada e devolve um inteiro correspondente ao número de parcelas vizinhas da coordenada
    recebida que escondam uma mina

    campo x coordenada -> int
    '''
    counter = 0
    for coord in obtem_coordenadas_vizinhas(c):
        if obtem_linha(coord) > obtem_ultima_linha(m) or obtem_coluna(coord) > obtem_ultima_coluna(m):
            continue
        if eh_parcela_minada(obtem_parcela(m, coord)):
            counter += 1
    return counter

def eh_campo(arg):
    '''
    Função que recebe um argumento e devolve True caso o argumento seja um TAD campo e caso contrário devolve False

    universal -> booleano
    '''
    if isinstance(arg, list) and len(arg) != 0:
        for lista in arg:
            if isinstance(lista, list) and len(lista) !=0:
                for parcela in lista:
                    if not eh_parcela(parcela):
                        return False
            else:
                return False
        return True
    return False

def eh_coordenada_do_campo(m, c):
    '''
    Função que recebe um campo e uma coordena e devolve True caso a coordenada recebida seja uma coordenada do campo recebido e caso
    contrário devolve False

    campo x coordenada -> booleano
    '''
    return ord('A') <= ord(obtem_coluna(c)) <= ord(obtem_ultima_coluna(m)) and 1 <= obtem_linha(c) <= obtem_ultima_linha(m) and eh_campo(m)

def campos_iguais(m1, m2):
    '''
    Função que recebe dois campos e devolve True apenas se os campos forem iguais, em caso contrário devolve False

    campo x campo -> booleano
    '''
    return eh_campo(m1) and eh_campo(m2) \
        and obtem_coordenadas(m1, 'limpas') == obtem_coordenadas(m2, 'limpas') \
        and obtem_coordenadas(m1, 'tapadas') == obtem_coordenadas(m2, 'tapadas') \
        and obtem_coordenadas(m1, 'marcadas') == obtem_coordenadas(m2, 'marcadas') \
        and obtem_coordenadas(m1, 'minadas') == obtem_coordenadas(m2, 'minadas') 

def campo_para_str(campo):
    '''
    Função que recebe um campo e devolve uma cadeia de caracteres que traduz a representação do campo em caracteres

    campo -> str
    '''
    campostr = '   '
    for linha in range(ord(obtem_ultima_coluna(campo)) - ord('A')+1):
        campostr += chr(ord('A')+ linha)
    campostr += '\n  +' + (ord(obtem_ultima_coluna(campo)) - ord('A') +1) * '-' + '+'
    for linha in range(len(campo)):
        campostr += '\n' + str(linha + 1).zfill(2) + '|'
        for coluna in range(len(campo[linha])):
            if eh_parcela_limpa(campo[linha][coluna]) and not eh_parcela_minada(campo[linha][coluna]) and obtem_numero_minas_vizinhas(campo,(chr(ord('A')+coluna), linha +1)) == 0:
                campostr += ' '
            elif eh_parcela_limpa(campo[linha][coluna]) and not eh_parcela_minada(campo[linha][coluna]) and obtem_numero_minas_vizinhas(campo,(chr(ord('A')+coluna), linha +1)) != 0:
                campostr += str(obtem_numero_minas_vizinhas(campo, (chr(ord('A')+coluna), linha +1))) 
            else:
                campostr += parcela_para_str(campo[linha][coluna])
        campostr += '|'
    campostr += '\n  +' + (ord(obtem_ultima_coluna(campo)) - ord('A') +1) * '-' + '+'
    return campostr


def coloca_minas(m, c, g, n):
    '''
    Função que recebe um campo, uma coordenada, um gerador e um inteiro e modifica destrutivamente o campo m escondendo n minas em parcelas dentro do campo. 
    As n coordenadas são geradas sequencialmente utilizando o gerador recebido, de modo a que não coincidam com a coordenada recebida nem com nenhuma parcela 
    vizinha desta, nem se sobreponham com minas colocadas anteriormente

    campo x coordenada x gerador x int -> campo
    '''
    counter = 0
    while counter != n:
        flag = False
        coord_try = obtem_coordenada_aleatoria(cria_coordenada(obtem_ultima_coluna(m), obtem_ultima_linha(m)), g)
        if  coordenadas_iguais(coord_try, c) or eh_parcela_minada(obtem_parcela(m, coord_try)):
            del coord_try
        else:
            for coord in obtem_coordenadas_vizinhas(c):
                if coordenadas_iguais(coord_try, coord):
                    del coord_try
                    flag = True
                    break
            if flag == False:
                    counter += 1
                    esconde_mina(obtem_parcela(m, coord_try))
    return m

def limpa_campo(m, c):
    '''
    Função que recebe um campo e uma coordenada e modifica destrutivamente o campo limpando a parcela na coordenada recebida, devolvendo-o. Se não houver nenhuma 
    mina vizinha escondida, limpa iterativamente todas as parcelas vizinhas tapadas. Caso a parcela se encontre já limpa, a operação não tem efeito

    campo x coordenada -> campo
    '''
    if eh_parcela_limpa(obtem_parcela(m,c)):
        return m
    elif obtem_numero_minas_vizinhas(m, c) == 0 and not eh_parcela_minada(obtem_parcela(m, c)):
        limpa_parcela(obtem_parcela(m, c))
        for coord in obtem_coordenadas_vizinhas(c):
            if eh_coordenada_do_campo(m, coord) and not eh_parcela_marcada(obtem_parcela(m, coord)):
                limpa_campo(m, coord)
    else:
        limpa_parcela(obtem_parcela(m, c))
        return m
    return m

def jogo_ganho(campo):
    '''
    Função auxiliar que recebe um campo do jogo das minas e devolve True se todas as parcelas sem minas se encontram limpas
    em caso contrário devolve False

    campo -> booleano
    '''
    return len(obtem_coordenadas(campo,'limpas')) == (obtem_ultima_linha(campo) * \
        (ord(obtem_ultima_coluna(campo)) - ord('A') + 1)) - len(obtem_coordenadas(campo, 'minadas'))

def turno_jogador(campo):
    '''
    Função auxiliar que recebe um campo de minas e oferece ao jogador a opção de escolher uma ação e uma coordenada

    campo -> booleano
    '''
    jogada_jogador=''
    while jogada_jogador != 'L' and jogada_jogador != 'M':
        jogada_jogador = input('Escolha uma ação, [L]impar ou [M]arcar:')
    while True:
        coordenada_jogador = input('Escolha uma coordenada:')
        try:
            if len(coordenada_jogador) == 3 and eh_coordenada_do_campo(campo, str_para_coordenada(coordenada_jogador)):
                break
        except:
            pass
    if jogada_jogador == 'L':
            limpa_campo(campo, str_para_coordenada(coordenada_jogador))
            if eh_parcela_minada(obtem_parcela(campo, str_para_coordenada(coordenada_jogador))) and eh_parcela_limpa(obtem_parcela(campo, str_para_coordenada(coordenada_jogador))):
                return False
            else:
                return not eh_parcela_minada(obtem_parcela(campo, str_para_coordenada(coordenada_jogador)))
    else:
        alterna_bandeira(obtem_parcela(campo, str_para_coordenada(coordenada_jogador)))
        return True

def minas(c,l,n,d,s):
    '''
    Função principal que permite jogar ao jogo das minas. A função recebe uma cadeia de carateres e 4 valores inteiros correspondentes, respetivamente, a:
    última coluna c; última linha l; número de parcelas com minas n; dimensão do gerador de númerps d; e estado inicial ou seed s para a geração de números 
    aleatórios. A função devolve True se o jogador conseguir ganhar o jogo, ou False caso contrário

    str x int x int x int x int -> booleano
    '''
    if not isinstance(s, int) or not isinstance(d, int) or (d != 32 and d != 64) or s <= 0 or s > 2**d:
        raise ValueError ('minas: argumentos invalidos')
    if not isinstance(c, str) or len(c) != 1 or ord(c) < ord('A') or ord(c) > 90 or not isinstance(l, int) or  l < 1 or l > 99:
        raise ValueError ('minas: argumentos invalidos')
    if not isinstance(n, int) or n <= 0 or n >= (((ord(c)-ord('A') +1) * l) -9):
        raise ValueError ('minas: argumentos invalidos')
    if ((ord(c)-ord('A') +1) * l) <= 9:
        raise ValueError ('minas: argumentos invalidos')
    campo = cria_campo(c, l)
    print('   [Bandeiras ' + str(len(obtem_coordenadas(campo, 'marcadas'))) + '/' + str(n) + ']')
    print(campo_para_str(campo))
    while True:
        coord_ini = input('Escolha uma coordenada:')
        try:
            if eh_coordenada_do_campo(campo, str_para_coordenada(coord_ini)) and len(coord_ini) == 3:
                break
        except IndexError:
            pass
    coloca_minas(campo, str_para_coordenada(coord_ini), cria_gerador(d, s), n)
    limpa_campo(campo, str_para_coordenada(coord_ini))
    print('   [Bandeiras ' + str(len(obtem_coordenadas(campo, 'marcadas'))) + '/' + str(n) + ']')
    print(campo_para_str(campo))
    while turno_jogador(campo):
        print('   [Bandeiras ' + str(len(obtem_coordenadas(campo, 'marcadas'))) + '/' + str(n) + ']')
        print(campo_para_str(campo))
        if jogo_ganho(campo):
            print('VITORIA!!!')
            return True
    print('   [Bandeiras ' + str(len(obtem_coordenadas(campo, 'marcadas'))) + '/' + str(n) + ']')
    print(campo_para_str(campo))
    print('BOOOOOOOM!!!')
    return False
