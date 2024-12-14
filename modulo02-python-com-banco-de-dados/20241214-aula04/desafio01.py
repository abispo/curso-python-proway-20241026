"""
Desafio 01 - Implementar um sistema de leitura e de alarme

1. Você deve implementar uma classe que representa um sensor de gás. A cada vez que esse sensor é lido, ele gera um valor. Esse valor é lido a partir do método ler(). Esse valor será um valor randômico entre 0 e 100. O valor inicial do sensor será de 0. BONUS: O valor lido não pode estar fora da faixa entre +5 e menos -5. Exemplo. Se o valor lido anteriormente foi de 60, o novo valor do sensor deve ficar entre 55 e 65. O sensor não deve retornar números negativos, o número mais baixo é 0.

2. Você deve implementar uma classe que irá representar um alarme. Essa classe terá um estado que representa o alarme ligado ou desligado, e 2 métodos: ligar e desligar. Esses métodos irão alterar o valor desse atributo.

3. Você deve implementar uma classe que irá representar um circuito de leitura desse sensor. Esse leitor irá consultar a cada segundo o sensor, ou seja, essa classe terá um método chamado checar, que irá fazer a checagem. Caso o valor lido do sensor seja maior ou igual a 80, esse leitor irá chamar o método para ligar o alarme. Mesmo com o alarme ligado, o leitor irá continuar a ler os dados do sensor. Caso esse valor lido do sensor seja menor que 80, o alarme deve ser desligado.
"""