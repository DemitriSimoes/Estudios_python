#%%
#PROGRAMA SORVETERIA
#tipo de sorvete
casquinha = 1.00
cascao = 2.50
cestinha = 4.00

#sabor do sorvete
s_morango = 'morango'
s_creme = 'creme'
s_chocolate = 'chocolate'

#cobertura
c_caramelo = 1.50
c_morango = 1.50
c_chocolate = 1.50
sem_cobertura = 0.00

#mensagens
mensagem_tipo = '\nFaça a sua escolha do tipo de sorvete\n 1. casquinha\n 2. cascao\n 3. cestinha\n Digite seu número: '
mensagem_sabor = '\nFaça a sua escolha o sabor do sorvete\n 1. morango\n 2. creme\n 3. chocolate\n Digite seu número: '
mensagem_cobertura = '''\nFaça a escolha da cobertura
1. cobertura de morango
2. cobertura de creme
3. cobertura de chocolate
4. sem cobertura
Digite seu número: '''
tipo_sorvete = input(mensagem_tipo)
sabor_sorvete = input(mensagem_sabor)
cobertura_sorvete = input(mensagem_cobertura)

if tipo_sorvete == '1' and sabor_sorvete == '1' and cobertura_sorvete == '1':
    print('\n>>Casquinha de', s_morango, ', cobertura de caramelo', ', total a pagar: $', casquinha+c_caramelo )
elif tipo_sorvete =='1' and sabor_sorvete == '1' and cobertura_sorvete =='2':
    print('\n>>Casquinha de', s_morango, ', cobertura de morango', ', total a pagar: $', casquinha+c_morango )
elif tipo_sorvete == '1' and sabor_sorvete == '1' and cobertura_sorvete == '3':
    print('\n>>Casquinha de', s_morango, ', cobertura de chocolate', ', total a pagar: $', casquinha+c_chocolate )
elif tipo_sorvete == '1' and sabor_sorvete == '1' and cobertura_sorvete == '4':
    print('\n>>Casquinha de', s_morango, ', sem cobertura', ', total a pagar: $', casquinha+sem_cobertura )

elif tipo_sorvete == '1' and sabor_sorvete == '2' and cobertura_sorvete == '1':
    print('\n>>Casquinha de', s_creme, ', cobertura de caramelo', ', total a pagar: $', casquinha+c_caramelo )
elif tipo_sorvete == '1' and sabor_sorvete == '2' and cobertura_sorvete == '2':
    print('\n>>Casquinha de', s_creme, ', cobertura de morango', ', total a pagar: $', casquinha+c_morango )
elif tipo_sorvete == '1' and sabor_sorvete == '2' and cobertura_sorvete == '3':
    print('\n>>Casquinha de', s_creme, ', cobertura de chocolate', ', total a pagar: $', casquinha+c_chocolate )
elif tipo_sorvete == '1' and sabor_sorvete == '2' and cobertura_sorvete == '4':
    print('\n>>Casquinha de', s_creme, ', sem cobertura', ', total a pagar: $', casquinha+sem_cobertura )

elif tipo_sorvete == '1' and sabor_sorvete == '3' and cobertura_sorvete == '1':
    print('\n>>Casquinha de', s_chocolate, ', cobertura de caramelo', ', total a pagar: $', casquinha+c_caramelo )
elif tipo_sorvete == '1' and sabor_sorvete == '3' and cobertura_sorvete == '2':
    print('\n>>Casquinha de', s_chocolate, ', cobertura de morango', ', total a pagar: $', casquinha+c_morango )
elif tipo_sorvete == '1' and sabor_sorvete == '3' and cobertura_sorvete == '3':
    print('\n>>Casquinha de', s_chocolate, ', cobertura de chocolate', ', total a pagar: $', casquinha+c_chocolate )
elif tipo_sorvete == '1' and sabor_sorvete == '3' and cobertura_sorvete == '4':
    print('\n>>Casquinha de', s_chocolate, ', sem cobertura', ', total a pagar: $', casquinha+sem_cobertura )

elif tipo_sorvete =='2' and sabor_sorvete == '1' and cobertura_sorvete =='1':
    print('\n>>Cascao de', s_morango, ', cobeertura de caramelo', ', total a pagar: $', cascao+c_caramelo)
elif tipo_sorvete =='2' and sabor_sorvete == '1' and cobertura_sorvete =='2':
    print('\n>>Cascao de', s_morango, ', cobeertura de morango', ', total a pagar: $', cascao+c_morango)
elif tipo_sorvete =='2' and sabor_sorvete == '1' and cobertura_sorvete =='3':
    print('\n>>Cascao de', s_morango, ', cobeertura de chocolate', ', total a pagar: $', cascao+c_chocolate)
elif tipo_sorvete =='2' and sabor_sorvete == '1' and cobertura_sorvete =='4':
    print('\n>>Cascao de', s_morango, ', sem cobertura', ', total a pagar: $', cascao+sem_cobertura)

