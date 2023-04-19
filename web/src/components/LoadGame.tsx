import { Dispatch, SetStateAction, useEffect, useState } from "react";
import Modal from "./Modal";
import socket from "../services/websocket";
import { LoadableGame } from "../types/LoadableGame";
import { useNavigate } from "react-router";

const LoadGame = ({
    setBoardID,
}: {
    setBoardID: Dispatch<SetStateAction<string>>;
}) => {
    const [loadGames, setLoadGames] = useState<LoadableGame[]>([]);
    const [loadModalOpen, setLoadModalOpen] = useState<boolean>(false);
    const [selectedGameID, setSelectedGameID] = useState<string>();
    const navigate = useNavigate();

    useEffect(() => {
        socket.emit("loadableGames", (data: LoadableGame[]) => setLoadGames(data));
        socket.on("loadGames", (data: LoadableGame[]) => setLoadGames(data));
    }, []);

    const loadGame = () => {
        if (selectedGameID) {
            setBoardID(selectedGameID);
            socket.emit("loadGame", selectedGameID);
            console.log(`Loading Game: ${selectedGameID}`);
            navigate("/game");
        }
    };

    const openGamesComponents = (
        <div className="min-w-[25vw]">
            {loadGames.map((game) => (
                <div
                    className={`btn-primary cursor-pointer text-2xl px-3 py-1 ${selectedGameID == game.id ? "bg-blue-500 text-white" : ""
                        }`}
                    onClick={() => setSelectedGameID(game.id)}
                >
                    <h1>
                        {game.type}: {game.player1} vs. {game.player2} | {game.size}x{game.size} - {game.state}
                    </h1>
                </div>
            ))}
        </div>
    );

    return (
        <>
            <button
                onClick={() => setLoadModalOpen(true)}
                className="text-4xl w-1/2 btn-primary"
            >
                Join Game
            </button>
            <Modal
                onSubmit={loadGame}
                visible={loadModalOpen}
                setVisibility={setLoadModalOpen}
                title="Your Games"
                submitText="Load"
                component={openGamesComponents}
            />
        </>
    );
};

export default LoadGame;
