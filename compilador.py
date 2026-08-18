#!/usr/bin/python
# coding: UTF-8
from os import system
import sys
cha = ' '
MainCount = 0
op = ''
v1 = ''
v = ''
goto = 1
vtipo = ''
tipov1 = ''
countOp = 0
linha = 1
coluna = 0
palavraReservadas = [["main", 1], ["tipo_float", 2], ["tipo_int", 3], ["tipo_char", 4], ["while", 5], ["do", 6], ["if", 7], ["else", 8], ["id", 9]]
dicionario_tipos = [[10, "Valor_int"], [11, "Valor_float"], [12, "Valor_char"]]
operadores_ari = [[13, "+"], [14, "-"], [15, "*"], [16, "/"], [17, "="]]
operadores_rel = [[18, ">"], [19, "<"], [20, ">="], [21, "<="], [22, "=="], [23, "!="]]
especial = [[24, "("], [25, ")"], [26, "{"], [27, "}"], [28, ";"], [29, ","], [30, "eof"]]

def lercaracter():
    global coluna, linha, cha
    cha = arq.read(1)
    if cha == '\n' or cha == '\r':
        linha += 1
        coluna = 0
    elif cha is '\t':
        coluna += 4
    else:
        coluna += 1

def verificacha():
    global cha
    retorno = 1
    if cha != ' ' and cha != '.' and cha != '+' and cha != '-' and cha != '*' and cha != '/' and cha != ')'\
        and cha != '>' and cha != '<' and cha != '=' and cha != ';'and cha != '!' and cha != ',' and cha != '\n' and cha != '\t':
        retorno = 0
    if retorno is 0:
        return True
    else:
        return False

class Pilha(object):
    def __init__(self):
        self.dados = []

    def empilha(self, elemento):
        self.dados.append(elemento)

    def desempilha(self):
        if not self.vazia():
            return self.dados.pop(-1)

    def vazia(self):
        return len(self.dados) == 0

def tabela(id,tipo):
    if VerificaID(id) is True:
        pid.empilha(id)
        ptip.empilha(tipo)
    return

def VoltaPilhaId():
    while True:
        if pidaux.vazia() is True:
            break
        else:
            pid.empilha(pidaux.desempilha())
    return

def VoltaPilhaTipo():
    while True:
        if ptipaux.vazia() is True:
            break
        else:
            ptip.empilha(ptipaux.desempilha())
    return

def VerificaID(idver):#haha, ->*
    if pid.vazia() is False and idver != "*":
        while True:
            idpilha = pid.desempilha()
            if idver == idpilha:
                print("Erro linha: ", linha, " coluna: ", coluna, " ultimo token: ", new.get_lex(),
                  ' Variavel ja declarada no escopo')
                sys.exit(0)
            elif idpilha != "*" and pid.vazia() is False:
                    pidaux.empilha(idpilha)
            else:#se chegar no fim do escopo ou no fim da pilha
                if idpilha == "*": #caso esteja em um escopo
                    pidaux.empilha(idpilha)
                VoltaPilhaId()
                break
    return True

def ExisteID(id):
    while True:
        idpilha = pid.desempilha()
        if id == idpilha:
            pid.empilha(idpilha)
            VoltaPilhaId()
            return True
        elif pid.vazia() is False:
            pidaux.empilha(idpilha)
        else:
            print("Erro linha: ", linha, " coluna: ", coluna, " ultimo token: ", new.get_lex(),
                  ' Variavel não declarada ')
            sys.exit(0)
    return

def PegaTipo(id):
    while True:
        idpilha = pid.desempilha()
        tipoId = ptip.desempilha()
        if id == idpilha:
            pid.empilha(idpilha)
            ptip.empilha(tipoId)
            VoltaPilhaId()
            VoltaPilhaTipo()
            return tipoId
        elif pid.vazia() is False:
            pidaux.empilha(idpilha)
            ptipaux.empilha(tipoId)
    return

def DestroyScope():
    while True:
        idpilha = pid.desempilha()
        if idpilha == "*":
            ptip.desempilha()
            return
        else:
            ptip.desempilha()
    return

