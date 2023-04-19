import { GameType } from "./Enums";

export type LoadableGame = {
    id: string;
    type: GameType;
    player1: string;
    player2: string;
    size: number;
    status: boolean;
};
