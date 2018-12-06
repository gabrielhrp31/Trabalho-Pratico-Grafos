# Quantidade de repeticoes desejada
NUM_REPETICOES=50
RANDOM=12833
PORCENTAGEM=80
INSTANCIA=graph250-01
# Reseta o contador inicial
CONTADOR=0
# Executa a aplicacao a quantidade de repeticoes especificada
until [ $CONTADOR -ge $NUM_REPETICOES ];
do
echo "Execucao No. $CONTADOR"
echo
python main.py $RANDOM $PORCENTAGEM g "$INSTANCIA.txt" "resultado-$INSTANCIA" $CONTADOR
# Incrementa o contador
let CONTADOR=CONTADOR+1
done