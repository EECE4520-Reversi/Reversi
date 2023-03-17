import { AxiosError } from "axios";
import { useEffect, useState } from "react";
import { makeMove } from "../services/backendservice";
import { GameData } from "../types/GameData";

export const GamePiece = ({
  state,
  idx,
  gameState,
  boardId,
  updateBoard,
}: {
  state: number;
  idx: number;
  gameState: number;
  boardId: string;
  updateBoard: (data: GameData) => void;
}) => {
  /*
    #   0 if empty
    #   1 if white
    #   2 if black
    #   3 is a viable Move
    */

  const colors = ["bg-transparent", "bg-white", "bg-black"];
  const [colorState, setColorState] = useState(state);
  const [lastColorState, setLastColorState] = useState<number | undefined>();
  const [angle, setAngle] = useState<number>(0);

  const delay = (ms: number) => new Promise(res => setTimeout(res, ms));

  const onClick = async () => {
    if (state !== 3) return;

    const data = await makeMove(idx, boardId)
    updateBoard(data[0])
    await delay(1000);
    updateBoard(data[1])
    
  };

  useEffect(() => {
    setLastColorState(colorState);
    setColorState(state);
    setAngle(angle == 0 ? 180 : 0);
  }, [state]);

  let outerStyle;
  let innerStyle;
  // If we were just selected
  if (lastColorState === 3 && colorState !== 3) {
    outerStyle = "picked";
    innerStyle = colors[colorState]; // Remove delay for new piece
  } else if (colorState !== 3) {
    // Normal piece
    outerStyle = `rotate-x-${angle}`;
    innerStyle = "delay-300 " + colors[colorState];
  } else {
    // Pickable piece
    outerStyle = `pickable`;
    innerStyle = "pickable-inner ";
    innerStyle += gameState === 1 ? "hover:bg-white" : "hover:bg-black";
  }

  return (
    <div className="border-gray-400 border-2 p-1">
      <div className={outerStyle} onClick={onClick}>
        <div className={`${innerStyle} rounded-full w-12 h-12`} />
      </div>
    </div>
  );
};