class Token:
    num = 1
    lex = " "

    def tok(self, num, lex):
        self.num = num
        self.lex = lex

    def get_num(self):
        return self.num

    def get_lex(self):
        return self.lex

def convertTo():
    global v1,v,MainCount,op,vtipo,tipov1
    if tipov1 == "Valor_int" and vtipo == "Valor_int" and op == operadores_ari[3][0]:
                print ("t"+str(MainCount)+" = int_to_float("+v1+")")
                v1 = "t"+str(MainCount)
                MainCount += 1
                print ("t"+str(MainCount)+" = int_to_float("+v+")")
                v = "t"+str(MainCount)
                MainCount += 1
    elif tipov1 == "Valor_float" and vtipo == "Valor_int":
                print ("t"+str(MainCount)+" = int_to_float("+v+")")
                v = "t"+str(MainCount)
                MainCount += 1
    elif tipov1 == "Valor_int" and vtipo == "Valor_float":
                print ("t"+str(MainCount)+" = int_to_float("+v1+")")
                v1 = "t"+str(MainCount)
                MainCount += 1
    return

def scanner():
    global cha, palavraReservadas, new, dicionario_tipos, operadores_ari, operadores_rel, especial
    while cha:
        lex = ""
        while cha == '\n' or cha == '\r' or cha == ' ' or cha == '\t':
            lercaracter()
        if str.isdigit(cha):  # se for digito
            lex += cha
            lercaracter()
            while str.isdigit(cha):
                lex += cha
                lercaracter()
            if verificacha() is True:
                lex += cha
                print("Erro linha: ", linha, " coluna: ", coluna, " ultimo token: ", lex,
                      'VALOR INTEIRO mal escrito ')
                sys.exit(0)
                return
            elif cha != '.':
                return new.tok(dicionario_tipos[0][0], lex)
            else:
                lex += cha
                lercaracter()
                if not (str.isdigit(cha)):
                    print("Erro linha: ", linha, " coluna: ", coluna, " ultimo token: ", lex,
                          'VALOR FLOAT mal escrito')
                    sys.exit(0)
                    return
                while str.isdigit(cha):
                    lex += cha
                    lercaracter()
                if verificacha() is True:
                    lex += cha
                    print("Erro linha: ", linha, " coluna: ", coluna, " ultimo token: ", lex,
                          'VALOR FLOAT mal escrito')
                    sys.exit(0)
                    return
                else:
                    return new.tok(dicionario_tipos[1][0], lex)
        elif cha == '.':
            lex += cha
            lercaracter()
            if not (str.isdigit(cha)):
                print("Erro linha: ", linha, " coluna: ", coluna, " ultimo token: ", lex,
                      'VALOR FLOAR mal escrito')
                sys.exit(0)
                return
            while str.isdigit(cha):
                lex += cha
                lercaracter()
            if verificacha() is True:
                lex += cha
                print("Erro linha: ", linha, " coluna: ", coluna, " ultimo token: ", lex,
                      ' VALOR FLOAR   mal escrito')
                sys.exit(0)
                return
            else:
                return new.tok(dicionario_tipos[1][0], lex)
        elif cha == '+':
            lex += cha
            lercaracter()
            return new.tok(operadores_ari[0][0], operadores_ari[0][1])
        elif cha == '-':
            lex += cha
            lercaracter()
            return new.tok(operadores_ari[1][0], operadores_ari[1][1])
        elif cha == '*':
            lex += cha
            lercaracter()
            return new.tok(operadores_ari[2][0], operadores_ari[2][1])
        elif cha == '/':
            lex += cha
            lercaracter()
            if cha == '/':
                while cha != '\n':
                    lercaracter()
            elif cha == '*':
                lercaracter()
                while cha:
                    lercaracter()
                    if cha == '':
                        print("Erro linha: ", linha, " coluna: ", coluna, " ultimo token: ", lex,
                              				'(fim de comentario \n Nao encontradp (*/) )')
                        sys.exit(0)
                        return
                    elif cha == '*':
                        lercaracter()
                        if cha == '/':
                            lercaracter()
                            break
            else:
                return new.tok(operadores_ari[3][0], operadores_ari[3][1])
        elif cha == '>':
            lex += cha
            lercaracter()
            if cha == '=':
                lex += cha
                lercaracter()
                return new.tok(operadores_rel[2][0], operadores_rel[2][1])
            else:
                return new.tok(operadores_rel[0][0], operadores_rel[0][1])
        elif cha == '<':
            lex += cha
            lercaracter()
            if cha == '=':
                lex += cha
                lercaracter()
                return new.tok(operadores_rel[3][0], operadores_rel[3][1])
            else:
                return new.tok(operadores_rel[1][0], operadores_rel[1][1])
        elif cha == '!':
            lex += cha
            lercaracter()
            if cha == '=':
                lex += cha
                lercaracter()
                return new.tok(operadores_rel[5][0], operadores_rel[5][1])
            else:
                print("Erro linha: ", linha, " coluna: ", coluna, " ultimo token: ", lex,
                     		 ' ((!=)) falta do ((=)) no operador relacional  mal escrito ')
                sys.exit(0)
                return
        elif cha == '=':
            lex += cha
            lercaracter()
            if cha == '=':
                lex += cha
                lercaracter()
                return new.tok(operadores_rel[4][0], operadores_rel[4][1])
            else:
                return new.tok(operadores_ari[4][0], operadores_ari[4][1])
        elif cha == '(':
            lex += cha
            lercaracter()
            return new.tok(especial[0][0], especial[0][1])
        elif cha == ')':
            lex += cha
            lercaracter()
            return new.tok(especial[1][0], especial[1][1])
        elif cha == '{':
            lex += cha
            lercaracter()
            return new.tok(especial[2][0], especial[2][1])
        elif cha == '}':
            lex += cha
            lercaracter()
            return new.tok(especial[3][0], especial[3][1])
        elif cha == ';':
            lex += cha
            lercaracter()
            return new.tok(especial[4][0], especial[4][1])
        elif cha == ',':
            lex += cha
            lercaracter()
            return new.tok(especial[5][0], especial[5][1])
        elif cha == '\'':
            lercaracter()
            if not(str.isdigit(cha)) and not(str.isalpha(cha)):
                print("Erro linha: ", linha, " coluna: ", coluna, " ultimo token: ", lex,
                      		' VALOR CHAR mal escrito ')
                sys.exit(0)
                return
            lex += cha
            lercaracter()
            if cha == '\'':
                lercaracter()
                return new.tok(dicionario_tipos[2][0], lex)
            else:
                print("Erro linha: ", linha, " coluna: ", coluna, " ultimo token: ", lex,
                      		' VALOR CHAR mal escrito  ')
                sys.exit(0)
                return
        elif str.isalpha(cha) or cha == '_':
            lex += cha
            lercaracter()
            while str.isalpha(cha) or cha is "_" or str.isdigit(cha):
                lex += cha
                lercaracter()
            if "main" == lex:
                return new.tok(palavraReservadas[0][1], palavraReservadas[0][0])
            elif "float" == lex:
                return new.tok(palavraReservadas[1][1], palavraReservadas[1][0])
            elif "int" == lex:
                return new.tok(palavraReservadas[2][1], palavraReservadas[2][0])
            elif "char" == lex:
                return new.tok(palavraReservadas[3][1], palavraReservadas[3][0])
            elif "while" == lex:
                return new.tok(palavraReservadas[4][1], palavraReservadas[4][0])
            elif "do" == lex:
                return new.tok(palavraReservadas[5][1], palavraReservadas[5][0])
            elif "if" == lex:
                return new.tok(palavraReservadas[6][1], palavraReservadas[6][0])
            elif "else" == lex:
                return new.tok(palavraReservadas[7][1], palavraReservadas[7][0])
            elif verificacha() is False:
                return new.tok(palavraReservadas[8][1], lex)
            else:
                lex += cha
                print("Erro linha: ", linha, " coluna: ", coluna, " ultimo token: ", lex,
                      ' id invalido  )')
                sys.exit(0)
                return
        elif cha == "":
            return new.tok(especial[6][0], especial[6][1])
        elif cha != -1:
            lex += cha
            print("Erro linha: ", linha, " coluna: ", coluna, " ultimo token: ", lex,
                  ' ( caracter incorreto (FORA DA LINGUAGEM ) )')
            sys.exit(0)
            return
        lercaracter()
    return

