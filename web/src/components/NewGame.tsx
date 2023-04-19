import { Dispatch, SetStateAction, useState } from "react";
import { Difficulty, GameState, GameType } from "../types/Enums";
import { GameData } from "../types/GameData";
import Modal from "./Modal";
import socket from "../services/websocket";
import { useNavigate } from "react-router";

const capitalize = (str: string) => {
  return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
};

const NewGame = ({
  gameData,
  setBoardID,
}: {
  gameData: GameData | undefined;
  setBoardID: Dispatch<SetStateAction<string>>;
}) => {
  const [visible, setVisible] = useState<boolean>(false);
  const [boardSize, setBoardSize] = useState<number>(gameData?.size || 8);
  const [difficulty, setDifficulty] = useState<Difficulty>(
    gameData ? gameData.difficulty : Difficulty.MEDIUM
  );
  const [gamemode, setGameMode] = useState<GameType>(
    gameData?.type || GameType.AI
  );
  const navigate = useNavigate();

  const onSubmit = () => {
    socket.emit(
      "createGame",
      boardSize,
      difficulty,
      gamemode,
      (boardId: string) => {
        setBoardID(boardId);
        console.log(`New Game: ${boardId}`);
        navigate("/game");
      }
    );
  };

  const newGameComponents = (
    <div>
      <div className="m-1">
        <h2 className="inline p-2 text-xl">Board Size:</h2>
        <input
          type="number"
          className="rounded w-10 text-black px-2"
          onChange={(event) => setBoardSize(parseInt(event?.target.value))}
          value={boardSize}
        />
      </div>
      <div className="mt-3">
        <h2 className="inline p-2 text-xl">Difficulty:</h2>
        <div className="flex justify-between space-x-5">
          {[Difficulty.EASY, Difficulty.MEDIUM, Difficulty.HARD].map((val) => {
            return (
              <div
                className="flex items-center"
                onClick={() => setDifficulty(val)}
                key={val}
              >
                <input
                  defaultChecked={difficulty === val}
                  id={`difficulty-radio-${val}`}
                  type="radio"
                  name="difficult-radio"
                  className="w-4 h-4 focus:ring-gray-600 ring-offset-gray-800 focus:ring-2 bg-gray-700 border-gray-600"
                />
                <label
                  htmlFor={`difficulty-radio-${val}`}
                  className="font-medium"
                >
                  {capitalize(Difficulty[val])}
                </label>
              </div>
            );
          })}
        </div>
      </div>
      <div className="mt-3">
        <h2 className="inline p-2 text-xl">Gamemode:</h2>
        <div className="flex justify-between space-x-5">
          {[GameType.LOCAL, GameType.AI, GameType.ONLINE].map((val) => {
            return (
              <div
                className="flex items-center"
                onClick={() => setGameMode(val)}
                key={val}
              >
                <input
                  defaultChecked={gamemode === val}
                  id={`gamemode-radio-${val}`}
                  type="radio"
                  name="gamemode-radio"
                  className="w-4 h-4 focus:ring-gray-600 ring-offset-gray-800 focus:ring-2 bg-gray-700 border-gray-600"
                />
                <label
                  htmlFor={`gamemode-radio-${val}`}
                  className="font-medium"
                >
                  {capitalize(GameType[val])}
                </label>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );

  return (
    <>
      <button
        onClick={() => setVisible(true)}
        className="text-4xl w-1/2 btn-primary"
      >
        Create Game
      </button>

      <Modal
        onSubmit={onSubmit}
        visible={visible}
        setVisibility={setVisible}
        title="New Game"
        submitText="Create"
        component={newGameComponents}
      />
    </>
  );
};

export default NewGame;
