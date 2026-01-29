package src;

import src.jogo.ambiente.Ambiente;
import src.jogo.ambiente.Evento;
import src.jogo.personagem.Personagem;

/**
 * O Jogo consiste em numa personagem que está presete num certo ambiente. Aqui, a personagem,
 * pode procurar animais e fotografálos, sendo que haverá certos eventos que mudarão a dinâmica
 * do jogo, como por exempplo, o Ruido, Fuga etc.
 * * A classe jogo vai executar o jogo criando o ambiente, a personagem e vai de seguida
 * * executar o jogo. Ou seja, esta classe é composta por pelas classes Ambiente e Personagem 
 * 
 */

public class Jogo{
    private static Personagem personagem;
    private static Ambiente ambiente;

    /**
     * O método main(), é a função que vai construir o jogo, ou seja,
     * vai criar um novo ambiente e uma nova personagem, usando o novo ambiente.
     * Depois executará o jogo. 
     * @param args
     */
    public static void main(String[] args) {
        ambiente = new Ambiente();
        personagem = new Personagem(ambiente);
        executar();
    }

    /**
     * O método executar() vai, comoo próprio nome indica, executar o programa.
     * Aqui, é usado um loop onde é execuatado o comportamento da personagem,
     * e o ambiente evolui. Este loop acaba, ou seja, o jogo acaba,
     * quando o ambiente evoluir (mudar de evento) para o evento TERMINAR.
     */
    private static void executar() {
        do{
            personagem.executar();
            ambiente.evoluir();
        }while(ambiente.getEvento() != Evento.TERMINAR);
    }

    
}