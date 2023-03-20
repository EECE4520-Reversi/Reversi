import { Dispatch, SetStateAction, useState } from "react";
import { createGame } from "../services/backendservice";
import { GameData } from "../types/GameData";
import Modal from "./Modal";

const NewGame = ({
  setGameData,
  gameData,
}: {
  setGameData: Dispatch<SetStateAction<GameData | undefined>>;
  gameData: GameData;
}) => {
  const [visible, setVisible] = useState<boolean>(false);
  const [boardSize, setBoardSize] = useState<number>(gameData.size || 8);
  const [difficulty, setDifficulty] = useState<0 | 1 | 2>(
    gameData ? gameData.difficulty : 1
  );
  const [gamemode, setGameMode] = useState<1 | 2 | 3>(gameData.type || 2);

  const onSubmit = () => {
    createGame(boardSize, difficulty, gamemode).then((gameData) => {
      setGameData(gameData);
      setVisible(false);
    });
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
          <div className="flex items-center" onClick={() => setDifficulty(0)}>
            <input
              defaultChecked={difficulty === 0}
              id="difficulty-radio-1"
              type="radio"
              name="difficult-radio"
              className="w-4 h-4 focus:ring-gray-600 ring-offset-gray-800 focus:ring-2 bg-gray-700 border-gray-600"
            />
            <label htmlFor="difficulty-radio-1" className="font-medium">
              Easy
            </label>
          </div>
          <div className="flex items-center" onClick={() => setDifficulty(1)}>
            <input
              defaultChecked={difficulty === 1}
              id="difficulty-radio-2"
              type="radio"
              name="difficult-radio"
              className="w-4 h-4 focus:ring-gray-600 ring-offset-gray-800 focus:ring-2 bg-gray-700 border-gray-600"
            />
            <label htmlFor="difficulty-radio-2" className="font-medium">
              Medium
            </label>
          </div>
          <div className="flex items-center" onClick={() => setDifficulty(2)}>
            <input
              defaultChecked={difficulty === 2}
              id="difficulty-radio-3"
              type="radio"
              name="difficult-radio"
              className="w-4 h-4 focus:ring-gray-600 ring-offset-gray-800 focus:ring-2 bg-gray-700 border-gray-600"
            />
            <label htmlFor="difficulty-radio-3" className="font-medium">
              Hard
            </label>
          </div>
        </div>
      </div>
      <div className="mt-3">
        <h2 className="inline p-2 text-xl">Gamemode:</h2>
        <div className="flex justify-between space-x-5">
          <div className="flex items-center" onClick={() => setGameMode(1)}>
            <input
              defaultChecked={gamemode === 1}
              id="gamemode-radio-1"
              type="radio"
              name="gamemode-radio"
              className="w-4 h-4 focus:ring-gray-600 ring-offset-gray-800 focus:ring-2 bg-gray-700 border-gray-600"
            />
            <label htmlFor="gamemode-radio-1" className="font-medium">
              Local
            </label>
          </div>
          <div className="flex items-center" onClick={() => setGameMode(2)}>
            <input
              defaultChecked={gamemode === 2}
              id="gamemode-radio-2"
              type="radio"
              name="gamemode-radio"
              className="w-4 h-4 focus:ring-gray-600 ring-offset-gray-800 focus:ring-2 bg-gray-700 border-gray-600"
            />
            <label htmlFor="gamemode-radio-2" className="font-medium">
              Versus AI
            </label>
          </div>
          <div className="flex items-center" onClick={() => setGameMode(3)}>
            <input
              defaultChecked={gamemode === 3}
              id="gamemode-radio-3"
              type="radio"
              name="gamemode-radio"
              className="w-4 h-4 focus:ring-gray-600 ring-offset-gray-800 focus:ring-2 bg-gray-700 border-gray-600"
            />
            <label htmlFor="gamemode-radio-3" className="font-medium">
              Online
            </label>
          </div>
        </div>
      </div>
    </div>
  );

  return (
    <div>
      <button
        className="bg-pink-500 text-white active:bg-pink-600 px-6 py-3 rounded"
        type="button"
        onClick={() => setVisible(true)}
      >
        New Game
      </button>

      <Modal
        onSubmit={onSubmit}
        visible={visible}
        setVisibility={setVisible}
        title="New Game"
        submitText="Create"
        component={newGameComponents}
      />
    </div>
  );
};

export default NewGame;