def declarar():#<decl_var> ::= <tipo> <id> {,<id>}* ;
    if new.get_num() == palavraReservadas[1][1] or new.get_num() == palavraReservadas[2][1] or new.get_num() == palavraReservadas[3][1]:
        if new.get_num() == palavraReservadas[1][1]:
            tipo = "Valor_float"
        elif new.get_num() == palavraReservadas[2][1]:
            tipo = "Valor_int"
        elif new.get_num() == palavraReservadas[3][1]:
            tipo = "Valor_char"
        scanner()
        if new.get_num() != palavraReservadas[8][1]:
            print("Erro linha: ", linha, " coluna: ", coluna, " ultimo token: ", new.get_lex(),
              ' Erro na declaraçao: id nao declarado ')
            sys.exit(0)
        else:
            tabela(new.get_lex(),tipo) #insere a variavel na tabela de simbolos
            scanner()
            while new.get_num() == especial[5][0]:
                scanner()
                if new.get_num() != palavraReservadas[8][1]:
                    print("Erro linha: ", linha, " coluna: ", coluna, " ultimo token: ", new.get_lex(),
                    ' Erro na declaraçao ')
                    sys.exit(0)
                else:
                    tabela(new.get_lex(),tipo)
                    scanner()
        if new.get_num() != especial[4][0]:
             print("Erro linha: ", linha, " coluna: ", coluna, " ultimo token: ", new.get_lex(),
              ' ( caracter incorreto (FORA DA LINGUAGEM ) )')
             sys.exit(0)
        else:
            scanner()
    return

