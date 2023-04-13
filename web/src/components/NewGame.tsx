import { Dispatch, SetStateAction, useState } from "react";
import { createGame } from "../services/backendservicews";
import { Difficulty, GameType } from "../types/Enums";
import { GameData } from "../types/GameData";
import Modal from "./Modal";

const capitalize = (str: string) => {
  return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
}

const NewGame = ({
  setGameData,
  gameData,
}: {
  setGameData: Dispatch<SetStateAction<GameData | undefined>>;
  gameData: GameData;
}) => {
  const [visible, setVisible] = useState<boolean>(false);
  const [boardSize, setBoardSize] = useState<number>(gameData.size || 8);
  const [difficulty, setDifficulty] = useState<Difficulty>(
    gameData ? gameData.difficulty : Difficulty.MEDIUM
  );
  const [gamemode, setGameMode] = useState<GameType>(
    gameData.type || GameType.AI
  );

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
          {[Difficulty.EASY, Difficulty.MEDIUM, Difficulty.HARD].map(
            (val) => {
              return (
                <div
                  className="flex items-center"
                  onClick={() => setDifficulty(val)}
                >
                  <input
                    defaultChecked={difficulty === val}
                    id={`difficulty-radio-${val}`}
                    type="radio"
                    name="difficult-radio"
                    className="w-4 h-4 focus:ring-gray-600 ring-offset-gray-800 focus:ring-2 bg-gray-700 border-gray-600"
                  />
                  <label htmlFor={`difficulty-radio-${val}`} className="font-medium">
                    {capitalize(Difficulty[val])}
                  </label>
                </div>
              );
            }
          )}
        </div>
      </div>
      <div className="mt-3">
        <h2 className="inline p-2 text-xl">Gamemode:</h2>
        <div className="flex justify-between space-x-5">
          {[GameType.LOCAL, GameType.AI, GameType.ONLINE].map((val) => {
            return <div className="flex items-center" onClick={() => setGameMode(val)}>
              <input
                defaultChecked={gamemode === val}
                id={`gamemode-radio-${val}`}
                type="radio"
                name="gamemode-radio"
                className="w-4 h-4 focus:ring-gray-600 ring-offset-gray-800 focus:ring-2 bg-gray-700 border-gray-600"
              />
              <label htmlFor={`gamemode-radio-${val}`} className="font-medium">
                {capitalize(GameType[val])}
              </label>
            </div>
          })}


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
