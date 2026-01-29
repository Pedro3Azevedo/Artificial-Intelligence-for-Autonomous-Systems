package src.maqest;
/**
 * !Ultima edição: 15/03/2022
 * A classe MaquinaEstados faz parte da biblioteca maqest
 * (Maquina de Estado), onde esta biblioteca representa um
 *  modelo de Dinâmica de um sistema. A dinâmica é expressa
 * como uma funçao de ranformaçao que, perante estado atual e
 * as entradas atuais, altera para o estado e as saídas seguintes.
 * 
 * A classe MaquinaEstados, neste caso é um genérico, que, no caso do trabalho de IASA,
 * a maquina de estados contêm eventos e accoes. 
 * Esta classe é composta pela classe Estado.
 */
public class MaquinaEstados<EV, AC> {

    public Estado<EV, AC> estadoAtual;
    
    /**
     * Quando se é instanciada uma MaquinaEstados, é necessario
     * fornecer o estado em que se encontra, para que, dependento
     * do evento que vai ocurrer, possa transitar de estado e efetuar
     * uma açao.
     * @param estado
     */
    public MaquinaEstados(Estado<EV, AC> estado) {
        this.estadoAtual = estado;
    }
    
    /**
     * metodo que retorna o estado atual do sistema
     * @return estadoAtual
     */
    public Estado<EV, AC> getEstado() {
        return estadoAtual;
    }

    /**
     * O metodo processar(), vai receber um evento, ou seja algo que
     * que acontecer que tem influencia no sistema, e com esse dado,
     * vai haver uma transação.
     * É portanto, criada uma transicao, onde, com o estado atual e 
     * com o evento decorrido, é processado e gerado apartir de um dicionario
     * (Map, denominado por transicoes). Aqui esta presente as possibilidades de
     * transação dependendo do estado e do evento.
     * Por fim, caso haja alguma transacao, o estad atual altera, e é returnada
     * a açao que a personagem vai atuar.
     * @param evento
     * @return accao da transicao
     */
    public AC processar(EV evento){
        Transicao<EV, AC> transicao = estadoAtual.processar(evento);
        if(transicao != null){
            estadoAtual = transicao.getEstadoSucessor();
            return transicao.getAccao();
        }
        return null;
    }
}