def fator(): #“(“ <expr_arit> “)” | <id> | <real> | <inteiro> | <char>
    global countOp,v1,tipov1,vtipo, MainCount,op,v,vtipo,tipov1
    if new.get_num() == especial[0][0]:
        scanner()
        while new.get_num() != especial[1][0]:
            Etipo = expressao()
        scanner()
        return Etipo
    elif new.get_num() == dicionario_tipos[0][0] or new.get_num() == dicionario_tipos[1][0] or new.get_num() == dicionario_tipos[2][0] or new.get_num() == palavraReservadas[8][1]:
        if new.get_num() == palavraReservadas[8][1]:
            ExisteID(new.get_lex())
            Etipo = PegaTipo(new.get_lex())
        else:
            if new.get_num() == dicionario_tipos[0][0]:
                Etipo = "Valor_int"
            elif new.get_num() == dicionario_tipos[1][0]:
                Etipo = "Valor_float"
            elif new.get_num() == dicionario_tipos[2][0]:
                Etipo = "Valor_char"
        if countOp == 0:
            v1 = new.get_lex()
            countOp = 1
            tipov1 = Etipo
        else:
            v = new.get_lex()
            vtipo = Etipo
        scanner()
        return Etipo
    else:
        print("Erro linha: ", linha, " coluna: ", coluna, " ultimo token: ", new.get_lex(),
                  ' Erro No fator ')
        sys.exit(0)

