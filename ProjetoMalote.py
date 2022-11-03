arq = open('maloteprotocolo.csv','a')
while True:
    rem=input('Digite o Remetente (0 p/sair): ')
    if rem=='0':
        break
    dest=input('Digite o destinatário: ')
    doc=input('Digite o Documento: ')
    ent=input('Digite aqui a data de entrada do documento:' )
    arq.write(rem+';'+dest+';'+doc+';'+ent+'\n')
arq.close()
