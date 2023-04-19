import { useEffect, useState } from "react";
import { GameState, GameType, TileState } from "../types/Enums";
import { GameData } from "../types/GameData";
import socket from "../services/websocket";
import { UserData } from "../types/UserData";

export const GamePiece = ({
  state,
  idx,
  gameData,
  player1Color,
  player2Color,
<<<<<<< HEAD
  userData,
=======
>>>>>>> 40bf264c4db7b2710872012bc1f659e17a41fd14
}: {
  state: TileState;
  idx: number;
  gameData: GameData;
  player1Color: string;
  player2Color: string;
<<<<<<< HEAD
  userData: UserData | undefined;
=======
>>>>>>> 40bf264c4db7b2710872012bc1f659e17a41fd14
}) => {
  /*
    #   0 if empty
    #   1 if white
    #   2 if black
    #   3 is a viable Move
    */

  const colors = ["transparent", player1Color, player2Color];
  const [colorState, setColorState] = useState<TileState>(state);
  const [lastColorState, setLastColorState] = useState<TileState | undefined>();
  const [angle, setAngle] = useState<number>(0);

  const delay = (ms: number) => new Promise((res) => setTimeout(res, ms));

  const onClick = async () => {
    if (state !== TileState.VIABLE) return;

    socket.emit("makeMove", gameData.id, idx);
  };

  useEffect(() => {
    setLastColorState(colorState);
    setColorState(state);
    setAngle(angle == 0 ? 180 : 0);
  }, [state]);

  let outerStyle;
  let innerStyle;
  let style = {};
  // If we were just selected
  if (lastColorState === TileState.VIABLE && colorState !== TileState.VIABLE) {
    outerStyle = "picked";
    style = { backgroundColor: colors[colorState] }; // Remove delay for new piece
  } else if (colorState !== TileState.VIABLE) {
    // Normal piece
    outerStyle = `rotate-x-${angle}`;
    innerStyle = "delay-300 ";
    style = { backgroundColor: colors[colorState] };
  } else if (
    gameData.type == GameType.LOCAL ||
    (gameData.type == GameType.AI && gameData.state != GameState.PLAYER2) ||
<<<<<<< HEAD
    (gameData.type == GameType.ONLINE &&
      userData?.username === gameData.currentTurn)
=======
    gameData.type == GameType.ONLINE // TODO: Add condition to show pickable pieces if its our turn currently
>>>>>>> 40bf264c4db7b2710872012bc1f659e17a41fd14
  ) {
    // Hide picks if vs AI and its AI turn
    // Pickable piece
    outerStyle = `pickable`;
    innerStyle = "pickable-inner ";
    innerStyle +=
      gameData.state === GameState.PLAYER1
        ? "hover:bg-white"
        : "hover:bg-black";
    style = {};
  }

  return (
    <div className="border-gray-400 border-2 p-1">
      <div className={outerStyle} onClick={onClick}>
        <div
          className={`${innerStyle} rounded-full w-12 h-12`}
          style={{ backgroundColor: colors[colorState] }}
        ></div>
      </div>
    </div>
  );
};