def termo_arit():
    global countOp,v1,tipov1,vtipo, MainCount,op,v
    if new.get_num() == operadores_ari[2][0] or new.get_num() == operadores_ari[3][0]:
        if v != '':
            pilhaop.empilha(op)
            pilhav1.empilha(v1)
            v1 = v
        op = new.get_lex()
        if new.get_num() == operadores_ari[3][0]:
            operador = operadores_ari[3][0]
        else:
            operador = operadores_ari[2][0]
        scanner()
        tipo1 = fator()
        tipo2 = termo_arit()
        if tipo1 == "Valor_int" and tipo2 == "Valor_int" and operador == operadores_ari[3][0]:
            convertTo()
            print ("t"+str(MainCount)+" = "+v1+op+v)
            v1 = "t"+str(MainCount)
            tipov1 = vtipo
            MainCount += 1
            if pilhaop.vazia() is True:
                v = ''
                op = ''
            else:
                v = v1
                op = pilhaop.desempilha()
                v1 = pilhav1.desempilha()
            return "Valor_float"
        elif tipo1 == tipo2:
            convertTo()
            print ("t"+str(MainCount)+" = "+v1+op+v)
            v1 = "t"+str(MainCount)
            tipov1 = vtipo
            MainCount += 1
            if pilhaop.vazia() is True:
                v = ''
                op = ''
            else:
                v = v1
                op = pilhaop.desempilha()
                v1 = pilhav1.desempilha()
            return tipo1
        elif tipo1 == "Valor_float" and tipo2 == "Valor_int":
            convertTo()
            print ("t"+str(MainCount)+" = "+v1+op+v)
            v1 = "t"+str(MainCount)
            tipov1 = vtipo
            MainCount += 1
            if pilhaop.vazia() is True:
                v = ''
                op = ''
            else:
                v = v1
                op = pilhaop.desempilha()
                v1 = pilhav1.desempilha()
            return "Valor_float"
        elif tipo1 == "Valor_int" and tipo2 == "Valor_float":
            convertTo()
            print ("t"+str(MainCount)+" = "+v1+op+v)
            v1 = "t"+str(MainCount)
            tipov1 = vtipo
            MainCount += 1
            if pilhaop.vazia() is True:
                v = ''
                op = ''
            else:
                v = v1
                op = pilhaop.desempilha()
                v1 = pilhav1.desempilha()
            return "Valor_float"
        elif tipo2 == None and operador == operadores_ari[3][0]:
            if tipo1 == "Valor_char":
                convertTo()
                print ("t"+str(MainCount)+" = "+v1+op+v)
                v1 = "t"+str(MainCount)
                tipov1 = vtipo
                MainCount += 1
                if pilhaop.vazia() is True:
                    v = ''
                    op = ''
                else:
                    v = v1
                    op = pilhaop.desempilha()
                    v1 = pilhav1.desempilha()
                return "Valor_char"
            else:
                convertTo()
                print ("t"+str(MainCount)+" = "+v1+op+v)
                v1 = "t"+str(MainCount)
                tipov1 = vtipo
                MainCount += 1
                if pilhaop.vazia() is True:
                    v = ''
                    op = ''
                else:
                    v = v1
                    op = pilhaop.desempilha()
                    v1 = pilhav1.desempilha()
                return "Valor_float"
        elif tipo2 == None and operador == operadores_ari[2][0]:
            convertTo()
            print ("t"+str(MainCount)+" = "+v1+op+v)
            v1 = "t"+str(MainCount)
            tipov1 = vtipo
            MainCount += 1
            if pilhaop.vazia() is True:
                v = ''
                op = ''
            else:
                v = v1
                op = pilhaop.desempilha()
                v1 = pilhav1.desempilha()
            return tipo1
        else:
            print("Erro linha: ", linha, " coluna: ", coluna, " ultimo token: ", new.get_lex(),
                  ' Erro de tipos de variaveis')
            sys.exit(0)
    return None

def termo():#<termo> "*" <fator> | <termo> “/” <fator> | <fator>
    tipo1 = fator()
    tipo2 = termo_arit()
    if tipo1 == tipo2:
        return tipo1
    elif tipo1 == "Valor_float" and tipo2 == "Valor_int":
        return "Valor_float"
    elif tipo1 == "Valor_int" and tipo2 == "Valor_float":
        return "Valor_float"
    elif tipo2 == None:
        return tipo1
    else:
         print("Erro linha: ", linha, " coluna: ", coluna, " ultimo token: ", new.get_lex(),
                  ' Erro de tipos de variaveis')
         sys.exit(0)

