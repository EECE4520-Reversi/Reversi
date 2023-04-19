import { GameType } from "./Enums";

export type LoadableGame = {
  id: string;
  player1: string;
  player2: string;
  size: number;
  state: boolean;
  type: GameType;
};
