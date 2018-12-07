# Quantidade de repeticoes desejada
NUM_REPETICOES=50
RANDOM=12833
PORCENTAGEM=60
INSTANCIA=("hamming-10-4" "vc4")
TAMANHO=${#INSTANCIA[@]}
for ((i=0;i<$TAMANHO;i++))
do
    CONTADOR=0
    # Executa a aplicacao a quantidade de repeticoes especificada
    until [ $CONTADOR -ge $NUM_REPETICOES ];
    do
    echo "Execucao No. $CONTADOR do arquivo ${INSTANCIA[$i]}"
    echo
    python main.py $RANDOM $PORCENTAGEM g "${INSTANCIA[$i]}.txt" "resultado-${INSTANCIA[$i]}"
    # Incrementa o contador
    let CONTADOR=CONTADOR+1
    done
done
for ((i=0;i<$TAMANHO;i++))
do
    CONTADOR=0
    # Executa a aplicacao a quantidade de repeticoes especificada
    until [ $CONTADOR -ge $NUM_REPETICOES ];
    do
    echo "Execucao No. $CONTADOR do arquivo ${INSTANCIA[$i]}"
    echo
    python main.py $RANDOM $PORCENTAGEM a "${INSTANCIA[$i]}.txt" "resultado-${INSTANCIA[$i]}"
    # Incrementa o contador
    let CONTADOR=CONTADOR+1
    done
done