def expr_arit():
    global countOp,v1,tipov1,vtipo, MainCount,op,v
    if new.get_num() == operadores_ari[0][0] or new.get_num() == operadores_ari[1][0]:
        if v != '':
            pilhaop.empilha(op)
            pilhav1.empilha(v1)
            v1 = v
        op = new.get_lex()
        scanner()
        tipo1 = termo()
        tipo2 = expr_arit()
        if tipo1 == tipo2:
            convertTo()
            print ("t"+str(MainCount)+" = "+v1+op+v)
            v1 = "t"+str(MainCount)
            tipov1 = vtipo
            MainCount += 1
            if pilhaop.vazia() is True:
                v = ''
                op = ''
            else:
                v = v1
                op = pilhaop.desempilha()
                v1 = pilhav1.desempilha()
            return tipo1
        elif tipo1 == "Valor_float" and tipo2 == "Valor_int":
            convertTo()
            print ("t"+str(MainCount)+" = "+v1+op+v)
            v1 = "t"+str(MainCount)
            tipov1 = vtipo
            MainCount += 1
            if pilhaop.vazia() is True:
                v = ''
                op = ''
            else:
                v = v1
                op = pilhaop.desempilha()
                v1 = pilhav1.desempilha()
            return "Valor_float"
        elif tipo1 == "Valor_int" and tipo2 == "Valor_float":
            convertTo()
            print ("t"+str(MainCount)+" = "+v1+op+v)
            v1 = "t"+str(MainCount)
            tipov1 = vtipo
            MainCount += 1
            if pilhaop.vazia() is True:
                v = ''
                op = ''
            else:
                v = v1
                op = pilhaop.desempilha()
                v1 = pilhav1.desempilha()
            return "Valor_float"
        elif tipo2 == None:
            convertTo()
            print ("t"+str(MainCount)+" = "+v1+op+v)
            v1 = "t"+str(MainCount)
            tipov1 = vtipo
            MainCount += 1
            if pilhaop.vazia() is True:
                v = ''
                op = ''
            else:
                v = v1
                op = pilhaop.desempilha()
                v1 = pilhav1.desempilha()
            return tipo1
        else:
            print("Erro linha: ", linha, " coluna: ", coluna, " ultimo token: ", new.get_lex(),
                  ' Erro de tipos de variaveis')
            sys.exit(0)
    return None

def expressao():#<expr_arit> "+" <termo>   | <expr_arit> "-" <termo> | <termo>
    tipo1 = termo()
    tipo2 = expr_arit()
    if tipo1 == tipo2:
        return tipo1
    elif tipo1 == "Valor_float" and tipo2 == "Valor_int":
        return "Valor_float"
    elif tipo1 == "Valor_int" and tipo2 == "Valor_float":
        return "Valor_float"
    elif tipo2 == None:
        return tipo1
    else:
        print("Erro linha: ", linha, " coluna: ", coluna, " ultimo token: ", new.get_lex(),
                  ' Erro de tipos de variaveis')
        sys.exit(0)

def atribuir(): #<atribuição> ::= <id> "=" <expr_arit> ";"
    global MainCount, countOp, op, v
    if new.get_num() == palavraReservadas[8][1]:
        ExisteID(new.get_lex())
        MainTipo = PegaTipo(new.get_lex())
        MainVar = new.get_lex()
        scanner()
        if new.get_num() == operadores_ari[4][0]:
            scanner()
            MainCount = 0
            countOp = 0
            TipoEx = expressao()
            if MainTipo == "Valor_char":
                if TipoEx != "Valor_char":
                    print("Erro linha: ", linha, " coluna: ", coluna, " ultimo token: ", new.get_lex(),
                  ' Erro de tipos de variaveis na atribução')
                    sys.exit(0)
            if MainTipo == "Valor_int":
                if TipoEx != "Valor_int":
                    print("Erro linha: ", linha, " coluna: ", coluna, " ultimo token: ", new.get_lex(),
                  ' Erro de tipos de variaveis na atribução')
                    sys.exit(0)
            if MainTipo == "Valor_float":
                if TipoEx == "Valor_char":
                    print("Erro linha: ", linha, " coluna: ", coluna, " ultimo token: ", new.get_lex(),
                  ' Erro de tipos de variaveis na atribução')
                    sys.exit(0)
            if new.get_num() != especial[4][0]:
                print("Erro linha: ", linha, " coluna: ", coluna, " ultimo token: ", new.get_lex(),
                  ' Erro de atribuiçao ')
                sys.exit(0)
            else:
                if MainCount == 0:
                    print(MainVar+" = "+v1)
                else:
                    print (MainVar+" = t"+str(MainCount-1))
                countOp = 0
                op = ''
                v = ''
                MainCount = 0
                scanner()
        else:
            print("Erro linha: ", linha, " coluna: ", coluna, " ultimo token: ", new.get_lex(),
                  ' Erro de atribuiçao ')
            sys.exit(0)
    else:
        print("Erro linha: ", linha, " coluna: ", coluna, " ultimo token: ", new.get_lex(),
                  ' Erro de atribuiçao ')
        sys.exit(0)
    return

