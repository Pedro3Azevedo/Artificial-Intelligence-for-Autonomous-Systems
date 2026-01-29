package src.jogo.personagem;

import src.jogo.ambiente.Evento;
import src.maqest.*;

/**
 * !Ultima edição: 15/03/2022
 * Esta classe, compõem uma personagem com a função de processar uma perceção e
 * criar uma ação. Esta classe depende do enumerado Ação e da classe Perceção.
 * Esta classe, vai controlar o estados e accoes da personagem, sendo que
 * quando a personagem vai processar, o controlo vai recolher o evento ocurrido,
 * de seguida processa esse evento e mostra a ação concecuente do processamento.
 */
public class Controlo {

    private MaquinaEstados<Evento, Accao> maqEst;

    public Estado getEstado() {
        return maqEst.getEstado();
    }

    /**
     * Neste construtor da classe, é criado os estados existentes,
     * de seguida, para cada estado é criada as transiçoes, o dicionario.
     * Uma transiçao é composta por um evento ocurrido, do estado seguinte
     * e uma accao.
     */
    public Controlo() {
        Estado<Evento, Accao> procura = new Estado<>("Procura");
        Estado<Evento, Accao> inspecao = new Estado<>("Inspecao");
        Estado<Evento, Accao> observacao = new Estado<>("Observacao");
        Estado<Evento, Accao> registo = new Estado<>("Registo");
       
        procura
            .transicao(Evento.RUIDO, inspecao, Accao.APROXIMAR)
            .transicao(Evento.SILENCIO, procura, Accao.PROCURAR)
            .transicao(Evento.ANIMAL, observacao, Accao.APROXIMAR);
        inspecao
            .transicao(Evento.ANIMAL, observacao, Accao.APROXIMAR)
            .transicao(Evento.RUIDO, inspecao, Accao.PROCURAR)
            .transicao(Evento.SILENCIO, procura);
        observacao
            .transicao(Evento.ANIMAL, registo, Accao.OBSERVAR)
            .transicao(Evento.FUGA, inspecao);
        registo
            .transicao(Evento.FUGA, procura)
            .transicao(Evento.FOTOGRAFIA, procura)
            .transicao(Evento.ANIMAL, registo, Accao.FOTOGRAFAR);

        maqEst = new MaquinaEstados<>(procura);
    }

    
    /**
     * Neste método, vai se á classe da perceção recolher o evento ocurrido
     * para que, atraves da maquina de estados e desse evento, se processe
     * uma accao, que será mostrada na classe mostrar().
     * @param percecao
     * @return
     */
    public Accao processar(Percecao percecao) {
        Evento evento = percecao.getEvento();
        Accao accao = maqEst.processar(evento);
        mostrar();
        return accao;
    }
    private void mostrar() {
        System.out.printf("Estado: %s\n", getEstado().getNome());
      }


   






}
