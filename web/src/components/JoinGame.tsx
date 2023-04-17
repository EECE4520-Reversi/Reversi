import { Dispatch, SetStateAction, useEffect, useState } from "react";
import Modal from "./Modal";
import socket from "../services/websocket";
import { JoinableGame } from "../types/JoinableGame";
import { useNavigate } from "react-router";

const JoinGame = ({
  setBoardID,
}: {
  setBoardID: Dispatch<SetStateAction<string>>;
}) => {
  const [openGames, setOpenGames] = useState<JoinableGame[]>([]);
  const [joinModalOpen, setJoinModalOpen] = useState<boolean>(false);
  const [selectedGameID, setSelectedGameID] = useState<string>();
  const navigate = useNavigate();

  useEffect(() => {
    socket.emit("joinableGames", (data: JoinableGame[]) => setOpenGames(data));
    socket.on("openGames", (data: JoinableGame[]) => setOpenGames(data));
  }, []);

  const joinGame = () => {
    if (selectedGameID) {
      setBoardID(selectedGameID);
      socket.emit("joinGame", selectedGameID);
      console.log(`Joining Game: ${selectedGameID}`);
      navigate("/game");
    }
  };

  const openGamesComponents = (
    <div className="min-w-[25vw]">
      {openGames.map((game) => (
        <div
          className={`btn-primary cursor-pointer text-2xl px-3 py-1 ${
            selectedGameID == game.id ? "bg-blue-500 text-white" : ""
          }`}
          onClick={() => setSelectedGameID(game.id)}
        >
          <h1>
            {game.player}: {game.size}x{game.size}
          </h1>
        </div>
      ))}
    </div>
  );

  return (
    <>
      <button
        onClick={() => setJoinModalOpen(true)}
        className="text-4xl w-1/2 btn-primary"
      >
        Join Game
      </button>
      <Modal
        onSubmit={joinGame}
        visible={joinModalOpen}
        setVisibility={setJoinModalOpen}
        title="Open Games"
        submitText="Join"
        component={openGamesComponents}
      />
    </>
  );
};

export default JoinGame;