def exp_relacional():#<expr_relacional> ::= <expr_arit> <op_relacional> <expr_arit>
    global MainCount, countOp, op
    TipoE1 = expressao()
    if MainCount == 0:
         varexp1 = v1
    else:
        varexp1 = "t"+str(MainCount-1)
    atual = MainCount
    countOp=0
    op = ''
    #agora verificar se é <, <=, >, >=, == ou !=
    if new.get_num() == operadores_rel[0][0] or new.get_num() == operadores_rel[1][0] or new.get_num() == operadores_rel[2][0] \
        or new.get_num() == operadores_rel[3][0] or new.get_num() == operadores_rel[4][0] or new.get_num() == operadores_rel[5][0]:
        opexp = new.get_lex()
        scanner()
        TipoE2 = expressao()
        if MainCount == atual:
            varexp2 = v1
        else:
            varexp2 = "t"+str(MainCount-1)
        print ("t"+str(MainCount)+" = "+varexp1+opexp+varexp2)
        boolean = "t"+str(MainCount)
        MainCount = 0
        countOp=0
        op = ''
        if TipoE1 == "Valor_char":
            if TipoE2 != "Valor_char":
                    print("Erro linha: ", linha, " coluna: ", coluna, " ultimo token: ", new.get_lex(),
                  ' Erro de tipos de variaveis na expressao relacional')
                    sys.exit(0)
        elif TipoE1 == "Valor_int" or TipoE1 == "Valor_float":
                if TipoE2 == "Valor_char":
                    print("Erro linha: ", linha, " coluna: ", coluna, " ultimo token: ", new.get_lex(),
                  ' Erro de tipos de variaveis na expressao relacional')
                    sys.exit(0)
    else:
        print("Erro linha: ", linha, " coluna: ", coluna, " ultimo token: ", new.get_lex(),
                  ' Erro na expressao relacional')
        sys.exit(0)
    return boolean

def comando_basico():#<atribuição> | <bloco>
    if new.get_num() == palavraReservadas[8][1]:
        atribuir()
    elif new.get_num() == especial[2][0]:
        bloco()
    return

def iteracao():#while "("<expr_relacional>")" <comando> | do <comando> while "("<expr_relacional>")"";"
    global goto
    if new.get_num() == palavraReservadas[4][1]:#while
        scanner()
        if new.get_num() != especial[0][0]:
            print("Erro linha: ", linha, " coluna: ", coluna, " ultimo token: ", new.get_lex(),
                  ' Erro na iteraçao while ')
            sys.exit(0)
        else:
            scanner()
            boolean = exp_relacional()
            if new.get_num() == especial[1][0]:
                scanner()
                print("if "+boolean+" == 0 goto L"+str(goto))
                forawhile = goto
                goto += 1
                print("L"+str(goto)+":")
                voltawhile = goto
                goto += 1
                if new.get_num() != especial[2][0]:
                    tabela("*","*")
                    comando()
                    DestroyScope()
                    print("goto L"+str(voltawhile))
                else:
                    comando()
                    print("goto L"+str(voltawhile))
                print("L"+str(forawhile)+":")
            else:
                print("Erro linha: ", linha, " coluna: ", coluna, " ultimo token: ", new.get_lex(),
                  ' Erro na iteração while ')
                sys.exit(0)
    elif new.get_num() == palavraReservadas[5][1]:#do while
        scanner()
        voltaDo = goto
        goto+=1
        print("L"+str(voltaDo)+":")
        if new.get_num() != especial[2][0]:
            tabela("*","*")
            comando()
            DestroyScope()
        else:
            comando()
        if new.get_num() != palavraReservadas[4][1]:
            print("Erro linha: ", linha, " coluna: ", coluna, " ultimo token: ", new.get_lex(),
                  ' Erro na iteração do while ')
            sys.exit(0)
        else:
            scanner()
            if new.get_num() != especial[0][0]:
                print("Erro linha: ", linha, " coluna: ", coluna, " ultimo token: ", new.get_lex(),
                  ' Erro na iteração do while ')
                sys.exit(0)
            else:
                scanner()
                boolean = exp_relacional()
                if new.get_num() != especial[1][0]:
                    print("Erro linha: ", linha, " coluna: ", coluna, " ultimo token: ", new.get_lex(),
                  ' Erro na iteração do while')
                    sys.exit(0)
                else:
                    scanner()
                    print("if "+boolean+" != 0 goto L"+str(voltaDo))
                    if new.get_num() == especial[4][0]:
                        scanner()
                    else:
                        print("Erro linha: ", linha, " coluna: ", coluna, " ultimo token: ", new.get_lex(),
                            ' Erro na iteração do while')
                        sys.exit(0)
    return

