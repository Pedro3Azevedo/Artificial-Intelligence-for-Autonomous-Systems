package src.maqest;

import java.util.Map;
import java.util.HashMap;

/**
 * !Ultima edição: 15/03/2022
 * A classe Estado, consiste nos Estados que uma maquina de estados
 * pode ter. Esta classe compões a classe MaquinaEstados, e é composta pela classse Transicao.
 * Esta classe é um genérico que, no caso do trabalho de IASA, vai depender de eventos e accoes.
 * A classe Estado é cnstituida por um nome e por um gupo de transiçoes.
 */
public class Estado<EV, AC>{
    private String nome;
    private Map<EV, Transicao<EV, AC>> transicoes;

    /**
     * A classe contrutor vai atribuir o nome do estado que é 
     * fornecido ao instanciar a classe. É iniciaizado o map de transiçoes,
     * que é um dicionario das tranciçoes que o estado pode conter. Este map é composto,
     * no caso do projeto de IASA, por Eventos e transiçoes. Dependendo do Evento que houve,
     * haverá uma certa transiçao
     * @param nome
     */
    public Estado(String nome){
        this.nome = nome;
        this.transicoes = new HashMap<>();
    }

    /**
     * Função que retorna o nome do estado
     * @return
     */
    public String getNome(){
        return this.nome;
    }

    /**
     * Neste método, vai se ao dicionário(map) das transiçoes, e apartir do 
     * evento que ocurreu (fornecido ao chamar a funçao), consegue se ver qual 
     * a transiçao a fazer, returnando a mesma.
     * @param evento
     * @return transiçao do envento recebido
     */
    public Transicao<EV, AC> processar(EV evento){
        return transicoes.get(evento);
    }

   /**
    * Chama a funçao a baixo para efetuar o mesmo, isto para transiçoes sem accao
    * @param evento
    * @param estadoSucessor
    * @return
    */
    public Estado<EV, AC> transicao(EV evento, Estado<EV, AC> estadoSucessor){
        return transicao(evento, estadoSucessor, null);
    }

    /**
     * Neste método é criado as transiçoes que são adicionadas ao dicionario de transiçoes
     * apartir do evento, do estado e da accao recebida. É returnado esta Estado(this).
     * @param evento
     * @param estadoSucessor
     * @param accao
     * @return
     */
    public Estado<EV, AC> transicao(EV evento, Estado<EV, AC> estadoSucessor, AC accao){
        transicoes.put(evento, new Transicao<EV, AC>(estadoSucessor, accao));
        return this;
    }

}