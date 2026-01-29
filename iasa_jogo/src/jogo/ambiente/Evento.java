package src.jogo.ambiente;

/**
 * !Ultima edição: 8/03/2022
 * Este enumerado, contêm os eventos possiveis de acontecerem no ambienre,
 * quando o jogo é executado.
 */
public enum Evento {
    SILENCIO, // evento em que nenhum animal faz barulho
    RUIDO, // evento onde um animal faz barulho
    ANIMAL, // evento onde se vê um animal
    FUGA, // evento em que o animal foge
    FOTOGRAFIA, // evento em que a personagem esta a registar o animal
    TERMINAR // evento para terminar o jogo
}
