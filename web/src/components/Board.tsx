import { Dispatch, SetStateAction, useEffect, useState } from "react";
import { GamePiece } from "./GamePiece";
import { GameData } from "../types/GameData";
import Modal from "./Modal";
import { GameState } from "../types/Enums";
import socket from "../services/websocket";
import { UserData } from "../types/UserData";

<<<<<<< HEAD
const Board = ({
  gameData,
  userData,
}: {
  gameData: GameData;
  userData: UserData | undefined;
}) => {
=======
const Board = ({ gameData }: { gameData: GameData }) => {
>>>>>>> 40bf264c4db7b2710872012bc1f659e17a41fd14
  const [gameOverVisible, setGameOverVisible] = useState<boolean>(false);
  const [settingsVisible, setSettingsVisible] = useState<boolean>(false);
  const [boardColor, setBoardColor] = useState<string>("#18843c");
  const [player1Color, setPlayer1Color] = useState<string>("#ffffff");
  const [player2Color, setPlayer2Color] = useState<string>("#000000");
  const [yourScore, setYourScore] = useState<number>(0);
  const [opponentScore, setOpponentScore] = useState<number>(0);

  const resetBoard = () => {
    socket.emit("resetBoard", gameData.id);
  };

  useEffect(() => {
    setGameOverVisible(gameData.state === GameState.GAMEOVER);
    setYourScore(gameData.players[0] === userData?.username ? gameData.score[0] : gameData.score[1]);
    setOpponentScore(gameData.players[1] === userData?.username ? gameData.score[0] : gameData.score[1]);
  }, [gameData]);

  const youWin = <h1 className="text-xl">You Win!</h1>;
  const youLose = <h1 className="text-xl">You Lose!</h1>;

  const settingsComponent = (
    <div className="grid">
      <div className="mt-3 flex justify-between">
        <h2 className="inline p-2 text-xl mr-10">Board Color</h2>
        <input
          className="my-auto"
          onChange={(e) => setBoardColor(e.target.value)}
          type="color"
          value={boardColor}
        />
      </div>
      <div className="mt-3 flex justify-between">
        <h2 className="inline p-2 text-xl">Player 1 Color</h2>
        <input
          className="my-auto"
          onChange={(e) => setPlayer1Color(e.target.value)}
          type="color"
          value={player1Color}
        />
      </div>
      <div className="mt-3 flex justify-between">
        <h2 className="inline p-2 text-xl">Player 2 Color</h2>
        <input
          className="my-auto"
          onChange={(e) => setPlayer2Color(e.target.value)}
          type="color"
          value={player2Color}
        />
      </div>
    </div>
  );

  return (
    <div className="p-3">
<<<<<<< HEAD
=======
      <button
        className="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded"
        onClick={resetBoard}
      >
        Reset
      </button>

>>>>>>> 40bf264c4db7b2710872012bc1f659e17a41fd14
      <button
        className="ml-2 bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded"
        onClick={() => setSettingsVisible(true)}
      >
        Settings
      </button>

      <div className="flex justify-around mt-5">
        <h3>Your Score: {yourScore}</h3>
        <h3>Opponent Score: {opponentScore}</h3>
      </div>

      <div className="flex items-center justify-center">
        <div
          className={`grid grid-cols-${gameData.size} grid-rows-${gameData.size}`}
          style={{ backgroundColor: `${boardColor}` }}
        >
          {gameData.board &&
            gameData.board.map((e, i) => (
              <GamePiece
                key={i}
                idx={i}
                state={e}
                gameData={gameData}
                player1Color={player1Color}
                player2Color={player2Color}
<<<<<<< HEAD
                userData={userData}
=======
>>>>>>> 40bf264c4db7b2710872012bc1f659e17a41fd14
              />
            ))}
        </div>
      </div>

      <Modal
        visible={gameOverVisible}
        setVisibility={setGameOverVisible}
        title="Game Over"
        submitText="Create"
        component={
          (gameData.score[0] > gameData.score[1] &&
            gameData.players[0] == userData?.username) ||
          (gameData.score[0] < gameData.score[1] &&
            gameData.players[1] == userData?.username)
            ? youWin
            : youLose
        }
      />

      <Modal
        visible={settingsVisible}
        setVisibility={setSettingsVisible}
        title="Settings"
        submitText="Save"
        component={settingsComponent}
      />
    </div>
  );
};

export default Board;
