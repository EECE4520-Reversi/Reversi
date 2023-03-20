import { Difficulty, GameState, GameType } from "./Enums";

export type GameData = {
  id: string;
  board: number[];
  state: GameState;
  winner: number;
  size: number;
  score: number[];
  difficulty: Difficulty;
  type: GameType;
};
