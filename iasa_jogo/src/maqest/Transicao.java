package src.maqest;

/**
 * !Ultima edição: 15/03/2022
 * Classe que reresenta as transiçoes de estados, estas transiçoes,
 * são a mudança do estado atual para um estado e accao seguinte.
 *  É um genérico que no trabalho de IASA depende das classe Evento e Accao. 
 * Esta classe depende de acoes e estados.
 * 
 */
public class Transicao<EV, AC> {
    private Estado<EV, AC> estadoSucessor;
    private AC accao;

    // método que devolve o estado seguinte que a transiçao provoca
    public Estado<EV, AC> getEstadoSucessor() {
        return this.estadoSucessor;
    }

    // método que devolve a açao da transiçao
    public AC getAccao() {
        return this.accao;
    }
    /**
     * Neste construtor, atribui o estado seguinte e a açao
     *  */
    public Transicao(Estado<EV, AC> estadoSucessor, AC accao) {
        this.estadoSucessor = estadoSucessor;
        this.accao = accao;
    }


    
}
