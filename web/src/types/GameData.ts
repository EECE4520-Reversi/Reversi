export type GameData = {
  id: string;
  board: number[];
  state: number;
  winner: number;
  size: number;
  score: number[];
  difficulty: 0 | 1 | 2;
  type: 1 | 2 | 3;
};
