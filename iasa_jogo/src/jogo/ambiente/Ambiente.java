package src.jogo.ambiente;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/**
 * !Ultima edição: 15/03/2022
 * Esta classe consiste no Ambiente de jogo, local onde se vai passar o mesmo,
 * este vai alternado entre eventos que defenirão o percurso do jogo.
 * 
 * É criada um nova instância desta classe na classe Jogo, fanzendo parte da sua
 * composição.
 * Esta classe, depende do enumerado Evento.
 * 
 */
public class Ambiente {

    private Scanner sc = new Scanner(System.in);
    private Evento evento;
    private Map<String, Evento> eventos;

    /**
     * 
     * No construro do ambiente inicializamos o "dicionario", atraves de um HashMap.
     * De seguida é adicionao elementos ao dicionario. Estes elementos vao ser os comandos
     * que vão ser introduzidos que vão corresponder ao eventos do ambiente.
     * Para tal, correspondeu os comandos ao primeiro caracter de cada evento,
     * com ecxeção do evento Fotografia que foi usado o caracter 'o'
     */
    public Ambiente() {
        eventos = new HashMap<>();
        eventos.put("s", Evento.SILENCIO);
        eventos.put("r", Evento.RUIDO);
        eventos.put("a", Evento.ANIMAL);
        eventos.put("f", Evento.FUGA);
        eventos.put("o", Evento.FOTOGRAFIA);
        eventos.put("t", Evento.TERMINAR);
    }

    /**
     * metodo que retorna o evento em que o ambiente se encontra.
     * 
     * @return evento
     */
    public Evento getEvento() {
        return evento;
    }

    /**
     * É neste método que é feita uma evolução do ambiente,
     * gerando um novo Evento e de seguida mostrar-lo.
     * Este evento gerado, vai ser guardado numa variável global desta classe,
     * onde a classe Personagem poderá aceder.
     */
    public void evoluir() {
        evento = gerarEvento();
        mostarEvento();
    }

    /**
     * 
     * Nese método é pedido para introduzir um comando, que corresponde a um evento.
     * Depois de ser introduzido um comando (o seja, um caracter), vai se ao Map eventos,
     * ver a que evento corresponde.
     * 
     * @return Evento
     */
    private Evento gerarEvento() {
        String s = "Selecione um Evento:\n's' - Silencio\n" +
        "'r' - Ruido\n'a' - Animal\n'f' - Fuga\n'o' - Fotografia\n" +
        "'t' - Terminaria\n ";
        System.out.println(s + "->");
        String comando = sc.next();
        return eventos.get(comando);
    }

    private void mostarEvento() {
        System.out.printf("Evento; %s\n", evento);
    }

}
