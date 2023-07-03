# Renomeador de Arquivos
  Programa desenvolvido para renomear screenshot's com base em uma informação presente na foto.

## Processo
  Inicialmente é setada a posição e as dimensões que as informaçoes que se encontram (nesse caso, elas sempre aparecem no mesmo local).
  Com essa informação em mãos é realizada um recorte da imagem original e esse recorte passa pelo pytesseract, que recolhe qualquer texto presente dessa imagem. (A etapa do recorte foi realizada com o objetivo de diminuir o tempo de operação do programa, visto que o pytesseract tem que analizar apenas uma fração do todo.
  Em seguida a imagem original é renomeada e o recorte é apagado.
