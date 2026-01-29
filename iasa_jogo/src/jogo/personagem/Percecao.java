package src.jogo.personagem;

import src.jogo.ambiente.Evento;

/**
 * !Ultima edição: 8/03/2022
 * Esta classe, quando cirada (no método da Classe Personagem, percecionar()), recebe um evento do ambiente.
 * Com os dados desta classe, vai ser criada uma ação para a Personagem atuar
 * 
 */
public class Percecao {
    private Evento evento;

    /**
     * No construto desta classe, é recebido o evento do ambiente,
     * este armazenarse-á numa variável global.
     * @param evento
     */
    public Percecao(Evento evento) {
        this.evento = evento;
    }

    /**
     * Retorna o evento captado do ambiente.
     * @return
     */
    public Evento getEvento(){
        return evento;
    }

}