def comando():#<comando_básico> | <iteração> | if "("<expr_relacional>")" <comando> {else <comando>}?
    global goto
    if new.get_num() == palavraReservadas[4][1] or new.get_num() == palavraReservadas[5][1]:#while e do while
        iteracao()
    elif new.get_num() == palavraReservadas[8][1] or new.get_num() == especial[2][0]: #bloco ({) e atribuir
        comando_basico()
    elif new.get_num() == palavraReservadas[6][1]:#if
        scanner()
        if new.get_num() != especial[0][0]:
            print("Erro linha: ", linha, " coluna: ", coluna, " ultimo token: ", new.get_lex(),
                  ' Erro na condiçao')
            sys.exit(0)
        else:
            scanner()
            boolean = exp_relacional()
            if new.get_num() == especial[1][0]:
                scanner()
                print("if "+boolean+" == 0 goto L"+str(goto))
                foraif = goto
                goto += 1
                dentroelse = goto
                goto += 1
                if new.get_num() != especial[2][0]:
                    tabela("*","*")
                    comando()
                    DestroyScope()
                else:
                    comando()
                if(new.get_num() == palavraReservadas[7][1]):#else
                    print("goto L"+str(dentroelse))
                    print("L"+str(foraif)+":")
                    goto += 1
                    scanner()
                    if new.get_num() != especial[2][0]:
                        tabela("*","*")
                        comando()
                        DestroyScope()
                    else:
                        comando()
                    print("L"+str(dentroelse)+":")
                else:
                    print("L"+str(foraif)+":")

            else:
                print("Erro linha: ", linha, " coluna: ", coluna, " ultimo token: ", new.get_lex(),
                  ' Erro na condiçao')
                sys.exit(0)
    return

def bloco():#“{“ {<decl_var>}* {<comando>}* “}”
    if new.get_num() != especial[2][0]: #se for diferente de {
        print("Erro linha: ", linha, " coluna: ", coluna, " Erro: abertura de bloco")
        sys.exit(0)
    else:
        tabela("*","*")
        scanner()
        while new.get_num() != especial[3][0]:#se for igual a } ai ele sai
            declarar()
            comando()
            if new.get_num() == especial[6][0]:
                print("Erro linha: ", linha, " coluna: ", coluna, " Erro: problema no bloco")
                sys.exit(0)
        DestroyScope()
        scanner()
    return

def programa():
    if new.get_num() == palavraReservadas[2][1]: #int
        scanner()
        if new.get_num() == palavraReservadas[0][1]:#main
            scanner()
            if new.get_num() == especial[0][0]:#(
                scanner()
                if new.get_num() == especial[1][0]:#)
                    scanner()
                    bloco()
                else:
                    print("Erro linha: ", linha, " coluna: ", coluna, " Erro: inicialização do programa 1")
                    sys.exit(0)
            else:
                print("Erro linha: ", linha, " coluna: ", coluna, " Erro: inicialização do programa 2")
                sys.exit(0)
        else:
             print("Erro linha: ", linha, " coluna: ", coluna, " Erro: inicialização do programa 3")
             sys.exit(0)
    else:
        print("Erro linha: ", linha, " coluna: ", coluna, " Erro: inicialização do programa 4")
        sys.exit(0)
    return

def parser():
    scanner()
    programa()
    return

nome_arq = sys.argv[1]
arq = open(nome_arq, "r")
new = Token()
pid = Pilha()
ptip = Pilha()
pidaux = Pilha()
ptipaux = Pilha()
pilhav1 = Pilha()
pilhaop = Pilha()
parser()
#arq._checkClosed() //windows
arq.closed # linux

