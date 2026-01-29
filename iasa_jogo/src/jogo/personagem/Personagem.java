package src.jogo.personagem;

import src.jogo.ambiente.Ambiente;
import src.jogo.ambiente.Evento;

/**
 * !Ultima edição: 15/03/2022
 * A classe Personagem tem duas funções, Percecionar e atuar.
 * A personagem vai estar atenta ao Ambiente e ver os eventos para depois 
 * realizar uma ação.
 * Esta classe, compoem a classe Jogo, ou seja, é criada uma nova instancia na classe.
 * A Personagem é composta po um controlo que terá a função de processar o que a personagem
 * prececionou, e atraves de uma máquina de estados, é alterado o estado atual. Ou seja,
 * quando acontece um Evento, a personagem vai percecionar, que consiste em ir á 
 * classe Controlo, onde aqui, vai se buscar o evento ocurrido para depois ser 
 * processado pela maquina de estados, que por sua vez, atraves do estado atual, e do evento
 * acederá a um dicionario(map), que indicara o estado seguinte e a ação da personagem a 
 * ser atuada.
 * 
 */
public class Personagem {
    private Controlo controlo = new Controlo(); //É criado um controlo que tem a funçao de processar os eventos
    private Ambiente ambiente;

    /**
     * Ao ser instanciada uma nova Peronagem,
     * é necessario fornecer o Ambiente que compõe o Jogo.
     * Este será armazenado numa variável global.
     * @param ambiente
     */
    public Personagem(Ambiente ambiente) {
        this.ambiente = ambiente;
    }

    /**
     * A Personagem vai percecionar o ambiente,
     * com os dados recebidos irá processa-los,
     * e por fim vai atuar.
     * Ou seja, neste método, chama se o método percecionar(),
     * para guardar o evento do ambiente, para depois ser criada uma ação,
     * este criada apartir da classe Controlo.
     * Por fim, é executada a ação.
     */
    public void executar(){
        Percecao percecao = percecionar();
        Accao accao = controlo.processar(percecao);
        atuar(accao);
    }

    /**
     * Quando se chama o método executar(), este irá 
     * prececionar(), ou seja, vai à classe ambiente 
     * recolher o evento em que este se encontra.
     * É portanto, criado uma perceçao devolvendo ao método 
     * anterior, para depois ir á classe Controlo para ser 
     * Processada, criando por sua vez uma ação para a Personagem
     * Executar.
     * @return Percecao
     */
    public Percecao percecionar(){
        Evento evento = ambiente.getEvento();
        Percecao percecao = new Percecao(evento);
        return percecao;
    }

    /**
     * Neste método, é recebida uma ação e esta é atuada.
     * @param accao
     */
    public void atuar(Accao accao){
        if(accao != null){
            System.out.printf("Açao: %s\na", accao);
        }
    }
}
