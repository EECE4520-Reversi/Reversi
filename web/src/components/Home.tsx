import { Dispatch, SetStateAction } from "react";
import { GameData } from "../types/GameData";
import NewGame from "./NewGame";
import JoinGame from "./JoinGame";
import LoadGame from "./LoadGame";
import { GameState } from "../types/Enums";

const Home = ({
  gameData,
  setBoardID,
  setPlayerNum
}: {
  gameData: GameData | undefined;
  setBoardID: Dispatch<SetStateAction<string>>;
  setPlayerNum: Dispatch<SetStateAction<GameState>>;
}) => {
  return (
    <div className="flex justify-center items-center h-[85%]">
      <div className="grid grid-cols-3 w-1/2 gap-10">
        <h1 className="col-span-3 text-9xl font-bold">Reversi</h1>

        <div className="col-span-3 gap-5 flex">
          <NewGame gameData={gameData} setBoardID={setBoardID} setPlayerNum={setPlayerNum} />
          <LoadGame setBoardID={setBoardID} />
          <JoinGame setBoardID={setBoardID} setPlayerNum={setPlayerNum} />
        </div>
      </div>
    </div>
  );
};

export default Home;
