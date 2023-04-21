import { GameType, Difficulty } from "./Enums";

export type LoadableGame = {
    id: string;
    type: GameType;
    players: Array<String>;
    size: number;
    status: Boolean;
    difficulty: Difficulty;
};