elif tipo_sorvete =='2' and sabor_sorvete == '2' and cobertura_sorvete =='1':
    print('\n>>Cascao de', s_creme, ', cobeertura de caramelo', ', total a pagar: $', cascao+c_caramelo)
elif tipo_sorvete =='2' and sabor_sorvete == '2' and cobertura_sorvete =='2':
    print('\n>>Cascao de', s_creme, ', cobeertura de morango', ', total a pagar: $', cascao+c_morango)
elif tipo_sorvete =='2' and sabor_sorvete == '2' and cobertura_sorvete =='3':
    print('\n>>Cascao de', s_creme, ', cobeertura de chocolate', ', total a pagar: $', cascao+c_chocolate)
elif tipo_sorvete =='2' and sabor_sorvete == '2' and cobertura_sorvete =='4':
    print('\n>>Cascao de', s_creme, ', sem cobertura', ', total a pagar: $', cascao+sem_cobertura)

elif tipo_sorvete =='2' and sabor_sorvete == '3' and cobertura_sorvete =='1':
    print('\n>>Cascao de', s_chocolate, ', cobeertura de caramelo', ', total a pagar: $', cascao+c_caramelo)
elif tipo_sorvete =='2' and sabor_sorvete == '3' and cobertura_sorvete =='2':
    print('\n>>Cascao de', s_chocolate, ', cobeertura de morango', ', total a pagar: $', cascao+c_morango)
elif tipo_sorvete =='2' and sabor_sorvete == '3' and cobertura_sorvete =='3':
    print('\n>>Cascao de', s_chocolate, ', cobeertura de chocolate', ', total a pagar: $', cascao+c_chocolate)
elif tipo_sorvete =='2' and sabor_sorvete == '3' and cobertura_sorvete =='4':
    print('\n>>Cascao de', s_chocolate, ', sem cobertura', ', total a pagar: $', cascao+sem_cobertura)

elif tipo_sorvete =='3' and sabor_sorvete =='1' and cobertura_sorvete == '1':
    print('\n>>Cestinha de', s_morango, ', cobertura de caramelo', ', total a pagar: $', cestinha+c_caramelo)
elif tipo_sorvete =='3' and sabor_sorvete =='1' and cobertura_sorvete == '2':
    print('\n>>Cestinha de', s_morango, ', cobertura de morango', ', total a pagar: $', cestinha+c_morango)
elif tipo_sorvete =='3' and sabor_sorvete =='1' and cobertura_sorvete == '3':
    print('\n>>Cestinha de', s_morango, ', cobertura de chocolate', ', total a pagar: $', cestinha+c_chocolate)
elif tipo_sorvete =='3' and sabor_sorvete =='1' and cobertura_sorvete == '4':
    print('\n>>Cestinha de', s_morango, ', sem cobertura', ', total a pagar: $', cestinha+sem_cobertura)

elif tipo_sorvete =='3' and sabor_sorvete =='2' and cobertura_sorvete == '1':
    print('\n>>Cestinha de', s_creme, ', cobertura de caramelo', ', total a pagar: $', cestinha+c_caramelo)
elif tipo_sorvete =='3' and sabor_sorvete =='2' and cobertura_sorvete == '2':
    print('\n>>Cestinha de', s_creme, ', cobertura de morango', ', total a pagar: $', cestinha+c_morango)
elif tipo_sorvete =='3' and sabor_sorvete =='2' and cobertura_sorvete == '3':
    print('\n>>Cestinha de', s_creme, ', cobertura de chocolate', ', total a pagar: $', cestinha+c_chocolate)
elif tipo_sorvete =='3' and sabor_sorvete =='2' and cobertura_sorvete == '4':
    print('\n>>Cestinha de', s_creme, ', sem cobertura', ', total a pagar: $', cestinha+sem_cobertura)

elif tipo_sorvete =='3' and sabor_sorvete =='3' and cobertura_sorvete == '1':
    print('\n>>Cestinha de', s_chocolate, ', cobertura de caramelo', ', total a pagar: $', cestinha+c_caramelo)
elif tipo_sorvete =='3' and sabor_sorvete =='3' and cobertura_sorvete == '2':
    print('\n>>Cestinha de', s_chocolate, ', cobertura de morango', ', total a pagar: $', cestinha+c_morango)
elif tipo_sorvete =='3' and sabor_sorvete =='3' and cobertura_sorvete == '3':
    print('\n>>Cestinha de', s_chocolate, ', cobertura de chocolate', ', total a pagar: $', cestinha+c_chocolate)
elif tipo_sorvete =='3' and sabor_sorvete =='3' and cobertura_sorvete == '4':
    print('\n>>Cestinha de', s_chocolate, ', sem cobertura', ', total a pagar: $', cestinha+sem_cobertura)
else:
    print('\nEscolha um número válido\n tente novamente...\n')